---
title: "Supplement"
anchor: "supplement"
previous: "chapter-20.html"
next: "appendix.html"
---

<span id="s1a"></span>

## [S1A. The Counting (Natural) Numbers](chapter-01.html#1a)

This definition of the counting numbers in terms of a *successor* function was made in 1899 by Giuseppe Peano. For further details, see the discussion in Section 20B, and the Gullberg text to which it refers.

This discussion may be found by first clicking on Chapter 20 in the list at the beginning of the text, then clicking on Section 20C, and then moving back up the page to the last part of Section 20B. <span id="s1b"></span>

## [S1B. Lists and Names](chapter-01.html#1b)

The function (or verb) denoted by `,.` can be used to *stitch* lists together to form tables, and lists and tables together to form further tables, as illustrated by the following:

```
   a=:1 4 7
   b=:2 5 8
   c=:3 6 9
   
   a,.b
1 2
4 5
7 8
   a,.b,.c
1 2 3
4 5 6
7 8 9
   table=:a,.b,.c
   table,.>:c
1 2 3  4
4 5 6  7
7 8 9 10
   >:table
2 3  4
5 6  7
8 9 10
   table,.>:>:>:table
1 2 3  4  5  6
4 5 6  7  8  9
7 8 9 10 11 12
```

The function denoted by `,` can be used to *catenate* lists and tables as illustrated by the following:

```
   a,b
1 4 7 2 5 8
   a,b,c
1 4 7 2 5 8 3 6 9
   table,a
1 2 3
4 5 6
7 8 9
1 4 7
   table,>:>:>:>:>:>:>:>:>:table
 1  2  3
 4  5  6
 7  8  9
10 11 12
13 14 15
16 17 18
```

The function denoted by `|:` can be used to *transpose* a table as follows:

```
   |:table
1 4 7
2 5 8
3 6 9
   |:table,>:c
1 4 7  4
2 5 8  7
3 6 9 10
```

Write various expressions employing the functions used in the preceding examples, and show the results produced. <span id="s1c"></span>

## [S1C. Iteration (Repetition)](chapter-01.html#1c)

Write the result of the expression `next for list list `, and compare your result with that produced by entering it on the computer. <span id="s1d"></span> <span id="s1d"></span>

## [S1D. Inverse](chapter-01.html#1d)

While we had only the counting numbers (which begin at `1`), our lists could contain neither negative numbers nor zero; but now that we have extended our domain to the integers this restriction is removed. We may therefore introduce the functions `i.` and `i:` that produce lists of integers as illustrated below:

```
   i.5   NB. The first five non-negative integers
0 1 2 3 4

   i:5   NB. The integers from _5 to 5
_5 _4 _3 _2 _1 0 1 2 3 4 5
```

In the foregoing we used `NB.` which indicates that what follows it is a note or comment that has no effect on the meaning of the preceding sentence.

The function denoted by `+:` *doubles* its argument. For example:

```
   x=:i:5
   x
_5 _4 _3 _2 _1 0 1 2 3 4 5
   +:x
_10 _8 _6 _4 _2 0 2 4 6 8 10
   double=:+:
   double x
_10 _8 _6 _4 _2 0 2 4 6 8 10
   y=:double for 2 x
   y
_20 _16 _12 _8 _4 0 4 8 12 16 20

   double for _1 y  NB. Inverse of double
_10 _8 _6 _4 _2 0 2 4 6 8 10

   double for _1 x
_2.5 _2 _1.5 _1 _0.5 0 0.5 1 1.5 2 2.5
```

Some of the results of the last expression are not integers. Just as the inverse of the successor function led us out of the domain of the counting numbers, so the inverse of `double` has led out of the domain of integers -- this time into *fractions* or *rationals*. These matters are treated further in Section 1J. <span id="s1e"></span>

## [S1E. Addition and Subtraction (+ and -)](chapter-01.html#1e)

Study the following function tables, and try to state the definitions of each of the functions denoted by `= > <. <: |` and `!`

Compare your definitions with those given below.

```
   a=:i.6
   a
0 1 2 3 4 5
   =table a
+-+-----------+
| |0 1 2 3 4 5|
+-+-----------+
|0|1 0 0 0 0 0|
|1|0 1 0 0 0 0|
|2|0 0 1 0 0 0|
|3|0 0 0 1 0 0|
|4|0 0 0 0 1 0|
|5|0 0 0 0 0 1|
+-+-----------+

   (=table a),.(>table a),.(<.table a)
+-+-----------+-+-----------+-+-----------+
| |0 1 2 3 4 5| |0 1 2 3 4 5| |0 1 2 3 4 5|
+-+-----------+-+-----------+-+-----------+
|0|1 0 0 0 0 0|0|0 0 0 0 0 0|0|0 0 0 0 0 0|
|1|0 1 0 0 0 0|1|1 0 0 0 0 0|1|0 1 1 1 1 1|
|2|0 0 1 0 0 0|2|1 1 0 0 0 0|2|0 1 2 2 2 2|
|3|0 0 0 1 0 0|3|1 1 1 0 0 0|3|0 1 2 3 3 3|
|4|0 0 0 0 1 0|4|1 1 1 1 0 0|4|0 1 2 3 4 4|
|5|0 0 0 0 0 1|5|1 1 1 1 1 0|5|0 1 2 3 4 5|
+-+-----------+-+-----------+-+-----------+

   (<:table a),.(|table a),.(!table a)
+-+-----------+-+-----------+-+------------+
| |0 1 2 3 4 5| |0 1 2 3 4 5| |0 1 2 3 4  5|
+-+-----------+-+-----------+-+------------+
|0|1 1 1 1 1 1|0|0 1 2 3 4 5|0|1 1 1 1 1  1|
|1|0 1 1 1 1 1|1|0 0 0 0 0 0|1|0 1 2 3 4  5|
|2|0 0 1 1 1 1|2|0 1 0 1 0 1|2|0 0 1 3 6 10|
|3|0 0 0 1 1 1|3|0 1 2 0 1 2|3|0 0 0 1 4 10|
|4|0 0 0 0 1 1|4|0 1 2 3 0 1|4|0 0 0 0 1  5|
|5|0 0 0 0 0 1|5|0 1 2 3 4 0|5|0 0 0 0 0  1|
+-+-----------+-+-----------+-+------------+
```

`=` is a *truth function* that compares its arguments for equality, giving `1` if the relation is true, and `0` if it is false.

`>` is a truth function called *greater than*.

`<.` is called *lesser-of* or *minimum*.

`<:` is a truth function called *less than or equal*.

`|` is *remainder* on dividing by the left argument.

`!` is the *binomial coefficient* (`m!n` is the number of different ways of choosing `m` things from `n` things). This table is commonly shown without the zeros, and called *Pascal's Triangle*. <span id="s1f"></span>

## [S1F. Bonding](chapter-01.html#1f)

Apply the bond (`with=:&`) to some of the functions `= < >. <: |` introduced in Section S1E, and show their results. Compare your results with the following:

```
   with=: &
   
   a=:i:3
   a
_3 _2 _1 0 1 2 3
   
   = with 2 a
0 0 0 0 0 1 0
   
   < with 2 a
1 1 1 1 1 0 0
   
   <: with 2 a
1 1 1 1 1 1 0
   
   <. with 2 a
_3 _2 _1 0 1 2 2
   
   2 with | a
1 0 1 0 1 0 1
   
   3 with | a
0 1 2 0 1 2 0
```

<span id="s1g"></span>

## [S1G. Multiplication or Times (\*)](chapter-01.html#1g)

Comment on the pattern of positive and negative numbers in the four quadrants defined by the row and column of zeros in the following multiplication table:

```
   * table i:4
+--+-----------------------------+
|  | _4  _3 _2 _1 0  1  2   3   4|
+--+-----------------------------+
|_4| 16  12  8  4 0 _4 _8 _12 _16|
|_3| 12   9  6  3 0 _3 _6  _9 _12|
|_2|  8   6  4  2 0 _2 _4  _6  _8|
|_1|  4   3  2  1 0 _1 _2  _3  _4|
| 0|  0   0  0  0 0  0  0   0   0|
| 1| _4  _3 _2 _1 0  1  2   3   4|
| 2| _8  _6 _4 _2 0  2  4   6   8|
| 3|_12  _9 _6 _3 0  3  6   9  12|
| 4|_16 _12 _8 _4 0  4  8  12  16|
+--+-----------------------------+
```

The idea of multiplication can be introduced at an elementary level by pictures of rectangles. For example:

```
   a=:3 4 $ 1
   a
1 1 1 1
1 1 1 1
1 1 1 1
   ,a
1 1 1 1 1 1 1 1 1 1 1 1
   +/,a
12
   +/a
3 3 3 3
   +/+/a
12

   b=:|:a
   b
1 1 1
1 1 1
1 1 1
1 1 1
   ,b
1 1 1 1 1 1 1 1 1 1 1 1
   +/,b
12
   +/b
4 4 4
   +/+/b
12
```

Discussion of the notation used here (such as `$`) may be found in Sections 2E and 2F.

In his imaginative and persuasive *Vision in Elementary Mathematics* \[22\], W.W. Sawyer uses similar (hand-drawn) pictures to introduce elementary concepts in arithmetic and algebra, clarifying the ideas by "translating" from pictures to notation and back.

Sawyer's pictures do not even require the somewhat abstract notion of the numeral `1` used above, but uses dots:

```
   c=: a { ' .'
   c
....
....
....
   |:c
...
...
...
...
   c='.'
1 1 1 1
1 1 1 1
1 1 1 1
   +/+/c='.'
12
```

Moreover, he draws a tied bag (rather similar to &) to denote an unknown quantity, and translates to algebraic expressions that denote unknowns by letters such as *x* and *y*. For example:

```
   g=:'&&...'
   g
&&...
```

translates to `2`*`x`*`+3`.

Addition is shown as:

```
   g,g
&&...&&...
```

which is denoted by `(2`*`x`*`+3)+(2`*`x`*`+3)` and is (pictorially) equivalent to that shown above, or to `&&&&......` which, in turn, translates to `4`*`x`*`+6`. <span id="s1h"></span>

## [S1H. Power and Exponent](chapter-01.html#1h)

See Section S1J for an extension of the power table to negative arguments. <span id="s1i"></span>

## [S1I. Monomials and Polynomials (p.)](chapter-01.html#1i)

Write various expressions using the polynomial function `p.` and show the results they produce. Include cases with negative coefficients and negative arguments, and compare your results with the following:

```
   b=:i:4
   b
_4 _3 _2 _1 0 1 2 3 4
   
   1 3 3 1 p. b
_27 _8 _1 0 1 8 27 64 125
   
   _1 3 _3 1 p. b
_125 _64 _27 _8 _1 0 1 8 27
   
   (b-1)^3
_125 _64 _27 _8 _1 0 1 8 27
   
   1 _4 6 _4 1 p. b
625 256 81 16 1 0 1 16 81
   
   (b-1)^4
625 256 81 16 1 0 1 16 81
```

<span id="s1j"></span>

## [S1J. Division (%)](chapter-01.html#1j)

Comment on the pattern in the rows and columns of the division table. Then make a division table for both positive and negative arguments, and compare your results with the following:

```
   c=:i:5r1
   c
_5 _4 _3 _2 _1 0 1 2 3 4 5

   %table c
+--+------------------------------------------------+
|  |  _5   _4   _3   _2 _1  0  1    2    3    4    5|
+--+------------------------------------------------+
|_5|   1  5r4  5r3  5r2  5 __ _5 _5r2 _5r3 _5r4   _1|
|_4| 4r5    1  4r3    2  4 __ _4   _2 _4r3   _1 _4r5|
|_3| 3r5  3r4    1  3r2  3 __ _3 _3r2   _1 _3r4 _3r5|
|_2| 2r5  1r2  2r3    1  2 __ _2   _1 _2r3 _1r2 _2r5|
|_1| 1r5  1r4  1r3  1r2  1 __ _1 _1r2 _1r3 _1r4 _1r5|
| 0|   0    0    0    0  0  0  0    0    0    0    0|
| 1|_1r5 _1r4 _1r3 _1r2 _1  _  1  1r2  1r3  1r4  1r5|
| 2|_2r5 _1r2 _2r3   _1 _2  _  2    1  2r3  1r2  2r5|
| 3|_3r5 _3r4   _1 _3r2 _3  _  3  3r2    1  3r4  3r5|
| 4|_4r5   _1 _4r3   _2 _4  _  4    2  4r3    1  4r5|
| 5|  _1 _5r4 _5r3 _5r2 _5  _  5  5r2  5r3  5r4    1|
+--+------------------------------------------------+
```

Comment on the patterns in the following extension of the power table to negative arguments. In particular, note the value of `0^0` (which may have surprised you in the power table in Section 1H).

For further justification of the choice of `1` for the value of the "indeterminate" expression `0^0`, see page 785 of Gullberg \[20\].

```
   ^table c
+--+-----------------------------------------------------+
|  |     _5    _4     _3   _2   _1 0  1  2    3   4     5|
+--+-----------------------------------------------------+
|_5|_1r3125 1r625 _1r125 1r25 _1r5 1 _5 25 _125 625 _3125|
|_4|_1r1024 1r256  _1r64 1r16 _1r4 1 _4 16  _64 256 _1024|
|_3| _1r243  1r81  _1r27  1r9 _1r3 1 _3  9  _27  81  _243|
|_2|  _1r32  1r16   _1r8  1r4 _1r2 1 _2  4   _8  16   _32|
|_1|     _1     1     _1    1   _1 1 _1  1   _1   1    _1|
| 0|      _     _      _    _    _ 1  0  0    0   0     0|
| 1|      1     1      1    1    1 1  1  1    1   1     1|
| 2|   1r32  1r16    1r8  1r4  1r2 1  2  4    8  16    32|
| 3|  1r243  1r81   1r27  1r9  1r3 1  3  9   27  81   243|
| 4| 1r1024 1r256   1r64 1r16  1r4 1  4 16   64 256  1024|
| 5| 1r3125 1r625  1r125 1r25  1r5 1  5 25  125 625  3125|
+--+-----------------------------------------------------+
```

<span id="s1k"></span>

## [S1K. Review and Supplement](chapter-01.html#1k)

Experiment with moving around in the text as follows:

Click on any one of the Chapters listed at the beginning of the text, and then click on the chapter heading to return to the list of chapters.

Click on any one of the Sections listed at the beginning of the selected chapter, and then click on the Section heading to return to the chapter.

Again select a chapter and a section within it. Then click on the label beginning with S that appears to the right of the section heading.

Click on the heading of the supplemental section to return to the corresponding main section. <span id="s1l"></span>

## [S1L. Notes](chapter-01.html#1l)

<span id="s2a"></span>

## [S2A. Introduction](chapter-02.html#2a)

To gain further familiarity with the computer, enter some of the expressions from the supplemental sections for Chapter 1. <span id="s2b"></span>

## [S2B. Number of places](chapter-02.html#2b)

The `!:` used in the expression `set=:9!:11` to define the function for setting the number of digits displayed is called the *foreign conjunction*, because it concerns matters other than the normal verbs such as `+ *` and `%`.

Click on the Help menu to display the items for which information is available. Then click on Foreign Conjunction, and then on item 9 to see the case used in defining `set`. Also click on the button marked \>\> to see further pages.

Finally press the Escape key (Esc) to remove the Help display. <span id="s2c"></span>

## [S2C. Displays](chapter-02.html#2c)

Sawyer \[22\] emphasizes the use of trees and tables for insight, and introduces an interesting non-numeric table as follows:

> In the Japanese Hiragana alphabet, each character represents a sound such as *ka, ru, si, or o*. There are 10 possible beginnings - the consonants k, s, t, n, m, y, r, w, and 'blank'; ... The ending is always one one of the five sounds a, e, i, o, u. How many characters are there in this alphabet? We could show this as a tree with 10 branches and 5 twigs on each ... This problem could equally well be solved by the rectangle ...

```
   Beginnings=:' KSTNHMYRW'
      Endings=:'aeiou'
   
   { Beginnings;Endings
+--+--+--+--+--+
| a| e| i| o| u|
+--+--+--+--+--+
|Ka|Ke|Ki|Ko|Ku|
+--+--+--+--+--+
|Sa|Se|Si|So|Su|
+--+--+--+--+--+
|Ta|Te|Ti|To|Tu|
+--+--+--+--+--+
|Na|Ne|Ni|No|Nu|
+--+--+--+--+--+
|Ha|He|Hi|Ho|Hu|
+--+--+--+--+--+
|Ma|Me|Mi|Mo|Mu|
+--+--+--+--+--+
|Ya|Ye|Yi|Yo|Yu|
+--+--+--+--+--+
|Ra|Re|Ri|Ro|Ru|
+--+--+--+--+--+
|Wa|We|Wi|Wo|Wu|
+--+--+--+--+--+
```

The *catalogue* function (`{`) used above may be further illustrated as follows:

```
   { 0 1 2;0 1 2;0 1 2
+-----+-----+-----+
|0 0 0|0 0 1|0 0 2|
+-----+-----+-----+
|0 1 0|0 1 1|0 1 2|
+-----+-----+-----+
|0 2 0|0 2 1|0 2 2|
+-----+-----+-----+

+-----+-----+-----+
|1 0 0|1 0 1|1 0 2|
+-----+-----+-----+
|1 1 0|1 1 1|1 1 2|
+-----+-----+-----+
|1 2 0|1 2 1|1 2 2|
+-----+-----+-----+

+-----+-----+-----+
|2 0 0|2 0 1|2 0 2|
+-----+-----+-----+
|2 1 0|2 1 1|2 1 2|
+-----+-----+-----+
|2 2 0|2 2 1|2 2 2|
+-----+-----+-----+

   { 'cht';'oa';'gtw'
+---+---+---+
|cog|cot|cow|
+---+---+---+
|cag|cat|caw|
+---+---+---+

+---+---+---+
|hog|hot|how|
+---+---+---+
|hag|hat|haw|
+---+---+---+

+---+---+---+
|tog|tot|tow|
+---+---+---+
|tag|tat|taw|
+---+---+---+
```

<span id="s2d"></span>

## [S2D. Integer Lists](chapter-02.html#2d)

Explain the difference between the following tables:

```
   %table i:4
+--+--------------------------------------------------+
|_4|    1   1.33333    2  4 __ _4   _2  _1.33333    _1|
|_3| 0.75         1  1.5  3 __ _3 _1.5        _1 _0.75|
|_2|  0.5  0.666667    1  2 __ _2   _1 _0.666667  _0.5|
|_1| 0.25  0.333333  0.5  1 __ _1 _0.5 _0.333333 _0.25|
| 0|    0         0    0  0  0  0    0         0     0|
| 1|_0.25 _0.333333 _0.5 _1  _  1  0.5  0.333333  0.25|
| 2| _0.5 _0.666667   _1 _2  _  2    1  0.666667   0.5|
| 3|_0.75        _1 _1.5 _3  _  3  1.5         1  0.75|
| 4|   _1  _1.33333   _2 _4  _  4    2   1.33333     1|
+--+--------------------------------------------------+
   %table i:4r1
+--+--------------------------------------+
|  |  _4   _3   _2 _1  0  1    2    3    4|
+--+--------------------------------------+
|_4|   1  4r3    2  4 __ _4   _2 _4r3   _1|
|_3| 3r4    1  3r2  3 __ _3 _3r2   _1 _3r4|
|_2| 1r2  2r3    1  2 __ _2   _1 _2r3 _1r2|
|_1| 1r4  1r3  1r2  1 __ _1 _1r2 _1r3 _1r4|
| 0|   0    0    0  0  0  0    0    0    0|
| 1|_1r4 _1r3 _1r2 _1  _  1  1r2  1r3  1r4|
| 2|_1r2 _2r3   _1 _2  _  2    1  2r3  1r2|
| 3|_3r4   _1 _3r2 _3  _  3  3r2    1  3r4|
| 4|  _1 _4r3   _2 _4  _  4    2  4r3    1|
+--+--------------------------------------+
```

<span id="s2e"></span>

## [S2E. Vocabulary](chapter-02.html#2e)

The Vocabulary provides *two* definitions for the symbol `-`; one (called Negate) for use with one argument, and the other (called Minus) for use with two arguments. For example:

```
   - i.7    NB. Monadic use
0 _1 _2 _3 _4 _5 _6
   
   3 - i.7  NB. Dyadic use
3 2 1 0 _1 _2 _3
```

Other functions also have both monadic and dyadic cases. For example, `a * b` denotes the product of `a` and `b`, while `*b` denotes the *sign* of `b`.

A deinition may be displayed directly without displaying the Vocabulary: simply place the cursor just to the left of the symbol, and press F1 while holding down the control key (Ctrl). <span id="s2f"></span>

## [S2F. Functions over lists](chapter-02.html#2f)

Just as the *over* adverb `/` modifies a verb to which it applies, the *prefix* adverb `\` modifies its argument verb, applying it to each prefix of the eventual argument. For example:

```
   a=:1 2 3 4 5
   +/a
15
   
   +/\a
1 3 6 10 15
   
   sum=:+/
   sum\a
1 3 6 10 15
   
   (sum 1),(sum 1 2),(sum 1 2 3),(sum 1 2 3 4),(sum 1 2 3 4 5)
1 3 6 10 15
   
   b=:1 2 3 4 5 6r1
   
   */\b
1 2 6 24 120 720
   
   !b
1 2 6 24 120 720
   
   %/\b
1 1r2 3r2 3r8 15r8 5r16
```

Consulting the Vocabulary if necessary, state the results of the following expressions, and check your results by executing them on the computer:

```
   c=:18 3 96 17 24 12
   <./c

   <./\c

   >./\c

   +./c

   +./\c

   c % +./\c

   *./\c

   (*./\c) % c
```

<span id="s2g"></span>

## [S2G. Notes](chapter-02.html#2g)

<span id="s3a"></span>

## [S3A. Plotting](chapter-03.html#3a)

The *link* function (denoted by `;`) used in the expression `PLOT x;f x` in Section 3A *boxes* its arguments and catenates them to form a two-element list. Together with the *laminate* function also introduced in Section 3A and the `,` and `,.` introduced in Section S1B, they provide four ways of forming lists and tables.

Experiment with their joint use, employing the *shape* function `$` to examine the shapes of results. <span id="s3b"></span>

## [S3B. Local behaviour and area](chapter-03.html#3b)

Use the Vocabulary to examine the definition of the *circle* function `o.` used in Section 3 B. In particular, experiment with the monadic case in expressions such as `o.1` and `o.2` and `o.1r2 `.

Examine a plot of the sine function (`sin=:1 with o.`) to determine the approximate area under one of its arches. Then define `cos=:2 with o.` and use `plot` to plot each of `sin` and `cos` against the argument, and against one another.

Look up the definition of `+:` (the double function) and plot `sin on +:` against `sin` .

Finally, plot `5 with o.` against `6 with o.` on the argument `1r12*i:10` to draw a hyperbola. <span id="s3c"></span>

## [S3C. Graphs versus function tables](chapter-03.html#3c)

1.  Determine the pairwise differences of various polynomials, including `0 0 1 with p.` and `2 0 1 with p.` and `1 4 6 4 1 with p.` .

<span id="s3d"></span>

## [S3D. Notes](chapter-03.html#3d)

<span id="s4a"></span>

## [S4A. Bonding](chapter-04.html#4a)

If the lists `c` and `d` are the same length (that is, have the same number of elements), then the polynomial `(c+d) with p.` is equivalent to the sum `c with p. + d with p.` . If one is shorter than the other, it must be extended by trailing zeros before adding it.

Test this assertion for various values of `c` and `d`.

A coefficient list that has a single non-zero element defines a polynomial that is a multiple of a power of its argument. In other words, it defines a *monomial* in the sense defined in Section 1I. For example:

```
   with=:&
   x=:i:4
   x
_4 _3 _2 _1 0 1 2 3 4
   0 0 1 with p. x
16 9 4 1 0 1 4 9 16
   x^2
16 9 4 1 0 1 4 9 16
   0 0 3 with p. x
48 27 12 3 0 3 12 27 48
   3*x^2
48 27 12 3 0 3 12 27 48
```

If `e` is the diagonal sum(s) of the multiplication table `c */ d`, then the function `e with p.` is equivalent to the product `g=: c with p. * d with p. `. Test this assertion for various values of the coefficients `c` and `d`.

The expression `1 1 with p. x` yields the result `1+x`, and `(1 1 with p. * 1 1 with p.) x` yields `(1+x)^2`. Determine (by hand and by computer) the coefficients of polynomials equivalent to further powers of `1+x`. Compare your results with the table of binomial coefficients `!table i.8`.

As shown in Section 6B, the list `d` obtained by multiplying a list of coefficients `c` by its indices `i.#c` and then deleting the leading element gives the polynomial `d with p.` that is the *derivative* or *rate of change* of the function `c with p. `. Thus:

```
   c=:1 2 1
   c
1 2 1
   i.#c
0 1 2
   c*i.#c
0 2 2
   d=:2 2
   x=:i:3
   x
_3 _2 _1 0 1 2 3
   (c with p. ,: d with p.) x
 4  1 0 1 4 9 16
_4 _2 0 2 4 6  8
```

Use the expression `PLOT x;(c with p. ,: d with p.) x` to plot the function together with its derivative, and observe that the derivative does represent the rate of change. Repeat for other polynomials.

Use the derivative operator `d.1` (discussed in Chapter 6) as illustrated below:

```
   c with p. d.1 x
_4 _2 0 2 4 6 8
   c with p. d.1 t. i.5
2 2 0 0 0
```

The operator `d.2` gives the *second derivative*, the derivative of the derivative. Experiment with its use.

Use the Taylor operator `t.` to determine the coessicients of sums, differences, products, and composition of various polynomials.

The operator `d._1` yields the *anti-derivative* or *integral* discussed in Chapter 18. Experiment with its use on various polynomials.

<span id="s4b"></span>

## [S4B. Notes](chapter-04.html#4b)

<span id="s5a"></span>

## [S5A. Introduction](chapter-05.html#5a)

1.  Press key F1 and use the Vocabulary to select the definitions of the functions `! | _1: 3: ]` used in the definition of the power series function `ps` . Then experiment with each of the following "components" of `ps`, and explain their behaviour:

    ```
       a=:4: | ]
       b=:3: = a
       c=:_1: ^ b
       d=:2 with |
       e=: d * c
       f=:% on !
       g=:f * e
    ```

<span id="s5b"></span>

## [S5B. Truncated power series](chapter-05.html#5b)

The function `pg=:% on !` is the power series function for the *growth* or *exponential* function discussed in Chapter 7. Evaluate, plot, and otherwise experiment with, its use.

Experiment with the growth function `g=:(pg 0 1 2 3 4 5 6) with p.` <span id="s5c"></span>

## [S5C. Notes](chapter-05.html#5c)

<span id="s6a"></span>

## [S6A. Approximation to the derivative (rate of change)](chapter-06.html#6a)

<span id="s6b"></span>

## [S6B. Derivatives of polynomials](chapter-06.html#6b)

Compare the behaviours of the functions:

```
   DER=: 1: }. ] * i. on #
   der=: 1: |. ] * i. on #
```

Note that their results are equivalent as polynomial coefficients, but that the latter has the (sometimes convenient) property of yielding a result with the same number of elements as the argument.

The point where the derivative of a function `f` reaches its lowest point (and therefore changes from decreasing to increasng) is called a *point of inflection* of `f`. Enter the following expressions, and comment on the resulting graphs:

```
der=: 1: |. ] * i. on #
c=: 4 _3 _2 1
PLOT x2;(c with p.,(der c)with p.,:(der der c)with p.)x2
```

<span id="s6c"></span>

## [S6C. Taylor coefficients](chapter-06.html#6c)

Experiment with the approximations to the exponential, sine, and cosine functions and their derivatives given in Section 6C, by applying them to the following argument:

```
   x=: i: 1j5
   x
_1 _0.6 _0.2 0.2 0.6 1
```

<span id="s6d"></span>

## [S6D. Notes](chapter-06.html#6d)

<span id="s7a"></span>

## [S7A. Growth polynomials](chapter-07.html#7a)

Execute the following expressions, and comment on the results:

```
   x=:i:2
   x
   ^x
   ^ - x
   %^x
   (^x)*(^-x)
   (^*^ on -) x
```

<span id="s7b"></span>

## [S7B. The name Exponential](chapter-07.html#7b)

<span id="s8a"></span>

## [S8A. Introduction](chapter-08.html#8a)

Plot the sine and cosine functions together, using the argument `y=:i:3j100`. <span id="s8b"></span>

## [S8B. Harmonics](chapter-08.html#8b)

For a discussion of Harmonic Analysis see Chapter 31 of Gullberg \[20\]. <span id="s8c"></span>

## [S8C. Decay](chapter-08.html#8c)

<span id="s9a"></span>

## [S9A. Inverse](chapter-09.html#9a)

Experiment with the use of the inverse adverb on other functions in expressions such as:

```
   INV=:^:_1
   a=:i.5
   a
0 1 2 3 4
   ^&3 a
0 1 8 27 64
   ^&3 INV a
0 1 1.25992 1.44225 1.5874
   ^&3 ^&3 INV a
0 1 2 3 4
   ^&1r3 a
0 1 1.25992 1.44225 1.5874
   
   ^ a
1 2.71828 7.38906 20.0855 54.5982
   ^INV ^ a
0 1 2 3 4
   
   a+2
2 3 4 5 6
   !a+2
2 6 24 120 720
   ! INV ! a+2
2 3 4 5 6
```

<span id="s9b"></span>

## [S9B. Equations](chapter-09.html#9b)

Repeat the first few steps of Section 9B to find approximations to the root of the function `g` defined therein. <span id="s9c"></span>

## [S9C. The method of false position](chapter-09.html#9c)

Define the function `g` as follows:

```
   c=: 4 6 _8 2
   g=: c with p.
```

Use the function `tighten` of Section 9C with the initial bracket `ab=: _1 1` to get approximations to one of the roots of `g`.

Then use other initial brackets to approximate the other two roots, and apply `g` to the results to confirm that they are indeed (near) roots. Compare your roots with the result of `p. c `.

Experiment with other polynomial functions. Note that a polynomial will have one less root than the number of elements in its coefficient, but that some of them will be *complex* in the sense defined in Chapter 19.

The method of false position will find only the *real* (that is, non-complex) roots. The result of `p. c` shows each complex root with a `j` separating its *real* and *imaginary* parts. <span id="s9d"></span>

## [S9D. Newton's method](chapter-09.html#9d)

Apply Newton's method to obtain the roots of various polynomials. <span id="s9e"></span>

## [S9E. Roots of Polynomials](chapter-09.html#9e)

Pages 87-88 of Gullberg \[20\] give a brief history of complex numbers. Gullberg uses the conventional notation *i* for the *imaginary* square root of negative one, and *a+bi* for the *complex* number obtained by adding the real number *a* to the product of the real number *b* with the imaginary *i*.

We will use the *function* `j.` which multiplies its single argument by the square root of negative one, and which forms a complex number from two arguments. For example:

```
   j.4
0j4
   (j.4)*(j.4)
_16
   3+j.4
3j4
   3 j. 4
3j4
   
   3j4 * 5j12
_33j56
   
   (3*5)+(3*0j12)+(0j4*5)+(0j4*0j12)
_33j56
```

The last result illustrates the fact that the multiplication of complex numbers follows the normal rules for the product of the sums of their components (`3 0j4 5` and `0j12`).

Experiment with multiplying other pairs of complex numbers. In particular, verify that the product of `3j4` with its *conjugate* `3j_4` yields a real number.

The (monadic) function `+` yields the conjugate of its argument. For example:

```
   +5j12
5j_12
   5j12 * +5j12
169
   %: 5j12 * +5j12
13
   | 5j12 
13
```

The foregoing illustrates that the square root of the product of a number with its conjugate is its *magnitude* (given by the function `|`). Verify that the magnitude of a real number is itself, as is its conjugate. <span id="s9f"></span>

## [S9F. Logarithms](chapter-09.html#9f)

<span id="s10a"></span>

## [S10A. Introduction](chapter-10.html#10a)

<span id="s10b"></span>

## [S10B. Word formation](chapter-10.html#10b)

<span id="s10c"></span>

## [S10C. Parsing](chapter-10.html#10c)

<span id="s10d"></span>

## [S10D. Conventional Mathematical Notation](chapter-10.html#10d)

<span id="s11a"></span>

## [S11A. Introduction](chapter-11.html#11a)

<span id="s11b"></span>

## [S11B. Informal proofs](chapter-11.html#11b)

Write an informal proof that `+/i.n` (the sum of the first `n` non-negative integers) is equivalent to `n*(n-1)%2`.

Make a table of the sum of squares (`+/*:i.n`) and try to find an equivalent expression that is easier to calculate. Then write an informal proof of the discovered relation. <span id="s11c"></span>

## [S11C. Formal proofs](chapter-11.html#11c)

Make formal proofs of the informal proofs of Section S11B. <span id="s11d"></span>

## [S11D. Inductive proofs](chapter-11.html#11d)

Make inductive proofs for the relations found in Section S11B. <span id="s11e"></span>

## [S11E. Recursive definition](chapter-11.html#11e)

Enter the following recursive definitions and apply the resulting functions to integer arguments to learn what you can about them:

```
   f=:1:`(+//.@(,:~)@($:@<:))@.*
   
   g=:1:`((],+/@(_2&{.))@$:@<:)@.*
```

See page 286 of Gullberg for a discussion of Fibonacci numbers. <span id="s11f"></span>

## [S11F. Guessing games](chapter-11.html#11f)

<span id="s12a"></span>

## [S12A. Anagrams](chapter-12.html#12a)

Execute the following:

```
a=: 'episcopal'
p=:1 0 6 3 2 4 5 8 7
p{a
!#a  NB. Number of permutations of a
index=: A. p
index
index A. a
```

<span id="s13a"></span>

## [S13A. Introduction](chapter-13.html#13a)

Define Boolean functions to determine various properties of numbers. For example, is a number the square of an integer; is it a cube; is it a prime? Consult the Vocabulary for functions concerning primes. <span id="s13b"></span>

## [S13B. Or, and, and not](chapter-13.html#13b)

When restricted to the arguments zero and one, multiplication is equivalent to the *and* function, and Boole used the symbol for multiplication to represent it. The analogy between *or* and addition is less compelling, but Boole used `+` for *or*. In a broader domain it is necessary to distinguish between the arithmetic and logical functions, and we therefore use ` + *` for the arithmetic functions, and `+. *.` for the logical.

Consult the Vocabulary for the significance of other arithmetic functions used as Booleans. Also note that `p <: q` tests whether `p` *implies* `q`. <span id="s13c"></span>

## [S13C. Lists and sets](chapter-13.html#13c)

Write functions to define the set of fricatives in the English alphabet. Do likewise for the set of all non-negative integers that are divisible by either `2` or `5`. <span id="s13d"></span>

## [S13D. Classification](chapter-13.html#13d)

Study the discussion of *classification* in the J Dictionary: Click on Help/Dictionary/Sample Topics/8. Classification. <span id="s14a"></span>

## [S14A. Introduction](chapter-14.html#14a)

<span id="s14b"></span>

## [S14B. Commutativity](chapter-14.html#14b)

<span id="s14c"></span>

## [S14C. Associativity](chapter-14.html#14c)

The functions `+` and `*` were seen to be both associative and commutative, whereas `-` and `%` were neither associative nor commutative. Try to find a function that is commutative but not associative.

Hint: Consult the Vocabulary for the functions `+:` (not-or) and `*:` (not-and).

An associative function `g` defined on a domain `d` is said to form a *group* if the table `d g/ d` has the following properties:

a\) there is a *unit element* `e` such that `e&g` and `g&e` are identity functions; that is, both `e&g d` and `g&e d` yield `d`.

b\) Each element `x` of `d` has an *inverse* `xi` in `d` such that `(x&g)@(xi&)` is the identity function.

For example:

```
   d=:0 1 2 3
   
   g=:4&|@+    NB. Addition modulo 4
   
   d g table d
+-+-------+
| |0 1 2 3|
+-+-------+
|0|0 1 2 3|
|1|1 2 3 0|
|2|2 3 0 1|
|3|3 0 1 2|
+-+-------+
```

In the foregoing table it is clear that `0` is the identity element. Thus:

```
   e=:0        NB. Identity element
   
   e&g d
0 1 2 3
   
   g&e d
0 1 2 3
```

Moreover, a little experimentation will show that `3` is the inverse of `1`, and that `2` is self-inverse:

```
   1 g d
1 2 3 0
   
   3 g 1 g d   NB. 3 is inverse of 1
0 1 2 3
   
   2 g d
2 3 0 1
   
   2 g 2 g d   NB. 2 is self-inverse
0 1 2 3
```

A group function on a given domain may also form a *subgroup* on a subset of the domain. For example:

```
   0 2 g table 0 2
+-+---+
| |0 2|
+-+---+
|0|0 2|
|2|2 0|
+-+---+
```

A function on the domain of the leading integers can be easily mapped onto another domain, so as to give a more abstract appearance to a group. For example:

```
   ad=:'ABCD'
   
   map=: ad&i."0
   
   map ad
0 1 2 3
   
   ad g&.map table ad
+-+----+
| |ABCD|
+-+----+
|A|ABCD|
|B|BCDA|
|C|CDAB|
|D|DABC|
+-+----+
```

Define a group of order eight as follows:

```
   d=:i.8
   
   g=:8&|@+
```

Then display the group table, and try to find any subgroups. Also show that the element `1` is a *generator* of the group by entering the expression `1&g ^:(i.12) d`. The result shows that the powers of the function `1&g` generate all rows of the group table. <span id="s14d"></span>

## [S14D. Symmetry](chapter-14.html#14d)

<span id="s14e"></span>

## [S14E. Distributivity](chapter-14.html#14e)

<span id="s14f"></span>

## [S14F. Distributivity of dyadic functions](chapter-14.html#14f)

<span id="s14g"></span>

## [S14G. Parity](chapter-14.html#14g)

<span id="s15a"></span>

## [S15A. Dot product and vector functions](chapter-15.html#15a)

It is important to note that the expression `dp=:+/ . *`*must* include a space before the dot, for otherwise the phrase `/.` would be recognized as the single entity that represents the *oblique* operator as shown in the Vocabulary. Compare the results of applying the word-formation function `;:` to the lists `'+/ . *'` and `'+/. *'` . <span id="s15b"></span>

## [S15B. Dot product as a linear function](chapter-15.html#15b)

If `sop=:+/\` (sum over prefixes), then `sopinv=: sop^:_1` is its inverse.Test this assertion by entering expressions such as `sopinv sop x=:2 3 5 7 11` and `sop sopinv x`.

Guess at the value of a matrix `mi` such that `mi & dp=:+/ . *` is equivalent to the function `sopinv`. Compare your guess with the result of applying `sopinv` to an identity matrix. <span id="s15c"></span>

## [S15C. Matrix inverse](chapter-15.html#15c)

<span id="s16a"></span>

## [S16A. Ascending and descending order of exponents](chapter-16.html#16a)

<span id="s16b"></span>

## [S16B. Products of polynomials](chapter-16.html#16b)

<span id="s16c"></span>

## [S16C. Multiplication of decimal numbers](chapter-16.html#16c)

A function to perform the normalization described in Section 16C (to reduce a list to an equivalent list with elements less than the base) can be defined (using the Explicit Definition described in Section 17C) as follows:

```
NORM=:4 : 0
  base=. x.
  list=: y.
result=. i.0
 carry=. 0

while. 0&lt;#list do.
next=. carry + {: list   NB. carry plus last of list
list=. }: list           NB. Delete last from list
rem=. base | next        NB. Remainder on div by base
result=. rem , result    
carry=. (next-rem) % base
end.

result
)
```

For example:

```
   a=: 2 34 56
   c=:10 NORM a
   c
5 9 6
   10 #. a  NB. Base 10 value of a
596
   10 #. c
596
```

However, an argument such as `23 4 5` requires a result with more elements than the argument, and the function `NORM` fails to account for this. Thus:

```
   b=: 23 4 5
   10 NORM b
3 4 5
```

The following function produces the correct result:

```
norm=:4 : 0
  base=. x.
  list=: y.
result=. i.0
 carry=. 0

while. -.*./0=carry,list do. NB. Not all zero
next=. carry + {: list   NB. carry plus last of list
list=. 0,}: list         NB. Delete last from list
rem=. base | next        NB. Remainder on div by base
result=. rem , result    
carry=. (next-rem) % base
end.

result
)

   10 norm b
2 3 4 5
```

Choose a pair of rather large numbers (of eight or more digits) and multiply them by the conventional method taught in elementary school. Then multiply them by the method given in Section 16C and compare the results. <span id="s16d"></span>

## [S16D. Other bases](chapter-16.html#16d)

Use the function `norm` of Section S16C with bases other than `10`. Also define and use the functions `n10=: 10 with norm` and `n2=:2 with norm`.

Repeat the exercise suggested in Section S16C, but using base `8`. <span id="s16e"></span>

## [S16E. Remainder, divisibility, and integer part](chapter-16.html#16e)

A prime number is one that has exactly two distinct divisors. Sum the columns of a divisibility table, and use the foregoing fact to identify the primes. <span id="s16f"></span>

## [S16F. Notes](chapter-16.html#16f)

<span id="s17a"></span>

## [S17A. Introduction](chapter-17.html#17a)

<span id="s17b"></span>

## [S17B. Designing an algorithm](chapter-17.html#17b)

<span id="s17c"></span>

## [S17C. Explicit definition](chapter-17.html#17c)

<span id="s18a"></span>

## [S18A. Introduction](chapter-18.html#18a)

<span id="s18b"></span>

## [S18B. Area under a graph as a function](chapter-18.html#18b)

<span id="s18c"></span>

## [S18C. Polynomial approximations](chapter-18.html#18c)

<span id="s19a"></span>

## [S19A. Imaginary numbers](chapter-19.html#19a)

<span id="s19b"></span>

## [S19B. Complex numbers](chapter-19.html#19b)

<span id="s19c"></span>

## [S19C. Division](chapter-19.html#19c)

<span id="s19d"></span>

## [S19D. The Exponential family](chapter-19.html#19d)

<span id="s20a"></span>

## [S20A. Introduction](chapter-20.html#20a)

<span id="s20b"></span>

## [S20B. Mathematics: from the Birth of Numbers](chapter-20.html#20b)

<span id="s20c"></span>

## [S20C. Concrete mathematics](chapter-20.html#20c)

<span id="s20d"></span>

## [S20D. Computer resources](chapter-20.html#20d)

<span id="s20e"></span>

## [S20E. Conclusion](chapter-20.html#20e)
