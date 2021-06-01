import flask, requests
import os
from flask import *
import json
import traceback
import pandas as pd
import numpy as np
import pickle

app = flask.Flask(__name__)

@app.route('/')
def index():
    return '<h3 style="text-align: center;">Welcome to Nusademy Webhook API!<h3>'

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(force=True)
    print(req)
    return {
        'fulfillmentText': 'Custom Webhook Response'
    }

@app.route('/predict', methods=['POST'])
def predict():
    if model:
            json_ = request.json
            print(json_)
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)

            prediction = list(model.predict(query))
            print(prediction)
            nanda='nanda'
            return nanda
    else:
        print ('Train the model first')
        return ('No model here to use')

if __name__ == "__main__":
    app.secret_key = 'SecretKey'

    with open("new_model.pkl", "rb") as f:
        model = pickle.load(f)
        print("model loaded into webhook")

    with open("model_columns.pkl", "rb") as f:
        model_columns = pickle.load(f)
        print("model column loaded!")

    app.debug = True
    app.run(host='0.0.0.0', port=80)
