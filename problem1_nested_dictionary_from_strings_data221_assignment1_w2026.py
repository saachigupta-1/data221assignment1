#!/usr/bin/env python
# coding: utf-8

# In[ ]:


threshold = 100
product = 1
currentNumber = 1

while product <= threshold:
    product *= currentNumber
    if product <= threshold:
        currentNumber += 1

print(product)
print(currentNumber)

