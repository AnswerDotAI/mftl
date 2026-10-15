---
title: "16: Polynomials and NUMBER SYSTEMS"
anchor: "16-polynomials-and-number-systems"
previous: "chapter-15.html"
next: "chapter-17.html"
---

[16A. Ascending and descending order of exponents](#16a)

[16B. Products of polynomials](#16b)

[16C. Multiplication of decimal numbers](#16c)

[16D. Other bases](#16d)

[16E. Remainder, Divisibility, and Integer part](#16e)

[16F. Notes](#16f)

<span id="16a"></span>

## [16A. Ascending and descending order of exponents](#16-polynomials-and-number-systems) [S16A.](supplement.html#s16a)

In conventional mathematics, polynomials are sometimes expressed with the exponents in ascending order (beginning with zero), and sometimes in descending order (beginning with the largest exponent). Thus:

ax<sup>0</sup>+bx<sup>1</sup>+cx<sup>2</sup>+dx<sup>3</sup>

ax<sup>3</sup>+bx<sup>2</sup>+cx<sup>1</sup>+dx<sup>0</sup>

Descending order is commonly used in high school, but ascending order is more suitable in advanced math, because in truncated power series a “largest exponent” may not be clearly identified.

To compare these schemes we will define two functions called `pa` (for ascending order), and `pd` (for descending). The former is the function `p.` that we have used in earlier chapters, and the latter may be expressed in terms of it using the reversal function (`|.`) to reverse the order of the coefficients. Thus:

```
   pa=: p.
   pd=: |. on [ pa ]
   x=: 0 1 2 3 4 5
   1 2 3 pa x
1 6 17 34 57 86
   1 2 3 pd x
3 6 11 18 27 38
   1 2 3 pd 10
123
```

The final example suggests that a descending polynomial with right argument `10` gives the value in decimal of the digits in the list of coefficients. In fact, the decimal number system (and number systems with bases other than ten) are “polynomial representations” of numbers, and we may find that schemes for multiplying polynomials lead to improved methods of multiplying multi-digit decimal numbers. <span id="16b"></span>

## [16B. Products of polynomials](#16-polynomials-and-number-systems) [S16B.](supplement.html#s16b)

The product of two polynomials `c1 with p.` and `c2 with p.` is itself a polynomial, whose coefficients can be computed from `c1` and `c2` by first forming their multiplication table. For example:

```
   c1=: 2 3 5
   c2=: 4 1 0 3
   c1 * table c2
+-+---------+
| | 4 1 0  3|
+-+---------+
|2| 8 2 0  6|
|3|12 3 0  9|
|5|20 5 0 15|
+-+---------+
```

The coefficient `8` in the upper left corner is the coefficient of `x^0` in the product polynomial, the elements of the next diagonal (`2 12`) are coefficients of `x^1`, the next diagonal has coefficients of `x^2`, and so on. The combined coefficients of successive powers may therefore be obtained by summing diagonals of the table to obtain `c3=: 8 14 23 11 9 15`. Thus:

```
   c3=: 8 14 23 11 9 15
   x=: 0 1 2 3 4 5
   (c1 p. x) * (c2 p. x)
8 80 840 4928 18800 54528
   c3 p. x
8 80 840 4928 18800 54528
```

In the expression `f/.` the oblique operator `/.` produces a function that applies `f` to each of the diagonals of a table argument. Thus:

```
   c1 */ c2
 8 2 0  6
12 3 0  9
20 5 0 15
   +//. c1 */ c2
8 14 23 11 9 15
   c3 = +//. c1 */ c2
1 1 1 1 1 1
```

We may therefore define a function `pc` to produce product coefficients as follows:

```
   pc=:  +//. on (*/)
   c1 pc c2
8 14 23 11 9 15
   1 1 pc 1 1
1 2 1
   1 1 pc 1 1 pc 1 1
1 3 3 1
```

Similar reasoning will show that the same function `pc` produces coefficients for the product of descending polynomials. This may be tested as follows:

```
   c1 pd x
5 10 19 32 49 70
   c2 pd x
3 8 39 120 275 528
   (c1 pd x)*(c2 pd x)
15 80 741 3840 13475 36960
   c3 pd x
15 80 741 3840 13475 36960
```

<span id="16c"></span>

## [16C. Multiplication of decimal numbers](#16-polynomials-and-number-systems) [S16C.](supplement.html#s16c)

The last result of Section 16A indicates that the result of `c pd 10` is the decimal value of the number whose digits are the elements of the list `c`. Thus:

```
   c1=:  1 2 3
   c2=:  1 2 0 3
   (c1 pd 10),(c2 pd 10)
123 1203
```

It follows that the elements of `c1 pc c2` represent the product of the numbers `123` and `1203`. Thus:

```
   ]c3=: c1 pc c2
1 4 7 9 6 9
   c3 pd 10
147969
   123*1203
147969
```

Consequently, the product can be obtained by making the table `c1 * table c2` and summing its diagonals:

```
   c1 * table c2
+-+-------+
| |1 2 0 3|
+-+-------+
|1|1 2 0 3|
|2|2 4 0 6|
|3|3 6 0 9|
+-+-------+
   1,(+/2 2),(+/0 4 3),(+/3 0 6),(+/6 0),9
1 4 7 9 6 9
```

However, these diagonal sums for other arguments may yield results greater than `9`, and therefore themselves be multi-digit numbers. For example:

```
   c4=: 1 2 3 4 5 6 7 
   c5=: 8 7 6 5 4
   ]c6=: c4 pc c5
8 23 44 70 100 130 160 126 92 59 28
   c6 pd 10
108214735818
   1234567*87654
108214735818
```

The result `c6` does correctly represent the product, but it is unsatisfactory in that its multi-digit elements cannot be simply squeezed together (as in `8234470100130160126925928`) to produce the correct product.

An equivalent list of single digits can, however, be obtained by “carrying” all but the final digit to the next higher element, as illustrated in the following sequence:

```
   c6=: 8 23 44 70 100 130 160 126 92 59 28
   c7=: 8 23 44 70 100 130 160 126 92 61 8
   c8=: 8 23 44 70 100 130 160 126 98 1 8
   c9=: 8 23 44 70 100 130 160 135 8 1 8
   c10=: 8 23 44 70 100 130 173 5 8 1 8
   c11=: 8 23 44 70 100 147 3 5 8 1 8
   c12=: 8 23 44 70 114 7 3 5 8 1 8
   c13=: 8 23 44 81 4 7 3 5 8 1 8
   c14=: 8 23 52 1 4 7 3 5 8 1 8
   c15=: 8 28 2 1 4 7 3 5 8 1 8
   c16=: 10 8 2 1 4 7 3 5 8 1 8
   c17=: 1 0 8 2 1 4 7 3 5 8 1 8  
   c6 pd 10
108214735818
   c17 pd 10
108214735818
```

Moreover, the entire *normalization* from `c6` to `c17` can be done easily by hand in a single process. In summary, multiplication of decimal numbers represented by the lists of digits `d1` and `d2` can be performed by hand by writing down the table `d1 * table d2`, summing the diagonals, and “normalizing” the results to single-digit elements (written together without spaces). This process may be compared with the commonly-taught scheme shown below:

```
     1234567
       87654
------------	   
     4938268
    6172835
   7407402
  8641969
 9876536 
------------
108214735818
```

In contrast to the three distinct steps of recording the multiplications in a table, summing its diagonals, and a final normalizion by carry, this conventional scheme combines multiplication and carry in each step of the production of each line, and again uses carrying in the final summation of the several lines.

Not only is this combined multiplication-and-carry more difficult to execute accurately, but the resulting record is almost impossible to check for possible errors except by repeating the entire process – a repetition that invites repetition of the same errors. <span id="16d"></span>

## [16D. Other bases](#16-polynomials-and-number-systems) [S16D.](supplement.html#s16d)

Just as `c pd 10` gives the decimal (or base-`10`) value of `c` as a weighted sum with weights of decreasing powers of `10`, so `c pd 8` gives the base-`8` value, using powers of `8` as weights. For example:

```
   c1=: 1 2 3
   c2=: 1 2 0 3  
   (c1 pd 8),(c2 pd 8)
83 643
   ]c3=: c1 pc c2
1 4 7 9 6 9
   c3 pd 8
53369
   (c1 pd 8)*(c2 pd 8)
53369
```

Again the result `c3` can be normalized, this time to the range `0` to `7`. This requires dividing by `8`, “carrying” the integer quotient, and leaving the remainder. Thus:

```
   c3
1 4 7 9 6 9
   1 4 7 9 7 1 pd 8
53369
   1 4 8 1 7 1 pd 8
53369
   1 5 0 1 7 1 pd 8
53369
```

<span id="16e"></span>

## [16E. Remainder, Divisibility, and Integer part](#16-polynomials-and-number-systems) [S16E.](supplement.html#s16e)

The carrying process used in preceding sections made use of the *remainder*. For example, `8` divides into `24` exactly (that is, an integer number of times), but it divides `27` leaving a remainder of `3`.

The remainder function is denoted by `|` and is illustrated by:

```
   | table i=: 1 2 3 4 5 6 7 8
+-+---------------+
| |1 2 3 4 5 6 7 8|
+-+---------------+
|1|0 0 0 0 0 0 0 0|
|2|1 0 1 0 1 0 1 0|
|3|1 2 0 1 2 0 1 2|
|4|1 2 3 0 1 2 3 0|
|5|1 2 3 4 0 1 2 3|
|6|1 2 3 4 5 0 1 2|
|7|1 2 3 4 5 6 0 1|
|8|1 2 3 4 5 6 7 0|
+-+---------------+
```

If the remainder `d|n` is zero, we say that `n` is *divisible* by `d`, as illustrated by the following divisibility table:

```
   =&0 on | table i
+-+---------------+
| |1 2 3 4 5 6 7 8|
+-+---------------+
|1|1 1 1 1 1 1 1 1|
|2|0 1 0 1 0 1 0 1|
|3|0 0 1 0 0 1 0 0|
|4|0 0 0 1 0 0 0 1|
|5|0 0 0 0 1 0 0 0|
|6|0 0 0 0 0 1 0 0|
|7|0 0 0 0 0 0 1 0|
|8|0 0 0 0 0 0 0 1|
+-+---------------+
```

The number `n-d|n` is divisible by `d`, and the result of the division `d%~n-d|n` is called the *integer quotient*. Thus:

```
   iq=: ([%~]-|)"0
   8 iq 22 23 24 25 26 27
2 2 3 3 3 3
   iq table i
+-+---------------+
| |1 2 3 4 5 6 7 8|
+-+---------------+
|1|1 2 3 4 5 6 7 8|
|2|0 1 1 2 2 3 3 4|
|3|0 0 1 1 1 2 2 2|
|4|0 0 0 1 1 1 1 2|
|5|0 0 0 0 1 1 1 1|
|6|0 0 0 0 0 1 1 1|
|7|0 0 0 0 0 0 1 1|
|8|0 0 0 0 0 0 0 1|
+-+---------------+
```

The integer quotient can also be obtained by applying the *integer part* function `<.` to the result of division. For example:

```
   i%5
0.2 0.4 0.6 0.8 1 1.2 1.4 1.6
   <.i%5
0 0 0 0 1 1 1 1
   <. on (%~) table i
+-+---------------+
| |1 2 3 4 5 6 7 8|
+-+---------------+
|1|1 2 3 4 5 6 7 8|
|2|0 1 1 2 2 3 3 4|
|3|0 0 1 1 1 2 2 2|
|4|0 0 0 1 1 1 1 2|
|5|0 0 0 0 1 1 1 1|
|6|0 0 0 0 0 1 1 1|
|7|0 0 0 0 0 0 1 1|
|8|0 0 0 0 0 0 0 1|
+-+---------------+
```

<span id="16f"></span>

## [16F. Notes](#16-polynomials-and-number-systems) [S16F.](supplement.html#s16f)

In his Chapter 6: The Dawn of nothing, Hogben provides an interesting discussion of number systems and the role of *zero* in their development. For example:

> Why this is necessarily true, is easy to see if we recall the Roman representation of 32, i.e. XXXII. If the Romans had written it in the form III II, there would have been no way of distinguishing it from 302, 320, 3,020, 3,200, etc. The one simple way of escape from this dilemma is to introduce a sign such as the Maya lozenge ..., a dot or a circle for the *empty* column of the abacus. We can then write 32, 302, 320, 3,020 as below:
>
> III II; IIIoII; III IIo; IIIoIIo
>
> ...If our base is *b*, we need only (*b*-1) other signs e.g. if *b*=10 the other signs we need are nine in all. We can then express any nameable number however great without enlarging our stock in trade.
>
> ...Its invention liberated the human intellect from the prison bars of the counting frame. The new script was a complete model of the mechanical process one performs with it. With a sign for the empty column, 'carrying over' on slate, paper or parchment is just as easy as carrying over on the abacus.
>
> ...In mediaeval Europe, the name for such rules was *algorithms*, a corruption of the name of a thirteenth century mathematician, spelled Al Khwarismi or Alkarismi.
