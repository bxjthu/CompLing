# define a dictionary mapping from letters to digits
replace = {'a': '', 'e': '', 'h': '', 'i': '', 'o': '', 'u': '', 'w': '', 'y': '',
                   'b': 1, 'f': 1, 'p': 1, 'v': 1,
                   'c': 2, 'g': 2, 'j': 2, 'k': 2,
                   'q': 2, 's': 2, 'x': 2, 'z': 2,
                   'd': 3, 't': 3,
                   'l': 4,
                   'm': 5, 'n': 5,
                   'r': 6
                   }

#################################################################################################
# First solution: an abstraction of the FST
#################################################################################################

def state(cur_i, in_l):
    '''
    An abstraction of one state (except the final-state) in the FST
    :param cur_i: index of current state
    :param c: input character for current state
    :return: output letter, index of next state
    '''
    # just in case there are some strange capital letters in a name
    in_l = in_l.lower()



    # index_of_a_state == output_digit_of_that_state; refer to the FST in lecture slides
    # e.g., output digit of q_1 is 1 
    # for convenience, replace q_0 with q_'', because its output digit is ''

    # self-loop
    if replace[in_l] == cur_i:
        # do not add anything to name_part
        out_d = ''
    # go to another state
    else:
        # add the corresponding digit to name_part
        out_d = str(replace[in_l])
    # get the index of next state
    next_j = replace[in_l]

    return out_d, next_j


def Soundex_1(name):
    '''
    Implementation of the Soundex algorithm
    :param name: input name
    :return: Soundex name
    '''
    # a simple check for the input; could be more sophisticated
    if type(name) != str:
        print ('The input must be a string!')
        return
    # keep the first letter
    new_name = name[0]
    # set cur_i to 's' since we start from the start_state;
    # you can name it however you want, as long as it's not in range(1, 7)
    cur_i = 's'

    # start from the second letter, and the start_state
    for l in name[1:]:
        # get the output of current state
        out_d, next_j = state(cur_i, l)
        # add output letter to name_part
        new_name += out_d
        # go to next_i
        cur_i = next_j

    # fill '0's if necessary; only keep the first 4 characters
    new_name = (new_name + '000')[:4]
    return new_name













#################################################################################################
# Second solution: an abstraction of the FST
#################################################################################################

def Soundex_2(name):
    '''
    Implementation of the Soundex algorithm
    :param name: input name
    :return: Soundex name
    '''
    # a simple check for the input; could be more sophisticated
    if type(name) != str:
        print ('The input must be a string!')
        return
    else:
        # make letters (except the first) in name a list
        name_part = list(name)[1:]
        # define a list to store digits
        digit = ''
        # define a variable to store the corresponding digit of the previous letter
        pre = 0

        for l in name_part:
            # just in case there are some strange capital letters in a name
            l = l.lower()
            # replace the current letter with its corresponding digit
            cur = replace[l]
            # if the digit of the current letter is different from that of the previous one
            if cur != pre:
                # append the digit to the list
                digit += str(cur)
                # update pre
                pre = cur
            # if not
            else:
                # skip this letter
                continue

        # fill '0's if necessary; only keep the first 3 digits
        digit = (digit + '000')[:3]
        # join the first letter and  digits
        new_name = name[0] + digit

        return new_name






print (Soundex_1('Jarrrofsky'), Soundex_2('Jarrrofsky'))
print (Soundex_1('Honeyman'), Soundex_2('Honeyman'))




