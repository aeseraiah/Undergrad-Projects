import numpy as np
from joblib import load
import json
from sklearn import datasets
import pandas as pd
import os
from flask import jsonify, render_template, request, redirect, url_for
from flask import send_file

UPLOAD_FOLDER='.'

bean_label_data = pd.read_csv("class_labels_new.csv", header=None)
labels = bean_label_data.to_numpy()

#bean_feature_data = pd.read_csv("features_xtest.csv")
#features = bean_feature_data.to_numpy()

#bean_feature_temp_data = pd.read_csv("temp_features.csv")
#features = bean_feature_temp_data.to_numpy()

def my_prediction(id):
    my_model = load('ada_model.pkl')
    dummy = np.array(id)
    dummyT = dummy.reshape(1,-1)
    dummy_str = dummy.tolist()

    prediction = my_model.predict(dummyT)
    name = labels[prediction]
    class_name = name.tolist()

    return class_name

def my_predictionF(file_name):
  my_model = load('ada_model.pkl')
  missing_value=["Undefined"]
  user_arry = pd.read_csv(file_name, na_values=missing_value)
  prediction = my_model.predict(user_arry)
  name = labels[prediction]
  df = pd.DataFrame(name)
  a = df.to_csv("input_prediction.csv", header=False)  

  all_results = ["Your bean prediction can be can be found in list and can be downloaded via /file/filename where filename = input_prediction.csv."]
  df2 = pd.DataFrame(all_results)
  new_json = df2.to_json()
  return new_json
  path = os.path.join(UPLOAD_FOLDER, a)
  return send_file(path, as_attachment=True)
