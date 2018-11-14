# Download Stanford Parser：https://nlp.stanford.edu/software/lex-parser.shtml#Download; unzip #
# Or download Stanford Parser: https://cloud.tsinghua.edu.cn/d/095d08f52f504f32b40d/; unzip #
# Required runtime enviroment for mac also avaible at https://cloud.tsinghua.edu.cn/d/095d08f52f504f32b40d/ #

from nltk.parse.stanford import StanfordParser
import os

# set environment variables to the path to your Stanford Parser
os.environ['STANFORD_PARSER'] = '/Users/baixiaojing/StanfordNLP/stanford-parser-full-2017-06-09/stanford-parser.jar'
os.environ['STANFORD_MODELS'] = '/Users/baixiaojing/StanfordNLP/stanford-parser-full-2017-06-09/stanford-parser-3.8.0-models.jar'

# choose the model for your parser
eng_parser = StanfordParser(model_path=u'edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz')

# parse the sentence
parse = eng_parser.parse("Can you book a flight to London?".split())

# form a tree
tree = list(parse)[0]

# draw a tree
tree.draw()
