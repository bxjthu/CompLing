# Python(3.5) script to build n-gram models, calculate perplexity and generate sentences
# For the course Computational Linguistics (2017 Fall) at Tsinghua University

import json
import numpy as np
from numpy.random import random_sample


##################################################################################################
##                                        Helper Functions                                      ##
##                                     Do Not Change Anything                                   ##
##################################################################################################

def file2sents(infile):
    '''This function returns an iterator (to save memory),
    which yields one sentence (after preprocessing) each time.
    :param infile: input txt file
    :return: you can regard the return of this function as
    a list of sentences, if you don't know what 'yield' does.
    '''
    with open(infile, 'r') as f:
        for line in f:
            for sent in preprocess(line):
                yield sent

def save_vocab(vocab, filename):
    '''Save the vocabulary to a local file for later use.
    :param vocab: a list of all tokens in the vocabulary
    :param filename: name of the local file in which you want to store the vocabulary
    '''
    with open(filename, 'w') as f:
        for t in vocab:
            print(t, file=f)

def load_vocab(filename):
    '''Load vocabulary from a local file
    :param filename: name of the local file in which the vocabulary is stored
    :return: a list of all tokens in the vocabulary
    '''
    vocab = []
    with open(filename, 'r') as f:
        for l in f:
            vocab.append(l.strip('\n'))
    return vocab

def save_model(model, filename):
    '''Save the model to a local file for later use.
    :param model: n-gram model
    :param filename: name of the local file in which you want to store the model
    '''
    with open (filename, 'w') as f:
        json.dump(model, f)

def load_model(filename):
    '''Load n-gram model from a local file
    :param filename: name of the local file in which the model is stored
    :return: n-gram model (a dictionary)
    '''
    with open (filename, 'r') as f:
        return json.load(f)

def generate_character(model, prev_c):
    '''It randomly generates a single token based on the n-1
    proceeding tokens and the n-gram model.
    :param model: n-gram model
    :param prev_c: n-1 proceeding tokens
    :return: predicted token (str)
    '''
    dic = model[prev_c]
    c = np.array(list(dic.keys()))
    p = np.array(list(dic.values()))
    a = sum(p)
    bins = np.cumsum(p)
    i = np.digitize(random_sample(1), bins)
    return c[i][0]



##################################################################################################
##                                  Functions You Need To Modify                                ##
##                            Do Not Change Function Names Or Arguments                         ##
##################################################################################################

def preprocess(line):
    '''This function takes as input a string, and only keeps lower-cased English letters,
    inside-line blank spaces (' '), and four kinds of punctuation marks ',.?!'.
    '#' is added at the very front as a sentence-beginning marker,
    and '*' is added at the end as a sentence-end marker;
    e.g., 'She is 4-year-old.' should be like '#she is yearold.*' after preprocessing.
    '.?!' and a line's end are signs where to cut a sentence.
    :param line: input line (str), which may contain several sentences
    :return: a list of sentences; e.g., ['#sent1*', '#sent2*', ...]
    '''
    #########################################
    #        Complete this function         #
    #########################################



def n_gram_count(n, infile):
    '''This function calculates the count of each n-gram
    in the input file (after preprocessing). If you can't
    handle n as a flexible input, you can only consider n=2
    and n=3, sing conditions like "if n == 2:". This rule
    also applies to other functions in this script.
    :param n: n in 'n-gram', size of the gram
    :param infile: input txt file
    :return: a dictionary which stores the count of each
    n-gram in the input file; e.g. {'#ab': 123, 'and': 349, ...}
    '''
    print ('counting n_grams...')
    sents = file2sents(infile)
    count = {}

    #########################################
    #        Complete this function         #
    #########################################

    return count

def get_vocab(infile):
    '''Get the vocabulary of the input file (after preprocessing). In our case,
    the vocabulary is just 27 english letters plus ',.?!#*'.
    However, it's always a good practice to extract the vocabulary
    of the corpus you're working on.
    :param infile: input txt file
    :return: a list of all tokens in the vocabulary
    '''
    print('getting vocabulary...')
    # we need to add '_' representing unknown tokens in the vocab
    vocab = ['_']
    sents = file2sents(infile)

    #########################################
    #        Complete this function         #
    #########################################

    return vocab



def n_gram_all(n, vocab):
    '''Generate all possible n-grams given a certain vocabulary.
    You need to think thoroughly about which n-grams are not possible.
    E.g., '##a' is allowed but '###' is not; '#*', '*a' and 'a#b' are
    also not allowed (why?).
    :param n: n in 'n-gram', size of the gram
    :param vocab: a list of all tokens in the vocabulary
    :return: a list of n-grams,; or use 'yield'.
    '''
    print('smoothing...')
    # use m to store the number of all possible n-grams
    m = 0

    #########################################
    #        Complete this function         #
    #########################################

    print ('number of all possible n-grams: ', m)

def n_gram_prob(all_gram, count, delta=0.1):
    '''Calculate the probability of each n-gram, using add-δ smoothing
    (please see J&M 3ed Chapter 4.5.1). You can arbitrarily choose a
    value between 0-1 for δ.
    :param all_gram: all possible n-grams
    :param count: a dictionary which stores the count of each
    n-gram in the input file
    :param delta: the parameter for add-δ smoothing
    :return: a dictionary which stores the probabilities of all possible n-grams;
    e.g. {'#ab': 0.001, 'and': 0.542, ...}
    '''
    print('calculating probabilities...')
    prob = {}

    #########################################
    #        Complete this function         #
    #########################################

    return prob

def n_gram_model(prob):
    '''Build n-gram models, which should be a dictionary storing possibilities
     of all possible n-grams. To make sentence generation an easier task, the model
     is suggested to be in the form like this: {'#a': {'a': 0.001, 'b': 0.003, ...},
     '#b': {'a': 0.004, 'b': 0.001, ...}, ...}.
    :param prob: a dictionary which stores the probabilities of all possible n-grams
    :return: n-gram model
    '''
    print('building n_gram models...')
    model = {}

    #########################################
    #        Complete this function         #
    #########################################

    return model

def perplexity(n, model, vocab, testfile):
    '''Calculate the perplexity of a text (after preprocessing)
    given an n-gram model and a vocabulary. Replace all unknown
    tokens in the text with the unknown sign '_'.
    :param n: n in 'n-gram', size of the gram
    :param model: n-gram model
    :param vocab: vocabulary
    :param testfile: name of the test file
    :return: perplexity of the test in the test file
    '''
    print('calculating perplexity...')

    #########################################
    #        Complete this function         #
    #########################################

def generate_from_LM(n, model, m=30):
    '''It generates a sentence with at most m tokens (not counting '#' or '*')
    based on the n-gram model. You should be aware of when to stop: when a '*'
    is predicted, or m tokens have already been predicted.
    :param n: n in 'n-gram', size of the gram
    :param model: n-gram model
    :param m: max length of the generated sentence
    :return: generated sentence (str)
    '''
    # every sentence should start form (n-1) times '#' to get the first predicted token
    sentence = '#'*(n-1)

    #########################################
    #        Complete this function         #
    #########################################

    return sentence




##################################################################################################
##                                         Main Function                                        ##
##                                   Make Changes As You Like                                   ##
##################################################################################################

if __name__ == '__main__':

    # name of the training data
    train = 'de'
    infile = 'data/training.{}'.format(train)
    # name of the test data
    testfile = 'data/test'

    # define n in g-gram
    n = 4
    # define delta in add-δ smoothing
    delta = 0.001

    # define max length of generated sentence
    m = 30

    # get n-gram count
    count = n_gram_count(n, infile)

    # get vocabulary
    vocab = get_vocab(infile)
    # save vocabulary
    save_vocab(vocab, '{}_{}.vocab'.format(train, n))
    # vocab = load_vocab('{}_{}.vocab'.format(train, n))

    # get all possible n-grams
    all_gram = n_gram_all(n, vocab)

    # get probabilities for all possible n-grams, using add-δ smoothing
    prob = n_gram_prob(all_gram, count, delta)

    # get n-gram model
    model = n_gram_model(prob)
    # save n-gram model
    save_model(model, '{}_{}.model'.format(train, n))
    # model = load_model('{}_{}.model'.format(train, n))

    # print perplexity
    print(perplexity(n, model, vocab, testfile))

    # print generated sentence
    print(generate_from_LM(n, model, m))










