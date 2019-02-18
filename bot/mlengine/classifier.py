from flask import Flask, abort, request
# from flask_cors import CORS
import json
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfTransformer
# from sklearn.linear_model import SGDClassifier
import pickle
from nltk.stem.snowball import SnowballStemmer
# from time import sleep
import importlib
from mlengine import trainer
import csv
from statistics import mode

import threading
# import logging
import sys
import os
from pathlib import Path

threadLock = threading.Lock()
quitEvent = threading.Event()

intents = {}
intents[0] = 'salute'

snow = SnowballStemmer('english')

file = (Path(os.path.dirname(os.path.abspath(__file__))+"/data/input.data").
        absolute())
pickels_dir = (Path(os.path.dirname(os.path.abspath(__file__))+"/pickels/").
               absolute())

# Importing models
# Models with stop_words

count_vect = pickle.load(
    open(pickels_dir + 'count_vect.pkl', 'rb'))
tfidf_transformer = pickle.load(
    open(pickels_dir + 'tfidf_transformer.pkl', 'rb'))
multinomial_clf = pickle.load(
    open(pickels_dir + 'multinomial_model.pkl', 'rb'))
sgdc_clf = pickle.load(
    open(pickels_dir + 'sgdc_model.pkl', 'rb'))
log_reg_clf = pickle.load(
    open(pickels_dir + 'log_reg_model.pkl', 'rb'))
lin_svc_clf = pickle.load(
    open(pickels_dir + 'lin_svc_model.pkl', 'rb'))
forest_clf = pickle.load(
    open(pickels_dir + 'forest_model.pkl', 'rb'))

# Models with no stop_words
count_small_vect = pickle.load(
    open(pickels_dir + 'count_small_vect.pkl', 'rb'))
tfidf_small_transformer = pickle.load(
    open(pickels_dir + 'tfidf_small_transformer.pkl', 'rb'))
multinomial_small_clf = pickle.load(
    open(pickels_dir + 'multinomial_small_model.pkl', 'rb'))
sgdc_small_clf = pickle.load(
    open(pickels_dir + 'sgdc_small_model.pkl', 'rb'))
log_reg_small_clf = pickle.load(
    open(pickels_dir + 'log_reg_small_model.pkl', 'rb'))
lin_svc_small_clf = pickle.load(
    open(pickels_dir + 'lin_svc_small_model.pkl', 'rb'))
forest_small_clf = pickle.load(
    open(pickels_dir + 'forest_small_clfmodel.pkl', 'rb'))


app = Flask(__name__)
# CORS(app)


def classify(data):
    if "text" not in data:
        abort(400)
    global threadLock
    array_statement = [data["text"]]

    array_statement = [" ".join([snow.stem(word)
                                 for word in sentence.split(" ")])
                       for sentence in array_statement]

    # thread lock
    threadLock.acquire()
    frases_new_counts = count_vect.transform(array_statement)
    frases_new_tfidf = tfidf_transformer.transform(frases_new_counts)

    if frases_new_counts.size < 2:
        frases_new_small_counts = count_small_vect.transform(array_statement)
        frases_new_tfidf = (tfidf_small_transformer.
                            transform(frases_new_small_counts))

    vote = []

    if frases_new_counts.size < 2:
        pred_multi = multinomial_small_clf.predict(frases_new_tfidf)[0]
        prob_multi = (multinomial_small_clf.predict_proba(frases_new_tfidf)
                      [0][pred_multi])
        vote.append(pred_multi)

        pred_sgdc = sgdc_small_clf.predict(frases_new_tfidf)[0]
        prob_sgdc = (sgdc_small_clf.predict_proba(frases_new_tfidf)
                     [0][pred_sgdc])
        vote.append(pred_sgdc)

        pred_log = log_reg_small_clf.predict(frases_new_tfidf)[0]
        prob_log = (log_reg_small_clf.predict_proba(frases_new_tfidf)
                    [0][pred_log])
        vote.append(pred_log)

        pred_lin = lin_svc_small_clf.predict(frases_new_tfidf)[0]
        prob_lin = (lin_svc_small_clf.predict_proba(frases_new_tfidf)
                    [0][pred_lin])
        vote.append(pred_lin)

        pred_forest = forest_small_clf.predict(frases_new_tfidf)[0]
        prob_forest = (forest_small_clf.predict_proba(frases_new_tfidf)
                       [0][pred_forest])
        vote.append(pred_forest)

    else:
        pred_multi = multinomial_clf.predict(frases_new_tfidf)[0]
        prob_multi = (multinomial_clf.predict_proba(frases_new_tfidf)
                      [0][pred_multi])
        vote.append(pred_multi)

        pred_sgdc = sgdc_clf.predict(frases_new_tfidf)[0]
        prob_sgdc = sgdc_clf.predict_proba(frases_new_tfidf)[0][pred_sgdc]
        vote.append(pred_sgdc)

        pred_log = log_reg_clf.predict(frases_new_tfidf)[0]
        prob_log = log_reg_clf.predict_proba(frases_new_tfidf)[0][pred_log]
        vote.append(pred_log)

        pred_lin = lin_svc_clf.predict(frases_new_tfidf)[0]
        prob_lin = lin_svc_clf.predict_proba(frases_new_tfidf)[0][pred_lin]
        vote.append(pred_lin)

        pred_forest = forest_clf.predict(frases_new_tfidf)[0]
        prob_forest = (forest_clf.predict_proba(frases_new_tfidf)
                       [0][pred_forest])
        vote.append(pred_forest)

    threadLock.release()
    prob_sum = prob_forest + prob_lin + prob_log + prob_sgdc + prob_multi
    prob_clf = (prob_sum)/5 * 100
    # thread unlock

    votes = mode(vote)

    confidence = (vote.count(votes)/len(vote)) * 100
    probability = (confidence + prob_clf)/2
    intent = intents[votes]
    print("Probability: ", probability, file=sys.stderr)
    print("Category: ", intent, file=sys.stderr)

    if probability > 70:
        json_msg = {'intent': intent,
                    'sentence': data["text"]}
        new_entry(json_msg)

    result = {'intent_id': format(votes),
              'intent': intent,
              # 'stem_phrase' : array_statement[0],
              # 'original_phrase': data["text"],
              'probability': "{:.2f}".format(probability)}

    return json.dumps(result)


def new_entry(data):
    if ("intent" or "sentence") not in data:
        abort(400)

    intent = data["intent"]
    sentence = data["sentence"]

    with open(file, "a") as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow([sentence, intent])


def retrain(quit=True, option=""):
    global threadLock
    while True:
        threadLock.acquire()
        importlib.reload(trainer)
        # thread lock
        # logging.debug('locking')
        global count_vect, tfidf_transformer, multinomial_clf
        global sgdc_clf, log_reg_clf, lin_svc_clf, forest_clf
        global count_small_vect, tfidf_small_transformer, multinomial_small_clf
        global sgdc_small_clf, log_reg_small_clf, in_svc_small_clf
        global forest_small_clf

        # Importing models
        # Models with stop_words

        count_vect = pickle.load(
            open(pickels_dir + 'count_vect.pkl', 'rb'))
        tfidf_transformer = pickle.load(
            open(pickels_dir + 'tfidf_transformer.pkl', 'rb'))
        multinomial_clf = pickle.load(
            open(pickels_dir + 'multinomial_model.pkl', 'rb'))
        sgdc_clf = pickle.load(
            open(pickels_dir + 'sgdc_model.pkl', 'rb'))
        log_reg_clf = pickle.load(
            open(pickels_dir + 'log_reg_model.pkl', 'rb'))
        lin_svc_clf = pickle.load(
            open(pickels_dir + 'lin_svc_model.pkl', 'rb'))
        forest_clf = pickle.load(
            open(pickels_dir + 'forest_model.pkl', 'rb'))

        # Models with no stop_words
        count_small_vect = pickle.load(
            open(pickels_dir + 'count_small_vect.pkl', 'rb'))
        tfidf_small_transformer = pickle.load(
            open(pickels_dir + 'tfidf_small_transformer.pkl', 'rb'))
        multinomial_small_clf = pickle.load(
            open(pickels_dir + 'multinomial_small_model.pkl', 'rb'))
        sgdc_small_clf = pickle.load(
            open(pickels_dir + 'sgdc_small_model.pkl', 'rb'))
        log_reg_small_clf = pickle.load(
            open(pickels_dir + 'log_reg_small_model.pkl', 'rb'))
        lin_svc_small_clf = pickle.load(
            open(pickels_dir + 'lin_svc_small_model.pkl', 'rb'))
        forest_small_clf = pickle.load(
            open(pickels_dir + 'forest_small_clfmodel.pkl', 'rb'))
        threadLock.release()
        if (quit.wait(60)
            or option != "timer"
                or not threading.main_thread().is_alive()):
            break
        # logging.debug('released')
        # thread_unlock
    result = {'result': "ok"}
    return(json.dumps(result))


@app.route('/classify', methods=['POST'])
def process():
    if not request.json:
        abort(400)
    return classify(request.json)


@app.route('/retrain', methods=['GET'])
def training():
    return retrain()


@app.before_first_request
def before_first_request():
    global training
    training.start()


option = "timer"
train = threading.Thread(name='training',
                         target=retrain,
                         args=(quitEvent, option,))

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5089, debug=True)

    quitEvent.set()
    train.join()
