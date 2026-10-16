---
title: "10: Language and Grammar"
anchor: "10-language-and-grammar"
previous: "chapter-09.html"
next: "chapter-11.html"
---

[10A. Introduction](#10a)

[10B. Word formation](#10b)

[10C. Parsing](#10c)

[10D. Conventional mathematical Notation](#10d)

<span id="10a"></span>

## [10A. Introduction](#10-language-and-grammar) [S10A.](supplement.html#s10a)

Despite its importance, the grammar of our native language is not acquired by formal instruction, but by imitation and casual guidance in conversation. Formal grammar becomes important only at a later stage, in addressing more complex and more precise uses of language.

Formal grammar becomes particularly important in writing, where the reader has no recourse to interjected questions, but must extract meaning from the text alone.

Similar considerations apply in mathematics. Although the Hogben remarks cited in our preface emphasize the importance of language and grammar, we have introduced the grammar of our language J only informally, allowing us to concentrate on the mathematical notions it has been used to convey.

This informal approach has been made tolerable by limiting the writing required of a student in Exercises to imitation of expressions already used, and by providing guidance through conversation with the computer, a native speaker of the language. This chapter will address the formal grammar of J, and will also comment on the more loosely structured grammar of conventional mathematical notation. <span id="10b"></span>

## [10B. Word formation](#10-language-and-grammar) [S10B.](supplement.html#s10b)

Grammar is commonly taken to concern parsing the words of a sentence into phrases, and determining the order in which the phrases are to be interpreted. However, it is worth noting that the comprehension of a sentence must begin by first breaking it into its component words.

In a written English sentence this process is so simple as to go unnoticed, although the separation by spaces is somewhat complicated by things such as hyphens and apostrophes. In oral communication it is also unnoticed, not because the breaking of a continuous stream of sound into words is simple, but because (except in the case of a foreign language) it is so deeply ingrained.

In the case of J the word formation requires some attention, although it is simple enough to have been thus far treated informally by example. The computer provides a word-formation function that may be applied to a sentence enclosed in quotes. Thus:

```
   ;: '12+27'
+--+-+--+
|12|+|27|
+--+-+--+
   ;: '12+.27'
+--+--+--+
|12|+.|27|
+--+--+--+
   ;: '12+0.27'
+--+-+----+
|12|+|0.27|
+--+-+----+
   ;: '+/1 2 3 4'
+-+-+-------+
|+|/|1 2 3 4|
+-+-+-------+
```

The formal rules are stated in the J Dictionary as follows:

> The alphabet is standard ASCII, comprising digits, letters (of the English alphabet), the underline (used in names and numbers), the (single) quote, and others (which include the space) to be referred to as graphics.
>
> Alternative spellings for the national use characters (which differ from country to country) are discussed under Alphabet (`a.`).
>
> Numbers are denoted by digits, the underbar (for negative signs and for infinity and minus infinity -- when used alone or in pairs), the period (used for decimal points and necessarily preceded by one or more digits), the letter `e` (as in `2.4e3` to signify `2400` in exponential form), and the letter `j` to separate the real and imaginary parts of a complex number, as in `3e4j_0.56`. Also see the discussion of Constants.
>
> A numeric list or vector is denoted by a list of numbers separated by spaces. A list of ASCII characters is denoted by the list enclosed in single quotes, a pair of adjacent single quotes signifying the quote itself: `'can''t'` is the five-character abbreviation of the six-character word `'cannot'`. The ace `a:` denotes the boxed empty list `<$0` .
>
> Names (used for pronouns and other surrogates, and assigned referents by the copula, as in `prices=: 4.5 12`) begin with a letter and may continue with letters, underlines, and digits. A name that ends with an underline or that contains two consecutive underlines is a locative, as discussed in Section II.I.
>
> A primitive or primary may be denoted by a single graphic (such as `+` for plus) or by a graphic modified by one or more following inflections (a period or colon), as in `+.` and `+:` for *or* and *nor*. A primary may also be an inflected name, as in `e.` and `o.` for membership and pi times. A primary cannot be assigned a referent.

It would clearly be confusing if it were possible to assign the name `+` to multiplication, as in `+=: *`. <span id="10c"></span>

## [10C. Parsing](#10-language-and-grammar) [S10C.](supplement.html#s10c)

The complete parsing rules are stated in the J dictionary as follows. The leading five-point summary will suffice for most purposes:

A sentence is evaluated by executing its phrases in a sequence determined by the parsing rules of the language. For example, in the sentence `10%3+2`, the phrase `3+2` is evaluated first to obtain a result that is then used to divide `10`. In summary:

Execution proceeds from right to left, except that when a right parenthesis is encountered, the segment enclosed by it and its matching left parenthesis is executed, and its result replaces the entire segment and its enclosing parentheses.

Adverbs and conjunctions are executed before verbs; the phrase `,"2-a` is equivalent to `(,"2)-a`, not to `,"(2-a)`.

Moreover, the left argument of an adverb or conjunction is the entire verb phrase that precedes it. Thus, in the phrase `+/ . */b`, the rightmost adverb `/` applies to the verb derived from the phrase `+/ . *`, not to the verb `* .`

A verb is applied dyadically if possible; that is, if preceded by a noun that is not itself the right argument of a conjunction.

Certain trains form verbs, adverbs, and conjunctions, as described in Section F.

To ensure that these summary parsing rules agree with the precise parsing rules prescribed below, it may be necessary to parenthesize an adverbial or conjunctival phrase that produces anything other than a noun or verb.

One important consequence of these rules is that in an unparenthesized expression the right argument of any verb is the result of the entire phrase to its right. The sentence `3*p%q^|r-5` can therefore be read from left to right: the overall result is `3` times the result of the remaining phrase, which is the quotient of `p` and the part following the `%`, and so on.

Parsing proceeds by moving successive elements (or their *values* except in the case of proverbs and names immediately to the left of a copula) from the tail end of a queue (initially the original sentence prefixed by a left marker §) to the top of a stack, and eventually executing some eligible portion of the stack and replacing it by the result of the execution.

For example, if `a=: 1 2 3`, then `b=: +/2*a` would be parsed and executed as follows:

```
§ b =:  + / 2 * a  
§ b =:  + / 2 *          1  2  3
§ b =:  + / 2          * 1  2  3
§ b =:  + /          2 * 1  2  3
§ b =:  +         /  2 * 1  2  3
§ b =:  +             /  2  4  6
§ b =:              + /  2  4  6
§ b             =:  + /  2  4  6
§ b                       =:  12
§                       b =:  12
§                            12
                           § 12
```

The foregoing illustrates two points: 1) Execution of the phrase `2 * 1 2 3` is deferred until the next element (the `/`) is transferred; had it been a conjunction, the `2` would have been *its* argument, and the monad `*` would have applied to `1 2 3`; and 2) Whereas the *value* of the name `a` moves to the stack, the name `b` (because it precedes a copula) moves unchanged, and the pronoun `b` is assigned the value `12`.

Parsing can be observed using the trace conjunction `13!:16 (q.v.)`. The executions in the stack are confined to the first four elements only, and eligibility for execution is determined only by the class of each element (noun, verb, etc., an unassigned name being treated as a verb), as prescribed in the following parse table.

The classes of the first four elements of the stack are compared with the first four columns of the table, and the first row that agrees in all four columns is selected. The bold italic elements in the row are then subjected to the action shown in the final column, and are replaced by its result. If no row is satisfied, the next element is transferred from the queue:

```
EDGE      VERB        NOUN   ANY        0  Monad
EDGE+AVN  VERB        VERB   NOUN       1  Monad
EDGE+AVN  NOUN        VERB   NOUN       2  Dyad 
EDGE+AVN  VERB+NOUN   ADV    ANY        3  Adverb
EDGE+AVN  VERB+NOUN   CONJ   VERB+NOUN  4  Conj
EDGE+AVN  VERB        VERB   VERB       5  Trident
EDGE      CAVN        CAVN   CAVN       6  Trident
EDGE      CAVN        CAVN   ANY        7  Bident
NAME+NOUN ASGN        CAVN   ANY        8  Is
LPAR      CAVN        RPAR   ANY        9  Paren

Legend:	AVN	denotes	ADV+VERB+NOUN
CAVN    denotes	CONJ+ADV+VERB+NOUN
EDGE    denotes	MARK+ASGN+LPAR
```

<span id="10d"></span>

## [10D. Conventional mathematical notation](#10-language-and-grammar) [S10D.](supplement.html#s10d)

This section is a discussion of mathematical notation from the vantage point of programming languages, with emphasis on ideas from programming that might be adopted without conflict in mathematical notation.

It includes a discussion of the learnability of mathematical notation as compared with other specialized notations and with native languages, as well as the importance of such learnability.

**SOME HISTORICAL VIEWS ON NOTATION** Mathematicians have often noted the power and importance of notation. In Part IV of his two-volume *A History of Mathematical Notations* [\[3\]](references.html#ref-3), Florian Cajori offers the following examples:

> By relieving the brain of all unnecesary work, a good notation sets it free to concentrate on more advanced problems, and in effect increases the mental power of the race... By the aid of symbolism we can make transitions in reasonings almost mechanically by the eye... **A. N. Whitehead**
>
> Nothing in the history of mathematics is to me so surprising or impressive as the power it has gained by its notation or language ... But in Napier’s time, when there was practically no notation, his discovery or invention \[of logarithms\] was accomplished by mind alone, without any aid from symbols. **J.W.L. Glaisher**
>
> Some symbols, like a<sup>n</sup>, ..., log n, that were used originally for only positive integral values of n stimulated intellectual experimentation when n is fractional, negative, or complex, which led to vital extensions of ideas. **F. Cajori**
>
> The quantity of meaning compressed into small space by algebraic signs, is another circumstance that facilitates the reasonings we are accustomed to carry on by their aid. **Charles Babbage**
>
> Symbols which initially appear to have no meaning whatever, acquire gradually, after subjection to what might be called experimenting, a lucid and precise significance. **E. Mach**

On the other hand, Cajori comments on the paucity of publications concerning the general question of notation, and quotes De Morgan (“a close student of the history of mathematics”) as follows: Mathematical notation, like language, has grown up without much looking to, at the dictates of convenience and with the sanction of the majority.

In Sections 740 ff, Cajori laments the lack of standardization of mathematical notation in the following excerpts:

**§740** Uniformity of mathematical notations has been a dream of many mathematicians ...

**§741** The admonition of history is clearly that the chance, haphazard procedure of the past will not lead to uniformity.

**§746** In this book we have advanced many other instances of “muddling along” through decades, without endeavor on the part of mathematicians to get together and agree on a common sign language.

**§748** In the light of the teaching of history it is clear that new forces must be brought into action in order to safeguard the future against the play of blind chance. ... We believe that this new agency will be organization and co-operation. To be sure, the experience of the past in this direction is not altogether reassuring.

However, in *William Oughtred: A Great Seventeenth-Century Teacher of Mathematics* [\[4\]](references.html#ref-4), Cajori touches on a quite different agency that bears upon the development and teaching of mathematics -- the mathematical instrument. On page 88 we have:

> In that preface William Forster quotes the reply of Oughtred to the question of how he (Oughtred) had for so many years concealed his invention of the slide rule from himself (Forster) whom he had taught so many other things. The reply was:
>
> > That the true way of Art is not by Instruments, but by Demonstration: and that it is a preposterous course of vulgar Teachers, to begin with Instruments, and not with the Sciences, and so in-stead of Artists, to make their Scholers only doers of tricks, and as it were Iuglers ... That the vse of instruments is indeed excellent, if a man be an Artist: but contemptible being set and opposed to Art. And lastly, that he meant to commend to me, the skill of Instruments, but first he would haue me well instructed in the Sciences.

On page 93 Cajori continues with:

> It may be claimed that there is a middle ground which more nearly represents the ideal procedure in teaching. Shall the slide rule be placed in the student’s hands at the time when he is engaged in the mastery of principles? Shall there be an alternate study of the theory of logarithms and of the slide rule -- on the idea of one hand washing the other -- ...

Writing in the early 1900’s, Cajori could not have foreseen the advent of that universal mathematical instrument, the modern computer, nor its spawning of the development and study of the notations of programming languages.

**PROGRAMMING LANGUAGES** Early computers provided a small set of operations such as addition and multiplication, and were controlled by programs specifying sequences of these operations. For example, on the Harvard Mark IV [\[5\]](references.html#ref-5), the program:

```
      00 0080 10
      00 0081 11
      10 0082 11
```

*loaded* the number contained in *register* 80 into the *accumulator*, added register 81 to it, and *stored* the resulting sum in register 82.

Programs were later developed to translate from languages more congenial to mathematicians into equivalent machine language programs for subsequent execution. For example, in BASIC, a language largely derived from FORTRAN (Formula Translator) [\[6\]](references.html#ref-6), one might write:

```
      Let a=3
      Let b=5
      Let c=(a+b)*(a-b)
```

Although a few symbols from programming languages (such as FORTRAN’s \* for multiplication) have been widely adopted in math, the mathematical notation used in exposition has been largely unaffected. On the other hand, many mathematicians have been forced to learn programming languages, or to work with programmers who translate their mathematical expressions.

Moreover, many have moved to Computer Science, unwittingly following the advice of Newton, as expressed in the following excerpt from page 95 of Cajori [\[4\]](references.html#ref-4):

> “I doubt not but that there shall be in convenient time, brought to light many precepts which may tend to ye perfecting of Navigation, and the help and safety of such whose Vocations doe inforce them to commit their lives and estates in the vast Ocean to the providence of God.” Thus farr that very good and judicious man Mr. Oughtred. I will add, that if instead of sending the Observations of Seamen to able Mathematicians at Land, the Land would send able Mathematicians to Sea, it would signify much more to the improvemt of Navigation and safety of Mens lives and estates on that element.

The need to make translation manageable has led to the development of languages with simple and precisely defined grammars, that is, rules for word-formation and parsing. Although mathematical notation undoubtedly possesses parsing rules, they are rather loose, sometimes contradictory, and seldom clearly stated. It is perhaps significant that Cajori’s History makes no mention of the matter of grammar.

The proliferation of programming languages shows no more uniformity than mathematics. Nevertheless, programming languages do bring a different perspective. Not only do they provide precisely defined grammars, but they address a much wider range of applications than do any one of the notations treated by Cajori. Moreover, they sometimes adopt notions from advanced mathematics and apply them fruitfully at elementary levels.

For example, the essential notion of Heaviside’s operators [\[7\]](references.html#ref-7) (introduced in the treatment of differential equations) is the application of an entity (called an operator) which, applied to a function, produces a related function; a notion more familiar in the form f ' for the derivative of f. In APL [\[8\]](references.html#ref-8), an operator (denoted by /) is used to provide reduction over a vector argument. The sum over a vector is obtained as follows:

```
   v<-2 7 1 8 2 8
   +/v
28
```

The operator applies to any function, such as `*` (times), `>.` (max), or `<.` (min), and may therefore obviate the use of many symbols such as the capital Greek sigma and pi for summation and product:

```
   (*/v),(>./v),(<./v)
1792 8 1
```

Because of their application to a broad range of topics, their strict grammar, and their strict interpretation, programming languages can provide new insights into mathematical notation. We begin with the matter of symbols.

**ECONOMY OF SYMBOLS** Far from introducing further symbols in the manner of Oughtred’s list (of some 150) shown in §181 of Cajori [\[3\]](references.html#ref-3), programming languages are largely confined to a standard alphabet (ASCII) whose special characters are limited to the following familiar list:

```
    = < > _  + * - %  ^ $ ~ |  . : , ;  
    # ! / \  [ ] { }  " ' ` @ & ? 
```

This economy is achieved in part by adopting from mathematics the use of *reserved* words such as sin, cos, e, and log -- reserved from use as names for variables. Further economies are implicit in notions that have been used in mathematics but not systematically exploited. We will illustrate them by their use in J, a language derived from APL.

**TRAINS** Some writers, such as March and Wolf in their *Calculus* [\[10\]](references.html#ref-10), denote the function that is the sum of functions `f` and `g` by `f+g`. This notion can be exploited more generally, including constructs such as `f+g*h` for `f` added to the product of `g` and `h`. For example, using `%` for divide, and `#` for number of elements:

```
   mean=:  +/ % #    NB. Arithmetic mean or average
   mean 1 2 3 4 5
3
   com=:  ] - +/ % # NB. ] is the identity function
   com 1 2 3 4 5    NB. Center on mean
_2 _1 0 1 2
```

Non-mathematical functions can be used in a train. For example, the function `;` (which boxes each argument and catenates the boxed results) can be used to display results for convenient comparison:

```
   (];mean;com;] - +/ % #) 1 2 3 4 5
+---------+-+-----------+-----------+
|1 2 3 4 5|3|_2 _1 0 1 2|_2 _1 0 1 2|
+---------+-+-----------+-----------+
```

**INFLECTION** A symbol formed by appending a dot or colon to a given function symbol will be said to be inflected, and such inflection is used to assign related symbols to related functions, providing names that therefore have some mnemonic value. For example, in his *Laws of Thought* [\[9\]](references.html#ref-9), George Boole used `1` and `0` to denote true and false, and used the symbols for *times* and *plus* to denote the logical functions *and* and *or*.

The analogy between *times* and *and* was helpful, and the conflict with the normal use of the symbols was of no concern within the confines of logic. In a wider context it is a concern, and J uses `*`. for *and* and `+`. for *or*. Similarly, `=` is used as a truth-function (like \< and \>), whereas =: is used as a copula (to assign a referent to a name), and \<. is used for lesser-of (that is, minimum). Thus:

```
   p=:  0 0 1 1 [ q=:  0 1 0 1
   (p *. q);(p +. q);(p + q);(p < q);(p <. q)
+-------+-------+-------+-------+-------+
|0 0 0 1|0 1 1 1|0 1 1 2|0 1 0 0|0 0 0 1|
+-------+-------+-------+-------+-------+
```

**AMBIVALENCE** In the expression `a-b` the symbol `-` denotes subtraction (a function of two arguments), whereas in `-b` it denotes negation, a different (albeit related) function of one argument. This ambivalence (a “binding power” of either two or one) introduces no confusion in conventional notation, and could be exploited for other functions:

```
   a=: 2
   b=: 5
   (a-b),(-b)   NB. Subtraction and Negation (0-b)
_3 _5
   (a%b),(%b)   NB. Division and Reciprocal (1%b)
0.4 0.2
   (a^b),(^b)   NB. Power and Exponential (e^b)
32 148.413
   (a^.b),(^.b) NB. Base-a log, Natural log (e^.b)
2.32193 1.60944
```

**BONDS** In their *Combinatory Logic* [\[11\]](references.html#ref-11), Curry and Feys developed a set of combinators, which we will treat as operators in the sense of Heaviside. One of these bonds a function of two arguments (such as `^`) to one of its arguments (such as `3`) to produce a function of one argument (the cube), an operation that has come to be called *Currying* in honour of its author. For example:

```
   cube=:  ^ with 3
   log10=:  10 with ^.
   (cube ; log10) 10 50 100 200 
+-------------------+-------------------+
|1000 125000 1e6 8e6|1 1.69897 2 2.30103|
+-------------------+-------------------+
```

Conclusion. Taken together, *trains*, *inflection*, *ambivalence*, and *bonds* provide highly mnemonic representations for a host of functions. Their advantages can be fully appreciated only by careful comparison with the alternatives now used in mathematics.

**A UNIFORM NOTATION** Cajori recognizes the importance of individual invention, but warns against individual efforts to impose a uniform system:

> **§727** Invention of Symbols. -- Whenever the source is known, it is found to have been individualistic -- the conscious suggestion of one mind.
>
> **§742** This confusion is not due to the absence of individual efforts to introduce order. Many an enthusiast has proposed a system of notation for some particular branch of mathematics, with the hope, perhaps, that contemporary and succeeding workers in the same field would hasten to adopt his symbols and hold the originator in grateful remembrance. Oughtred in the seventeenth century used over one hundred and fifty signs for elementary mathematics -- algebra, geometry, and trigonometry.

Comments about the hope of grateful remembrance appear unkind; perhaps Oughtred invented symbols to clarify his own thinking, and as a tool for teaching. Nevertheless, Cajori’s main point is sound -- any attempt to impose an individual system is vain and hopeless.

However, such a system *can* be used as a basis for the discussion of mathematical notation: the precision provided (or enforced) by programming languages and their execution can identify lacunas, ambiguities, and other areas of potential confusion in conventional notation.

Discussion here will focus on such matters, and may suggest remedies. Discussion will also center on a single programming language (J), for the following reasons:

\* As indicated in my A Personal View of APL [\[12\]](references.html#ref-12), it was designed “as a simple, precise, executable notation for the teaching of a wide range of subjects”.

\* It has received some use in mathematical exposition.

\* Its simple grammar is defined by a ten-by-four table in terms of six parts of speech.

\* It uses vectors, matrices, and higher-dimensional arrays, based on the unifying concept of *rank* or *order* in Tensor Calculus [\[13\]](references.html#ref-13).

\* In addition to the bond operator already discussed, it embraces some fifteen or more operators (such as dual, Taylor, and Hypergeometric) of interest in mathematics.

**GRAMMAR** The evaluation, interpretation, or execution of the mathematical expression (or sentence) `log(a+b)*(a-b)` is carried out by identifying the primitive operations (such as addition) and then performing them in an appropriate order. The process begins with word-formation (identification of the individual words: `log`, left parenthesis, `a`, `+`, `b`, etc.), and continues with parsing the sequence of words according to a formal or informal grammar based upon the parts of speech (variables, functions, punctuation, etc.).

In natural language, the word-formation is largely unnoticed, except in listening to an unfamiliar language. In programming languages, the word-formation and parsing are commonly lumped together under the term syntax.

In J, the word- formation may be made explicit by applying the word-formation function (`;:`) to a quoted character string:

```
   ;:'log(a+b)*(a-b)'
+---+-+-+-+-+-+-+-+-+-+-+-+
|log|(|a|+|b|)|*|(|a|-|b|)|
+---+-+-+-+-+-+-+-+-+-+-+-+
```

Although programming languages adopt the term grammar from English, most use terms for the parts of speech adopted from mathematics. J, on the other hand, uses terms from English, avoiding certain ambiguities (such as the use of *operator* both as a synonym for function in elementary math, and as an operator in the sense of Heaviside), and providing additional distinctions.

The following fragment exemplifies all of the parts of speech:

```
   sqr=: ^ with 2
   area=: sqr 4
   +/\4#3
3 6 9 12
	
              PARTS OF SPEECH
			 
      MATH TERMS           ENGLISH (J) TERMS
	  
      Constants	   2 3 4   Nouns
      Variable	   area    Pronoun
      Functions	   ^ #     Verbs
      Function	   sqr     Proverb
      Operators	   / \     Adverbs
      Operator	   with    Conjunction
                   ( )     Punctuation
                   =:       Copula
```

The choice of English terms is based on the analogy between the “action words” *verb* and *function* (which derives from the Latin *fungio*, to perform). Moreover, *adverb* describes the action of an operator in applying to a verb to produce a verb, and *conjunction* reflects the use of the copulative conjunction *and* to produce a verb such as "run and hide". The word *proverb* (in the sense used here) is pronounced with a long o.

The term *variable* merits further comment. The expressions `2+2` and `2*2` and `2^2` yield identical results, *only* for the specific argument `2`, but `2*2` and `sqr 2` are identical for *any* argument. Such an identity is usually expressed by using a variable argument in the form `x*x` and `sqr x` .

However, the use of the term *variable* for the pronoun `pi` in the expression `pi=: 3.14159` is jarring, since there is no intent to allow its value to vary. Although the term *pronoun* is not commonly used in mathematics, Hogben uses it (p 432) to refer to the symbol *e* used for Euler’s number.

**SYNONYMS, ANONYMS, AND SUBSTITUTION** A synonym of a word is a word with a similar, but not necessarily equivalent, meaning. Synonyms that occur in mathematical notation can be misleading if they are carelessly interpreted.

For example, division may be expressed as a%b or a/b. Are they equivalent? If so, are a%b%c and and a/b/c and a%b/c and a/b%c equivalent? Or do they differ in order of execution?

It may be said that “one would never write such forms”, but if not, why not? Are there any rules that forbid it, and how is the beginning student to know? Notice that a/ 3/4 would probably be accepted, if only because the form 3/4 no longer denotes division: it is the commonly-accepted form of the constant three-quarters.

Synonyms for multiplication raise further questions. For example, are the following expressions all executed in the same order: a%b\*c and a%bc and a/b\*c and 3/4c?

The term anonym (a nameless person) will be used for any nameless entity: in the product abc, the matrix product M N (or MN), and the power x<sup>n</sup>, the functions applied are unnamed.

Although this anonymity normally goes unremarked, it has consequences. As remarked in the section on Programming Languages, the notation `+/v` can replace the Greek sigma for summation and, more generally, `f/` can replace other such symbols, but only for functions that are not anonymous.

Moreover, the strict use of the anonymous form abc forbids the use of multi-character mnemonic names such as age and area in elementary algebra, giving the unfortunate impression that algebra is about letters rather than about the use of names.

Multi-character names that end in digits do get used: a2 is interpreted as a single name rather than as the product of a and 2, although 2a is interpreted as two times a.

An important general notion is the validity of substituting equals for equals, and it is particularly valuable in mathematics. Nevertheless, conventional mathematical notation does not always permit it.

For example, using the anonymous form xy:

```
   x=:  3 [ y=:  4
   (x*y),(3*4),(xy),(34) NB. xy is NOT a J expression
12 12 12 34
```

**HIERARCHY AND ORDER OF EXECUTION** The polynomial expression 3x+4x<sup>2</sup>+2x<sup>4</sup> evaluates correctly only under the convention that the power function is executed before multiplication, and multiplication before addition. This heirarchy is adopted throughout mathematics, and in almost all programming languages.

In APL and J there is no heirarchy, the need for parentheses in polynomials (as in many other expressions) being obviated by the use of vectors, as in `+/3 4 2*x^1 2 4`, and in `+/c*x^e`.

The expression `1-2-3-4-5` may be interpreted differently according to how it is parenthesized: the following interpretations are used in mathematics and in J:

```
   (((1-2)-3)-4)-5  NB. Math
   1-(2-(3-(4-5)))  NB. J
```

The math result is the first element less the sum of the rest (i.e., `1-(2+3+4+5)`), and the J result is the alternating sum `(1+3+5)-(2+4)`.

Since `f/v` inserts the function `f` between elements of `v`, the J expression `-/v` gives the alternating sum, a commonly-needed result that is expressed in math as the sum over (Greek sigma) <code>(-1)<sup>i</sup> v</code>. Similarly, the alternating product is expressed as `%/v`.

Heirarchy introduces ambiguities, particularly for synonyms and anonyms, which may or may not be accorded the same positions: are a/bc and a/b\*c equivalent?

**CONSTANTS** Mathematics reserves various symbols for constants, such as *e* (for Euler’s number), and the Greek pi. Programming languages use “scientific” notation of the form `3e6` to denote `3*10^6`. Producing no conflict, this has also been widely adopted in mathematics.

Notations such as `3j4` (a complex number) and `1r2` (a rational) and `1r2p1` could be similarly adopted for many convenient constants, as illustrated by the following examples from J:

```
   2p1 1r2p1 1r4p_1   NB. Multiples of powers of pi
6.28319 1.5708 0.0795775
   3x2 2b101    NB. 3 times e sqared,101 in base 2
22.1672 5 
   2ad30 NB. Complex number, magnitude 2 at 30 deg.
1.73205j1
```

**NEUTRAL OR IDENTITY ELEMENT** In Section 2.6 of *Concrete Mathematics* [\[2\]](references.html#ref-2), Graham, Knuth and Patashnik state that “... a product of no factors is conventionally taken to be 1 (just as a sum of no terms is conventionally 0).”

These choices are not mere conventions, and may be based more firmly on the *neutral* or *identity element* of a function, that is, a value `n` (when it exists) such that `n f x` yields `x` for any argument `x`. For example, `0` is the neutral of `+`, and `1` is the neutral of `*`.

Using `k{.v` and `k}.v` to take and drop the first `k` elements of a vector `v`, we may write identities concerning sums and products over partitions of a vector:

```
   v=:  2 3 5 7 11  
   k=:  3
   (k{.v);(k}.v);((+/k{.v) + (+/k}.v));(+/v)    
+-----+----+--+--+
|2 3 5|7 11|28|28|
+-----+----+--+--+
   (*/v);((*/k{.v) * (*/k}.v))
+----+----+
|2310|2310|
+----+----+
```

The indicated identities hold as well for the case `k=: 0` (for which `k{.v` is an empty vector), but only because the results of `+/i.0` and `*/i.0` are defined to be the neutrals of `+` and `*`. The neutral of minimum (`<./i.0`) is infinity, in effect defining it.

**EMPTY CASES IN DEFINITION** In a definition of the form x(x-1)...(x-m+1) (As in Eq 2.43 of Concrete Mathematics [\[2\]](references.html#ref-2) together with the note: m factors for m not equal to 0), the notation does not show explicitly what happens in the case of m=0.

In vector notation, this definition (of the falling factorial function) becomes `*/x-i.m`, correctly including the case of the empty vector that occurs when `m` is zero. Moreover, `*/x+s*i.m` covers a host of cases; in particular, the values `_1` and `0` and `1` for `s` give the falling factorial, the ordinary power function, and the rising factorial. Non-integer values of `s` are equally useful in the finite calculus.

Because the factors in the expression change in steps like the stope in a mine, these functions are collectively called *stopes*, and the fit operator `!.` provides them in expressions of the form `^!.s`.

Furthermore, `p.!.s` provides the corresponding polynomial functions (in which the power function `^` used in the ordinary polynomial is replaced by the stope function `^!.s`). Compare the use of `^!.s` with the notations discussed in the introductory Note on Notation in [\[2\]](references.html#ref-2).

**DUALS** It is a familiar observation that almost every stated task t is preceded by some preparation p, and followed by restoration (the inverse of p). This is sometimes expressed as performing “t under p”, as in “surgery under anesthetic”.

In mathematics, the terms *dual* and *duality* are sometimes used, as in “*or* is the dual of *and* under (or with respect to) negation”, and “the duality of *and* and *or*”.

The use of under is ubiquitous in mathematics and related disciplines, but often cloaked in other terms, such as similarity in the product S<sup>-1</sup> A S, where S is a matrix of eigenvectors that maps to “natural” coordinates.

We will express “t under p” as `t under p`, using the “under” operator `under=: &.` . Thus:

```
   under=: &.
   0 0 1 1 +. under -. 0 1 0 1 NB. Or under not is and
0 0 0 1
   3 + under ^. 4      NB. Times as add under natural log
12
   3 – under (10 with ^.) 4 NB. Division using base-10 log
0.75

   (<2 1 3) + under p. (<1 0 4)    NB. Add polynomials 
+-+------------------+
|2|3.68614 1 0.813859|
+-+------------------+
```

This last example uses the function `p.` to map the polynomial roots given by the arguments to corresponding coefficients, which are then added and mapped back to give the equivalent multiplier `2` and roots `3.68614 1 0.813859`.

**LEARNABILITY OF LANGUAGE** The learnability of a discipline depends strongly on the learnability of the language used. In teaching mathematics we should therefore consider the learnability of the language used, and compare it with that of specialized languages (such as musical notation), and of our native tongue.

For example, a child can quickly learn to transcribe the following tune from musical notation to a piano, perhaps by merely watching it done by an adult:

```
--------------------------------
   O                   O
--------------------------------
        O         O         O
--------------------------------		  
             O
--------------------------------

--------------------------------
```

Further refinements such as the indication of time, sharps, flats, and phrasing may be added and learned with equal facility.

Two matters warrant further comment:

\* A less graphic presentation of the notes (such as the sequence e c a c e c) would be more difficult for a beginner to learn. Moreover, the phenomenal rate of transcription by a pianist could hardly be achieved using parallel lists of named notes. Admittedly, this speed is due in part to the musical coherence of the piece transcribed, just as our speed in reading a meaningful English sentence is much greater than in reading gibberish.

\* The ease of learning musical notation claimed in this example is due in part to the tool used; in this case the piano. The linear arrangement of the piano keys mirrors the vertical movement over the musical staff, and proves much easier to understand than the multiple strings (and absence of frets) on a violin.

With the computer and programming languages, mathematics has newly-acquired tools, and its notation should be reviewed in the light of them. The computer may, in effect, be used as a patient, precise, and knowledgeable “native speaker” of mathematical notation.

In *The Language Instinct* [\[14\]](references.html#ref-14), Pinker has treated the phenomenal learnability of natural languages as an inborn instinct in children, and in *The Symbolic Species* [\[15\]](references.html#ref-15), Deacon has presented the co-evolution of language and the human brain as an explanation of this miracle of an inborn facility.

In Deacon’s view, language has developed under evolutionary pressure to have, at least for elementary purposes, a uniform structure that is easily learned, particularly by infants. For example, the pattern in the sentences:

```
	Hold the doll
	Drop the ball
```

applies uniformly to other nouns and verbs. Moreover, these patterns extend to simple compound sentences and tenses:

```
	Drop the ball and hold the doll
	I dropped the ball and holded the doll
```

Of course a child never hears a phrase such as “holded the doll”, but uniformly applies the pattern used in “dropped”, finally adopting the anomalous forms of strong verbs such as hold. According to Pinker, this adoption occurs at a time quite independent of badgering by adults (No, dear, you held the doll).

However, in contrast to our native tongue, mathematical notation is neither uniform nor easy to learn. Consider the following examples, expressed first in English:

```
(base 10) logarithm of 3    log10 3

negation of 3               -3

factorial 3                 3! (Order of noun and verb reversed)

(# of combs of)             3 above 5 in large parentheses 

3 to the power 5            3 superscript 5

3 beside 5                  (3,5) (Parens mandatory for vectors)

this is 3                   Let t=3 (Single-letter names only)

that is  5                  Let u=5

this plus that              t+u

(is) this lessthan that     t<u Usually treated as assertions,

(is) this equalto that      t=u     rather than as more usable truth- 
                                    functions that return results
```

A review of earlier sections will suggest other examples of non-uniform notation that further increase the difficulties for a beginner.

Experienced mathematicians may well accept such non-uniformities as obvious or natural. Moreover, they will be properly concerned about the continued readability of older literature if any change were to be made. However, this is not a new problem, and there are known ways in which such change may be addressed.

Are such non-uniformities essential to mathematics, or are they simply relics of the “...chance, haphazard procedure of the past...” cited by Cajori, and therefore replacable? To illustrate the possibilities, we will repeat the foregoing examples together with equivalent expressions in two distinctly different programming languages:

```
English                 Math                 J         C

logarithm of 3          log10 3              10^.3     log10(3.0)  

negation of 3           3                    -3        -3

factorial 3             3!                   !3        fact(3)

(# of combs of)         3 above 5 in parens  3!5       outof(3,5)

3 to the power 5        3 superscript 5      3^5       pow(3.0,5.0)

3 beside 5              (3,5)                3,5

this is 3               Let t=3              this=: 3   this=3

that is 5               Let u=5              that=: 5   that=5

this plus that          t+u                  this+that this+that

(is) this equalto that  t=u                  this=that this==that
```

**A PROGRAM FOR MATHEMATICAL NOTATION** We cannot expect our mathematical notation to be as accessible as our native language. In particular, it can never enjoy the ever-present opportunity to experiment and to provide immediate and gratifying results that is enjoyed by our native language, at least not for very young children.

However, we might make mathematical notation more accessible by:

\* Complementing existing notation by notation possessing a simple and uniform grammar and using only familiar and readily available symbols.

\* Making this complementary notation executable on a computer, so that a student might easily obtain gratifying results that encourage exploration.

\* Providing material to guide exploration in a restrained manner that does not stifle the thrill of independent discovery.

**EXPLORATION** We now present examples of using the computer in exploring a few functions and operators, as well as in exploring the grammar of the notation used. We invite mathematicians to ponder the question of how they might be presented in conventional notation.

**Exp 1** From the functions: `+ - * ^ ! +. *. ^. < = > >:` select a few for exploration by entering expressions such as:

```
   16 + 36           
52 
   16 +. 36
4
```

Observe the results and attempt to identify and name the functions used; but do not spend too much time, since the next exploration provides better tools.

**Exp 2** Enter `x=: 0 1 2 3 4 5` and `y=: x` and `x +/ y` to produce an addition table. Then enter expressions for further tables to identify each of the functions listed in Exp 1. Which of the functions appear to be commutative?

**Exp 3** Define and experiment with functions such as `f=: +/*-/` and `g=: </+.=/`

**Exp 4** Repeat explorations 2 and 3 using the following symmetric lists, and comment on any interesting characteristics of the resulting tables:

```
   ]y=: x=:  0 1 2 3 4 5 6 - 3
_3 _2 _1 0 1 2 3
```

**Exp 5** Evaluate the familiar sum over (denoted by capital Greek sigma) <code>c<sub>i</sub>x<sup>i</sup></code> at `x=0`, assuming that (as is often stated) zero to the power zero is undefined.

**Exp 6** Use the results of the following expressions (and similar experiments) to state in English (and in conventional math notation) the relations among the tables generated:

```
   2 3 5 7;11 13
   x (-/ ; -~/) y
   x (</ ; =/ ; g ; <:/) y
```

**Exp 7** Enter expressions of the following forms, and then describe in English (and in mathematical notation) the effects of `~` , and state what part of speech it is in J:

```
   x (-/ ; -~/) y
   x (!/ ; !~/) y
   x (*./ ; *.~/) y
```

**Exp 8** Examine the production of tables of Stirling numbers by the expression

```
   S1=:  %.S2=:  |: (^/%.^!._1/)~ i.10r1
   
(%. N is matrix inverse, and M %. N is “matrix divide”)
```

**Exp 9** To explore the rhematic (word-formation) rules of J, enter expressions such as: `;: 'TABLE=: x (*./ ; *.~/) y'`

**Exp 10** Enter the expressions `trace=: 13 !: 16` and `9 trace 1` to invoke the tracing of subsequent expressions, that is, to show their detailed parsing and execution. Then enter `TABLE=: x (*./ ; *.~/) y` and other expressions from earlier explorations.

Tracing may be switched off by entering `9 trace 0` .

The parsing table from Section C illuminates the annotations provided by the trace.

**Exp 11** For further simple explorations use Exercises from Chapter 1 of Iverson [\[16\]](references.html#ref-16).

**SUMMARY** In this section we have attempted to:

\* Use the strict grammar and precise interpretation of programming languages to illuminate some of the vagaries of a mathematical notation that has, as De Morgan said, “...grown up without much looking to, at the dictates of convenience ...”

\* Indicate the potentially benign effects on the learnability of mathematical notation that can be provided by simple uniform notation combined with the opportunity for precise and independent exploration using computers.

\* Sketch the possibilities of adopting some complementary and non-conflicting notation executable on computers.
