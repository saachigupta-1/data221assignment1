#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def distribution_analysis(numbers):
    result_dictionary = {}
    total_count = len(numbers)

    for value in sorted(set(numbers)):
        counter_of_number = 0
        for number in numbers:
            if number <= value:
                counter_of_number = counter_of_number + 1
        result_dictionary[value] = (counter_of_number / total_count) * 100

    return result_dictionary


numbers = [3, 1, 2, 3, 4, 2]
print(distribution_analysis(numbers))

