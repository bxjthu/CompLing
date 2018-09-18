class: center, middle
# Computational Linguistics<br>
##1. Introduction
** Xiaojing Bai **

** Tsinghua University **

** https://bxjthu.github.io/CompLing **
---
class: center, middle
##That the powerful play goes on,
##and you may contribute a verse.
<img src="images/ainewworld.gif" width=300>
---
class: center, middle
<font color="gray">
##That the powerful play goes on,
##and you may contribute a verse.</font>
##What will your verse be?<br><br><br>
---
## At the end of this session you will
+ understand what computational linguistic is in the general sense;

+ understand what this course is for and what it focuses on;

+ have some preliminary but important ideas about computational linguistic;

+ get started with Python, NLTK, and PyCharm;

+ learn basic data types and sequence operations in Python.
---
class: center, middle
##Giving computers the ability
##to process human language
---
<img src="images/apps.png" width=105%>
---
class: center, middle
##Giving computers the ability
##to process human language
A vibrant interdisciplinary field <br>
with many names corresponding to its many facets
<br>

Overlapping fields in different departments
---
## What is _Computational Linguistics?_
.left-column-1[
<img src="images/acl_nav.png" width=200>
]

.right-column-1[
<img src="images/acl_logo.png" width=400><br><br>

The premier international scientific and professional society for people working on computational problems involving human language

Founded in 1962 and originally named the Association for Machine Translation and Computational Linguistics

For more information: https://www.aclweb.org/
]
---
## What is _Computational Linguistics?_
Computational linguistics is the scientific study of <font color="red">language</font> from a computational perspective.

Computational linguists are interested in providing <font color="red">computational models</font> of various kinds of linguistic phenomena. These models may be <font color="red">"knowledge-based"</font> ("hand-crafted") or <font color="red">"data-driven"</font> ("statistical" or "empirical").

Work in computational linguistics is in some cases motivated from a scientific perspective in that one is trying to provide <font color="red">a computational explanation for a particular linguistic or psycholinguistic phenomenon</font>; and in other cases the motivation may be more purely technological in that one wants to provide <font color="red">a working component of a speech or natural language system</font>.

---
## What is _Computational Linguistics?_
Indeed, the work of computational linguists is incorporated into many <font color="red">working systems</font> today, including speech recognition systems, text-to-speech synthesizers, automated voice response systems, web search engines, text editors, language instruction materials, to name just a few.

> _“Linguistics has <font color="red">a hundred-year history</font> as a scientific discipline, and computational linguistics has <font color="red">a fifty-year history</font> as a part of computer science. But it is only in <font color="red">the last decade or so</font> that language understanding has emerged as an industry reaching millions of people, with information retrieval and machine translation available on the Internet, and speech recognition becoming popular on desktop computers."_

.right[Peter Norvig and Stuart Russell. _Foreword_. J+M 2nd]
---

## Fire the _linguists_ ?
_<p align="right">“Every time I fire a linguist, <br>_
_the performance of the speech recognizer goes up.”</p>_                 
<p align="right">Frederick Jelinek (1932 – 2010)</p>

###Rationalism vs. Empiricism (rule-based vs. statistics-based)

Suggested readings:

.smaller[
+ Church, K. (2011). A pendulum swung too far. _Linguistic Issues in Language Technology_, 6(5), 1-27.

+ Wintner, S. (2009). What science underlies natural language engineering?. _Computational Linguistics_, 35(4), 641-644.

+ 宗成庆 (2008).《统计自然语言处理》. 北京: 清华大学出版社.

+ 冯志伟 (2008). 序言.《统计自然语言处理》 (宗成庆著). 北京: 清华大学出版社.
]
---
## [About this course](https://bxjthu.github.io/CompLing/)

+ Overview

+ Aims

+ Prerequisite

+ Teaching

+ Readings

+ Grading

+ Tentative schedule

---
## Preliminary but important …

+ Some brief history

+ Knowledge in natural language processing

+ Complexity of language

+ Models and algorithms<br><br>

Required reading: [J+M_1](https://bxjthu.github.io/CompLing/readings/1/J+M_1.pdf)

---
## Some brief history - a sketch
+ 1940s – 1950s: foundational insights

+ 1957 – 1970: the two camps

+ 1970 – 1983: four paradigms

+ 1983 – 1993: empiricism and finite-state models redux 

+ 1994 – 1999: the field comes together

+ 2000 – 2008: the rise of machine learning

---
## Some brief history - old events
+ 1949 Warren Weaver’s memorandum

+ 1950 Turing Test

+ 1952 First conference on MT at MIT 

+ 1954 First MT demo by Georgetown University and IBM 

+ 1954 _Mechanical Translation_ >>> 1980 _Computational Linguistics_ 

+ 1957 Chomsky’s _Syntactic Structures_ 

+ 1962 The Association for Machine Translation and <font color="red">Computational Linguistics</font> 

+ 1966 The (in)famous ALPAC report 

---
.left-column-3[
##Knowledge in natural language processing

Mankind ﬁnds a mysterious, obviously artiﬁcial, monolith buried on the moon and, with the intelligent computer HAL, sets off on a quest... <br><br>

_Dave Bowman: Open the pod bay doors, HAL. _

_HAL: I’m sorry Dave, I’m afraid I can’t do that. _<br><br>

.smaller[Stanley Kubrick and Arthur C. Clarke:<br>
_2001: A Space Odyssey_]
]

.right-column-3[
<br><br>
<img src="images/2001.png" width=300>
]
---
##Knowledge in natural language processing
###What would HAL need to know about language?

---
##Knowledge in natural language processing
###Homework 0: Task 1

Question 1: With an electronic application in your daily life, which has the ability to process human language, analyze what it would need to know about language to perform the particular NLP task(s)?

---
##Knowledge in natural language processing
###What would HAL need to know about language?

+ **Phonetics and phonology**: knowledge about linguistic sounds

+ **Morphology**: knowledge of the meaningful components of words

+ **Syntax**: knowledge of the structural relationships between words

+ **Semantics**: knowledge of meaning

+ **Pragmatics**: knowledge of the relationship of meaning to the goals and intentions of the speaker

+ **Discourse**: knowledge about linguistic units larger than a single utterance

---
##Knowledge in natural language processing
<video width="1000" controls src="images/hal-1.mp4" type="video/mp4"</video>

---
##Knowledge in natural language processing
<video width="1000" controls src="images/hal-2.mp4" type="video/mp4"</video>

---
##Complexity of language
###Resolving ambiguity at different levels
e.g. _I made her duck._
---
##Complexity of language
###Resolving ambiguity at different levels
e.g. _I made her duck._

+ I cooked waterfowl for her.

+ I cooked waterfowl belonging to her.

+ I created the (plaster?) duck she owns.

+ I caused her to quickly lower her head or body.

+ I waved my magic wand and turned her into undifferentiated waterfowl.

---
##Complexity of language
###Difficulties in Chinese information processing .smaller[中文信息处理]

Suggested readings:

.smaller[
俞士汶等: [汉语自动分析的特殊困难与对策](https://bxjthu.github.io/CompLing/readings/1/俞士汶_汉语自动分析的特殊困难与对策.pdf)

詹卫东: [现代汉语歧义现象举例](https://bxjthu.github.io/CompLing/readings/1/ambiguity_examples.pdf)
]
---
##Models and algorithms
###How do NLP systems work?

<p align="center"><img src="images/NLP.JPG" width=900></p>
---
##Models

+ A model of an **object** is a physical representation that shows what it looks like or how it works. The model is often smaller than the object it represents.

+ A model of a **system or process** is a theoretical description that can help you understand how the system or process works, or how it might work. 

+ Language model: a <font color="red">formal</font> description of linguistic knowledge

+ Important models: state machines, rule systems, logic, probabilistic models, vector-space models

---
##Models - rule systems
<img src="images/grammar_model_1.png" width=320>
<img src="images/grammar_model_2.png" width=320>
<img src="images/grammar_model_3.png" width=320>
---
##Models - rule systems and probabilistic models
.left-column-1[
<img src="images/grammar_model_1.png" width=320>
]
.right-column-1[
<img src="images/grammar_model_4.png" width=500>
<img src="images/grammar_model_5.png" width=700>
]
---
##Algorithms
###Homework 0: Task 1

Question 2:

1) Read the algorithm in [the picture](https://bxjthu.github.io/CompLing/docs/images/algorithm_quit_job.jpeg) carefully, which is supposed to help when one wants to know whether he should quit his job. Is the algorithm properly designed?

2) Design an algorithm likewise, which can identify English sentences that use the passive voice (_e.g. The book has been returned_).
---
.left-column-2[
##Algorithms
]
.right-column-2[
<div style="text-align:center"><img src="images/algorithm.png" width=500></div>
]

---
.left-column-2[
##Algorithms
+ An algorithm is a series of mathematical <font color="red">steps</font>, especially in a computer program, which will give you the answer to a particular kind of problem or question.

+ Important algorithms: state space search algorithms, machine learning algorithms
]
.right-column-2[
<div style="text-align:center"><img src="images/algorithm.png" width=500></div>
]

---
.left-column-2[
##Algorithms
###Post-class practice (optional)
Write code to implement this algorithm, which can identify English sentences that use the passive voice.

<br>
.smaller[
_An_: a set of the past participles of irregular verbs

_Bn_: a set of words that end with "ed" but are not the past participles of regular verbs
]
]
.right-column-2[
<div style="text-align:center"><img src="images/algorithm.png" width=500></div>
]

---
##The Turing Test

.left-column-3[
<img src="images/turing_1.png" width=550>
]
.right-column-3[
<img src="images/turing_2.png" width=300>
<br><br><br>By Alan Turing in 1950
]
---
##The Turing Test

We may hope that machines will eventually compete with men in all purely
intellectual fields. But which are the best ones to start with? Even this is a
difficult decision. Many people think that a very abstract activity, like the
playing of chess, would be best. It can also be maintained that it is best to
provide the machine with the best sense organs that money can buy, and
then <font color="red">teach it to understand and speak English</font>. This process could follow
the normal teaching of a child. Things would be pointed out and named,
etc. Again I do not know what the right answer is, but I think both approaches
should be tried.

**We can only see a short distance ahead, but we can see plenty there that
needs to be done. ** <br> <br>

.right[
Turing, A. M. (1950). Computing machinery <br>
and intelligence. _Mind_, 59(236), 433-460.
]

---
.left-column-2[
<img src="images/imitation_game.jpg" width=400>]
.right-column-2[
<br><br><br><br><br><br><br><br><br><br><br><br><br><br>
.smaller[
Directed by Morten Tyldum <br>
Written by Graham Moore <br>
Based on _Alan Turing: The Enigma by Andrew Hodges_ ]]
---
## At the end of this session you will
+ understand what computational linguistic is in the general sense;

+ understand what this course is for and what it focuses on;

+ have some preliminary but important ideas about computational linguistic;

+ get started with Python, NLTK, and PyCharm;

+ learn basic data types and sequence operations in Python.

---
##Homework

+ Review: [J+M_1](https://bxjthu.github.io/CompLing/readings/1/J+M_1.pdf) (Quiz 1 on Sept. 26, 2018)

+ Read: [J+M_2](https://bxjthu.github.io/CompLing/readings/2/J+M_2.pdf)

+ Read and practice: http://www.nltk.org/book/ch01.htmlz

---
class: center, middle
##Next session

Regular Expressions, Text Normalization,

and Finite State Transducers
