import pandas as pd
import numpy as np
import json
from joblib import load

def hello_world():
    bean_label_data = pd.read_csv("class_labels_new.csv")
    bean_label_numpy_data = bean_label_data.to_numpy()
    df1 = pd.DataFrame(bean_label_numpy_data)

    new_json_1 = df1.to_json()
    #dumps1 = json.dumps(new_json_1)


    bean_feature_data = pd.read_csv("features.csv")
    bean_feature_numpy_data = bean_feature_data.to_numpy()
    df2 = pd.DataFrame(bean_feature_numpy_data)

    new_json_2 = df2.to_json()
    #dumps2 = json.dumps(new_json_2)



    #print (type(dumps1))
    #print(type(bean_feature_numpy_data))
    #print(bean_label_numpy_data.shape)
    #print(bean_feature_numpy_data.shape)
    print(type(new_json_1))
    print(type(new_json_2))
    print(new_json_1)
    print(new_json_2)
    #return new_json_2.shape
