import re, subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit
from bs4 import BeautifulSoup

site = Path(__file__).parent/'docs'


def render_page(path):
    text = path.read_text(encoding='utf-8')
    assert '\ufffd' not in text and not re.search(r'[\x80-\x9f]', text)
    _, frontmatter, body = text.split('---', 2)
    ruby = r"puts Kramdown::Document.new(STDIN.read, input: 'GFM', syntax_highlighter: nil).to_html"
    result = subprocess.run(['ruby', '-r', 'kramdown', '-r', 'kramdown-parser-gfm', '-e', ruby], input=body, text=True, capture_output=True, check=True)
    return frontmatter, BeautifulSoup(result.stdout, 'html.parser')


def test_book_links():
    pages, anchors = {}, {}
    for page in site.glob('*.md'):
        metadata, soup = render_page(page)
        name = page.with_suffix('.html').name
        pages[name] = soup
        anchor = re.search(r'^anchor: "?([^"\n]+)', metadata, re.M).group(1)
        anchors[name] = {t['id'] for t in soup.find_all(id=True)} | {anchor}
    assert len(pages) == 25
    preface_codes = {t.get_text() for t in pages['preface.html'].find_all('code') if not t.find_parent('pre')}
    assert {'0.333333', '0.857143', '0.046875'} <= preface_codes
    for name, soup in pages.items():
        for code in soup.find_all('code'):
            if not code.find_parent('pre'): assert code.get_text() == code.get_text().strip(), name
        for citation in soup.find_all(string=re.compile(r'\[\d+\]')):
            if not citation.find_parent(['pre', 'code']): assert citation.find_parent('a'), (name, citation)
        for tag in soup.find_all():
            for attr in ('href', 'src'):
                if attr not in tag.attrs: continue
                url = urlsplit(tag[attr])
                if url.scheme: continue
                assert not url.netloc
                target = unquote(url.path) or name
                if url.fragment: assert unquote(url.fragment) in anchors[target], (name, tag[attr])
                if url.path: assert target in pages or (site/target).is_file(), (name, target)
