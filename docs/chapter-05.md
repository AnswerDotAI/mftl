---
title: "5: Power Series"
anchor: "5-power-series"
previous: "chapter-04.html"
next: "chapter-06.html"
---

[5A. Introduction](#5a)

[5B. Truncated power series](#5b)

[5C. Notes](#5c)

<span id="5a"></span>

## [5A. Introduction](#5-power-series) [S5A.](supplement.html#s5a)

Elements of a list may be identified and selected by its indices, beginning at zero. For example:

```
   a=:  1 2 3 4 5 6 ^ 3
   a
1 8 27 64 125 216
   0 { a
1
   1 { a
8
   5 { a
216
   6 { a
|index error
|   6    {a
```

A polynomial whose coefficients may be expressed as a function of their indices is called a power series. For example:

```
   g=: ! with 3
   g i. 8
1 3 3 1 0 0 0 0
   (g i.8) with p. 0 1 2 3 4 5 6
1 8 27 64 125 216 343
```

`g 0` gives the number of distinct ways that zero things can be chosen from three things; `g 1` gives the number of ways that one thing can be chosen, and so on, to the case `g 4` which shows that four things can be chosen from three in no ways. The resulting coefficients are those used in `c3` in Section 4A; `h=: ! with 4` gives those used in `c4`, and so on. The coefficients:

```
   0 1 0 _1r6 0 1r120 0 _1r5040
   1 0 _1r2 0 1r24 0 _1r720 0 1r40320
```

used in Section 3A can also be expressed as power series. Both lists are reciprocal factorials (such as `1r24` and `1r120`) multiplied by `_1` or `0` or `1`. The power series function for the first is given by:

```
   ps=: % on ! * 2 with | * _1: ^ 3: = 4: | ]
   ps 0 1 2 3 4 5 6 7 8 9 10r1
0 1 0 _1r6 0 1r120 0 _1r5040 0 1r362880 0
```

**Exercises**

Define a power series function `pc` for the second list of coefficients given above.

<span id="5b"></span>

## [5B. Truncated power series](#5-power-series) [S5B.](supplement.html#s5b)

For the power series `g=: ! with 3`, the coefficients following the first four are all zero, and the truncated series `g i.4` therefore defines a polynomial that is equivalent to the longer list produced by `g i.8`. Thus:

```
   g i.4
1 3 3 1
   (g i.4) with p. x=: 0 1 2 3 4 5 6
1 8 27 64 125 216 343
   g i.8
1 3 3 1 0 0 0 0
   (g i.8) with p. x
1 8 27 64 125 216 343
```

On the other hand, the power series: `ps=: % on ! * 2 with | * _1: ^ 3: = 4: | ]` never “terminates” with all zeros. However, the reciprocal factorial factor (`% on !`) ensures that successive terms diminish rapidly in magnitude, and a short series may therefore provide a good approximation. For example:

```
   ] c12=: ps i. 12r1
0 1 0 _1r6 0 1r120 0 _1r5040 0 1r362880 0 _1r39916800
   ] c10=: ps i. 10r1
0 1 0 _1r6 0 1r120 0 _1r5040 0 1r362880
   set 9
   dec (c12 with p. ,c10 with p.) 2
0.909296136 0.909347443
```

However, the definition of the polynomial in Section 1I shows that successive coefficients are multiplied by successive powers of the argument `x`. For large arguments, the growth of this factor may be fast enough to overpower the decrease in the coefficient. For example:

```
   dec (c12 with p. ,c10 with p.) 5
_1.1336173 0.08963018
```

For small arguments (particularly for those less than one in magnitude), reasonably short power series of the type that includes a reciprocal factorial factor provide good approximations. For example:

```
   dec ((ps i.20) with p.,(ps i.18) with p.) 5
_0.958933165 _0.958776369
   y=: 1r5 * i:5
   y
_1 _4r5 _3r5 _2r5 _1r5 0 1r5 2r5 3r5 4r5 1

   sin=: 1 with o.   
   ((ps i.10) with p.,.(ps i.8) with p.,.sin) y
_0.841471010 _0.841468254 _0.841470985
_0.717356093 _0.717355723 _0.717356091
_0.564642473 _0.564642446 _0.564642473
_0.389418342 _0.389418342 _0.389418342
_0.198669331 _0.198669331 _0.198669331
           0            0            0
 0.198669331  0.198669331  0.198669331
 0.389418342  0.389418342  0.389418342
 0.564642473  0.564642446  0.564642473
 0.717356093  0.717355723  0.717356091
 0.841471010  0.841468254  0.841470985 
```

As illustrated by the last column, these truncated power series are approximations to the trigonometric sine function (on radian arguments). Moreover, the Taylor operator `t.` can be used to produce the power series for the sine as follows:

```
   sin t. i. 12r1
0 1 0 _1r6 0 1r120 0 _1r5040 0 1r362880 0 _1r39916800

   sign sin t. i. 12r1
0 1 0 _1 0 1 0 _1 0 1 0 _1
```

**Exercises**

Try Taylor series of other functions, including the exponential `^`

Comment on the results of the following:

```
   q=: (^t.i),.(1 with o.t.i),.(2 with o.t.i=: i.12x)
   q,.*q
```

<span id="5c"></span>

## [5C. Notes](#5-power-series) [S5C.](supplement.html#s5c)

Power series are of great importance in math, and it is tempting to digress in a discussion of reasons for this importance, much as was done for polynomials in Section 4A.

However, it was possible to confine that discussion to rather elementary ideas, whereas a meaningful discussion of the uses of power series would quickly lead to more advanced and less familiar mathematical notions outside the experience of many readers.

The same is true of many topics (such as the derivative, symbolic logic, sets, and permutations), and we will leave the reader to observe the importance of topics as they are exploited in later work. In other words, some faith is expected of the reader – a belief that topics will be introduced only if they are both important and interesting.
