import numpy as np
arr = [[2,3,4],[2,3,5]]


x = np.size(arr)
print(x)

def size(array):
  x = len(arr)
  y = len(arr[0])
  size = x*y
  return size

print(size(arr))

# print(df1,"\n")
# x = np.reshape(arr, [1,6])
# df = pd.DataFrame(x)
# print(df)