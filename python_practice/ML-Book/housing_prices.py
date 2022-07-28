from sklearn import datasets

housing = datasets.load_boston()

print(housing.data)
print(housing.target)

X, y = shuffle(housing.data, housing.target, random_state=7)

num_training = int(.8*len(X))
X_train, y_train = X 