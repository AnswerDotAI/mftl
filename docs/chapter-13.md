---
title: "13: Logic and Sets"
anchor: "13-logic-and-sets"
previous: "chapter-12.html"
next: "chapter-14.html"
---

[13A. Introduction](#13a)

[13B. Or, and, and not](#13b)

[13C. Lists and sets](#13c)

[13D. Classification](#13d)

<span id="13a"></span>

## [13A. Introduction](#13-logic-and-sets) [S13A.](supplement.html#s13a)

*Boolean* or *symbolic* logic concerns propositions, a proposition being simply a function that produces one of only two possible results. These two results are commonly referred to as true and false, and (following George Boole, the father of symbolic logic) will be denoted by the numbers `1` and `0`. For example:

```
   f1=: <&0
   f2=: >&0
   x=: i:3
   x
_3 _2 _1 0 1 2 3
   f1 x
1 1 1 0 0 0 0
   f2 x
0 0 0 0 1 1 1
```

The proposition `f1` is true (that is, gives the result `1`) for any negative number, and is said to define the set of negative numbers; `f2` defines the set of positive numbers.

The list of positive numbers that occur in a list `y` may be obtained by using the result `f2 y` to copy from `y` each element of `y` for which `f2 y` is true. For example:

```
   y=: 3 1 4 1 5 9 - 3
   y
0 _2 1 _2 2 6
   f2 y
0 0 1 0 1 1
   (f2 y) # y
1 2 6
```

<span id="13b"></span>

## [13B. Or, and, and not](#13-logic-and-sets) [S13B.](supplement.html#s13b)

The function `or=: +.` may be applied to two propositions to yield a proposition that is true if either of the propositions is true. For example:

```
   or=: +.
   g=: f1 or f2
   g x
1 1 1 0 1 1 1
```

Similarly for `and=: *.`, the proposition proposition `h=: f1 and f2` is true only if both `f1` and `f2` are true. Since a number cannot be both positive and negative, `h` can never be true, and is said to define an empty set. Thus:

```
   and=: *.
   h=: f1 and f2
   h x
0 0 0 0 0 0 0
   (h x) # x

   (g x) # x
_3 _2 _1 1 2 3
```

The (monadic) function `not=: -.` negates a boolean result. For example:

```
  not=: -.
  (f1,.(not on f1),.g,.(not on g),.h,.(not on h)) x
1 0 1 0 0 1
1 0 1 0 0 1
1 0 1 0 0 1
0 1 0 1 0 1
0 1 1 0 0 1
0 1 1 0 0 1
0 1 1 0 0 1
```

<span id="13c"></span>

## [13C. Lists and sets](#13-logic-and-sets) [S13C.](supplement.html#s13c)

The set of English vowels is defined by the proposition `vow`, developed as follows:

```
   s=: 'do you love me'
   'aeiou' =/ s
0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 0 0 1
0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 1 0 0 1 0 0 0 1 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0 0 0 0 0
   or/'aeiou' =/ s
0 1 0 0 1 1 0 0 1 0 1 0 0 1

   vow=: or/ on ('aeiou'&(=/)) 
   vow s
0 1 0 0 1 1 0 0 1 0 1 0 0 1
   (vow s)#s
oouoee
   (not vow s)#s
d y lv m

   alphabet=: 'abcdefghijklmnopqrstuvwxyz '
   (vow alphabet)#alphabet
aeiou
```

It is important to understand that the set of English vowels is defined by the function `vow`, *not* by the list `'aeiou'` (nor by the same list that resulted from applying the function to the universe of the entire alphabet).

Otherwise one might confuse the question of the ordering of the defining list `'aeiou'` or repetitions of its elements (neither of which affect the definition of the function) with the question of whether a set is ordered (which it is not). <span id="13d"></span>

## [13D. Classification](#13-logic-and-sets) [S13D.](supplement.html#s13d)

A single proposition can be used to classify its arguments according to whether they belong to the set it defines, and several propositions can be used to provide several classifications. Consider, for example, a list of transactions that are recorded as a list of account numbers (`an`) and a corresponding list of credits (`cr`) to the accounts, as well as the list of all possible account numbers (`all`). Thus:

```
   an=: 1010 1040 1030 1030 1060 1010 1040 1040 1050
   cr=:  131  755  458  532  218   47  678  679  934
   all=: 1010 1020 1030 1040 1050 1060
   c=: all =/ an
   c
1 0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0
0 0 1 1 0 0 0 0 0
0 1 0 0 0 0 1 1 0
0 0 0 0 0 0 0 0 1
0 0 0 0 1 0 0 0 0
   eachrow=: "1
   cr +/ on * eachrow c
178 0 990 2112 934 218
```
