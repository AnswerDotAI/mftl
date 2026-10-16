---
title: "19:Complex Numbers and the Exponential Family"
anchor: "19-complex-numbers-and-the-exponential-family"
previous: "chapter-18.html"
next: "chapter-20.html"
---

[19A. Imaginary numbers](#19a)

[19B. Complex numbers](#19b)

[19C. Division](#19c)

[19D. The Exponential Family](#19d)

<span id="19a"></span>

## [19A. Imaginary numbers](#19-complex-numbers-and-the-exponential-family) [S19A.](supplement.html#s19a)

In Chapter 1 we began with the counting numbers (`1 2 3 4` etc.) and found that the introduction of subtraction as the inverse of addition led to a new class of *negative* numbers (when we attempted to subtract a larger number from a smaller).

Such negative numbers were once regarded as curious absurdities, but are found to serve consistently and usefully under addition, subtraction, and multiplication.

Similarly, the introduction of division as the inverse of multiplication leads to the consistent and useful notion of fractional numbers.

Because the square of any number (positive or negative) is non-negative, the introduction of the square root as the inverse of the square leads to a further extension when applied to a negative number. These new numbers were (and still are) called *imaginary*. For example:

```
   set=: 9!:11
   set 4

   sqr=: *:
   sqrt=: sqr^:_1
   a=: i.10
   a
0 1 2 3 4 5 6 7 8 9
   sqr a
0 1 4 9 16 25 36 49 64 81
   sqrt a
0 1 1.414 1.732 2 2.236 2.449 2.646 2.828 3
   b=: sqrt -a
   b
0 0j1 0j1.414 0j1.732 0j2 0j2.236 0j2.449 0j2.646 0j2.828 0j3
   sqr b
0 _1 _2 _3 _4 _5 _6 _7 _8 _9
```

<span id="19b"></span>

## [19B. Complex numbers](#19-complex-numbers-and-the-exponential-family) [S19B.](supplement.html#s19b)

The sum of a real and an imaginary number is called a *complex* number. For example:

```
   a+b
0 1j1 2j1.414 3j1.732 4j2 5j2.236 6j2.449 7j2.646 8j2.828 9j3
   sqr (a+b)
0 0j2 2j5.657 6j10.39 12j16 20j22.36 30j29.39 42j37.04 56j45.25 72j54
   a + table b
+-+-------------------------------------------------------------+
| |0 0j1 0j1.414 0j1.732 0j2 0j2.236 0j2.449 0j2.646 0j2.828 0j3|
+-+-------------------------------------------------------------+
|0|0 0j1 0j1.414 0j1.732 0j2 0j2.236 0j2.449 0j2.646 0j2.828 0j3|
|1|1 1j1 1j1.414 1j1.732 1j2 1j2.236 1j2.449 1j2.646 1j2.828 1j3|
|2|2 2j1 2j1.414 2j1.732 2j2 2j2.236 2j2.449 2j2.646 2j2.828 2j3|
|3|3 3j1 3j1.414 3j1.732 3j2 3j2.236 3j2.449 3j2.646 3j2.828 3j3|
|4|4 4j1 4j1.414 4j1.732 4j2 4j2.236 4j2.449 4j2.646 4j2.828 4j3|
|5|5 5j1 5j1.414 5j1.732 5j2 5j2.236 5j2.449 5j2.646 5j2.828 5j3|
|6|6 6j1 6j1.414 6j1.732 6j2 6j2.236 6j2.449 6j2.646 6j2.828 6j3|
|7|7 7j1 7j1.414 7j1.732 7j2 7j2.236 7j2.449 7j2.646 7j2.828 7j3|
|8|8 8j1 8j1.414 8j1.732 8j2 8j2.236 8j2.449 8j2.646 8j2.828 8j3|
|9|9 9j1 9j1.414 9j1.732 9j2 9j2.236 9j2.449 9j2.646 9j2.828 9j3|
+-+-------------------------------------------------------------+
```

Since a complex number is a sum of a real and an imaginary number, the product of complex numbers is treated consistently as a product of sums. The steps in the multiplication may be illustrated as follows:

```
   c=: 2j3
   d=: 4j5
   c*d
_7j22
   (2+0j3)*(4+0j5)
_7j22
   (2*(4+0j5))+(0j3*(4+0j5))
_7j22
   (2*4)+(2*0j5)+(0j3*4)+(0j3*0j5)
_7j22
   8+0j10+0j12+_15
_7j22
   _7+0j22
_7j22
```

Note that the product of two imaginaries (`0j3` and `0j5`) yields a negative real number. <span id="19c"></span>

## [19C. Division](#19-complex-numbers-and-the-exponential-family) [S19C.](supplement.html#s19c)

We begin by dividing the product `e=: c*d` by `c` and then by `d` to get the expected results `d` and `c`:

```
   ]e=: c*d
_7j22
   e%c
4j5
   e%d
2j3
```

To get a general procedure for division, we first note that division by a real number is straightforward. For example:

```
   12j22 % 2
6j11
```

Similarly, we note that multiplication of both numerator and dednominator by the same number leaves the quotient unchanged. For example:

```
   e%c
4j5
   g=: 2j_3
   (e*g)%(c*g)
4j5
```

Finally, we note that the denominator `c*g` is a real number, a result of choosing `g` as the *conjugate* of `c`, that is, obtained from `c` by reversing the sign of its imaginary part:

```
   c*g
13
```

The function `conj=: +` yields the conjugate of its argument, and it can therefore be used to provide division by first producing an equivalent quotient with a real denominator. For example:

```
   conj=: +
   p=: 2j5
   q=: 3j_4
   p%q
_0.56j0.92
   conj q
3j4
   p*conj q
_14j23
   q*conj q
25
   (p*conj q)%(q*conj q)
_0.56j0.92
NB. Compare with p%q
```

<span id="19d"></span>

## [19D. The Exponential Family](#19-complex-numbers-and-the-exponential-family) [S19D.](supplement.html#s19d)

In Chapter 14 we showed that the hyperbolic sine and the hyperbolic cosine belonged to the exponential family in the sense that they could be obtained from the exponential as its odd and even parts. Using imaginary numbers, we can treat the sine and cosine similarly.

The function `j.` multiplies its argument by `0j1` (the square root of negative one). For example:

```
   j.i.10
0 0j1 0j2 0j3 0j4 0j5 0j6 0j7 0j8 0j9
```

Consequently, each term in the polynomial `c with p. on j.` differs from that in the polynomial `c with p.` by a power of `0j1` determined by its exponent. For example:

```
  0j1^0 1 2 3 4 5 6 7 8

1 0j1 _1 0j_1 1 0j1 _1 0j_1 1

   c=: 1 2 3 4 5 6 7
   f=: c with p.
   f t. i.10 NB. Taylor coefficients
1 2 3 4 5 6 7 0 0 0

   f on j. t. i.10
1 0j2 _3 0j_4 5 0j6 _7 0 0 0
```

Consequently, the Taylor coefficients of the function `^ with j.` are the same as those of the sum `cos+j. sin`, and the cosine and sine can be obtained from the even and odd parts of `^ with j.`

**Exercises**

Define the following odd and even operators:

```
   O=:  .: -
   E=:  .. -
```

and experiment with their use on the function `f=: 0 1 2 3 4 5 with p.` using expressions such as `f E` and `f E i:4` and `(f O+f E) i:4`

Experiment with the odd and even parts of other polynomials, as well as with the functions `^` and `sin=: 1 with o.` and `cos=: 2 with o.` and `cosh=: 6 with o.`.
