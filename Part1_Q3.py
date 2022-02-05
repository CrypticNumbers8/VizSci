import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import random
from array import array
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import scipy.stats.qmc
#from pyDOE import *
import lhsmdu

a1 = np.random.uniform(low = 0.0, high = 1.0, size = 100)  

#print("length of array:",len(a1))
# #print(a1)
# plt.title('Boxplot of 100 random numbers uniformly distributed in [0,1]')
# plt.xlabel('Array')
# plt.ylabel('Values of elements in the array')
# plt.boxplot(a1)
# #plt.show()


# plt.hist(a1, bins=20, color='yellow', edgecolor='red')
# plt.title("Histogram representing the 100 random numbers uniformly distributed in [0,1]")
# plt.xlabel("Random numbers in range [0,1]")
# plt.ylabel("Frequency according to magnitude range")
# #plt.show()


a2 = np.random.normal(50,14,200)



#print(a2)
print("length of array:", len(a2))
temp_a2 = sorted(a2)
print("5 min elements:", temp_a2[:5])
print("5 max elements:", temp_a2[-5:])


# # In[98]:


# plt.boxplot(a2)


# plt.title('Boxplot of 200 random numbers normally distributed in [1,100]')
# plt.xlabel('Array')
# plt.ylabel('Values of elements in the array')

# #plt.show()


# # In[99]:


# plt.hist(a2, bins=20, color='yellow', edgecolor='blue')

# plt.title("Histogram representing 200 random numbers normally distributed in [1,100]")
# plt.xlabel("Random numbers in approx range of [0, 100]")
# plt.ylabel("Frequency according to magnitude range")
# #plt.show()

#writing arrays into binary files
output_file = open('bin_file_1','wb')
float_array_a1 = array('d', a1)
#float_array_a2 = array('d', a2)
float_array_a1.tofile(output_file)
#float_array_a2.tofile(output_file)
output_file.close()

input_file = open('bin_file_1','rb')
float_array_a1_read = array('d')
float_array_a1_read.fromstring(input_file.read())
#print(float_array_a1_read)


output_file1 = open('bin_file_2','wb')
float_array_a2 = array('d', a2)
#float_array_a2 = array('d', a2)
float_array_a2.tofile(output_file1)
#float_array_a2.tofile(output_file)
output_file1.close()

input_file1 = open('bin_file_2','rb')
float_array_a2_read = array('d')
float_array_a2_read.fromstring(input_file1.read())
#print("float read back:",float_array_a2_read)


count, bins_count = np.histogram(float_array_a1_read)

pdf = count/sum(count)

cdf = np.cumsum(pdf)

# plotting PDF and CDF
plt.plot(bins_count[1:], cdf, label="CDF", color = 'red')
plt.legend()

plt.title('CDF of Array a1(100 random nos uniformly distributed between [0,1])')
plt.xlabel('Fraction of total numbers in the array')
plt.ylabel('Probability values')

plt.show()


count, bins_count = np.histogram(float_array_a2_read)

pdf = count/sum(count)

cdf = np.cumsum(pdf)

# plotting PDF and CDF
plt.plot(bins_count[1:], cdf, label="CDF", color = 'green')

plt.title('CDF of Array a2(200 random nos normally distributed between approx [1,100])')
plt.xlabel('Fraction of total numbers in the array')
plt.ylabel('Probability values')


plt.legend()
plt.show()


