#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

assignmentlist = [["1", "2", "3", "4", "5", "6", "7"], 
               ["8", "9", "10", "11", "12", "13", "14"], \
               ["15", "16", "17", "18", "19", "20", "21"], \
               ["22", "23", "24", "25", "26", "27", "28"], \
               ["29", "30", "31", "-", "-", "-", "-"]]

August2005 = pd.DataFrame(assignmentlist, 
                                  columns=["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"])

August2005

