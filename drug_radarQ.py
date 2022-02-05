#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np



# In[22]:


df = pd.read_csv('air.csv')
print(df)



# In[23]:

df.head(10)


# In[24]:


df.tail(10)

# df.drop(df.index[[1,10]], inplace = True)

# In[26]:

# for index,row in df.iterrows():
# 	row['Genre'] == row['Genre'].replace(' Tickets','')

print(df.head(5))
# plt.scatter(x = df['age'], y = df['alcohol-frequency'], label = 'alcohol-frequency')
# #plt.scatter(x = df['age'], y = df['marijuana-frequency'], label = '2')
# plt.scatter(x = df['age'], y = df['cocaine-frequency'], label = 'cocaine-frequency')
# plt.scatter(x = df['age'], y = df['meth-frequency'], label = 'meth-frequency')
# #plt.scatter(x = df['age'], y = df['heroin-frequency'], label = '5')


#plt.legend()
#plt.show()



categories = ['2014', '2015','2016']

restaurant_1 = df['incidents_85_99']
restaurant_2 = df['Incidents_00_14']
#restaurant_3 = df['fatalities_85_99']


label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(restaurant_2))

plt.figure(figsize=(8, 8))
plt.subplot(polar=True)
plt.plot(label_loc, restaurant_1, label='Aerolineas Argentinas')
plt.plot(label_loc, restaurant_2, label='Air Canada')
#plt.plot(label_loc, restaurant_3, label='Air France')
plt.title('Incidents realted to airlines Aerolineas Argentinas and Air Canada', size=25)
#lines, labels = plt.thetagrids(np.degrees(label_loc), labels=categories)
plt.legend()
plt.show()
