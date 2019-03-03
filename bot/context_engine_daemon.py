from flask import Flask, request
from mlengine import context_engine
import json

app = Flask(__name__)
@app.route("/process_message")
def normal_req():
    res = context_engine.process_message(request.json)
    return json.dumps(res)


@app.route("/process_welcome")
def welcome_req():
    res = context_engine.process_welcome(request.json)
    return json.dumps(res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=30000, debug=True)
