#!/usr/bin/env python3
arr = range(1,30)

def return_evens(num_list):
    pass
    return [num for num in num_list if num % 2 == 0 ]

def make_exclamation(sentence_list):
    pass
def make_exclamation(sentences):
    exclamated_sentences = [sentence + "!" for sentence in sentences]
    return exclamated_sentences


test = return_evens(arr)
print(test)

sent = make_exclamation(['Hello', 'Put on this', 'Go away'])
print(sent)