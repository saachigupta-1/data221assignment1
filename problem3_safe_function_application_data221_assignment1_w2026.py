#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def power_of_numbers(x, y):
    return x ** y


pairs_of_numbers = [[5, 2], [3, -1], [4, 3], [2, 0]]
results_after_power = []

for x, y in pairs_of_numbers:
    if y >= 0:
        results_after_power.append(power_of_numbers(x, y))

print(results_after_power)

