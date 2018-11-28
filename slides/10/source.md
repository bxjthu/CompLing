class: center, middle
# Computational Linguistics<br>
## 10. Semantic Similarity and <br>Word Sense Disambiguation

** Xiaojing Bai **

** Tsinghua University **

** https://bxjthu.github.io/CompLing **

---

## Recap: Can a computer understand the meaning of a sentence?

.left-column-3[
+ How could we tell if it did?

+ Alan Turing: Can a computer think?

  Internal states vs.observable behaviors

+ Natural language understanding

  Using observable behaviors to judge the capacity

+ Computational approaches to natural language
]
.right-column-3[
<img src="images/turing_2.png" width=320>
]
???
Turing side-stepped the question of somehow examining the internal states of a computer by instead using its behavior as evidence of intelligence.

---

## Recap: meaning representation

First-order logic as a meaning representation language
+ Basic elements
+ Variables and quantifiers
+ Lambda notation
+ The semantics of FOL
+ Event and state representations

Some notes: Broadly speaking, logic-based approaches to natural language semantics focus on those aspects of natural language which guide our judgments of <font color="red">consistency</font> and <font color="red">inconsistency</font>. The syntax of a logical language is designed to make these features formally explicit. As a result, determining properties like consistency can often be reduced to symbolic manipulation, that is, to a task that can be carried out by a computer.

???
Recap: meaning representation

+ First-order logic as a meaning representation language

+ Syntax-driven semantic analysis

+ A simplifying assumption: representing word meanings as unanalyzed symbols like _EAT_ or _JOHN_ or _RED_

More on
+ A richer model of the semantics of words
+ Lexical semantics
+ Computational lexical semantics

---

## Recap: representing the meaning of a word

+ Dictionary entries

+ Feature structures

+ Relational databases

+ Trees

+ Synsets

+ Vectors

---

## Recap: representing the meaning of a word

+ Lexical semantics<br>
  Different aspects of word meaning: word senses, word similarity and relatedness, lexical fields and frames, connotation, etc.

+ Vector semantics<br>
  Learning computational representations of the meaning of words directly from their distributions in text

---

## Recap: vectors as meaning representations

What's the difference?

<img src="images/vector_doc.png" width=700>
<img src="images/vector_word_doc.png" width=700>
<img src="images/vector_word.png" width=700>

???
Document vector (column vector): represent the meaning of a document by the words it tends to contain
Word vector (row vector): represent the meaning of a word by the documents it tends to occur in

term-document matrix vs. term-term matrix
the row (target) word
the column (context) word

---

## Recap: vectors as meaning representations

What's the difference?

.left-column-4[
<img src="images/battle_fool.png" width=600>
]

.right-column-4[
> <img src="images/result_data.png" width=400>
]

???
The spatial visualization of document vectors
The spatial visualization of word vectors
---

## At the end of this session you will

+ know about how word similarity can be measured

+ understand what are word senses and the possible relations between them

+ understand how word senses are defined in WordNet

+ understand the goal and applications of WSD

+ know about the types of algorithms for WSD

---
## Cosine for measuring word similarity

+ Word similarity as vector similarity

+ Vector similarity as the cosine of the angle between the vectors: \\(\cos(\vec{v},\vec{w})\\)

  <img src="images/result_data.png" width=400>
---
## Cosine for measuring word similarity

\\(\text{dot-product}(\vec{v},\vec{w})=\vec{v}\cdot\vec{w}\\)

+ Algebraic definition: \\(\vec{v}\cdot\vec{w}=\sum_{i=1}^Nv_iw_i=v_1w_1+v_2w_2+...+v_Nw_N\\)

+ Geometric definition: \\(\vec{v}\cdot\vec{w}=|\vec{v}||\vec{w}|\cos\theta\\)

  <img src="images/cosine.png" width=500>

???
Equivalence of the definitions
$$\cos(\vec{v},\vec{w})=\frac{\vec{v}\cdot\vec{w}}{|\vec{v}||\vec{w}|}=\frac{\sum_{i=1}^Nv_iw_i}{\sqrt{\sum_{i=1}^Nv_i^2}}$$
\\(\frac{2}{\sqrt{\sum_{i=1}^Nv_i^2}\sqrt{\sum_{i=1}^Nv_i^2}}\\)
---
.left-column-3[
## Cosine for measuring similarity: an example

<img src="images/cosine_example_1.png" width=400>

$$\cos(\text{apricot,information})=\frac{2+0+0}{\sqrt{4+0+0}\sqrt{1+36+1}}=\frac{2}{2\sqrt{38}}=.16$$

<br>
$$\cos(\text{digital,information})=\frac{0+6+2}{\sqrt{0+1+4}\sqrt{1+36+1}}=\frac{8}{\sqrt{38}\sqrt{5}}=.58$$

]
.right-column-3[
<img src="images/cosine.png" width=350>
]

---
## Food for your thought

Is the simple frequency of co-occurrence the best measure of association between words?

Are word vectors based on raw frequencies informative and discriminative enough to represent word meaning?

---
## The rationale behind the tf-idf vector model

<img src="images/non-tf-idf.png" width=800>

<img src="images/tf-idf.png" width=800>

The tf-idf weighting of the value for word _t_ in document _d_:

\\(w_{t,d} \\) = term frequency × inverse document frequency

---
## PPMI: measure of the association between words

+ Simple frequency isn’t the best measure!

  Words that are frequent but not informative or discriminative: _the, it, they_

+ Positive Pointwise Mutual	Information	(PPMI)

  How much more are the two words co-occurring in our corpus than we would have a priori expected them to appear by chance?

$$ PMI(w,c) = \log_2 \frac{P(w,c)}{P(w)P(c)} $$

$$ PPMI(w,c) = max (\log_2 \frac{P(w,c)}{P(w)P(c)} ,0)$$

???
在概率论中，如果x和y无关，p(x,y)=p(x)p(y)；如果x和y越相关，p(x,y)和p(x)p(y)的比就越大。

---

## Word senses

_carpet vs. carpets_

_sing vs. sing, sang, sung_

---

## Word senses

_carpet vs. carpets_

_sing vs. sing, sang, sung_

+ Lemma or citation form: the grammatical form of a word that is used to represent a word in dictionaries and thesaurus

+ Wordform: the full inflected or derived form of a lemma

---

## Word senses

_carpet vs. carpets_

_sing vs. sing, sang, sung_

+ Lemma or citation form: the grammatical form of a word that is used to represent a word in dictionaries and thesaurus

+ Wordform: the full inflected or derived form of a lemma

** Word sense ** : a discrete representation of one aspect of the meaning of a lemma

.smaller[
E.g.

_Instead, a <font color="red">bank</font> can hold the investments in a custodial account in the client’s name._

_But as agriculture burgeons on the east <font color="red">bank</font>, the river will shrink even more._
]
???
individually separate and distinct
---

## Relations between the senses of a word

+ Senses coincidentally sharing an orthographic form but not related

+ Related terms

  + Homonym: .smaller[e.g. bank ("financial institution") vs. bank ("sloping mound")]

  + Homonymy

  + Homograph: .smaller[e.g. bank; bat("club for hitting a ball") vs. bat ("nocturnal flying animal")]

  + Homophone: .smaller[e.g. write vs. right; piece vs. peace]

+ Related problems for NLP

???
homonym | ˈhɒmənɪm |: each of two or more words having the same spelling or pronunciation but different meanings and origins
the relation between the senses is one of homonymy
When two senses are related semantically, we call the relationship between them polysemy rather than homonymy.
Metonymy is the use of one aspect of a concept or entity to refer to other aspects of the entity, or to the entity itself.
This particular subtype of polysemy relation is often called metonymy.  
---

## Relations between the senses of a word

+ Senses semantically related

+ Related terms

  + Polysemy: .smaller[e.g. bank, school, university, hospital]

  + Metonymy: .smaller[e.g. the White House, Jane Austen, Plums]

---

## Relations between senses (rather than words)

+ Synonymy

+ Antonymy

+ Hypernymy

+ Hyponymy

+ Meronymy

---

## How to define the meaning of a word sense?

Examples from _American Heritage Dictionary_ (Morris, 1985)

|  |  
:--|:--|:--
**right** &nbsp;&nbsp;&nbsp;|_adj._ &nbsp;&nbsp;&nbsp;|located nearer the right hand esp. being on the right when facing the same direction as the observer
&nbsp;|  |  
**left** |_adj._ |located nearer to this side of the body than the right
&nbsp;|  |  
**red** &nbsp;&nbsp;&nbsp;|_n._ |the color of blood or a ruby
&nbsp;|  |  
**blood** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|_n._ &nbsp;&nbsp;&nbsp;|the red liquid that circulates in the heart, arteries and veins of animals

---
## WordNet: a database of lexical relations

+ Defining a sense through its relationship with other senses

+ The most commonly used resource for English sense relations

+ Three databases: 1) nouns, 2) verbs, 3) adjectives and adverbs

+ Representing a concept in logical terms vs. represents a concept as a list of the word senses that can be used to express the concept

+ WordNet 3.1

---
## Noun relations in WordNet

<img src="images/wordnet_noun.png" width=1000>

---
## Verb relations in WordNet

<img src="images/wordnet_verb.png" width=1000>

---

## More details about WordNet

+ [WordNet online](http://wordnetweb.princeton.edu/perl/webwn)

+ [Database statistics](http://wordnet.princeton.edu/wordnet/man/wnstats.7WN.html)

+ [A glossary of WordNet terms](https://wordnet.princeton.edu/wordnet/man/wngloss.7WN.html)

+ [Five Papers on WordNet](http://wordnetcode.princeton.edu/5papers.pdf)

+ [FAQ for linguists](https://wordnet.princeton.edu/wordnet/frequently-asked-questions/for-linguists/)

+ [Wordnet with NLTK](http://www.nltk.org/book/ch02.html#wordnet)

---

## Word sense disambiguation (WSD)

+ Lexical ambiguity and an avalanche of competing interpretations

+ WSD: the task of selecting the correct sense for a word
  + Input: a word in context along with a fixed inventory of potential senses<br>
  + Output: the correct word sense for that use

  _Reports said the plant was likely to close in December, leaving many jobless._<br><br>
  plant 1: leafy green organism<br>
  plant 2: equipment and fixtures for manufacturing<br>

+ Applications
---
## Types of algorithms for WSD

+ Supervised
.smaller[
  We know the answers for many examples and can use them to learn from their (automatically determinable) characteristics. We then apply the learned model to a comparable set of examples (not the same ones).
]
+ **Weakly supervised (knowledge-based)**
.smaller[
  **We start with no known answers, but we use secondary texts (dictionary glosses) to infer underlying relationships through the Lesk algorithm.**
]
+ Semi-supervised
.smaller[
  We know the answers for a small number of examples, and can gain more examples from the data by finding similar cases and inferring the answers they should have through bootstrapping.
]
+ Unsupervised
.smaller[
  We start with no known answers, and no predefined senses. The set of “senses” is created automatically from the instances of each word in the training set.
]
---

## Weakly supervised or knowledge-based WSD

+ Indirect supervision

+ Knowledge from dictionaries, thesauruses or similar knowledge bases

+ The original Lesk algorithm (Lesk, 1986)

+ The simplified Lesk algorithm (Kilgarriff and Rosenzweig, 2000)

---

.left-column-2[
## The simplified Lesk algorithm

<img src="images/lesk.png" width=550>

.smaller[
The COMPUTEOVERLAP function returns the number of words in common between two sets, ignoring function words or other words on a stop list.
]
]

.right-column-4[
<br><br>
.smaller[
_The <font color="red">bank</font> can guarantee <font color="red">deposits</font> will eventually cover future tuition costs because it invests in adjustable-rate <font color="red">mortgage</font> securities._

bank1

Gloss: a financial institution that accepts <font color="red">deposits</font> and channels the money into lending activities

Examples: _“he cashed a check at the bank”, “that bank holds the <font color="red">mortgage</font> on my home”_

bank2

Gloss: sloping land (especially the slope beside a body of water)

Examples: _“they pulled the canoe up on the bank”, “he sat on the bank of the river and watched the currents”_
]
]

---

## The simplified Lesk algorithm

+ Choosing the sense whose dictionary gloss or definition shares the most words with the target word’s neighborhood

+ The original Lesk algorithm (Lesk, 1986)

  Choosing the sense whose dictionary gloss or definition shares the most words with the dictionary glosses or definitions of the target word’s neighborhood

.smaller[
|  |  
:--|:--|:--
pine | 1 | kinds of <font color="red">evergreen tree</font> with needle-shaped leaves
| 2 | waste away through sorrow or illness
cone | 1 | solid body which narrows to a point
| 2 | something of this shape whether solid or hollow
| 3 | fruit of certain <font color="red">evergreen trees</font>
]
---

## Two Python implementations of the Lesk algorithms

http://www.nltk.org/howto/wsd.html

https://github.com/alvations/pywsd

<br>

```
*
* >>> wn.synset('car.n.01').definition()
* 'a motor vehicle with four wheels; usually propelled by an internal combustion engine'
*
* >>> wn.synset('car.n.01').examples()
* ['he needs a car to get to work']
*
```

---

## Measuring word similarity with WordNet

.smaller[
_They didn’t have <font color="red">newspapers</font>, <font color="red">books</font> and even <font color="red">cell phones</font> to transmit their viewpoints like we do._
]
+ A fundamental task for semantic models is to predict how similar two words’ meanings are

+ Applications: query expansion, learning sentiment lexicons, paraphrasing...

+ Thesaurus methods

+ Goal: measure how close the two target words are within the hierarchy

+ [WordNet::Similarity](http://maraca.d.umn.edu/cgi-bin/similarity/similarity.cgi)

+ [Computing semantic similarity with NLTK](http://www.nltk.org/book/ch02.html#wordnet)

---

## At the end of this session you will

+ know about how word similarity can be measured

+ understand what are word senses and the possible relations between them

+ understand how word senses are defined in WordNet

+ understand the goal and applications of WSD

+ know about the types of algorithms for WSD


---

##Homework

+ Read/Review

  + [J+M_6](https://bxjthu.github.io/CompLing/readings/9/J+M_6.pdf) (6.1-6.7)
  + [J+M_C](https://bxjthu.github.io/CompLing/readings/10/J+M_C.pdf)

+ Practice

  + http://www.nltk.org/book/ch02.html#wordnet

---
class: center, middle
## Next session

Semantic Role Labeling and Computational Discourse
