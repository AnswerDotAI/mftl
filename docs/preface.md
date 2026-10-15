---
title: "Preface"
anchor: "preface"
previous: "index.html"
next: "chapter-01.html"
---

In 1936, Lancelot Hogben published his still-popular *Mathematics for the Million* \[1\], stating his objective as follows:

> The view which we shall explore is that mathematics is the language of size, shape and order and that it is an essential part of the equipment of an intelligent citizen to understand this language. If the rules of mathematics are the rules of grammar, there is no stupidity involved when we fail to see that a mathematical truth is obvious. The rules of ordinary grammar are not obvious. They have to be learned. They are not eternal truths. They are conveniences without whose aid truths about the sorts of things in the world cannot be communicated from one person to another.

Our objective is similar, but we now have new tools: the development of computer programming has provided languages with grammars that are simpler and more tractable than that of conventional mathematical notation. Moreover, the general availability of the computer makes possible convenient and accurate experimentation with mathematical ideas.

For example, the exclusive use of decimal notation in beginning mathematics entails the perplexing use of approximations such as `0.333333` and ` 0.857143` for the fractions one-third and six-sevenths, intermixed with exact values such as ` 0.046875` for the drill-bit-size three sixty-fourths. The present treatment also uses *rational* arithmetic, with exact representations such as `1r3` and `6r7` and `3r64`, leading to the following computer production of an addition table for fractions:

```
   + table 1r1 1r2 1r3 1r4 1r5 1r6 1r7 1r8
+---+--------------------------------------------+
|   |  1  1r2   1r3   1r4   1r5   1r6   1r7   1r8|
+---+--------------------------------------------+
|  1|  2  3r2   4r3   5r4   6r5   7r6   8r7   9r8|
|1r2|3r2    1   5r6   3r4  7r10   2r3  9r14   5r8|
|1r3|4r3  5r6   2r3  7r12  8r15   1r2 10r21 11r24|
|1r4|5r4  3r4  7r12   1r2  9r20  5r12 11r28   3r8|
|1r5|6r5 7r10  8r15  9r20   2r5 11r30 12r35 13r40|
|1r6|7r6  2r3   1r2  5r12 11r30   1r3 13r42  7r24|
|1r7|8r7 9r14 10r21 11r28 12r35 13r42   2r7 15r56|
|1r8|9r8  5r8 11r24   3r8 13r40  7r24 15r56   1r4|
+---+--------------------------------------------+
```

Hogben continues with:

> The fact is that modern mathematics does not borrow much from antiquity. To be sure, every useful development in mathematics rests on the historical foundation of some earlier branch. At the same time, every new branch liquidates the usefulness of clumsier tools which preceded it.
>
> Although algebra, trigonometry, the use of graphs, the calculus all depend on the rules of Greek geometry, less than a dozen from the two hundred propositions of Euclid’s elements are essential to help us in understanding how to use them. The remainder are complicated ways of doing things we can do more simply when we know later branches of mathematics.

These facts make it possible to present to the layman a simple view of calculus as the study of the rate of change of a function, and to use it to provide insight into matters such as the sine and cosine functions (so useful in trigonometry and the study of mechanical and electrical vibrations), and into the exponential and its inverse the logarithm (so useful in growth and decay processes, and in matters such as the familiar musical scale).

The presentation consists largely of examples, organized in function tables and illustrated by graphs. The more analytical aspects of proofs and the grammar of mathematical notation are deferred to Chapters 11 and 10. These chapters can, however, be profitably consulted at almost any point.

An overview is provided by the Table of Contents which (when the text is used interactively on the computer) can be "clicked on with a mouse" to jump to any desired Section. Chapters 1-3 introduce Numbers, Computer use, and Graphs and visualization. Chapters 4-8 introduce many of the important tools of applied mathematics. The topics of these chapters are commonly considered to be too difficult for the layman, but are examples of Hogben's comment about "...doing things we can do more simply when we know later branches of mathematics." In particular, the treatment is greatly simplified by the use of a programming language that makes simple the use of lists (vectors) and tables (matrices).

A supplement at the end of the book contains sections that expand on the treatments in the main text. They are not essential to the main thread of development, but should be consulted on occasion (by clicking on S1A, S1B, etc.).

Although familiarity with Hogben’s book is not essential to a study of the present text, it is highly recommended to the layman, especially the brief prologue. We conclude with the continuation of the preceding quote:

> For the mathematical technician these complications may provide a useful discipline. The person who wants to understand the place of mathematics in modern civilization is merely distracted and disheartened by them. What follows is for those who have been already disheartened and distracted, and have consequently forgotten what they may have learned already, or fail to see the meaning or usefulness of what they remember. So we shall begin at the very beginning.

## 
