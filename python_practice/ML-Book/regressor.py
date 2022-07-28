import sys
import numpy as np 
from sklearn import preprocessing
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

X = [4,3,5,7,6]
y = ['dog', 'cat', 'horse', 'shoe', 'house']

num_training = int(.8*len(X))
print("num_training:", num_training)

num_test = len(X) - num_training
print("num_test:", num_test)

print(X[:4])
X_train = np.array(X[:num_training]).reshape((num_training,1))
y_train = np.array(y[:num_training])

print("X_train:\n",X_train)
print("y_train:\n",y_train)

X_test = np.array(X[num_training:]).reshape((num_test,1))
y_test = np.array(y[num_training:])

print("X_test:\n",X_test)
print("y_test:\n",y_test)

#for y_train:
label_encoder = preprocessing.LabelEncoder()
label_encoder.fit(y_train)
encoded_labels = label_encoder.transform(y_train)
print(encoded_labels)

#for y_test:
label_encoder = preprocessing.LabelEncoder()
label_encoder.fit(y)
encoded_labels_test = label_encoder.transform(y)
print(encoded_labels_test)

linear_regressor = linear_model.LinearRegression()
linear_regressor.fit(X_train, encoded_labels)

polynomial = PolynomialFeatures(degree=3)

X_train_transformed = polynomial.fit_transform(X_train)
print("X_train_transformed\n",X_train_transformed)
print("X_train\n",X_train)

datapoint = [[2]]
poly_datapoint = polynomial.fit_transform(datapoint)
print("poly_datapoint\n",poly_datapoint)

poly_linear_model = linear_model.LinearRegression()
poly_linear_model.fit(X_train_transformed, encoded_labels)
print("Datapoint has not been trasnformed\n", linear_regressor.predict(datapoint))
print("Datapoint has been transformed\n",poly_linear_model.predict(poly_datapoint))