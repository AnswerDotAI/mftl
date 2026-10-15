---
title: "2: Computer Use and Experimentation"
anchor: "2-computer-use-and-experimentation"
previous: "chapter-01.html"
next: "chapter-03.html"
---

[2A. Introduction](#2a)

[2B. Number of places](#2b)

[2C. Displays](#2c)

[2D. Integer Lists](#2d)

[2E. Vocabulary](#2e)

[2F. Functions over lists](#2f)

[2G. Notes](#2g)

<span id="2a"></span>

## [2A. Introduction](#2-computer-use-and-experimentation) [S2A.](supplement.html#s2a)

A computer can be programmed to “interpret” or “execute” sentences expressed in a variety of *notations* or *programming languages*; commonly used languages include Cobol, Fortran, APL, C, and J. The treatment of numbers in Chapter 1 is all expressed in J, a system that can be obtained from Website www.jsoftware.com .

A computer-executed language such as J not only permits one to do extensive calculations quickly and accurately, it may also permit precise experimentation with mathematical ideas. In particular, J provides computation both in the rational arithmetic used in Chapter 1, and in the more familiar decimal notation.

For example, a list of rationals such as `r=: 1r5 2r5 3r5 4r5 5r5 6r5` and a list of integers `a=: 5 * r` derived from it will produce results expressed as rationals when functions such as addition, multiplication, and division are applied to them. Thus:

```
   r=: 1r5 2r5 3r5 4r5 1 6r5
   a=: 5 * r
   % table a
+-+---------------------+
| |1   2   3   4   5   6|
+-+---------------------+
|1|1 1r2 1r3 1r4 1r5 1r6|
|2|2   1 2r3 1r2 2r5 1r3|
|3|3 3r2   1 3r4 3r5 1r2|
|4|4   2 4r3   1 4r5 2r3|
|5|5 5r2 5r3 5r4   1 5r6|
|6|6   3   2 3r2 6r5   1|
+-+---------------------+

   % table r
+---+-----------------------+
|   |1r5 2r5 3r5 4r5   1 6r5|
+---+-----------------------+
|1r5|  1 1r2 1r3 1r4 1r5 1r6|
|2r5|  2   1 2r3 1r2 2r5 1r3|
|3r5|  3 3r2   1 3r4 3r5 1r2|
|4r5|  4   2 4r3   1 4r5 2r3|
|  1|  5 5r2 5r3 5r4   1 5r6|
|6r5|  6   3   2 3r2 6r5   1|
+---+-----------------------+
```

However, the list `c=: 1 2 3 4 5 6`, which is identical to `a` except that it is not defined as a rational, yields decimal approximations under division. Thus:

```
   c=: 1 2 3 4 5 6
   % table c
+-+--------------------------------+
| |1   2        3    4   5        6|
+-+--------------------------------+
|1|1 0.5 0.333333 0.25 0.2 0.166667|
|2|2   1 0.666667  0.5 0.4 0.333333|
|3|3 1.5        1 0.75 0.6      0.5|
|4|4   2  1.33333    1 0.8 0.666667|
|5|5 2.5  1.66667 1.25   1 0.833333|
|6|6   3        2  1.5 1.2        1|
+-+--------------------------------+
```

It should be noted that the inclusion of even one rational in a list makes it behave as a rational.

The function `x:` applied to an argument causes its result to be treated as a rational when other functions are applied to it. Moreover, its inverse causes functions applied to its results to treat it in decimal form. Thus:

```
   rat=: x:
   dec=: rat^:_1
     
   d=: rat c
   d
1 2 3 4 5 6
   % table d
+-+---------------------+
| |1   2   3   4   5   6|
+-+---------------------+
|1|1 1r2 1r3 1r4 1r5 1r6|
|2|2   1 2r3 1r2 2r5 1r3|
|3|3 3r2   1 3r4 3r5 1r2|
|4|4   2 4r3   1 4r5 2r3|
|5|5 5r2 5r3 5r4   1 5r6|
|6|6   3   2 3r2 6r5   1|
+-+---------------------+
   e=: dec d
   e
1 2 3 4 5 6
   % table e
+-+--------------------------------+
| |1   2        3    4   5        6|
+-+--------------------------------+
|1|1 0.5 0.333333 0.25 0.2 0.166667|
|2|2   1 0.666667  0.5 0.4 0.333333|
|3|3 1.5        1 0.75 0.6      0.5|
|4|4   2  1.33333    1 0.8 0.666667|
|5|5 2.5  1.66667 1.25   1 0.833333|
|6|6   3        2  1.5 1.2        1|
+-+--------------------------------+
```

**Exercises**

1.  To gain familiarity with the use of the computer, enter some of the expressions from Chapter 1, and compare the results with those shown in the text.

<span id="2b"></span>

## [2B. Number of places](#2-computer-use-and-experimentation) [S2B.](supplement.html#s2b)

The precision of the decimal approximations in the table `% table c` is limited to six digits after the decimal point. This is a matter of convenience in display -- the results are actually computed to about eighteen decimal digits, of which only the first few are shown.

The following function may be defined and used to display any number of digits:

```
   set=: 9!:11  
   set 12
   2 % 3
0.666666666667
   dec 2r3
0.666666666667
   set 6
```

<span id="2c"></span>[](#2-computer-use-and-experimentation)

## 2C. Displays

[S2C.](supplement.html#s2c) Tables and other results may also be displayed for convenient comparison, using the comma-dot to place them side-by-side, and the comma to place one table below another. For example:

```
   (+ table r),.(- table r)
+---+-------------------------+---+----------------------------+
|   |1r5 2r5 3r5 4r5    1  6r5|   |1r5  2r5  3r5  4r5    1  6r5|
+---+-------------------------+---+----------------------------+
|1r5|2r5 3r5 4r5   1  6r5  7r5|1r5|  0 _1r5 _2r5 _3r5 _4r5   _1|
|2r5|3r5 4r5   1 6r5  7r5  8r5|2r5|1r5    0 _1r5 _2r5 _3r5 _4r5|
|3r5|4r5   1 6r5 7r5  8r5  9r5|3r5|2r5  1r5    0 _1r5 _2r5 _3r5|
|4r5|  1 6r5 7r5 8r5  9r5    2|4r5|3r5  2r5  1r5    0 _1r5 _2r5|
|  1|6r5 7r5 8r5 9r5    2 11r5|  1|4r5  3r5  2r5  1r5    0 _1r5|
|6r5|7r5 8r5 9r5   2 11r5 12r5|6r5|  1  4r5  3r5  2r5  1r5    0|
+---+-------------------------+---+----------------------------+

  (* table a),(* table r)
+---+--------------------------------+
|   |        1  2  3  4  5  6        |
+---+--------------------------------+
| 1 |        1  2  3  4  5  6        |
| 2 |        2  4  6  8 10 12        |
| 3 |        3  6  9 12 15 18        |
| 4 |        4  8 12 16 20 24        |
| 5 |        5 10 15 20 25 30        |
| 6 |        6 12 18 24 30 36        |
+---+--------------------------------+
|   | 1r5   2r5   3r5   4r5   1   6r5|
+---+--------------------------------+
|1r5|1r25  2r25  3r25  4r25 1r5  6r25|
|2r5|2r25  4r25  6r25  8r25 2r5 12r25|
|3r5|3r25  6r25  9r25 12r25 3r5 18r25|
|4r5|4r25  8r25 12r25 16r25 4r5 24r25|
|  1| 1r5   2r5   3r5   4r5   1   6r5|
|6r5|6r25 12r25 18r25 24r25 6r5 36r25|
+---+--------------------------------+
```

Function tables may also be produced without their bordering arguments by using the operator `/`, and other functions may be applied to such tables. For example:

```
    a %/ a
1 1r2 1r3 1r4 1r5 1r6
2   1 2r3 1r2 2r5 1r3
3 3r2   1 3r4 3r5 1r2
4   2 4r3   1 4r5 2r3
5 5r2 5r3 5r4   1 5r6
6   3   2 3r2 6r5   1

   (a %/ a)*(a */ a)
 1  1  1  1  1  1
 4  4  4  4  4  4
 9  9  9  9  9  9
16 16 16 16 16 16
25 25 25 25 25 25
36 36 36 36 36 36
```

<span id="2d"></span>[](#2-computer-use-and-experimentation)

## 2D. Integer Lists

[S2D.](supplement.html#s2d) `i.5` produces a list of the first five non-negative integers, and `i:5` produces a symmetric list from `_5` to `5`. Both are convenient for exploring tables:

```
      (* table i.5),.(* table i:5)
+-+-----------+--+---------------------------------------+
| |0 1 2  3  4|  | _5  _4  _3  _2 _1 0  1   2   3   4   5|
+-+-----------+--+---------------------------------------+
| |           |_5| 25  20  15  10  5 0 _5 _10 _15 _20 _25|
| |           |_4| 20  16  12   8  4 0 _4  _8 _12 _16 _20|
| |           |_3| 15  12   9   6  3 0 _3  _6  _9 _12 _15|
|0|0 0 0  0  0|_2| 10   8   6   4  2 0 _2  _4  _6  _8 _10|
|1|0 1 2  3  4|_1|  5   4   3   2  1 0 _1  _2  _3  _4  _5|
|2|0 2 4  6  8| 0|  0   0   0   0  0 0  0   0   0   0   0|
|3|0 3 6  9 12| 1| _5  _4  _3  _2 _1 0  1   2   3   4   5|
|4|0 4 8 12 16| 2|_10  _8  _6  _4 _2 0  2   4   6   8  10|
| |           | 3|_15 _12  _9  _6 _3 0  3   6   9  12  15|
| |           | 4|_20 _16 _12  _8 _4 0  4   8  12  16  20|
| |           | 5|_25 _20 _15 _10 _5 0  5  10  15  20  25|
+-+-----------+--+---------------------------------------+
```

**Exercises**

Examine the second multiplication table above, and formulate a rule for the sign of a product in terms of the signs of its factors.

Examine the rows and columns, and give reasons for the alternation of signs between quadrants.

The *signum* or *sign* function denoted by `*` gives `_1` for a negative argument, `0` for a zero argument, and `1` for a positive argument. When applied on (that is, to the result of) multiplication it yields a table that shows the pattern of the signs in the multiplication table more clearly. Thus:

```
   sign=: *
     on=: @
	 
   (sign on *) table i:5
+--+-------------------------------+
|  |_5 _4 _3 _2 _1 0  1  2  3  4  5|
+--+-------------------------------+
|_5| 1  1  1  1  1 0 _1 _1 _1 _1 _1|
|_4| 1  1  1  1  1 0 _1 _1 _1 _1 _1|
|_3| 1  1  1  1  1 0 _1 _1 _1 _1 _1|
|_2| 1  1  1  1  1 0 _1 _1 _1 _1 _1|
|_1| 1  1  1  1  1 0 _1 _1 _1 _1 _1|
| 0| 0  0  0  0  0 0  0  0  0  0  0|
| 1|_1 _1 _1 _1 _1 0  1  1  1  1  1|
| 2|_1 _1 _1 _1 _1 0  1  1  1  1  1|
| 3|_1 _1 _1 _1 _1 0  1  1  1  1  1|
| 4|_1 _1 _1 _1 _1 0  1  1  1  1  1|
| 5|_1 _1 _1 _1 _1 0  1  1  1  1  1|
+--+-------------------------------+   
```

The pattern of signs in the multiplication table may be made more understandable by considering the behaviour of individual rows and columns: each proceeds by "counting by" the number at its head. For example, the row headed by `3` begins with `_15`, and proceeds by steps of three through `_12` and `_9` to `15`. At some point it passes through the column of zeros, and the result must therefore change sign. Similar remarks apply to "counting by negative numbers", and to columns. <span id="2e"></span>[](#2-computer-use-and-experimentation)

## 2E. Vocabulary

[S2E.](supplement.html#s2e) The complete J vocabulary can be displayed by pressing the key labelled F1, can then be printed as indicated, and can be closed by pressing the Escape key (labelled Esc). With the vocabulary displayed, the complete definition of any of its items may be displayed (and perhaps printed) by clicking the mouse on the desired item.

It may be interesting to explore the behaviour of various functions by producing their tables, either before or after studying their definitions. Moreover, it may be helpful to first assign more familiar names. For example:

```
   gcd=: +.
   lcm=: *.
   (gcd table ,. lcm table) a
+-+-----------+-+----------------+
| |1 2 3 4 5 6| |1  2  3  4  5  6|
+-+-----------+-+----------------+
|1|1 1 1 1 1 1|1|1  2  3  4  5  6|
|2|1 2 1 2 1 2|2|2  2  6  4 10  6|
|3|1 1 3 1 1 3|3|3  6  3 12 15  6|
|4|1 2 1 4 1 2|4|4  4 12  4 20 12|
|5|1 1 1 1 5 1|5|5 10 15 20  5 30|
|6|1 2 3 2 1 6|6|6  6  6 12 30  6|
+-+-----------+-+----------------+
```

Composite functions can also be tabled. For example:

```
   ((lcm */ gcd) table ,. (* table)) a
+-+----------------+-+----------------+
| |1  2  3  4  5  6| |1  2  3  4  5  6|
+-+----------------+-+----------------+
|1|1  2  3  4  5  6|1|1  2  3  4  5  6|
|2|2  4  6  8 10 12|2|2  4  6  8 10 12|
|3|3  6  9 12 15 18|3|3  6  9 12 15 18|
|4|4  8 12 16 20 24|4|4  8 12 16 20 24|
|5|5 10 15 20 25 30|5|5 10 15 20 25 30|
|6|6 12 18 24 30 36|6|6 12 18 24 30 36|
+-+----------------+-+----------------+
```

**Exercises**

Choose other functions from the Vocabulary for experiments such as:

```
   < table a
   ((< table ,. > table),(<: table,.= table)) a
```

Make and study tables for the greatest common divisor (`gcd=: +.`) and the least common multiple (`lcm=: *.`).

Exercise 3 of Section 1J asked to formulate rules for multiplying rational numbers. Re- examine the matter using the `gcd` function and the function `nd=: 2&x:` that gives the numerator and denominator (as a two-element list) of a rational number.

Extend the discussion of the preceding exercise to the division of rationals.

Use `i.` and `i:` to make tables of the comparison functions `<` and `>` and `=` .

Make tables for `<.` (minimum) and `>.` (maximum).

Make the table `! table i.5`, and comment on the results.

The expression `3!5` gives the number of distinct collections of three items that can be chosen from a collection of five distinct items. For example, here are the ways of choosing three at a time from the first five letters of the alphabet:

```
   ABC
   ABD
   ABE
   ACD
   ACE
   ADE
   BCD
   BCE
   BDE
   CDE
```

The function `!` might therefore be called `outof` but, for reasons that will appear later, we will call it the *binomial coefficient* function, and abbreviate it as `bc`. If the zeros in the table produced in Exercise 7 are ignored, a triangle remains. This triangle (or some orientation of it) is (wrongly, according to Hogben, p194) called Pascal’s triangle.

Functions for other useful lists are easily defined:

```
   even=:  2:*i.
    odd=:  1:+2:*i.
    pow=:  2:^i.
     i1=:  1:+i.
     i2=:  2:+i.
   (even,.odd,.pow,.i1,.i2) 6
 0  1  1 1 2
 2  3  2 2 3
 4  5  4 3 4
 6  7  8 4 5
 8  9 16 5 6
10 11 32 6 7
```

The expressions `2^3` and `2^2` are defined by `2*2*2` and `2*2`, respectively, but it is not clear what this implies for `2^1` (multiplication with one factor?) or for `2^0` and `2^_1`. Function tables give clues to the pattern to be expected:

```
   2 3 ^ table 2 3 4 5
+-+-----------+
| |2  3  4   5|
+-+-----------+
|2|4  8 16  32|
|3|9 27 81 243|
+-+-----------+
```

The patterns progress to the right by multiplying by the argument (`2` or `3`); conversely they progress to the left by dividing by the argument, giving the following results for the exponents `1` and `0`, and for negative exponents:

```
   2 3 ^ table 0 1 2 3 4 5
+-+---------------+
| |0 1 2  3  4   5|
+-+---------------+
|2|1 2 4  8 16  32|
|3|1 3 9 27 81 243|
+-+---------------+

   2 3 ^ table i:5r1
+-+---------------------------------------+
| |   _5   _4   _3  _2  _1 0 1 2  3  4   5|
+-+---------------------------------------+
|2| 1r32 1r16  1r8 1r4 1r2 1 2 4  8 16  32|
|3|1r243 1r81 1r27 1r9 1r3 1 3 9 27 81 243|
+-+---------------------------------------+

   ^ table i:5r1
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

<span id="2f"></span>[](#2-computer-use-and-experimentation)

## 2F. Functions over lists

[S2F.](supplement.html#s2f) The expression `1+4+1+4+2` is said to apply addition *over* the list `1 4 1 4 2`. This sum may also be expressed by applying the *over* adverb `/` to the function `+`, as in `+/1 4 1 4 2`. It may be applied to other functions similarly:

```
   a=: 1 4 1 4 2
   +/a
12
   */a
32
   >./a
4
   +./a
1
   *./a
4
   n=: 6
   b=: i1 n
   b
1 2 3 4 5 6
   +/b
21
   */b
720
```

The `/` used in the expressions `+/` and `*/` is called an *adverb* because it applies to a verb to produce a related verb. In math, an adverb is also called an *operator*, a rather non-committal term adopted by the mathematician Oliver Heaviside about a century ago.

The sum `+/` and the list `i.` can be used to clarify (or at least re-express) the polynomial function introduced in Section 1I. Thus:

```
   x=: 4
   c=: 2 3 4
   c p. x
78
   x^0 1 2
1 4 16
   c*x^0 1 2
2 12 64
   +/c*x^0 1 2
78
   +/c*x^i.3
78
```

In the final expression above it was essential that the argument `3` equalled the number of items in the list of coefficients. This can be expressed for any coefficient list by using the number function `#` as follows:

```
   #c
3
   i.#c
0 1 2
   +/c*x^i.#c
78
   d=: 1 4 6 4 1
   +/d*x^i.#d
625
   (d p. x),(x+1)^4
625 625
```

<span id="2g"></span>[](#2-computer-use-and-experimentation)

## 2G. Notes

[S2G.](supplement.html#s2g) These two chapters have provided numerous examples of the evaluation of a variety of functions, but have not provided proofs or demonstrations of the properties of these functions or of relations among them.

On the other hand, the use of lists and tables has provided organized presentations of these examples that make it easy to recognize properties -- properties such as the commutativity of the functions plus, times, maximum, and greatest common divisor in the symmetry of their tables, as well as certain “skew-symmetries” evident in the tables for subtraction, division, and less-than.

Careful study of function tables can provide other insights such as the “counting by a constant” that occurs in rows and columns of certain functions, leading, in particular, (in Section 2D) to an informal proof or demonstration of the necessity for the familiar behaviour of the products of signed numbers -- the product of numbers of opposite signs is negative, and the product of two of the same sign is positive.

Conclusions about functions (such as the relation of prime numbers to the multiplication table, and rules for the multiplication of rational numbers) have been left to Exercises, as in those for Sections 1G and 1J. It is important to attempt these Exercises -- to repeat Hogben’s advice: “What you get out of the book depends on your co-operation in the business of learning”.

Nevertheless, we will devote some attention to deriving certain relations, and will devote a separate chapter (11) to the treatment of proofs. Similarly in the matter of language (whose importance is so strongly stated by Hogben in the paragraph shown in our preface), we have introduced the necessary notation in context with no general discussion of the grammar involved, and will defer such matters to a separate chapter (10).

However, these cited chapters are relatively self-contained, and can be consulted at any point. But first we will introduce graphing as a further tool for making certain mathematical relations evident. Concerning graphs, Hogben has this to say (p 86):

> A third kind of pictorial language used in mathematics has its origin in the construction of star maps and later of earth maps in the last two centuries before the beginning of the Christian era.
>
> Such is co-ordinate geometry for which the slang word is graphs. It did not come into its own before the century of Newton, whereafter it led to many discoveries.
>
> Unlike Euclid’s geometry, it can bring the measurement of time into the picture. For instance, it exposes (Fig. 1) why and when Achilles (pp 12-13) caught up with (and passed) the tortoise.
