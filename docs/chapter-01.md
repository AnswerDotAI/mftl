---
title: "1: Numbers"
anchor: "1-numbers"
previous: "preface.html"
next: "chapter-02.html"
---

[1A. The Counting (Natural) Numbers](#1a)

[1B. Lists and Names](#1b)

[1C. Iteration (Repetition)](#1c)

[1D. Inverse](#1d)

[1E. Addition and Subtraction (+ and -)](#1e)

[1F. Bonding](#1f)

[1G. Multiplication or Times (\*)](#1g)

[1H. Power and Exponent (^)](#1h)

[1I. Monomials and Polynomials (p.)](#1i)

[1J. Division (%)](#1j)

[1K. Review and Supplement](#1k)

[1L. Notes](#1l)

<span id="1a"></span>

## [1A. The Counting (Natural) Numbers](#1-numbers) [S1A.](supplement.html#s1a)

The *Counting numbers* begin with `1 2 3 4` and go on forever, because every counting number has a *successor* that comes next after it. Thus:

```
   >: 1
2
   >: 2
3
   >: 3  
4
   >: 4
5
   >: >: 1
3
   >: >: >: >: 2
6

   >: 1 2 3 4 5 6
2 3 4 5 6 7
```

`>:` "performs an action" upon the number to which it is applied, and is therefore analogous to an "action word" or *verb* in English. In math, such a verb is also called a *function* (from Latin *fungi*, to perform or execute).

The number to which a verb applies may be called a *noun*. In math it is also called an *argument*, in the sense of a *topic* or *subject* ("You and love are still my argument" -- Shakespeare). <span id="1b"></span>

## [1B. Lists and Names](#1-numbers) [S1B.](supplement.html#s1b)

A collection of numbers may be written as a *list*, in the form `2 3 5 7 11`, and verbs may be applied to such lists. For example:

```
   >: 2 3 5 7 11
3 4 6 8 12
   >: >: >: 2 3 5 7 11
5 6 8 10 14
```

A *name* may be assigned to a number or list by using the *copula* `=:`, and the name may then be used to refer to its *referent*. For example:

```
   primes=: 2 3 5 7 11
   >: primes
3 4 6 8 12
   b=: >: primes
   >: >: b
5 6 8 10 14
```

The main copulas used in English are "is" and "are". They may be used in reading mathematical expressions aloud, as in "primes are `2 3 5 7 11`" for `primes=:2 3 5 7 11`, and "first is one" for `first=:1`.

Names may also be assigned to verbs. There appears to be no English word that corresponds to `>:` except, perhaps, the command "next" used to summon a successor from a queue. Thus:

```
   next=: >:
   next 5
6
   next next 5
7
```

<span id="1c"></span>

## [1C. Iteration (Repetition)](#1-numbers) [S1C.](supplement.html#s1c)

The expression `next ^: 3` produces a verb that is equivalent to applying the verb `next` **for** three times. Thus:

```
   primes
2 3 5 7 11
   next ^: 3 primes
5 6 8 10 14
   next next next primes
5 6 8 10 14
   for=: ^:
   
   next for 3 primes
5 6 8 10 14
   list=: 1 2 3 4
   next for list primes
3 4 6  8 12
4 5 7  9 13
5 6 8 10 14
6 7 9 11 15
```

<span id="1d"></span>

## [1D. Inverse](#1-numbers) [S1D.](supplement.html#s1d)

The verb `previous=: <:` "undoes" the work of the verb `next=: >:`, and is said to be its *inverse*. Thus:

```
   previous=: <:

   primes
2 3 5 7 11
   previous primes
1 2 4 6 10
   next previous primes
2 3 5 7 11
   previous next primes
2 3 5 7 11
   previous 3
2
   previous 2
1
   previous 1
0
   previous 0
_1
   previous _1
_2
```

Because `1` is the **first** counting number, the zero (`0`) and the negative numbers (`_1` and `_2`) shown above are not counting numbers. But they are *integers*, so called because they are unbroken or intact (in=not, tag=touch), as distinguished from the *fractions* (broken or fractured) referred to in the preface.

Adopting the seemingly-innocent notion of a verb that undoes the effect of `next` has, rather surprisingly, led us out of the original domain of counting numbers, and forced the adoption of a broader class, the *integers*, that includes the zero and negative numbers.

In adopting further inverses we will again experience the same need to broaden our domain, to include *rational* numbers, and *imaginary* numbers. Moreover, the surprising effect of inverse processes is not confined to mathematics.

Consider the effect of reversing a movie projector to run a film backward. If the film shows a locomotive moving forward along a track, the result of reversal is unremarkable. But if it concerns the dropping of an egg on the pavement, or a dive from a diving-board, the result is a startling illustration of the important distinction between *reversible* and *irreversible* processes.

Finally, the inverse of a function can be obtained by using iteration (`for`) with the right argument `_1`. Thus:

```
   next for _1 primes
1 2 4 6 10
   >: ^: _1 primes
1 2 4 6 10
   >: ^: _1
<:
   next for _3 _2 _1 0 1 2 3 primes
_1 0 2  4  8
 0 1 3  5  9
 1 2 4  6 10
 2 3 5  7 11
 3 4 6  8 12
 4 5 7  9 13
 5 6 8 10 14
```

<span id="1e"></span>

## [1E. Addition and Subtraction (+ and -)](#1-numbers) [S1E.](supplement.html#s1e)

The effect of the verb `next for 3` is to *add* `3` to its argument, and `next for 3 primes` is equivalent to the addition `primes + 3` (using the familiar Saint George's cross to denote the verb). Thus:

```
   next for 3 primes
5 6 8 10 14
   primes + 3
5 6 8 10 14
   0 1 2 3 4 5 + 0 1 2 3 4 5
0 2 4 6 8 10
   + table 0 1 2 3 4 5
+-+------------+
| |0 1 2 3 4  5|
+-+------------+
|0|0 1 2 3 4  5|
|1|1 2 3 4 5  6|
|2|2 3 4 5 6  7|
|3|3 4 5 6 7  8|
|4|4 5 6 7 8  9|
|5|5 6 7 8 9 10|
+-+------------+
```

The last result is an *addition table*, which may be "read" as follows:

> To find the result of `3 + 4`, choose the result (`7`) found in the row headed by `3` and the column headed by `4`.

The verb `+ table` is only one example of a *function* table, and other functions may be used. For example:

```
   previous for 3 primes
_1 0 2 4 8
   primes - 3
_1 0 2 4 8

   - table 0 1 2 3 4 5
+-+----------------+
| |0  1  2  3  4  5|
+-+----------------+
|0|0 _1 _2 _3 _4 _5|
|1|1  0 _1 _2 _3 _4|
|2|2  1  0 _1 _2 _3|
|3|3  2  1  0 _1 _2|
|4|4  3  2  1  0 _1|
|5|5  4  3  2  1  0|
+-+----------------+
```

**Exercises**

Read from the addition table the sums `2 + 5` and `5 + 2` and verify that they agree. Make similar comparisons of additions of numbers that are similarly interchanged or *commuted.*

Because of the agreements noted in Exercise 1, addition is said to be *commutative*. Use the subtraction table to find whether subtraction is commutative.

<span id="1f"></span>

## [1F. Bonding (&)](#1-numbers) [S1F.](supplement.html#s1f)

The verb `+ & 3` is equivalent to "add `3`", that is, to `next for 3`. Thus:

```
   + & 3 primes
5 6 8 10 14
   primes + 3
5 6 8 10 14

   with=: &
   + with 3 primes
5 6 8 10 14
   next for 3 primes
5 6 8 10 14

   - with 3 primes
_1 0 2 4 8
   primes - 3
_1 0 2 4 8

   - with 3 + with 3 primes
2 3 5 7 11
   + with 2 primes
4 5 7 9 13
   + with 2 for 0 1 2 3 4 primes
 2  3  5  7 11
 4  5  7  9 13
 6  7  9 11 15
 8  9 11 13 17
10 11 13 15 19
```

Although the referent of `primes` is the list `2 3 5 7 11`, it would not be correct to substitute the referent for the name in the foregoing expression, because the resulting `0 1 2 3 4 2 3 5 7 11` would be treated as a single list argument to `for`. Thus:

```
   + with 2 for 0 1 2 3 4 2 3 5 7 11
+&2^:0 1 2 3 4 2 3 5 7 11
```

The lists may, however, be separated by parentheses:

```
   + with 2 for 0 1 2 3 4 (2 3 5 7 11)
 2  3  5  7 11
 4  5  7  9 13
 6  7  9 11 15
 8  9 11 13 17
10 11 13 15 19
```

<span id="1g"></span>

## [1G. Multiplication or Times (\*)](#1-numbers) [S1G.](supplement.html#s1g)

Three times four `(3 * 4)` is said to be the addition of four copies (“plies”) of three. Thus:

```
   3 + 3 + 3 + 3
12
   3 * 4
12
   * table 0 1 2 3 4 5 6 7 8 9 10
+--+--------------------------------+
|  |0  1  2  3  4  5  6  7  8  9  10|
+--+--------------------------------+
| 0|0  0  0  0  0  0  0  0  0  0   0|
| 1|0  1  2  3  4  5  6  7  8  9  10|
| 2|0  2  4  6  8 10 12 14 16 18  20|
| 3|0  3  6  9 12 15 18 21 24 27  30|
| 4|0  4  8 12 16 20 24 28 32 36  40|
| 5|0  5 10 15 20 25 30 35 40 45  50|
| 6|0  6 12 18 24 30 36 42 48 54  60|
| 7|0  7 14 21 28 35 42 49 56 63  70|
| 8|0  8 16 24 32 40 48 56 64 72  80|
| 9|0  9 18 27 36 45 54 63 72 81  90|
|10|0 10 20 30 40 50 60 70 80 90 100|
+--+--------------------------------+
```

**Exercises**

Study the multiplication table, and comment on its properties (such as commutativity).

The numbers in column `5` are *multiples* of `5`, that is, they result from multiplying by `5`. Verify that they progress by "counting by fives", and check for similar properties in other columns and rows.

Comment on any patterns you find in the rows, columns, or diagonals of other function tables.

Make the table `* table 2 3 4 5 6 6 7 8 9 10` and make a list of the counting numbers beginning with `2` (and up to perhaps `19`) that *do not* occur in it. These numbers are called *primes*.

<span id="1h"></span>

## [1H. Power and Exponent (^)](#1-numbers) [S1H.](supplement.html#s1h)

Just as repeated application of addition is equivalent to another important function (multplication, or `*`), so repeated multiplication is equivalent to *power*, or `^ `. Thus, `3 ^ 4` is equivalent to `3 * 3 * 3 * 3`. The right argument (in this case `4`) is often called the *exponent*, and the expression `3 ^ 4` is read as “three power four” or “three to the power four”. For example:

```
   3 ^ 4
81
   3*3*3*3
81
   0 1 2 3 4 5 ^2
0 1 4 9 16 25

   ^ table 0 1 2 3 4 5
+-+-------------------+
| |0 1  2   3   4    5|
+-+-------------------+
|0|1 0  0   0   0    0|
|1|1 1  1   1   1    1|
|2|1 2  4   8  16   32|
|3|1 3  9  27  81  243|
|4|1 4 16  64 256 1024|
|5|1 5 25 125 625 3125|
+-+-------------------+
```

<span id="1i"></span>

## [1I. Monomials and Polynomials (p.)](#1-numbers) [S1I.](supplement.html#s1i)

An expression such as `5*4^3` is called a *monomial* (one name) with the *coefficient* `5`, the argument `4`, and the exponent `3`; a sum of monomials is called a *polynomial* (many names). For example:

```
   5 * 4 ^ 3
320

   (5*4^3) + (_2*4^4) + (1*4^1)
_288
```

A polynomial in which the exponents in the successive monomials are successive integers beginning with zero, is said to be in *standard form*, and may be expressed using the polynomial function `p.`, with the list of coefficients as the left argument. For example:

```
   x=:  4
   (2*x^0) + (3*x^1) + (4*x^2)
78
   2 3 4 p. x
78
```

**Exercises**

Evaluate the following expressions, and comment on the results:

```
   a=: 0 1 2 3 4 5
   1 2 1 p. a
   (a+1) ^ 2
   1 3 3 1 p. a
   (a+1) ^ 3
   c4=: 0 1 3 3 1 + 1 3 3 1 0
   c4 p. a
   (a+1) ^ 4
```

<span id="1j"></span>

## [1J. Division (%)](#1-numbers) [S1J.](supplement.html#s1j)

Division (to be denoted by `%`) "undoes" the work of multiplication. For example:

```
   a=: 0 1 2 3 4 5 6
   b=: a * 2
   b
0 2 4 6 8 10 12
   b % 2
0 1 2 3 4 5 6
   b % 3
0 0.666667 1.33333 2 2.66667 3.33333 4
```

Just as the inverse of addition introduced new numbers outside the domain of the counting numbers, so some of the results of this inverse function lie outside of the domain of integers. These non-integral results (such as `0.666667`) are "decimal approximations to" a new class of numbers, called *fractions* or *rationals*.

Just as we introduced a way to represent negative numbers, so we introduce a representation for rationals: `2r3` for the fraction two-thirds, `4r3` for the fraction four-thirds, etc. Thus:

```
   1r3+1r3
2r3
   a=: 0 1r2 1r3 1r4 1r5 1r6
   
   a+a
0 1 2r3 1r2 2r5 1r3
   a-a
0 0 0 0 0 0
   a * a
0 1r4 1r9 1r16 1r25 1r36

   + table a
+---+------------------------------+
|   |  0  1r2  1r3  1r4   1r5   1r6|
+---+------------------------------+
|  0|  0  1r2  1r3  1r4   1r5   1r6|
|1r2|1r2    1  5r6  3r4  7r10   2r3|
|1r3|1r3  5r6  2r3 7r12  8r15   1r2|
|1r4|1r4  3r4 7r12  1r2  9r20  5r12|
|1r5|1r5 7r10 8r15 9r20   2r5 11r30|
|1r6|1r6  2r3  1r2 5r12 11r30   1r3|
+---+------------------------------+

   - table a
+---+--------------------------------+
|   |  0   1r2   1r3   1r4   1r5  1r6|
+---+--------------------------------+
|  0|  0  _1r2  _1r3  _1r4  _1r5 _1r6|
|1r2|1r2     0   1r6   1r4  3r10  1r3|
|1r3|1r3  _1r6     0  1r12  2r15  1r6|
|1r4|1r4  _1r4 _1r12     0  1r20 1r12|
|1r5|1r5 _3r10 _2r15 _1r20     0 1r30|
|1r6|1r6  _1r3  _1r6 _1r12 _1r30    0|
+---+--------------------------------+

   * table a
+---+--------------------------+
|   |0  1r2  1r3  1r4  1r5  1r6|
+---+--------------------------+
|  0|0    0    0    0    0    0|
|1r2|0  1r4  1r6  1r8 1r10 1r12|
|1r3|0  1r6  1r9 1r12 1r15 1r18|
|1r4|0  1r8 1r12 1r16 1r20 1r24|
|1r5|0 1r10 1r15 1r20 1r25 1r30|
|1r6|0 1r12 1r18 1r24 1r30 1r36|
+---+--------------------------+

   % table a
+---+---------------------+
|   |0 1r2 1r3 1r4 1r5 1r6|
+---+---------------------+
|  0|0   0   0   0   0   0|
|1r2|_   1 3r2   2 5r2   3|
|1r3|_ 2r3   1 4r3 5r3   2|
|1r4|_ 1r2 3r4   1 5r4 3r2|
|1r5|_ 2r5 3r5 4r5   1 6r5|
|1r6|_ 1r3 1r2 2r3 5r6   1|
+---+---------------------+
```

**Exercises**

Study the foregoing tables, and comment on their properties. (See the Exercises in Section 1G.)

Comment on the `_` that occurs in the first column of the division table (it denotes *infinity*).

Study the multiplication table, and try to formulate rules for the multiplication of rationals.

<span id="1k"></span>

## [1K. Review and Supplement](#1-numbers) [S1K.](supplement.html#s1k)

Using notation provided by a programming language (that will allow us to experiment with our math on a computer), we have introduced:

The *counting numbers* `1 2 3 4` etc.

The use of *lists* and of *names* that are assigned *referents* by a *copula*.

The *iteration* operator `for=: ^:` that applies a function for a specified number of times.

The function *addition*.

Its *inverse* (*subtraction*).

The class of *integers* that includes *zero*, and the *negative numbers* `_1 _2 _3 _4` etc. introduced by subtraction.

The *multiplication* that is given by iterated addition.

The *division* that is inverse to multiplication.

The *fractions* or *rationals* that are introduced by division.

The *power* function and the *polynomials* based upon it.

Some of the assigned names (such as the `for` assigned by the expression `for=: ^:`) are "utilities" that will be utilized throughout the text, and are collected for easy reference in Appendix 1.

The pace of this text is brisk, moving on quickly to further topics as soon as the essential foundations for them are established. For example, although the Polynomials of Chapter 4 could provide a rich subject in itself, we pass on after a brief three pages to the Power Series of Chaper 5, and the Slope and Derivative of Chapter 6.

This gives a quick exposure to significant, and sometimes surprising, consequences of otherwise dull foundations. On the other hand, the reader may eventually (or immediately) want further treatments of the successive foundations: these are provided in a separate part of the book called Supplement.

In a printed text, the need to move between a given section and the corresponding supplemental section in a different part of the book might prove onerous. However, in reading the text from a computer (through a Browser), this switching back and forth is made by a click of a mouse.

For example, click on the S1K that appears to the right of the heading for this section to read the further discussion in the supplemental section S1K, and click on its heading to return.

The *Find* facility can be used as an index to find the occurrences of words in the text; invoke it by pressing F while holding down the control key, or select it from the Search menu. <span id="1l"></span>

## [1L. Notes](#1-numbers) [S1L.](supplement.html#s1l)

On page 75 Hogben says:

> It may therefore be soothing for many to whom mathematical expressions evoke a malaise comparable to being seasick, if they can learn to think of mathematics less as an exploit in reasoning than as an exercise in translating an unfamiliar script like Braille or the Morse code.
>
> In this chapter we shall therefore abandon the historical approach and deal mainly with two topics: for what sort of communication do we use this highly space-saving – now international – written language, and on what sort of signs do we rely. To emphasize that the aim of this chapter is to accustom the reader to approach mathematical rules as Exercises in economical translation, every rule in the sign language of mathematics will have an arithmetical illustration …

He continues with:

> In contradistinction to common speech which deals largely with the quality of things, mathematics deals only with matters of size, order, and shape. … First let us consider what different sorts of signs go to the making of a mathematical statement. We may classify these as:
>
> punctuation;
>
> models;
>
> labels (e.g. 5 or x) for enumeration, measurement, and position in a sequence;
>
> signs for relations;
>
> signs for operations.

Conventional mathematical notation uses three pairs of symbols for punctuation: `( )` and `[ ]` and `{ }`. We will use only the pair `( )` for this purpose, and will use the others for operations: `{` for indexing (selection), `{.` and `}.` for take and drop of a first item, and `{:` and `}:` for take and drop of a last item.

Hogben offers the following suggestions for study:

> Although care has been taken to see that all the logical, or, as we ought to say, the grammatical rules are put in a continuous sequence, you must not expect that you will necessarily follow every step in the argument the first time you read it. An eminent Scottish mathematician gave a very sound piece of advice for lack of which many people have been discouraged unnecessarily. “Every mathematical book that is worth anything”, said Chrystal, “must be read backwards and forwards …”
>
> ---------------------
>
> …Always have a pen and paper, preferably squared paper, in hand …. when you read the text for serious study, and work out all the numerical examples as you read …. What you get out of the book depends on your co-operation in the business of learning.

To this we may add the advice to use the computer in the manner introduced in the next chapter, and illustrated throughout the entire text. In particular, do not hesitate to do any computer experiments that may occur to you – the worst that can happen is the appearance of an error message of some kind, after which you may continue without any special action.

## 
