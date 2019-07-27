import numpy as np
import time

a = np.array([1,2,3,4])
print(a)

a = np.random.rand(1000)
b = np.random.rand(1000)

tic = time.time()
z = np.dot(a,b)
toc = time.time()

print('Vectorized version' + str(1000*(tic-toc) + "ms"))

"""
The Vectorize version takes less time
about 300 times lower to 
implementing deep learning algorithm faster

SMID single instruction multiple data

use built-in function, enable numpy take more advantage

whenever possible, avoid explicit for-loops

u = A*v

"""

"""
u = np.zeros((n,1))
for i in range(n):
    u[i] = math.exp(x[i])
    
import numpy as np
u = np.exp(v)

np.log(v)
np.maximum(v,0) 

optimize the algorithm without using any for loop

Broadcasting 
calculate Z 1*M matrix

how about these value a 
find a way to compute a1, a2, a3
stacking horizontally
capital 
how to capital z as a variable
instead of using for, you can implement 

propogation

2.14 Vectorizing Logistic Regression

"""
"""
cal = A.sum(axis=0)
print(cal)
percentage = 100*A/cal.reshape(1,4)

1*4 vector [100,100,100,100] = [102,103,104,105]

being the parameter b in the vector

some matrix here and you add it to a 1 by n matrix
turn ti


how you implement neural network
compute A interchange with B
l
"""
