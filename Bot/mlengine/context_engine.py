from flask import Flask
from model.user import *


def process_message(data):
    log('Context Engine: Context processing started')
    message = text_normalization(data['message'])
    user = data['user']

def process_welcome(data):
    log('Context Engine: Welcome process')
    message = text_normalization(data['message'])
    user = data['user']

    context = context_manager.get_context()
    if context:
        if context_manager.check_freshness(context):

    else:
        context_manager.create_context(data, welcome_process = True)

#Structure how to store context and log in interaction log

app = Flask(__name__)
@app.route("/process_message")
def normal_req(request.json):
    res = process_message(request.json)
    return json.dumps(res)

@app.route("/process_welcome")
def welcome_req(request.json):
    res = process_welcome(request.json)
    return json.dumps(res)

context_manager = ContextManager()

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 30000, debug = True)
