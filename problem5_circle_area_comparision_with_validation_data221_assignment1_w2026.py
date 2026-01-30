#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    if radiusOfCircle1 <= 0 or radiusOfCircle2 <= 0:
        return "Radii must be positive integers."

    area1 = math.pi * radiusOfCircle1 ** 2
    area2 = math.pi * radiusOfCircle2 ** 2

    smallerArea = min(area1, area2)
    largerArea = max(area1, area2)

    percentageCovered = (smallerArea / largerArea) * 100
    return percentageCovered


print(circleAreaCoverage(3, 5))

