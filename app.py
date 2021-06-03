#import libraries
import flask
import numpy as np
from flask import *
import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from google_trans_new import google_translator  
from urllib.request import urlopen
import cloudpickle as cp
import os.path
from os import path
from recommendation import *
import recommendation as job_recommend

#import model
with open("model_EI.pkl", "rb") as f:
    model_EI = pickle.load(f)
with open("model_FT.pkl", "rb") as f:
    model_FT = pickle.load(f)
with open("model_JP.pkl", "rb") as f:
    model_JP = pickle.load(f)
with open("model_NS.pkl", "rb") as f:
    model_NS = pickle.load(f)
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
if path.exists('vectorizer.pkl'):
    print("available")
else:
    print("file not found")

translator = google_translator()  

def listToString(s): 
    str1 = ""     
    for ele in s: 
        str1 += ele  
    return str1 

#flask app
app = flask.Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to Nusademy Webhook API!'

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(force=True)
    print(req)
    return {
        'fulfillmentText': 'Custom Webhook Response',
                'fulfillmentText': 'Custom Webhook Response',
    }

@app.route('/predict',methods=['POST'])
def predict():
    userInput = request.get_json(force=True)
    userInput = userInput['queryResult']
    userInput=userInput['queryText']
    userInput = translator.translate(userInput,lang_tgt='en')  
    if len(userInput) ==0:
        return 'Silahkan Isi Teks Dulu'

    replacements = [
        (r"(http.*?\s)", " "),
        (r"[^\w\s]", " "),
        (r"\_", " "),
        (r"\d+", " "),
        (r"\{}","")]
    
    for old_data, new in replacements:
        userInput = re.sub(old_data,new, userInput)
    
    userInput = [userInput]
    print(userInput)
    userInput_Vectorized = vectorizer.transform(userInput)

    predict_EI = model_EI.predict(userInput_Vectorized)
    predict_NS = model_NS.predict(userInput_Vectorized)
    predict_FT = model_FT.predict(userInput_Vectorized)
    predict_JP = model_JP.predict(userInput_Vectorized)


    output_EI = 'E' if predict_EI == 0 else "I"
    output_NS = 'N' if predict_NS == 0 else "S"
    output_FT = 'F' if predict_FT == 0 else "T"
    output_JP = 'J' if predict_JP == 0 else "P"

    result = [output_EI,output_NS,output_FT,output_JP]
    result = listToString(result)
    result = job_recommend.check_personality(result)
    print(result)
    return {
        'fulfillmentText': result
    }

if __name__ == "__main__":
    app.secret_key = 'SecretKey'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
