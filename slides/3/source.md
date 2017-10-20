class: center, middle
# Computational Linguistics<br>
##3. Finite State Transducers and<br> Morphological Parsing

** Xiaojing Bai **

** Tsinghua University **

** https://bxjthu.github.io/CompLing **

---
##Recap
+ An FSA describes a <font color="red">finite</font> set of <font color="red">states</font> together with <font color="red">event</font>-driven <font color="red">transitions</font> between states, with transitions indicated by labelled arcs. 

+ Possible events were drawn from a finite set called the <font color="red">alphabet</font>. 

+ There is <font color="red">a start state</font> and <font color="red">several final states</font>.

+ The sequence of events that leads from the start state to a final state is said to be a sequence that is <font color="red">accepted</font> by the FSA. (acceptor/recognizer vs. generator)

+ The set of all accepted sequences is called a <font color="red">regular language</font>, which can also be defined with a <font color="red">regular expression</font> or a <font color="red">regular grammar</font>. 

<img src="images/baa_fsa.png" width=500>

---
##Deterministic FSA vs. non-deterministic FSA
.left-column-3[
<img src="images/baa_fsa.png" width=500>

<img src="images/baa_nfsa_1.png" width=500>

<img src="images/baa_nfsa_2.png" width=500>
]
.right-column-3[

+ In an DFSA, a state q<sub>_i_</sub> has only one possible next state given the input _i_.

+ In an NFSA, a state q<sub>_i_</sub> may have more than one possible next state given an input _i_.

+ For any NFSA, there is an exactly equivalent DFSA.
] 

---
###Exercise 1: Draw an FSA for ...

###Exercise 2: Write a RE that matches ...

###Exercise 3: Write codes to ...

###Exercise 4: Write codes to ...

---
##Regular expressions

+ Two kinds of errors

 + <font color="red">False positives</font>: matching strings that we should not have matched<br> (e.g. _there, then, other_)

 + <font color="red">False	 negatives</font>: not matching strings that we should have matched<br>	(e.g. _The_)

+ With NLP applications, reducing the error rate	often involves two antagonistic efforts

 + Increasing	 <font color="red">accuracy</font>	or	<font color="red">precision</font> (minimizing false positives)
 
 + Increasing <font color="red">coverage</font> or <font color="red">recall</font> (minimizing false negatives).
 
---
##Regular expressions
<img src="images/regex_1.png" width=300>
<img src="images/regex_2.png" width=300>
<img src="images/regex_3.png" width=300>

Alternatively, try .\*af{1,2}g.{0,1}k.*
---

## At the end of this session you will
+ understand what a finite state transducer is and how it might be used in morphological parsing;<br><br>

+ learn how to define a function, what is a namespace, what is a scope, and how they work.

---
##Finite state transducer (FST)

+ Finite-state morphological parsing

+ An augmentation to FSA

+ Used to map between representations (e.g. from /baa+!/ to /boo+!/)

<img src="images/baa_fsa.png" width=500>
<img src="images/baa_fst.png" width=500>

---
##FST: a formal definition

.left-column-2[

_Q_: a finite set of _N_ **states**
>_{q<sub>0</sub>, q<sub>1</sub>, q<sub>2</sub>, ... q<sub>N-1</sub>}_

_Σ_: a finite **input alphabet** of symbols 

_∆_: a finite **output alphabet** of symbols

_q<sub>0</sub>_: the **start state**

_F_: the set of **final states**, _F_ &#8838; _Q_ 
]

.right-column-2[

_δ(q, i)_: the **transition function**. Given a state _q_ &#8712; _Q_ and an input symbol _i_  &#8712; _Σ_, _δ(q, i)_ returns a set of new states, each state _q'_ &#8712; _Q_. 

_σ(q, i)_: the **output function**. Given a state _q_ &#8712; _Q_ and an input symbol _i_  &#8712; _Σ_, _σ(q, i)_ returns a set of output symbols, each symbol _o_ &#8712; _∆_ .
]

<img src="images/baa_fst.png" width=500>


---
##FST: a formal definition

.left-column-1[

_Q={q<sub>0</sub>, q<sub>1</sub>, q<sub>2</sub>, q<sub>3</sub>, q<sub>4</sub>}_

_Σ= {b,a,!}_ 

_∆= {b,o,!}_

_q<sub>0</sub>=q<sub>0</sub>_

_F= {q4}_ 
]

.right-column-1[
<img src="images/fst_tb1.png" width=340>
<img src="images/fst_tb2.png" width=340>


.center[<img src="images/baa_fst.png" width=550>]
]

---
##Morphological parsing

Example: Searching for singulars and plurals for English words

> _woodchuck|woodchuck<font color="red">s</font>_

> _fox|fox<font color="red">es</font>; fish|fish; peccuary|peccuar<font color="red">ies</font>; goose|g<font color="red">ee</font>se_

---
##Morphological parsing

Example: Searching for singulars and plurals for English words

> _woodchuck|woodchuck<font color="red">s</font>_

> _fox|fox<font color="red">es</font>; fish|fish; peccuary|peccuar<font color="red">ies</font>; goose|g<font color="red">ee</font>se_

###Parsing
Take an input and produce some sort of linguistic structure for it

+ Morphological, syntactic, semantic, discourse

+ A string, or a tree, or a network

---
##Morphological parsing

English morphology
+ Morphemes: stems and affixes
+ Types of affixes
+ Ways of combining morphemes to form words
.left-column-2[
<img src="images/morph_1.png" width=350><br>
<img src="images/morph_2.png" width=450>
]
.right-column-2[
<img src="images/derive_1.png" width=350><br>
<img src="images/derive_2.png" width=350>
]
---
##Morphological parsing

Uses 
+ Input for other parsings, esp. syntactic parsing
 
+ Web search, spell checking, ...

---
##Morphological parsing

.left-column-2[
Input&nbsp;&nbsp;&nbsp;|Morphological Parse   
-----|------
cat | _cat + N + Sing_cats | _cat + N + PL_hope | _hope + V_hopes | _hope + V + 3P + Sing_
fox | _fox + N + Sing_ 
fox | _fox + V_foxes | _fox + N + PL_foxes | _fox + V + 3P + Sing_ 
foxed | _fox + V + PastPart_
]

.right-column-2[
.left-column-2[
Stem&nbsp;&nbsp;&nbsp;|Category
-----|------
cat|_N_hope|_V_fox|_N_fox|_V_
]
.right-column-2[Affix&nbsp;&nbsp;&nbsp;|Category
-----|------^s|_PL_^s|_+ 3P + Sing_ 
^ed|_+ PastPart_
<br>
]
]
cats → _cat^s → cat + N + PL_

foxed → _fox^ed → fox + V + PastPart_

---

##Lexions and morphotactic FSAs

**Lexion**: a list of the stems and affixes of a language<br>
**morphotactics**: a model to show how the stems and affixes can fit together

reg-noun&nbsp;&nbsp;&nbsp;|irreg-sg-noun&nbsp;&nbsp;&nbsp;|irreg-pl-noun&nbsp;&nbsp;&nbsp;|plural---|---|---|---fox|goose|geese|scat|sheep|sheep|dog|mouse|mice|

.left-column-1[
<br>A morphotactic FSA<br> for English nominal inflection
]
.right-column-1[
<img src="images/fsa_n_inflection.png" width=380>
]
---
##Lexions and morphotactic FSAs

reg-verb &nbsp;&nbsp;| irreg-verb &nbsp;&nbsp;| irreg-past &nbsp;&nbsp;| past&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | past-part &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| pres-part&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 3sg
--|--|--|--|--|--|--walk | cut | caught | -ed | -ed | -ing | -s 
fry|speak|ate| | | | talk|sing|eaten| | | | impeach||sang| | | | 

.left-column-1[
<br><br>A morphotactic FSA<br> for English verbal inflection
]
.right-column-1[
<img src="images/fsa_v_inflection.png" width=600>
]
---
##FSTs for morphological parsing

reg-noun&nbsp;&nbsp;&nbsp; | irreg-pl-noun&nbsp;&nbsp;&nbsp; | irreg-sg-noun&nbsp;&nbsp;&nbsp;
---|---|---
fox | g o:e o:e s e | goose 
cat | sheep | sheep 
aardvark | m o:i u:&epsilon; s:c e | mouse

.left-column-3[
<img src="images/fst_n_inflection.png" width=600>
]
.right-column-3[
cat → _cat + N + Sg_

cat^s → _cat + N + PL_

geese → _goose + N + PL_

fox^s → _fox + N + PL_
]
---
##FSTs for morphological parsing

**Orthographic rules**: a model to show the changes that occur in a word

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="images/ribbon_cat.png" width=530>

<img src="images/ribbon_fox.png" width=600>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="images/ortho_rule.png" width=220>

---
##FSTs for morphological parsing
<img src="images/ortho_rule.png" width=220>

.left-column-1[
<br><br>An FST for the <br>E-insertion rule
]
.right-column-1[
<img src="images/fst_ortho_rule.png" width=600>
]

---
##Morphological parsing with FST lexion and rules
.left-column-2[
+ **Lexion**: a list of the stems and affixes of a language

+ **morphotactics**: a model to show how the stems and affixes can fit together

+ **Orthographic rules**: a model to show the changes that occur in a word
]
.right-column-2[
<img src="images/fst_combined.png" width=400>
]

---
##Segmentation in Chinese

"这个门的<font color="red">把手</font> 坏了好几天了"<br>
"你<font color="red">把手</font> 抬高一点儿"

"这条马路可以<font color="red">并排</font> 行驶四辆大卡车"<br>
"教务科指定了专任讲师<font color="red">并排</font> 好了课程时间表"

"人身上哪怕有一点小<font color="red">病痛</font> ，都会影响到工作学习"<br>
"这种<font color="red">病痛</font> 起来真要人命"

"本来他是想去赴宴的，<font color="red">不过</font> 这两天胃口不好，就只得做罢了"<br>
"这次考试要还是<font color="red">不过</font> ，我就自杀"

---
## At the end of this session you will

+ understand what a finite state transducer is and how it might be used in morphological parsing;<br><br>

+ learn how to define a function, what is a namespace, what is a scope, and how they work.

---
##Assignment

**1. Review**

+ J+M 3 

> Questions: 1) How might morphological parsing work for the NLP applications in our daily life? Any example? 2) What might be the difficulties of morphological parsing in Chinese?

+ In-class practice for session 3

+ Practical 3

**2. Practice**

+ Finish the exercise of Practical 3 and submit your codes at 网络学堂.

---
class: center, middle
##Next session

N-grams and Hidden Markov Models



