###############################
# Constructing and manipulating CFG
###############################

from nltk import nonterminals, Nonterminal, Production

# Create some nonterminals
S, NP, VP, PP = nonterminals('S, NP, VP, PP')
N, V, P, Det = nonterminals('N, V, P, Det')

print(Production(S, [NP]))

# Create some Grammar Productions
from nltk import CFG

my_grammar = CFG.fromstring("""
  S -> NP VP
  PP -> P NP
  NP -> Det N | NP PP
  VP -> V NP | VP PP
  Det -> 'a' | 'the'
  N -> 'dog' | 'cat'
  V -> 'chased' | 'sat'
  P -> 'on' | 'in'
""")

print(my_grammar.productions())

# Check the coverage of input words by the grammar
try:
    my_grammar.check_coverage(['a','dog'])
    print("All words covered")
except:
    print("Strange")
try:
    print(my_grammar.check_coverage(['a','toy']))
except:
    print("Some words not covered")

# Parse sentences with your grammar
sent = ['a', 'dog', 'chased', 'a', 'cat']
parser = nltk.ChartParser(my_grammar)
for tree in parser.parse(sent):
    print(tree)
    
# View the tree    
TreeView(tree)

###############################
# Constructing and manipulating PCFG
###############################

# A demo

nltk.grammar.pcfg_demo()

###############################
# Constructing and manipulating DG
###############################

my_grammar = nltk.DependencyGrammar.fromstring("""
	'shot' -> 'I' | 'elephant' | 'in'
	'elephant' -> 'an' | 'in'
	'in' -> 'pajamas'
	'pajamas' -> 'my'
""")

print(my_grammar)

pdp = nltk.ProjectiveDependencyParser(my_grammar)
sent = 'I shot an elephant in my pajamas'.split()
trees = pdp.parse(sent)
for tree in trees:
	print(tree)

TreeView(tree)
