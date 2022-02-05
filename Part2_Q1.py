#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import csv
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_csv('NOAA-Temperatures_new.csv')
print(df)


# In[4]:


df.head()


# In[8]:


year = df['Year']
val = df['Value']


# In[14]:


df = df.assign(Fahrenheit = lambda x:(9/5)*x['Value'] + 32)

val_f = df['Fahrenheit']
df.head()

print(sum(val_f)/len(val_f))
# In[33]:


fig = plt.figure(figsize = (20,14))


# In[54]:


x_p = [i for i in range(1880,2020,10)]

plt.bar(year,val_f,color = 'green', edgecolor = 'white')
plt.title('Bar plot of NOAA-Temperatures')
plt.tick_params(axis='x', colors='black', direction='out', length=4, width=3)
plt.xlabel('Year')
plt.axhline(y = 32, color = 'r', linestyle = '-', label = '32 Fahrenheit')
plt.axhline(y = 32, color = 'b', linestyle = '-', label = 'Avg Fahrenheit')
y1 = plt.ylabel('Degrees F+/- From Average')
y1.set_rotation(90)
plt.legend()

plt.savefig('NOAA.jpg')
plt.show()

