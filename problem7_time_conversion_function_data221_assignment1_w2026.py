#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def convert_seconds(seconds_since_midnight):
    if seconds_since_midnight < 0 or seconds_since_midnight >= 86400:
        return "Invalid number of seconds."

    hours = seconds_since_midnight // 3600
    minutes = (seconds_since_midnight % 3600) // 60
    seconds = seconds_since_midnight % 60

    if hours >= 12:
        period = "PM"
    else:
        period = "AM"

    display_hour = hours % 12
    if display_hour == 0:
        display_hour = 12

    return (f"{display_hour} {minutes} {seconds} {period}")


print(convert_seconds(19067))

