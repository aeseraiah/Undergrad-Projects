import numpy as np

X = np.array([[3,1], [2,5], [1,8], [6,4], [5,2], [3,5], [4,7], [4,-1]])
y = [0, 1, 1, 0, 0, 1, 1, 0]



#if y[i]==0:
##    class_0 = np.array([X[i]] for i in range(len(X)))
#    i = i + 1   
#else:
#    class_1 = np.array([X[i]] for i in range(len(X)))
#    i = i + 1

#THIS IS NOT THE SAME
class_0 = np.array([X[i] for i in range(len(X)) if y[i]==0])
class_1 = np.array([X[i] for i in range(len(X)) if y[i]==1])

print(class_0)
print(class_1)

line_x = range(10)
line_y = line_x

plt.plot(line_x, line_y, color='black', linewidth=3)
plt.show()