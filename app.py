import flask
import os
from flask import send_from_directory, request

app = flask.Flask(__name__)

@app.route('/')

@app.route('/webhook', methods=['POST'])
def webhook():
    request = request.get_json(force=True)
    print(request)

    return {
        'fulfillmentText': 'Test Response from Webhook'
    }

if __name__ == "__main__":
    app.secret_key = 'SecretKey'
    app.debug = True
    app.run()
