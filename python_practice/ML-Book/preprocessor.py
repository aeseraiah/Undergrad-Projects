import numpy as np
from sklearn import preprocessing
import keras
from keras.utils import to_categorical

data = np.array([[3,-1.5, 2, -5.4], [0, 4, -0.3, 2.1], [1, 3.3, -1.9, -4.3]])

data_standardized = preprocessing.scale(data)
#print(data)
x1 = data[0]
#print(data)
i = 0
k=0
sum=0

for k in range(0, len(x1)):
    sum = sum + x1[k]

#print(sum/len(x1))

#print(x1.mean(axis=0))

data_standardized = preprocessing.scale(x1)

data_mean = data_standardized.mean(axis=0)
#print(data_mean)

#print(x1)
#print(data_standardized)

encoder = preprocessing.OneHotEncoder()
encoder.fit([[0,2,1,12], [1,3,5,3], [2,3,2,12], [1,2,4,3]])

encoded_vector = encoder.transform([[0,2,1,12]]).toarray()

#print(encoded_vector)

e = encoder.fit([[0,2,1,12], [1,3,5,3]])
e_vector = encoder.transform([[0,2,1,12]]).toarray()
print(e_vector)


