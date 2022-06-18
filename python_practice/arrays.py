arr = [[2,3,4],[2,3,5]]

def sizeof(array):
  x = len(arr)
  y = len(arr[0])
  size = x*y
  return size

print(sizeof(arr))

# print(df1,"\n")
# x = np.reshape(arr, [1,6])
# df = pd.DataFrame(x)
# print(df)