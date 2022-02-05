#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import csv
import matplotlib.pyplot as plt
#from pandas.tools.plotting import parallel_coordinates


# In[4]:


df = pd.read_csv('Covid - Copy.csv')
print(df)


# In[5]:


df.head()


# In[6]:


df.tail()


# In[7]:


pd.plotting.parallel_coordinates(df, 'MMSA')
for row, index in df.iterrows():
    row[]