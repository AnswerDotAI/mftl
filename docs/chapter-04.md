---
title: "4: Polynomials"
anchor: "4-polynomials"
previous: "chapter-03.html"
next: "chapter-05.html"
---

[4A. Bonding](#4a)

[4B. Notes](#4b)

<span id="4a"></span>

## [4A. Bonding](#4-polynomials) [S4A.](supplement.html#s4a)

The polynomial function introduced in Chapter 1 is a function of two arguments, the first of which is commonly called the coefficients of the function. Using the example from Chapter 1:

```
   x=: 4
   2 3 4 p. x
78
   c=: 2 3 4
   c p. x
78
   g=: c with p.
   g x
78
```

The expression `g=: c with p.` illustrates the fact that the function `p.` can be bonded with a list of coefficients to define a specific polynomial function `g`. Consider the following examples:

```
   c2=: 1 2 1
   c3=: 1 3 3 1
   c4=: 1 4 6 4 1
   y=: 0 1 2 3 4 5
   f2=: c2 with p.
   f2 y
1 4 9 16 25 36

   f3=: c3 with p.
   f3 y
1 8 27 64 125 216

   (f2 y) * (f3 y)
1 32 243 1024 3125 7776
   g=: f2 * f3
   g y
1 32 243 1024 3125 7776
```

The Taylor operator `t.` applies to a polynomial such as `f3` to produce a function which, applied in turn to an integer `i`, gives coefficient `i` of the polynomial. For example:

```
   f3 t. 2
3
   f3 t. 0 1 2 3 4 5 6
1 3 3 1 0 0 0
   (f2 * f3) t. 0 1 2 3 4 5 6
1 5 10 10 5 1 0
```

The result of `f2 f3 y` is said to be the result of applying `f2` to the result of `f3`. The corresponding function is denoted by `f2 on f3`. For example:

```
   f3 y
1 8 27 64 125 216
   f2 1 8 27 64 125 216
4 81 784 4225 15876 47089
   f2 f3 y
4 81 784 4225 15876 47089
   h=: f2 on f3
   h y
4 81 784 4225 15876 47089
   h t. 0 1 2 3 4 5 6 7 8
4 12 21 22 15 6 1 0 0
```

**Exercises**

Determine the coefficients of various polynomials such as:

```
   g1=: f2 * f2
   g2=: f2 * f2 * f2
   g3=: f3 - f2
   g4=: f3 on g
```

Polynomials are important for a number of reasons:

\* Because of the wide choice of coefficients available, polynomials can be defined to approximate most functions of practical interest.

\* As already illustrated for sums, products, and composition of polynomials, they are *closed* under a number of important functions, in the sense that the resulting function is again a polynomial. These include:

```
SUM          c with p. + d with p.

DIFFERENCE   c with p. - d with p.

PRODUCT      c with p. * d with p.

COMPOSITION  (c with p.) on (d with p.)

SLOPE        or rate of increase over an interval

DERIVATIVE   or limit of the slope over small intervals

AGGREGATE    or area under the graph of a function

INTEGRAL     or limit of the area for small intervals
```

In most of these cases, the Taylor operator can be used to obtain the coefficients of the resulting polynomial. <span id="4b"></span>

## [4B. Notes](#4-polynomials) [S4B.](supplement.html#s4b)

This brief treatment of polynomials is enough to provide a basis for the treatment of the important topics of Power Series, Slope and Derivative, Growth and Decay, and Vibrations in the next four chapters. We therefore defer further discussion of the polynomial to Chapter 16: Polynomials and Number Systems. That chapter may, however, be attempted at any point.

With increasing use of computer experimentation, it becomes important to learn to use the available tools. In particular:

Use the left and right arrows to position the cursor, and use the delete (Del) and Backspace keys to delete text.

Use the up arrow to move the cursor to an earlier line, press the Enter key to bring it to the entry line, and then edit and re-enter it.

Hold down the Ctrl key and press N to open a script window that does not execute entries, but allows them to be freely edited and then run (in the execution window, to which you may return by entering Ctrl Tab).

The run is performed by entering Ctrl Shift W, or silently by entering Ctrl W. A selected segment may be run by using the mouse or shift key to highlight it, and then entering Ctrl E.

Learn to use more general facilities by using the mouse to drop the Help menu, and then using it to select the index and other information offered.

Any unfamiliar term such as *sine* or *magnitude* (or its synonym *absolute value*) may be found in an English dictionary, or it may be ignored and returned to as suggested in Section 1L.
