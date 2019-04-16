
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
from collections import Counter
from model.logger import log, LogTypes


def load_from_pickle(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data


threadLock = threading.Lock()
quitEvent = threading.Event()

intents = {}
intents[0] = 'salute'
intents[1] = 'bye'
intents[2] = 'help'
intents[3] = 'unknown'
intents[4] = 'get_measurements'
intents[5] = 'new_table'
intents[6] = 'start_training'

snow = SnowballStemmer('english')

file = Path(os.path.dirname(os.path.abspath(__file__))+"/data/input.data")
file = str(file.absolute())
pickels_dir = Path(os.path.dirname(os.path.abspath(__file__))+"/pickels/")
# pickels_dir = str(pickels_dir.absolute())

# Importing models
# Models with stop_words
count_vect = load_from_pickle(
    pickels_dir / 'count_vect.pkl')
tfidf_transformer = load_from_pickle(
    pickels_dir / 'tfidf_transformer.pkl')
multinomial_clf = load_from_pickle(
    pickels_dir / 'multinomial_model.pkl')
sgdc_clf = load_from_pickle(
    pickels_dir / 'sgdc_model.pkl')
log_reg_clf = load_from_pickle(
    pickels_dir / 'log_reg_model.pkl')
lin_svc_clf = load_from_pickle(
    pickels_dir / 'lin_svc_model.pkl')
forest_clf = load_from_pickle(
    pickels_dir / 'forest_model.pkl')

# Models with no stop_words
count_small_vect = load_from_pickle(
    pickels_dir / 'count_small_vect.pkl')
tfidf_small_transformer = load_from_pickle(
    pickels_dir / 'tfidf_small_transformer.pkl')
multinomial_small_clf = load_from_pickle(
    pickels_dir / 'multinomial_small_model.pkl')
sgdc_small_clf = load_from_pickle(
    pickels_dir / 'sgdc_small_model.pkl')
log_reg_small_clf = load_from_pickle(
    pickels_dir / 'log_reg_small_model.pkl')
lin_svc_small_clf = load_from_pickle(
    pickels_dir / 'lin_svc_small_model.pkl')
forest_small_clf = load_from_pickle(
    pickels_dir / 'forest_small_clfmodel.pkl')


# CORS(app)
def start_training_thread():
    global train
    train.start()


def cleanup():
    quitEvent.set()
    train.join()


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
        pred_multi = multinomial_small_clf.predict(frases_new_tfidf)
        prob_multi = (multinomial_small_clf.predict_proba(frases_new_tfidf)
                      [0][pred_multi[0]])
        vote.append(pred_multi[0])

        pred_sgdc = sgdc_small_clf.predict(frases_new_tfidf)
        prob_sgdc = (sgdc_small_clf.predict_proba(frases_new_tfidf)
                     [0][pred_sgdc[0]])
        vote.append(pred_sgdc[0])

        pred_log = log_reg_small_clf.predict(frases_new_tfidf)
        prob_log = (log_reg_small_clf.predict_proba(frases_new_tfidf)
                    [0][pred_log[0]])
        vote.append(pred_log[0])

        pred_lin = lin_svc_small_clf.predict(frases_new_tfidf)
        prob_lin = (lin_svc_small_clf.predict_proba(frases_new_tfidf)
                    [0][pred_lin[0]])
        vote.append(pred_lin[0])

        pred_forest = forest_small_clf.predict(frases_new_tfidf)
        prob_forest = (forest_small_clf.predict_proba(frases_new_tfidf)
                       [0][pred_forest[0]])
        vote.append(pred_forest[0])

    else:
        pred_multi = multinomial_clf.predict(frases_new_tfidf)
        prob_multi = (multinomial_clf.predict_proba(frases_new_tfidf)
                      [0][pred_multi[0]])
        vote.append(pred_multi[0])

        pred_sgdc = sgdc_clf.predict(frases_new_tfidf)
        prob_sgdc = sgdc_clf.predict_proba(frases_new_tfidf)[0][pred_sgdc[0]]
        vote.append(pred_sgdc[0])

        pred_log = log_reg_clf.predict(frases_new_tfidf)
        prob_log = log_reg_clf.predict_proba(frases_new_tfidf)[0][pred_log[0]]
        vote.append(pred_log[0])

        pred_lin = lin_svc_clf.predict(frases_new_tfidf)
        prob_lin = lin_svc_clf.predict_proba(frases_new_tfidf)[0][pred_lin[0]]
        vote.append(pred_lin[0])

        pred_forest = forest_clf.predict(frases_new_tfidf)
        prob_forest = (forest_clf.predict_proba(frases_new_tfidf)
                       [0][pred_forest[0]])
        vote.append(pred_forest[0])

    threadLock.release()
    prob_sum = prob_forest + prob_lin + prob_log + prob_sgdc + prob_multi
    prob_clf = (prob_sum)/5 * 100
    # thread unlock
    try:
        decission = mode(vote)
    except Exception as e:

        log("Two intents possible", LogTypes.LOG_WARNING)
        c = Counter([1, 1, 2, 2, 3])
        c.most_common(1)
        decission = c[0]

    confidence = (vote.count(decission)/len(vote)) * 100
    probability = (confidence + prob_clf)/2
    intent = intents[decission]
    print("Probability: ", probability, file=sys.stderr)
    print("Category: ", intent, file=sys.stderr)

    if probability > 70:
        json_msg = {'intent': intent,
                    'sentence': data["text"]}
        new_entry(json_msg)

    result = {'intent_id': format(decission),
              'intent': intent,
              # 'stem_phrase' : array_statement[0],
              # 'original_phrase': data["text"],
              'probability': "{:.2f}".format(probability)}

    return json.dumps(result)


def new_entry(data):
    if ("intent" or "sentence") not in data:
        abort(400)

    intent = data["intent"].rstrip()
    sentence = data["sentence"].rstrip()

    with open(file, "a", newline='') as csv_file:
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
        global forest_small_clf, lin_svc_small_clf

        # Importing models
        # Models with stop_words
        count_vect = load_from_pickle(pickels_dir / 'count_vect.pkl')
        tfidf_transformer = load_from_pickle(
            pickels_dir / 'tfidf_transformer.pkl')
        multinomial_clf = load_from_pickle(
            pickels_dir / 'multinomial_model.pkl')
        sgdc_clf = load_from_pickle(
            pickels_dir / 'sgdc_model.pkl')
        log_reg_clf = load_from_pickle(
            pickels_dir / 'log_reg_model.pkl')
        lin_svc_clf = load_from_pickle(
            pickels_dir / 'lin_svc_model.pkl')
        forest_clf = load_from_pickle(
            pickels_dir / 'forest_model.pkl')

        # Models with no stop_words
        count_small_vect = load_from_pickle(
            pickels_dir / 'count_small_vect.pkl')
        tfidf_small_transformer = load_from_pickle(
            pickels_dir / 'tfidf_small_transformer.pkl')
        multinomial_small_clf = load_from_pickle(
            pickels_dir / 'multinomial_small_model.pkl')
        sgdc_small_clf = load_from_pickle(
            pickels_dir / 'sgdc_small_model.pkl')
        log_reg_small_clf = load_from_pickle(
            pickels_dir / 'log_reg_small_model.pkl')
        lin_svc_small_clf = load_from_pickle(
            pickels_dir / 'lin_svc_small_model.pkl')
        forest_small_clf = load_from_pickle(
            pickels_dir / 'forest_small_clfmodel.pkl')

        threadLock.release()
        # try:
        #     quit.wait(60)
        # except:
        if (quit.wait(60)
            or option != "timer"
                or not threading.main_thread().is_alive()):
            break
        # logging.debug('released')
        # thread_unlock
    result = {'result': "ok"}
    return(json.dumps(result))


option = "timer"
train = threading.Thread(name='train',
                         target=retrain,
                         args=(quitEvent, option,))
