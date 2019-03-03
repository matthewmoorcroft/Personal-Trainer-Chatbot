from flask import Flask, abort, request
from mlengine import classifier

app = Flask(__name__)


@app.route('/classify', methods=['POST'])
def process():
    if not request.json:
        abort(400)
    return classifier.classify(request.json)


@app.route('/retrain', methods=['GET'])
def training():
    return classifier.retrain()


@app.before_first_request
def before_first_request():
    classifier.start_training_thread()


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5089, debug=True)

    classifier.cleanup()
