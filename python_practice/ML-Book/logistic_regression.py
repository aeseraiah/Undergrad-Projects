import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

X = np.array([[4,7], [3.5, 8], [3.1, 6.2], [.5,1]])
y = np.array([0,0,1,1])

classifier = linear_model.LogisticRegression(solver='liblinear', C=100)

classifier.fit(X, y)

plot_classifier(classifier, X, y)

def plot_classifier(classifier, X, y):x
    x_min, x_max = min(X[:, 0]) - 1.0, max(X[:, 0]) 