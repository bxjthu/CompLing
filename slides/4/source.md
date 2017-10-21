class: center, middle
# Computational Linguistics<br>
##4. N-grams and Hidden Markov Models

** Xiaojing Bai **

** Tsinghua University **

** https://bxjthu.github.io/CompLing **

---
##Recap
+ Acceptor/recognizer vs. generator



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
##Questions
 
+ How might morphological parsing work for the NLP applications in our daily life? Any example?

+ What might be the difficulties of morphological parsing in Chinese?

---

.left-column-2[
##I have the gub!
<video width="480" height="360" controls src="images/gub.mp4" type="video/mp4"</video>
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
#####_Take the Money and Run_ (1969)
]
]
---
##At the end of this session you will

+ understand what a finite state transducer is and how it might be used in morphological parsing;<br><br>

+ learn how to define a function, what is a namespace, what is a scope, and how they work.


---

“You are uniformly charming!” cried he, with a smile of associating and now and then I bowed and they perceived a chaise and four to wish for.
"Jane Austen"
Random sentence generated from a Jane Austen trigram model

---
##Assignment

**1. Review**

+ J+M 3 

> Questions: 1) How might morphological parsing work for the NLP applications in our daily life? Any example? 2) What might be the difficulties of morphological parsing in Chinese?

+ In-class practice for session 3

+ Practical 3

**2. Practice**

+ Finish the exercise of Practical 3 and submit your codes at 网络学堂. (DDL: Oct. 25)

---
class: center, middle
##Next session

N-grams and Hidden Markov Models



