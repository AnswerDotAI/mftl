---
title: "12: Anagrams and Permutations"
anchor: "12-anagrams-and-permutations"
previous: "chapter-11.html"
next: "chapter-13.html"
---

[12A. Anagrams](#12a)

<span id="12a"></span>

## [12A. Anagrams](#12-anagrams-and-permutations) [S12A.](supplement.html#s12a)

Although we have discussed the importance of relations and analysis (proofs) in math, our exclusive use of numeric arguments has probably given the impression that math is exclusively about numbers. To redress the balance, we will now treat some relations concerning English words, beginning with sorting and anagrams.

The letters in a word can be sorted into alphabetical order by using the function `sort=: /:~` (which applies equally to numeric arguments). For example:

```
   sort=: /:~
   w0=: 'REVEL'
   sort w0
EELRV
   w1=: 'LEVER'
   sort w1
EELRV
   w0=w1
0 1 1 1 0
   (sort w0)=(sort w1)
1 1 1 1 1
```

As shown in the last results the words are not equal, but they are similar, in the sense that they are anagrams, or permutations of one another, containing the same letters but in a different order. Although it is not an English word, we will also call the word `'EELVR'` an anagram.

**Exercises**

Make a table of all anagrams of the word `w2=: 'AH'` (including itself).

Repeat Exercise 1 for the word `w3=: 'ART'` .

Repeat Exercise 1 for the word `w4a=: 'SPOT'` .

Repeat Exercise 1 for the word `w4b=: 'ABCD'` . To check your work, use the anagram function `A.` as illustrated below:

```
   0 A. w2=: 'AH'
AH
   1 A. w2
HA
   0 1 A. w2
AH
HA
   0 1 2 3 4 5 A. w3=: 'ART'
ART
ATR
RAT
RTA
TAR
TRA
   6 A. w3
|index error
|   6     A.w3
```

The last result indicates that there are only six anagrams of the three-letter word, with the indices `i.6`. Similar tests will show that there are twenty-four anagrams of four-letter words, leading to the following tables:

```
   (i.24) A. w4a=: 'SPOT'
SPOT
SPTO
SOPT
SOTP
STPO
STOP
PSOT
PSTO
POST
POTS
PTSO
PTOS
OSPT
OSTP
OPST
OPTS
OTSP
OTPS
TSPO
TSOP
TPSO
TPOS
TOSP
TOPS

   trans=: |:   NB. Function to transpose a table
   trans (i.24) A. w4a=: 'SPOT'
SSSSSSPPPPPPOOOOOOTTTTTT
PPOOTTSSOOTTSSPPTTSSPPOO
OTPTPOOTSTSOPTSTSPPOSOSP
TOTPOPTOTSOSTPTSPSOPOSPS

   trans (i.24) A. w4b=: 'ABCD'
AAAAAABBBBBBCCCCCCDDDDDD
BBCCDDAACCDDAABBDDAABBCC
CDBDBCCDADACBDADABBCACAB
DCDBCBDCDACADBDABACBCABA

   trans (i.24) A. i.4
0 0 0 0 0 0 1 1 1 1 1 1 2 2 2 2 2 2 3 3 3 3 3 3
1 1 2 2 3 3 0 0 2 2 3 3 0 0 1 1 3 3 0 0 1 1 2 2
2 3 1 3 1 2 2 3 0 3 0 2 1 3 0 3 0 1 1 2 0 2 0 1
3 2 3 1 2 1 3 2 3 0 2 0 3 1 3 0 1 0 2 1 2 0 1 0

   (trans (i.24) A. i.4) { 'arst'
aaaaaarrrrrrsssssstttttt
rrssttaassttaarrttaarrss
strtrsstatasrtatarrsasar
tstrsrtstasatrtarasrsara

   trans (i.24) A. 'arst'
aaaaaarrrrrrsssssstttttt
rrssttaassttaarrttaarrss
strtrsstatasrtatarrsasar
tstrsrtstasatrtarasrsara
```

The last results illustrate that anagrams of lists of numbers may be made, and that if these lists are indices (such as `i.4`) they may be used to index a word to produce its anagrams.

**Exercises**

Experiment with the function `anag=: trans on (i. on ! on # A. ])` on various lists of numbers and letters.

In making tables of anagrams by hand as required in the first list of Exercises, it was probably easy to do the first two by simply jotting down the anagrams unsystematically. However, for larger tables it becomes difficult to avoid repetitions and to ensure that the table is complete, especially if one does not know how many there are in all.

The number of anagrams of an `n`-letter word can be obtained by a simple argument: the leading letter can be chosen in `n` ways, so that the total is `n` times the number of anagrams of an (`n-1`)-letter word, leading to the product `n` times `n-1` times `n-2`, etc. -- in other words, `!n`. Thus:

```
   #w4a
4
   !#w4a
24
```

A comparison of Exercises 3 and 4 indicates that it is easier to write the table for a word whose letters are in some systematic order, preferably alphabetic. The result of `(i.24) A. 'ABCD'` suggests a systematic approach: choose the first letter of the word as the initial letter, and append to it the table for the remaining letters organized by the same principle; then choose the second letter as the initial, and so on.

**Exercises**

Enter `i.4 3 2` and `(i.4 3 2) A. 'ABCD'` and `<"2(i.4 3 2) A. 'ABCD'` . Study the results, and try similar expressions for shorter and longer words.

If `p` is any one of the six permutations of `0 1 2`, then `3,p` is a permutation of order four. However, if `p` is prefixed by any of the other possible beginnings of a permutation of order four (`2` or `1` or `0`) the result is not a permutation, but it can be made so by incrementing each element of `p` that is greater than or equal to the prefix. Thus:

```
   P=: (i.6) A. 0 1 2
   
P;(3,.P);(P>:2);(P+P>:2);(2,.P+P>:2);(1,.P+P>:1);(0,.P+P>:0)
+-----+-------+-----+-----+-------+-------+-------+
|0 1 2|3 0 1 2|0 0 1|0 1 3|2 0 1 3|1 0 2 3|0 1 2 3|
|0 2 1|3 0 2 1|0 1 0|0 3 1|2 0 3 1|1 0 3 2|0 1 3 2|
|1 0 2|3 1 0 2|0 0 1|1 0 3|2 1 0 3|1 2 0 3|0 2 1 3|
|1 2 0|3 1 2 0|0 1 0|1 3 0|2 1 3 0|1 2 3 0|0 2 3 1|
|2 0 1|3 2 0 1|1 0 0|3 0 1|2 3 0 1|1 3 0 2|0 3 1 2|
|2 1 0|3 2 1 0|1 0 0|3 1 0|2 3 1 0|1 3 2 0|0 3 2 1|
+-----+-------+-----+-----+-------+-------+-------+
```

This suggests a method for making permutations of the next higher order: replicate and modify the table of permutations of order `n`, and prefix each by an element of `i.n+1`. The scheme can also be used as the basis for a recursive definition of a function for making tables of permutations.
