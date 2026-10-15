---
title: "11: Proofs"
anchor: "11-proofs"
previous: "chapter-10.html"
next: "chapter-12.html"
---

[11A. Introduction](#11a)

[11B. Informal proofs](#11b)

[11C. Formal proofs](#11c)

[11D. Inductive proofs](#11d)

[11E. Recursive definition](#11e)

[11F. Guessing games](#11f)

<span id="11a"></span>

## [11A. Introduction](#11-proofs) [S11A.](supplement.html#s11a)

Although proofs are an important (and many might say *the essential*) part of mathematics, we will spend little time on them in this book.

In introducing his book *Proofs and Refutations: The Logic of Mathematical Discovery* \[17\], Imre Lakatos makes the following point:

> Its modest aim is to elaborate the point that informal, quasi-empirical, mathematics does not grow through a monotonous increase of the number of indubitably established theorems but through the incessant improvement of *guesses* \[Italics added\] by speculation and criticism, by the logic of proofs and refutations.
>
> The main point of the present book is to exploit new tools for the exploration of relations and patterns, that can be used by both mathematicians and laymen to find those guesses that are amenable to, and worthy of, proof.

We recommend the reading of Lakatos at any point: his book is highly entertaining, instructive, and readable by any layman with the patience to look up the meanings of a small number of words such as polyhedron, polygon, and convex. The following quotes from Lakatos reflect his view of the importance of guessing:

> Just send me the theorems, then I shall find the proofs. **Chrysippus**
>
> I have had my results for a long time, but I do not yet know how I am to arrive at them. **Gauss**
>
> If only I had the theorems! Then I should find the proofs easily enough. **Riemann**
>
> I hope that now all of you see that proofs, even though they may not prove, certainly do help to *im*prove our conjecture. **Lakatos**
>
> On the other hand those who, because of the usual deductive presentation of mathematics, come to believe that the path of discovery is from axioms and/or definitions to proofs and theorems, may completely forget about the possibility and importance of naive guessing. **Lakatos**

We cite two further comments on the effects of excessive formalism in the teaching of mathematics:

> Plato’s exaltation of mathematics as an august and mysterious ritual had its roots in dark superstitions which troubled, and fanciful puerilities which entranced, people who were living through the childhood of civilization, when even the cleverest people could not clearly distinguish the difference between saying that 13 is a ‘prime’ number and saying that 13 is an unlucky number.
>
> His influence on education has spread a veil of mystery over mathematics and helped to preserve the queer freemasonry of the Pythagorean brotherhoods, whose members were put to death for revealing secrets now printed in school books.
>
> It reflects no discredit on anyone if this veil of mystery makes the subject distasteful. Plato’s great achievement was to invent a religion which satisfies the emotional needs of people who are out of harmony with their social environment, and just too intelligent or too individualistic to seek sanctuary in the cruder forms of animism. **Hogben**
>
> … the author has the notion that mathematical formulas have their “secret life,” behind their Golem-like appearance. To bring out the “secret life” of mathematical relations by an occasional narrative digression does not appear to him a profanation of the sacred rituals of formal analysis but merely an attempt to a more integrated way of understanding The reader who has to struggle through a maze of “lemmas,” “corollaries,” and “theorems,” can easily get lost in formalistic details, to the detriment of the essential elements of the results obtained.
>
> By keeping his mind on the principal points he gains in depth, although he may lose in details. The loss is not serious, however, since any reader equipped with the elementary tools of algebra and calculus can easily interpolate the missing details.
>
> It is a well-known experience that the only truly enjoyable and profitable way of studying mathematics is the method of “filling in details” by one’s own efforts. **Lanczos\[18\]**

However, it is important to remember that in addition to the mathematics that is important to the intelligent layman, there is another mathematics, as expressed by G.H. Hardy in his A Mathematician’s Apology \[19\]:

> There are then two mathematics. There is the real mathematics of the real mathematicians, and there is what I will call ‘trivial’ mathematics, for want of a better word. The trivial mathematics may be justified by arguments which would appeal to Hogben, or other writers of his school, but there is no such defence for the real mathematics, which must be justified as an art if it can be justified at all. There is nothing in the least paradoxical or unusual in this view, which is that held commonly by mathematicians.

<span id="11b"></span>

## [11B. Informal proofs](#11-proofs) [S11B.](supplement.html#s11b)

We will illustrate a proof by first guessing at a relation, using the function `odd` from Section 2E:

```
   odd=: 1:+2:*i.
   odd 6
1 3 5 7 9 11
   +/odd 6
36
   (+/ odd 1),(+/odd 2),(+/odd 3),(+/odd 4),(+/odd 5)
1 4 9 16 25
```

It appears that the sum of the first `n` odd integers is `n*n`, a relation we will demonstrate by using a few facts illustrated by the following:

```
   |. odd 6
11 9 7 5 3 1
   (+/odd 6),(+/|.odd 6)
36 36
   (odd 6)+(|.odd 6)
12 12 12 12 12 12
   6 # 2*6      NB. Six copies of twice six 
12 12 12 12 12 12
   half=: % with 2
   half 6 # 2*6
6 6 6 6 6 6
   +/half 6 # 2*6
36
   +/6#6
36
   6*6 
36
```

We now write a sequence of (obviously?) equivalent sentences:

```
   n=: 6
   +/odd n
36
   +/|.odd n
36
   half (+/odd n)+(+/|.odd n)
36
   half +/(odd n)+(|.odd n)
36
   half +/6 # 2*6
36
   +/6 # 6
36
   n*n
36
```

Because a value (`6`) was assigned to the argument `n`, each of the foregoing sentences were executable, and were executed to give results whose equality provided some assurance that an error had not been made. We will, however, write an informal proof as a similar sequence, omitting the results that would have been produced by their execution. Thus:

```
   +/odd n
   +/|.odd n
   half (+/odd n)+(+/|.odd n)
   half +/(odd n)+(|.odd n)
   half +/6 # 2*6
   +/6 # 6
   n*n
```

<span id="11c"></span>

## [11C. Formal proofs](#11-proofs) [S11C.](supplement.html#s11c)

In a formal proof it is necessary to state clearly the justification for each equivalence, that is, the reason why each statement is believed to be equivalent to the one that precedes it. For example, we will begin to convert the foregoing informal proof to a formal proof as follows:

```
   +/odd n
   +/|.odd n
   half (+/odd n)+(+/|.odd n)
   half +/(odd n)+(|.odd n)
   half +/6 # 2*6    
   +/6 # 6     NB. Half of sum is sum of halves
   n*n         NB. Def of multiplication (in 1G)
```

A stickler for logic might ask why he should believe that half of a sum equals the sum of the halves of the list summed. A convincing answer is not as easy as might be supposed, leading to an appreciation of the following statement from Lakatos:

> TEACHER: This decomposition of the conjecture suggested by the proof opens new vistas for testing. The decomposition deploys the conjecture on a wider front, so that our criticism has more targets.

What about other steps, such as the equivalence of `+/odd n` and `+/|.odd n`? It may seem obvious, but what is special about `+/` that would not apply for another function such as `%/` ? A mathematician might say (and offer proofs that) functions such as `+/` and `*/` and `gcd/` and `>./` are *symmetric*, meaning that they give the same result when applied to any permutation (re-ordering) of their arguments.

For the layman it may be best to accept informal proofs, but harbor a healthy suspicion that obvious ideas are sometimes wrong. In a further quotation from Lakatos:

> TEACHER: I agree with you that the conjecture has received a severe criticism by Alpha’s counterexample. But it is untrue that the proof has "completely misfired". If, for the time being, you agree to my earlier proposal to use the word ‘proof’ for a ‘thought experiment’ which leads to a decomposition of the original conjecture into ‘subconjectures’, instead of using it in the sense of a ‘guarantee of certain truth’, you need not draw this conclusion.
>
> … You are interested only in proofs which ‘prove’ what they have set out to prove. I am interested in proofs even if they do not accomplish their intended task. Columbus did not reach India but he discovered something quite interesting.

**Exercises**

Determine and test an expression equivalent to `+/even n`, and write an informal proof of the equivalence.

Repeat Exercise 1 for `+/i.n`

Examine and discuss the Taylor series `+/ on i. t. i. 4`

<span id="11d"></span>

## [11D. Inductive proofs](#11-proofs) [S11D.](supplement.html#s11d)

Suppose that by assuming that `+/ on odd n` were equal to `n*n` for a certain value of `n`, we were able to use this assumption to prove that `+/ on odd n+1` must therefore equal `(n+1)*(n+1)`, we could then conclude that equality must hold for all succeeding values, `n+2` and `n+3`, and so on.

If, independently of this assumption, we are able to show further that equality does hold for some specific value (such as `n=: 0`), we may further conclude that the relation is true for all integers greater than or equal to that value. For example:

```
+/ on odd n+1

(+/odd n)+(2*n)+1   NB. From definition of odd

(n*n)+(2*n)+1       NB. Assumed "induction hypothesis"

(n+1)*(n+1)         NB. Simple algebra
```

<span id="11e"></span>

## [11E. Recursive definition](#11-proofs) [S11E.](supplement.html#s11e)

A function that is defined in terms of itself is said to be recursively defined. For example, a factorial function `fac` might be defined by saying that `fac n` is `n * fac n-1`. However, it is necessary to further define its value for some specific argument; for example, to define `fac 0` as `1`.

A recursive definition therefore depends upon three functions, such as `]*fac on <:` to perform the recursion, the constant function `1:` for the specific argument `0`, and the “conditional function” `= with 0` to choose between them. Thus:

```
   fac=:  (]*fac  on  <:) ` 1:  @. (= with 0)
   fac 0
1
   fac 4
24
   !4
24
```

In the foregoing, the tie operator `` ` `` forms a gerund from the two functions to which it is applied, and the agenda operator `@.`selects one of them according to the result of the conditional function `= with 0`.

A recursively defined function provides a convenient base for an hypothesis for use in an inductive proof. For example a function `sodd` for the sum of the odd integers might be recursively defined as follows:

```
   sodd=: (sodd on <: + 2 with * - 1:)`0: @. (= with 0)
  (sodd 0),(sodd 1),(sodd 2),(sodd 3),(sodd 4)
0 1 4 9 16
```

The first and “main” function of the three used in this recursive definition may be interpreted as follows: `sodd n` is equal to `(sodd n-1) + (2*n) – 1` or, equivalently, that `sodd n+1` equals `(sodd n) + (2*n+1) – 1`.

We will use this last relation in an inductive proof that the sum of the first `n` odd numbers is `n*n`, using the inductive hypothesis of Section D as follows:

```
   sodd n+1
   (sodd n) + (2*n+1) – 1  NB. Recursive def of sodd
   (n*n) + (2*n+1) – 1     NB. Induction hypothesis
   (n+1)*(n+1)             NB. Simple algebra
```

**Exercises**

Make recursive definitions for functions such as the sum of even integers and the sum of all integers. Then write proofs of the appropriate identities.

Test and prove the equality suggested by the following expressions for the sum of squares:

```
   n=: 6
   d=:  0 1r6 _1r2 1r3
   +/*:i.n
55
   d p. n
55
```

<span id="11f"></span>

## [11F. Guessing games](#11-proofs) [S11F.](supplement.html#s11f)

The quotes from Lakatos in Section 11A emphasize the importance of guessing at relationships, and the use of proofs to test and refine the resulting conjectures. We will now discuss techniques for guessing, emphasizing the use of the computer. However, games are seductive; the reader should perhaps limit the time spent on this section, but plan to return to it again and again.

**EACHBOX and BOX** The list function `i.` applies to an argument such as `3 4` to produce a table, but we may also wish to apply it to each of the arguments `3` and `4` to produce separate lists. Thus:

```
   a=: 3 4
   i. a
0 1  2  3
4 5  6  7
8 9 10 11
   i.3
0 1 2
   i.4
0 1 2 3
   eachbox=: &.>
   i. eachbox a
+-----+-------+
|0 1 2|0 1 2 3|
+-----+-------+
```

**PREFIX** In summing the list `2 7 1 8`, we may also wish to obtain the “subtotals” or “partial sums” by applying sumation over each prefix of the list. Thus:

```
   pref=: \
   sum=: +/
   a=: 2 7 1 8
   sum a
18
   sum pref a
2 9 10 18
   */pref a
2 14 14 112
   <./pref a
2 2 1 1
   >./pref a
2 7 7 8
```

**DIAGONAL** It is sometimes necessary to apply a function to each diagonal of a table. For example:

```
   diag=: /.
   c=: 1 2 1
   d=: 1 3 3 1
   t=: c */d
   t
1 3 3 1
2 6 6 2
1 3 3 1
   sum diag t
1 5 10 10 5 1
```

**DIFFERENCES** If `f` is a function and `g` is a guess at an equivalent function, then `f-g` gives the needed correction. For example:

```
   x=: 0 1 2 3 4 5 6 7r1
   
   each=:"0
   
   f=: +/ on i. each    NB. Sums of integers
   f x
0 0 1 3 6 10 15 21
   g=: (^ with 2 % 2:) each 
   g x
0 1r2 2 9r2 8 25r2 18 49r2
   (f-g) x
0 _1r2 _1 _3r2 _2 _5r2 _3 _7r2

   corr=: (- % 2:) each 
   corr x
0 _1r2 _1 _3r2 _2 _5r2 _3 _7r2

   gc=: g+corr          NB. Corrected guess
   (f=gc) x
1 1 1 1 1 1 1 1
```

**RATIOS** The ratio `f%g` may sometimes provide a better guide to correction. Consider, for example, the following sums of powers:

```
   f1=: +/ on (^&1) on i. each
   f2=: +/ on (^&2) on i. each
   f3=: +/ on (^&3) on i. each
   f4=: +/ on (^&4) on i. each
   f5=: +/ on (^&5) on i. each
   (f1,f2,f3,f4,:f5) x
0 0 1  3   6   10   15    21
0 0 1  5  14   30   55    91
0 0 1  9  36  100  225   441
0 0 1 17  98  354  979  2275
0 0 1 33 276 1300 4425 12201
```

For `f1` the equivalent function `g1` is, of course, the function `gc` derived above, and we will use the ratio `f3%g1` to look for a definition of a function `g3` corresponding to `f3`. Thus:

```
   g1=: gc
   (f3%g1) x
0 0 1 3 6 10 15 21
   g1 x
0 0 1 3 6 10 15 21
```

It therefore appears that `g3` may be expressed as the product of `g1` with itself:

```
   g3=: g1*g1
   (f3=g3) x
1 1 1 1 1 1 1 1
```

**TAYLOR COEFFICIENTS** For functions such as `g1` and `g3` that are expressed directly in terms of powers, quotients, products, and sums, the Taylor operator may be applied to give the coefficients of an equivalent polynomial. For example:

```
   x=: 0 1 2 3 4 5 6 7r1
   c1=: g1 t. x
   c1
0 _1r2 1r2 0 0 0 0 0
   c1&p. x
0 0 1 3 6 10 15 21
   f1 x
0 0 1 3 6 10 15 21
   c3=: g3 t. x
   c3
0 0 1r4 _1r2 1r4 0 0 0
   (f3=c3&p.) x
1 1 1 1 1 1 1 1
```

**POLYNOMIAL APPROXIMATIONS** The Taylor operator does not apply to functions such as the square root, and we use instead an expression that gives coefficients that approximate the function. Thus:

```
   f=: %:
   f x
0 1 1.4142 1.7321 2 2.2361 2.4495 2.6458
   (f x)*(f x)  NB. To verify that f is square root 
0 1 2 3 4 5 6 7
   c=: (f x) %. (x ^/ i.#x)
   c p. x
0 1 1.4142 1.7321 2 2.2361 2.4495 2.6458
```

It may be noted that the polynomial appeared to give not just an approximation, but the exact result. However, the result may be far from correct for arguments other than the `x` used in computing the coefficients, especially so for arguments outside the range of the elements of `x`. For example:

```
   c p. x+1r2
0.64666 1.2301 1.5796 1.8717 2.1204 2.3468 2.5436 2.8157
   f x+1r2
0.70711 1.2247 1.5811 1.8708 2.1213 2.3452 2.5495 2.7386
   c p. 9
5.9577
   f 9
3
```
