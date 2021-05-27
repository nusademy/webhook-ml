import flask, requests, jsonify
import os
from flask import send_from_directory, request
import json
import traceback
import pandas as pd
import numpy as np

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
    return 'predict_test'

if __name__ == "__main__":
    app.secret_key = 'SecretKey'
    app.debug = True
    app.run()
