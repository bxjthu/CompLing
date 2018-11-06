import nltk
from nltk.parse.generate import generate
# generate(grammar, start=None, depth=None, n=None) Generates an iterator of all sentences from a CFG.
# param grammar: The Grammar used to generate sentences.
# param start: The Nonterminal from which to start generate sentences.
# param depth: The maximal depth of the generated tree.
# param n: The maximum number of sentences to return.
# return: An iterator of lists of terminal tokens.

recap_grammar = nltk.CFG.fromstring("""
    S -> NP VP
    VP -> VP PP
    VP -> V
    VP -> V NP
    VP -> V VP
    NP -> NP PP
    PP -> P NP
    V -> 'can'
    V -> 'fish'
    NP -> 'they'
    NP -> 'fish'
    NP -> 'rivers'
    NP -> 'pools'
    NP -> 'December'
    NP -> 'Scotland'
    NP -> 'it'
    P -> 'in'
    """)

for sentence in generate(recap_grammar):
    print(' '.join(sentence))
