import numpy as np
from joblib import load
import json
from sklearn import datasets
import pandas as pd
import os
from flask import jsonify, render_template, request, redirect, url_for
from flask import send_file
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns
import base64


UPLOAD_FOLDER='.'


dry_beans_dataset = pd.read_csv('Dry_Beans_Dataset.csv')
#dataset = dry_beans_dataset.to_numpy()


bean_label_data = pd.read_csv("class_labels_new.csv", header=None)
labels = bean_label_data.to_numpy()

#labels_csv = pd.read_csv("labels_new.csv")
#labels_1 = labels_csv.to_numpy()

#test_labels_np = pd.read_csv("test_labels_np.csv")
#test_labels_np_1 = test_labels_np.to_numpy()

test_labels_enc = pd.read_csv("test_labels_enc.csv")
test_labels_enc_1 = test_labels_enc.to_numpy()

train_labels_enc = pd.read_csv("train_labels_enc.csv")
train_labels_enc_1 = test_labels_enc.to_numpy()

train_features = pd.read_csv("train_features.csv")
train_features_1 = train_features.to_numpy()



def model_explanation(file_name):
  my_model = load('ada_model.pkl')
  missing_value=["Undefined"]
  user_arry = pd.read_csv(file_name, na_values=missing_value)
  test_prediction = my_model.predict(user_arry)
  train_prediction = my_model.predict(train_features_1)
  test_accuracy = accuracy_score(test_labels_enc_1, test_prediction)
  train_accuracy = accuracy_score(train_labels_enc, train_prediction)
  train_accuracy = train_accuracy.tolist()
  
  #testing:
  train_f1 = f1_score(train_labels_enc, train_prediction, average='weighted')
  train_f1 = train_f1.tolist()
  train_scores_str_f1 = json.dumps(train_f1)
  
  test_f1 = f1_score(test_labels_enc_1, test_prediction, average='weighted')
  test_f1 = test_f1.tolist()
  test_scores_str_f1 = json.dumps(test_f1)
 
  #end of testimg
 
  test_accuracy = test_accuracy.tolist()
  train_scores_str = json.dumps(train_accuracy)
  test_scores_str = json.dumps(test_accuracy)

  test_results = confusion_matrix(test_labels_enc_1, test_prediction)
  cm_display = ConfusionMatrixDisplay(test_results).plot()
  plt.savefig("input_cm.png")
  test_results = test_results.tolist()
  cm_test_str = json.dumps(test_results)
 
  train_results = confusion_matrix(train_labels_enc, train_prediction)
  cm_display = ConfusionMatrixDisplay(train_results).plot()
  plt.savefig("training_cm.png")
  train_results = train_results.tolist()
  cm_train_str = json.dumps(train_results)


  plt.figure(figsize = (20,20))
  f = sns.heatmap(dry_beans_dataset.corr(),
              annot = True,
              cmap = "Blues",
              fmt = ".2f",
              vmin = -1.00, vmax = 1.00)
  plt.savefig("feature_correlation.png")
  
  data = {}
  with open('feature_correlation.png', mode='rb') as file:
      img = file.read()
  data['img'] = base64.encodebytes(img).decode('utf-8')
  feature_corr = json.dumps(data)



  
  #all_results = [cm_test_str, cm_train_str, test_scores_str, train_scores_str, "hello", "Again hello"] 
  all_results = ["Accuracy and f1 metric for input data AND training data can be found in list and can be downloaded via /file/filename where filename = input_training.csv. In addition, input_training.csv includes Confusion Matrix for accuracy of both training and input data as well as feature correlation. The .png version of Confusion Matrix for both training and input accuracy can also be located in list and can additionally be downloaded via /file/filename where filename = input_cm.png or filename = training_cm.png. The .png version of the feature correlation can also be downloaded via /file/filename where filename = feature_correlation.png. As seen in feature_correlation.png, many features are highly correlated. However, performing feature reduction for the most correlated features did not improve performance/accuracy of the model. Therefore, all 16 features were used."]
  results = [cm_test_str, cm_train_str, test_scores_str, train_scores_str, test_scores_str_f1, train_scores_str_f1, feature_corr]  
  df = pd.DataFrame(results)
  df.index = ['input cm', 'training cm', 'input accuracy', 'train accuracy', 'input f1', 'train f1', 'feature corr'] 
  b = df.to_csv("input_training.csv", header=False)

  df2 = pd.DataFrame(all_results)
  new_json = df2.to_json()
  return new_json
  path = os.path.join(UPLOAD_FLDER, b)
  return send_file(path, as_attachment=True)
  
