import requests
import numpy as np
from joblib import Memory
from sklearn import datasets, svm
from sklearn.datasets import load_svmlight_file
from sklearn.svm import SVC
from os import listdir
from flask import Flask, request
from flask import jsonify
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import json
import matplotlib.pyplot as plt
from sklearn.utils.multiclass import unique_labels
from flask import Flask, request, send_file, make_response
import io


bean_label_data = pd.read_csv("class_labels_new.csv")
bean_feature_data = pd.read_csv("features.csv")

def plot_confusion_matrix(y_true, y_pred, classes,
                          normalize=False,
                          title=None,
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if not title:
        if normalize:
            title = 'Normalized confusion matrix'
        else:
            title = 'Confusion matrix, without normalization'

    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    # Only use the labels that appear in the data
    classes = classes[unique_labels(y_true, y_pred)]
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image

# Important things to note are io.BytesIO() and send_file magicial powers, io from the io module and send_file is flask
def gen_cof_mat(arg1,arg2):
    #x = iris_data.data
    #y = iris_data.target
    #class_names = iris_data.target_names
    X_train, X_test, y_train, y_test = train_test_split(X, Y)
    c_value = float(arg1)
    kernel_val = arg2
    classifier = SVC(kernel=kernel_val, C = c_value)
    model = 
    y_pred = classifier.fit(X_train, y_train).predict(X_test)
    np.set_printoptions(precision=2)
    # Plot non-normalized confusion matrix
    # Plot normalized confusion matrix
    bytes_obj = plot_confusion_matrix(y_test, y_pred, classes=Y)

    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')



