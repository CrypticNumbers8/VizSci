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
import math

#Reference: "https://stackoverflow.com/questions/26137195/latin-hypercube-sampling-with-python"

random_sample_list = []
x1 = []
y1 = []

for i in range(1000):
	x = random.uniform(0,1)
	y = random.uniform(0,1)
	x1.append(x)
	y1.append(y)

l11 = lhsmdu.sample(1000,1) # Latin Hypercube Sampling of two variables, and 10 samples each.

l22 = lhsmdu.sample(1000,1) # Latin Hypercube Sampling of two variables, and 10 samples each.


#print(l)
l1 = []
l2 = []

for i in range(len(l11)):
	l1.append(l11[i][0])

for i in range(len(l22)):
	l2.append(l22[i][0])


print(l[-5:])

plt.scatter(x1,y1, color = 'r', label='Random-Sampled')
plt.scatter(l1,l2, color = 'g', label='LHSMDU')

plt.xlabel("x-coordinate value")
plt.ylabel("y-coordinate value")
plt.title("Scatter plot containing two 1000 by 2 arrays(Random-Sampled and LHSMDU)")

plt.legend(loc = 'upper right')
#plt.show()

z1 = []

for i in range(1000):
	z1.append(math.sin(10*x1[i])*math.cos(10*y1[i]))

plt.title('Contour plot with 10 levels')
plt.xlabel('x-coordinates of Random-Sampled 1000 by 2 array')
plt.ylabel('y-coordinates of Random-Sampled 1000 by 2 array')
plt.tricontourf(x1,y1,z1,levels = 10)
plt.legend()
plt.show()

# print(z1)