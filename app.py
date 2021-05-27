import flask, requests,
import os
from flask import *
import json
import traceback
import pandas as pd
import numpy as np
import pickle

app = flask.Flask(__name__)

@app.route('/')

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
        try:
            json_ = request.json
            print(json_)
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)

            prediction = list(model.predict(query))

            return jsonify({'prediction': str(prediction)})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

if __name__ == "__main__":
    app.secret_key = 'SecretKey'

    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
        print("model loaded into webhook")

    with open("model_columns.pkl", "rb") as f:
        model_columns = pickle.load(f)
        print("model column loaded!")

    app.debug = True
    app.run(host='0.0.0.0', port=80)
