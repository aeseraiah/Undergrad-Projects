import numpy as np

pd = [2,3]

# for p in range(1, len(pd)):
#     le = np.sqrt(np.diff(pd(p).x)^2 + np.diff(pd(p).y)^2)
#     curJumps = le > 1/8.77
#     jumps = (np.mean(curJumps))

arr = np.array([10,10,11,11])

for i in range(len(arr)):
    curJumps = arr[i] > 8
    jumps = (np.mean(curJumps))
print(jumps)