#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import csv
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv('Birthlast.csv')
print(df)


# In[3]:


df.head()


# In[4]:


df.tail()


# In[39]:


fig = plt.figure(figsize = (10, 5))
 
plt.bar(df['date_of_month'], df['births'], color = 'green')
plt.xlabel('date of month')
plt.ylabel('no of births')
plt.title('Number of births on every date of month')
#plt.legend()
plt.show()


# In[41]:


fig = plt.figure(figsize = (10, 5))
 
plt.bar(df['month'], df['births'], color = 'green')
plt.xlabel('day of week')
plt.ylabel('no of births')
plt.title('Total Number of births on every month of the year')
#plt.legend()
plt.show()


# In[24]:


fig = plt.figure(figsize = (10, 5))
 
plt.bar(df['day_of_week'], df['births'], color = 'green')
#plt.legend()
plt.show()


# In[29]:


df1 = df[df['day_of_week'] == 6]
df1.head()


# In[32]:


df2 =  df1[df1['date_of_month'] == 13]


# In[37]:


print(sum(df2['births']))

