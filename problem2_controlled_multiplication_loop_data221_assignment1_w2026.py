#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def length_and_parity_counter(words):
    my_dictionary_of_results = {}

    for word in words:
        length_of_word = len(word)

        if length_of_word % 2 == 0:
            parity_of_word = "even"
        else:
            parity_of_word = "odd"

        my_dictionary_of_results[word] = {
            "length": length_of_word,
            "parity": parity_of_word
        }

    return my_dictionary_of_results

words = ["data"]
print(length_and_parity_counter(words))


