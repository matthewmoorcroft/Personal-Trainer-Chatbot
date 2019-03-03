from flask import Flask
# from model.user import *
from ..model.logger import log
from mlengine.context_manager import ContextManager
import requests
import json


"""Message goes to context if it doesn't understand, goes to classifier if it
doesn't understand sends to user context answer"""


def process_message(data):
    log('Context Engine: Context processing started')
    # message = text_normalization(data['message'])
    message = data['message']
    user = data['user']
    json = {'text': message}
    res = requests.post('http://localhost:30000/classify',
                        json=json)
    return res.json['intent']


def process_welcome(data):
    log('Context Engine: Welcome process')
    # message = text_normalization(data['message'])
    message = data['message']
    user = data['user']

    context = context_manager.get_context()
    if context:
        if context_manager.check_freshness(context):
            print()

    else:
        context_manager.create_context(data, welcome_process=True)

# Structure how to store context and log in interaction log


app = Flask(__name__)
@app.route("/process_message")
def normal_req():
    res = process_message(requests.json)
    return json.dumps(res)


@app.route("/process_welcome")
def welcome_req():
    res = process_welcome(requests.json)
    return json.dumps(res)


context_manager = ContextManager()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=30000, debug=True)
