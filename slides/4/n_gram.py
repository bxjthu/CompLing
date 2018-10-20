''' This is what we call 'comment' in python,
i.e., any line beginning with '#', or any lines between the 3-quote symbols will not be executed.
You can write anything here, seriously, anything, even a poem.
But normally we use comments to make our code more understandable.
So, here comes the skeleton code to help you do the n-gram calculations in the prac session today.
'''

import re
import operator

##################################################################################################
##                                       Preprocessing                                          ##
##                                                                                              ##
##################################################################################################

# read in the toy corpus file
toy_corpus = open('toy_corpus.txt', 'r')

# create a list to store the sentences
sents = []

# iterate over the lines of the toy corpus file
for line in toy_corpus:

	# filter out punctuations in the sentence (try to add more!)
	cleaned_sent = re.sub(pattern=r'[,\.!\?]', repl='', string=line)

	## you can always print the intermediate result out to see what the code has done so far
	## for the sake of clarity, we have commented the following printing statements here
	## if you want, you can uncomment them with 'cmd + /'(mac) or 'ctl + /'(win).
	# print(cleaned_sent)

	# add 2 <s> before and 2 <\s> after the sentence, because we're gonna play with trigrams
	padded_sent = '<s> ' * 2 + cleaned_sent + ' <\s>' * 2
	# print(padded_sent)

	# transform the sentence to lowercase, and split it into words with backspace
	split_sent = padded_sent.lower().split()
	# print(split_sent)

	# add the split sentence to the sents list
	sents.append(split_sent)

# print(sents)

##################################################################################################
##                            Unigram probability calculation                                   ##
##                                                                                              ##
##################################################################################################

# create a dictionary to store the unigram probabilities
# structure is {'w1':prob1, 'w2':prob2, ...}
uni_dict = {}

# iterate over every sentence
for sent in sents:
	# iterate over every word in the sentence
	for i in range(2, len(sent) - 2): # notice here we ignore the <s> / <\s> symbols, since we're calculating unigram probs
		if sent[i] not in uni_dict: # if the current word hasn't yet been met,
			uni_dict[sent[i]] = 0 # we add it to the unigram dictionary, and initialize its count to be 0
		uni_dict[sent[i]] += 1 # then, we increase the count by 1

# print(uni_dict)

# here, we transform the values in uni_dict from wordcount to word probability
# by dividing them with the total word count
uni_dict = {word: count/sum(uni_dict.values()) for word, count in uni_dict.items()}

## the above line is a compact way to do the transformation
## it's equal to these following lines:
# total_count =sum(uni_dict.values())
# for key, value in uni_dict.items():
# 	uni_dict[key] /=total_count

# sort the unigram dictionary according to probability values
sorted_uni_list = sorted(uni_dict.items(), key=operator.itemgetter(1), reverse=True)
# print out the top 10 unigrams
print('Top 10 unigrams:\n', dict(sorted_uni_list[:10]))


##################################################################################################
##                             Bigram probability calculation                                   ##
##                                                                                              ##
##################################################################################################

# similarly, create a dicionary to store bigram-probability pairs
# but differently, its structure is {'w1':{'w1':prob1, 'w2':prob2, ...}, 'w2':{'w1':prob1, 'w2':prob2, ...}}
# i.e. the values of this dictionary are also dictionaries!
bi_dict = {}

for sent in sents:
	for i in range(1, len(sent) - 2): # here we only iterate from the 2nd <s> to the last word, why?

		if sent[i] not in bi_dict: # if w1 hasn't been met,
			bi_dict[sent[i]] = {} # a dictionary is initialized for it

		if sent[i+1] not in bi_dict[sent[i]]: # if the w1w2 sequence hasn't been met,
			bi_dict[sent[i]][sent[i+1]] = 0 # we add w2 as a key to bi_dict[w1], and initialize its count to be 0
		bi_dict[sent[i]][sent[i+1]] += 1 # and then increase the count by 1

# similarly, here we transform all bigram counts to probability values
# but differently, here we're calculating conditional probabilites
bi_dict = {w1:{w2: count/sum(bi_dict[w1].values()) for w2, count in bi_dict[w1].items()} for w1, w1_dict in bi_dict.items()}

## the above line is a compact way to do the transformation
## it's equal to these following lines:
# for w1 in bi_dict:
# 	w1_total_count = sum(bi_dict[w1].values())
# 	for w2 in bi_dict[w1]:
# 		bi_dict[w1][w2] /= w1_total_count

## see what we've got for the bigram dict!
# print(bi_dict)

# here, we want to print out the 10 most common words at the start of a sentence
# i.e. after <s>
sorted_bi_list_start = sorted(bi_dict['<s>'].items(), key=operator.itemgetter(1), reverse=True)
print('10 most common starting words:\n', dict(sorted_bi_list_start[:10]))

##################################################################################################
##                            Trigram probability calculation                                   ##
##                                                                                              ##
##################################################################################################

# following previous two parts,
# try to write code to calculate trigram probabilities on your own!
# if you can, try to calculate the probability of sentences in the corpus using trigrams too.