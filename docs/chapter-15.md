---
title: "15: Linear Vector Functions"
anchor: "15-linear-vector-functions"
previous: "chapter-14.html"
next: "chapter-16.html"
---

[15A. Dot product and vector functions](#15a)

[15B. Dot product as a linear vector function](#15b)

[15C. Matrix inverse](#15c)

<span id="15a"></span>

## [15A. Dot product and vector functions](#15-linear-vector-functions) [S15A.](supplement.html#s15a)

The expression `+/w*x` gives a sum over the argument `x` weighted by the vector `w`. For example:

```
   x=: 2 3 5 7 11
   w=: 0 1 2 3 4
   w*x
0 3 10 21 44
   +/w*x
78
```

The dot operator (`.`) applied to the functions `+/` and `*` produces an equivalent function called the *dot*, *inner*, or *matrix* product. Thus:

```
   dp=: +/ . *
   w dp x
78
```

Moreover, `dp` applies to a matrix (table) left argument to produce a vector (list) of results, using successive rows of the matrix as weights. For example:

```
   a=: 3 1 4
   b=: 2 7 8
   c=: 2 1 0
   ]m=: a,b,:c
3 1 4
2 7 8
2 1 0

   m dp 2 3 5
29 65 7
   b dp 2 3 5
65

   g=: m with dp
   g 2 3 5
29 65 7
```

If `m` is a square matrix (as in the present example), then `m with dp` applies to a vector to produce a vector of the same number of elements. We will call such a function a *vector* function. <span id="15b"></span>

## [15B. Dot product as a linear vector function](#15-linear-vector-functions) [S15B.](supplement.html#s15b)

The dot product with a vector or matrix left argument distributes over addition, and is therefore a linear function, as defined in Section 14F. For example:

```
   x=: 2 3 5
   y=: 0 1 2
   f=: 2 7 8 with dp

   ((f x)+(f y)) , (f x+y)
88 88
   g=: m with dp
   ((g x)+(g y)) ,: (g x+y)
38 88 8
38 88 8
```

The function `I=: =/~ on i.` yields a result called an *identity matrix*, because when used with `dp` it produces an identity function (that yields its argument unchanged). For example:

```
   I=: i. =/ i.
   ]i=:  I 3
1 0 0
0 1 0
0 0 1
   i with dp 2 3 5
2 3 5
```

A linear vector function need not be expressed as a dot product, but if it is not, the required matrix is easily determined. For example, `sop=: +/\` (sums over prefixes) is a linear vector function, and the matrix `m` for an equivalent function `m with dp` may be determined as follows:

```
   x=: 2 3 5 7 11
   y=: 0 1 2 3 4
   sop=: +/\
   ((sop x)+(sop y)) ,: (sop x+y)
2 6 13 23 38
2 6 13 23 38

   ]i=: I # x
1 0 0 0 0
0 1 0 0 0
0 0 1 0 0
0 0 0 1 0
0 0 0 0 1

   i dp x
2 3 5 7 11
   sop i dp x
2 5 10 17 28
   (sop i) dp x
2 5 10 17 28

   ]m=: sop i
1 0 0 0 0
1 1 0 0 0
1 1 1 0 0
1 1 1 1 0
1 1 1 1 1
```

The resulting matrix provides an interesting way of looking at the sums over prefixes: the ones in the successive rows indicate the elements included in the successive sums. <span id="15c"></span>

## [15C. Matrix inverse](#15-linear-vector-functions) [S15C.](supplement.html#s15c)

The inverse of a linear vector function `m with dp` is itself a linear vector function, and can therefore be expressed in the form `mi with dp`. The matrix `mi` may be obtained from `m` by applying the matrix inverse function `%.` . Thus:

```
   ]z=:  m dp x=: 2 3 5 7 11
2 5 10 17 28
   mi=: %.m
   mi dp z
2 3 5 7 11
   mi
 1  0  0  0 0
_1  1  0  0 0
 0 _1  1  0 0
 0  0 _1  1 0
 0  0  0 _1 1
```

The pairs `_1 1` in the rows of the inverse `mi` indicate that the inverse of the sum over prefixes is a differencing operation, and the matrix `mi` may be called a difference matrix.

**Exercises**

Experiment with various linear vector functions such as reversal (`|.`), rotation (`2 with |.`) and `8 with A.`.

Comment on the matrices that represent them and their inverses.
