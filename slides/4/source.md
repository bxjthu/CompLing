class: center, middle
# Computational Linguistics

##4. N-gram Language Models

** Xiaojing Bai **

** Tsinghua University **

** https://bxjthu.github.io/CompLing **

---

##Recap: Chomsky hierarchy

<img src="images/chomsky_hierachy_nl.png" width=800>

---
##Recap: FSA vs. FST

Recognizer (acceptor) vs. generator

.left-column-2[
A recognizer takes a string as input and <font color="red">outputs</font> _accept_ if the string is in a string of the language, and _reject_ if it is not.A generator takes a string as input and <font color="red">outputs</font> a new string.
]
.right-column-2[
> <img src="images/baa_fsa.png" width=450>

> <img src="images/baa_fst.png" width=450>
]

???

##Recap: FSA for English numbers 1-999

Updating ...<br>
<img src="images/999.png" width=1000>

---
##Recap: a formal definition of FST

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
##Recap: morphological parsing
.left-column-2[
+ **Lexion**: a list of the stems and affixes of a language

+ **morphotactics**: a model to show how the stems and affixes can fit together

+ **Orthographic rules**: a model to show the changes that occur in a word
]
.right-column-2[
<img src="images/fst_combined.png" width=400>
]

---
##Recap: questions

Difficulties of normalization and morphological parsing in Chinese?

这个门的<font color="red">把手</font>坏了好几天了。<br>
你<font color="red">把手</font>抬高一点儿。

人身上哪怕有一点小<font color="red">病痛</font>，都会影响到工作学习。<br>
这种<font color="red">病痛</font>起来真要人命。

报名选手持本人学生证，于比赛当日指定时段到达赛场。<br>
把“手持”改成“携带”？
---
##Recap: questions

Difficulties of normalization and morphological parsing in Chinese?

+ Ambiguities
+ Unknown words
+ What is a WORD?

---
##Recap: questions

How might morphological parsing work for us?

<img src="images/CCP_Congress_18th_WordCloud.jpg" width=400> <img src="images/CCP_Congress_19th_WordCloud.jpg" width=400>

.right[.smaller[[A Computational Linguistic Analysis of Party Congress Reports](images/Analysis_Party_Congress_Reports.pdf) by Li Yimeng]]
---

class: center, middle
<img src="images/word.png" width=600>

---

class: center, middle
##We will have a quiz next ...

---
##At the end of this session you will

+ understand how n-grams can model a language;<br>

+ learn how to use corpus data to compute the probabilities of n-grams;<br>

+ understand how n-grams may help to develop NLP applications;<br>

+ learn how to build n-gram models with Python.

---
.left-column-2[
##Handwriting recognition
_I have the gub!_

<video width="480" height="360" controls src="https://bxjthu.github.io/CompLing/slides/4/images/gub.mp4" type="video/mp4"</video>
]

.right-column-2[
<br><br>
> _Bank Teller #1:_<br>
Does this look like "<font color="red">gub</font>" or "gun"?

> _Bank Teller #2: _<br>
Gun. See? But what does "<font color="red">abt</font>" mean?

> _Virgil:_ <br>
It's "act". A-C-T. Act natural. Please put fifty thousand dollars into this bag and act natural.

> _Bank Teller #1:_ <br>
Oh, I see. This is a holdup?
.right[
######_Take the Money and Run_ (1969)
]
]

???
Take the Money and Run is a 1969 American mockumentary comedy film directed by Woody Allen and starring Allen and Janet Margolin (with Louise Lasser in a small role). Written by Allen and Mickey Rose, the film chronicles the life of Virgil Starkwell (Woody Allen), an inept bank robber.
---

##Speech recognition

&nbsp;|&nbsp;
 -|-
<video width="480" height="320" controls src="https://bxjthu.github.io/CompLing/slides/4/images/helen.mp4" type="video/mp4"</video> | <img src="images/siri.jpg" height=320>
---
##Augmentative communication

<img src="images/hawking.jpg" width=700>

---

.left-column-2[
##Language generation

_“You are uniformly charming!” cried he,_

_with a smile of associating and now and_

_then I bowed and they perceived a chaise_

_and four to wish for._

<br>
.right[A random sentence generated from<br>a **Jane Austen <font color="red">trigram</font> model**
]
]
.right-column-2[
.right[
<img src="images/jane_austen.jpg" width=400>
]
]

---
class: center, middle
<img src="images/delicious.png" width=850>

---

class: center, middle
<img src="images/delicious1.png" width=850>

---

##N-grams for &nbsp;&nbsp;这菜不错！不咸！

+ unigram: 这 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;菜 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;不 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;错 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;！ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;不 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;咸 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;！
<br>
+ bigram: &nbsp;&nbsp;这菜 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;菜不 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;不错 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;错！ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;！不 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;不咸 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;咸！

+ trigram: &nbsp;这菜不 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;菜不错 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;不错！ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;错！不 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ！不咸 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 不咸！

+ 4-gram: &nbsp;&nbsp;这菜不错 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 菜不错！&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 不错！不 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 错！不咸&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ！不咸！

+ 5-gram: &nbsp;&nbsp;这菜不错！&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 菜不错！不 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 不错！不咸 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 错！不咸！

+ ...

+ n-gram

---
## Conditional probability
Conditional probability is the probability of event A given the occurrence of event B, written as $P(A|B)$.

## Joint probability
Joint probability is the probability of two events in conjunction, i.e. the probability of both events together, written as $P(A \cap B)$ or $P(A,B)$.

If A and B are independent, i.e. knowing the outcome of A does not change the probability of B, or $P(B|A) = P(B)$, then $P(A \cap B) = P(A)P(B)$.

If A and B are not independent, e.g. knowing the outcome of A does change the probability of B, or $P(B|A) \neq P(B)$, then $P(A \cap B) = P(A)P(B|A)$.
---

.left-column-2[
##N-grams as a model of language

**Basic problem: **<br>
Is this a probable sequence of words in the language and how probable is it?
]

---

.left-column-2[
##N-grams as a model of language

**Basic problem: **<br>
Is this a probable sequence of words in the language and how probable is it?

<br>
Using corpus data for probabilities

```
*<s>welcome home</s>
*
*<s>welcome back</s>
*
*<s>welcome home</s>
*
*<s>you are a welcome sight</s>
*
*<s>what a welcome</s>

```
.center[
.smaller[**A toy corpus**]
]
]

.right-column-4[
<br><br>
.smaller[
w<sub>n−1</sub> | w<sub>n</sub> | count&nbsp;&nbsp; | probability
--|--|:--:|:--:
`<s>` | welcome&nbsp;&nbsp; | 3 | 0.60
`<s>` | what | 1 | 0.20
`<s>` | you | 1 | 0.20
a | welcome | 2 | 1.00
are | a | 1 | 1.00
back | `</s>` | 1 | 1.00
home | `</s>` | 2 | 1.00
sight | `</s>` | 1 | 1.00
welcome&nbsp;&nbsp; | home | 2 | 0.40
welcome | back | 1 | 0.20
welcome | sight | 1 | 0.20
welcome | `</s>` | 1 | 0.20
what | a | 1 | 1.00
you | are | 1 | 1.00

.center[
**The bigram counts and probabilities <br>for the toy corpus**
]
]
]

---
.left-column-2[
##Probabilities of bigrams

\\(
P(w\_n | w\_{n-1}) =
\frac{C(w\_{n-1}w\_n)}{\sum\_{w}C(w\_{n-1}w)} =
\frac{C(w\_{n-1}w\_n)}{C(w\_{n-1})}
\\)

##Probabilities of sequences

\\(
P(w\_1^n)
\approx \prod\_{k=1}^n P(w\_k|w\_{k-1})
\\)

Why approximately equal to?<br><br>

\\(
\footnotesize
\begin{aligned}
P(w\_1^n) & = P(w\_1)P(w\_2|w\_1)P(w\_3|w\_1^2) \cdots P(w\_n|w\_1^{n-1}) \\\
& = \prod\_{k=1}^n P(w\_k|w\_1^{k-1})
\end{aligned}
\\)
]

.right-column-4[
<br><br>
.smaller[
w<sub>n−1</sub> | w<sub>n</sub> | count&nbsp;&nbsp; | probability
--|--|:--:|:--:
`<s>` | welcome&nbsp;&nbsp; | 3 | 0.60
`<s>` | what | 1 | 0.20
`<s>` | you | 1 | 0.20
a | welcome | 2 | 1.00
are | a | 1 | 1.00
back | `</s>` | 1 | 1.00
home | `</s>` | 2 | 1.00
sight | `</s>` | 1 | 1.00
welcome&nbsp;&nbsp; | home | 2 | 0.40
welcome | back | 1 | 0.20
welcome | sight | 1 | 0.20
welcome | `</s>` | 1 | 0.20
what | a | 1 | 1.00
you | are | 1 | 1.00

.center[
**The bigram counts and probabilities <br>for the toy corpus**
]
]
]

---
##The increasing power of higher-order n-grams

<img src="images/ngram_order.png" width=1000>

---
##N-grams and their dependence on their training sets

<img src="images/ngram_training.png" width=850>

---
##N-grams for Machine translation

.left[
他 | 向 | 记者 | 介绍了 | 主要 | 内容
---|---|---|---|---|---
He &nbsp; |to &nbsp; |reporters &nbsp; |introduced &nbsp; |main &nbsp; |content
]

1. he introduced reporters to the main contents of the statement

2. he briefed to reporters the main contents of the statement

3. he briefed reporters on the main contents of the statement

---
## Advanced issues and further readings

+ J+M_3.2: Evaluating Language Models (required)

+ J+M_3.3: Generalizations and Zeros (required)

+ J+M_3.3: Smoothing (optional)

---
##At the end of this session you will

+ understand how n-grams can model a language;<br>

+ learn how to use corpus data to compute the probabilities of n-grams;<br>

+ understand how n-grams may help to develop NLP applications;<br>

+ learn how to build n-gram models with Python.

---
##Homework

+ Review (Quiz 4 on Oct. 24, 2018)

  + [J+M_3](https://bxjthu.github.io/CompLing/readings/4/J+M_3.pdf) (3.1-3.3)
  + [J+M_2](https://bxjthu.github.io/CompLing/readings/2/J+M_2.pdf)
  + [J+M_second_edition_3](https://bxjthu.github.io/CompLing/readings/2/J+M_second_edition_3.pdf) (3.1)]

+ Read

  + [Mathematical foundations](https://bxjthu.github.io/CompLing/readings/4/pre_math_manning_schutze.pdf)
  + [J+M_8](https://bxjthu.github.io/CompLing/readings/5/J+M_8.pdf) (8.1-8.4)

+ Read and practice

  + [n-gram.py](n_gram.py) by Qing Lyu

---
class: center, middle
##Next session

Hidden Markov Models and Part-Of-Speech Tagging
