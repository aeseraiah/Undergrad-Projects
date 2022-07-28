from cmath import pi


import numpy as np 
x = np.array([1,2,3])

t = [5,3,2]

y = []
noise = .5
for i in range(len(x)):
    y.append(np.sin(2*np.pi*i) + noise)
    i = i + 1


print(y)