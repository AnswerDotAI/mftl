# Math for the Layman archive

A static copy of Kenneth E. Iverson's *Math for the Layman*, restored from [Trinity University's July 11, 2017 Wayback snapshot](https://web.archive.org/web/20170711100604/http://www.cs.trinity.edu/About/The_Courses/cs301/math-for-the-layman/).

The book is stored as 25 Markdown pages in `docs/`: a contents page, preface, 20 chapters, supplement, appendix, and references. All 18 graph images are local copies from July 17, 2016 captures, the closest available image captures found around the requested snapshot.

The archive's HTTP header incorrectly declares UTF-8. The text was decoded as Windows-1252 and saved as UTF-8. Prose and J examples are preserved, with examples and tables in fenced code blocks. Formatting whitespace around inline code is removed. Cross-references use explicit anchors and relative links between chapters; numbered citations link to bibliography entries. Small HTML elements remain for anchors, superscripts, and subscripts. Original rights remain with their owners.

GitHub Pages renders the Markdown with its built-in Jekyll support. `_layouts/book.html` supplies the archive notice and navigation; `style.css` supplies the shared reading layout. Edit the Markdown directly. There is no conversion step when publishing.

## Preview

With Jekyll installed, run from this directory:

```bash
jekyll serve --source docs
```

Open <http://127.0.0.1:4000/>. A plain static server will not render the Markdown or shared layout.

## GitHub Pages

After uploading this directory to a repository, select **Deploy from a branch**, branch `main`, and folder `/docs` in its Pages settings. No custom domain is configured.

## Checks and recovery records

Run `pytest -q` with Ruby, the `kramdown` and `kramdown-parser-gfm` gems, `pytest`, and `beautifulsoup4` installed. The checks render all pages with the GFM parser selected by the Pages configuration and check inline code, citations, cross-page links, anchors, and local assets. They do not build Jekyll.

`meta/original.html` contains the untouched source bytes. `meta/captures.json` records the exact capture URLs. The one-off conversion script and fidelity checks are also in `meta/`, which is ignored by git.
