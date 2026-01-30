#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

data = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}

DataFrame = pd.DataFrame(data)

DataFrame["D"] = DataFrame["A"] * DataFrame["B"]

print(DataFrame)

