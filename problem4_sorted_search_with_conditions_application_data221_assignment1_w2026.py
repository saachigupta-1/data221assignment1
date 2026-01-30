#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import random

values_of_generated_numbers = [random() for num in range(20)]
x = random()

values_of_generated_numbers.sort() #sorts it in an ascending order

firstIndex = -1

for i in range(len(values)):
    if values_of_generated_numbers[i] >= x:
        firstIndex = i
        break

print("Sorted values:", values_of_generated_numbers)
print("x value:", x)

if firstIndex != -1:
    print("First matching index:", firstIndex)
else:
    print("No value greater than or equal to x")

