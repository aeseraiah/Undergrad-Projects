import os
from flask import jsonify, render_template, request, redirect, url_for
from flask import send_file
import numpy as np
from joblib import load
import json
import pandas as pd



UPLOAD_FOLDER='.'

def upload(filename):
    f = request.files['file']
    f.save(filename)
    all_results = ["Your file has been successfully uploaded and can be located in list."]
    df2 = pd.DataFrame(all_results)
    new_json = df2.to_json()
    return new_json

def download(filename):
    path = os.path.join(UPLOAD_FOLDER, filename)
    return send_file(path, as_attachment=True)
    return 'The file has been successfully downloaded.'
    

def list_files():
    files = []
    for filename in os.listdir(UPLOAD_FOLDER):
        path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)
