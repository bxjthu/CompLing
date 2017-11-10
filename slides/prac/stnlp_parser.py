# 1. Download Stanford Parser：https://nlp.stanford.edu/software/lex-parser.shtml#Download; unzip


from nltk.parse.stanford import StanfordParser
import os

# set environment variables to the path to your Stanford Parser
os.environ['STANFORD_PARSER'] = '/Users/yeyuxiao/StanfordNLP/stanford-parser-full-2017-06-09/stanford-parser.jar'
os.environ['STANFORD_MODELS'] = '/Users/yeyuxiao/StanfordNLP/stanford-parser-full-2017-06-09/stanford-parser-3.8.0-models.jar'

# choose the model for your parser
eng_parser = StanfordParser(model_path=u'edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz')

# parse the sentence
parse = eng_parser.parse("Can you book a flight to London?".split())

# form a tree
tree = list(parse)[0]

# draw a tree
tree.draw()