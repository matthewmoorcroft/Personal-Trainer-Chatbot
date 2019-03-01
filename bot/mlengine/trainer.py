from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import pickle
from nltk.stem import SnowballStemmer
from pathlib import Path
import csv
import os


def save_to_pickle(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)


intents = {}
intents['salute'] = 0
intents['bye'] = 1
intents['help'] = 2
intents['get_measurements'] = 3
intents['new_table'] = 4
intents['start_training'] = 5
codigo_intent = {}


phrases = []
intent = []
snow = SnowballStemmer('english')

file = Path(os.path.dirname(os.path.abspath(__file__))+"/data/input.data")
file = str(file.absolute())
pickels_dir = Path(os.path.dirname(os.path.abspath(__file__))+"/pickels/")
pickels_dir = str(pickels_dir.absolute())


with open(file, 'r') as inp:
    for row in csv.reader(inp, delimiter=';'):
        phrases.append(row[0])
        intent.append(intents[row[1]])

phrases = [" ".join(
    [snow.stem(word) for word in sentence.split(" ")]) for sentence in phrases]

# Training with stop_words
count_vect = CountVectorizer(stop_words='english')
phrases_train_counts = count_vect.fit_transform(phrases)
tfidf_transformer = TfidfTransformer()
phrases_train_tfidf = tfidf_transformer.fit_transform(phrases_train_counts)

multinomial_clf = MultinomialNB(alpha=0.01)
sgdc_clf = SGDClassifier(loss='log',
                         max_iter=1000, tol=1e-4)
log_reg_clf = LogisticRegression(solver='lbfgs',
                                 multi_class='auto')
lin_svc_clf = SVC(kernel='linear',
                  probability=True)
forest_clf = RandomForestClassifier(n_estimators=100,
                                    random_state=0)

multinomial_clf = multinomial_clf.fit(phrases_train_tfidf, intent)
sgdc_clf = sgdc_clf.fit(phrases_train_tfidf, intent)
log_reg_clf = log_reg_clf.fit(phrases_train_tfidf, intent)
lin_svc_clf = lin_svc_clf.fit(phrases_train_tfidf, intent)
forest_clf = forest_clf.fit(phrases_train_tfidf, intent)

save_to_pickle(count_vect,
               pickels_dir + 'count_vect.pkl')
save_to_pickle(tfidf_transformer,
               pickels_dir + 'tfidf_transformer.pkl')
save_to_pickle(multinomial_clf,
               pickels_dir + 'multinomial_model.pkl')
save_to_pickle(sgdc_clf,
               pickels_dir + 'sgdc_model.pkl')
save_to_pickle(log_reg_clf,
               pickels_dir + 'log_reg_model.pkl')
save_to_pickle(lin_svc_clf,
               pickels_dir + 'lin_svc_model.pkl')
save_to_pickle(forest_clf,
               pickels_dir + 'forest_model.pkl')


# Training with no stop_words
count_small_vect = CountVectorizer()
phrases_small_counts = count_small_vect.fit_transform(phrases)
tfidf_small_transformer = TfidfTransformer()
phrases_small_tfidf = tfidf_small_transformer.fit_transform(
    phrases_small_counts)

multinomial_small_clf = MultinomialNB(alpha=0.01)
sgdc_small_clf = SGDClassifier(loss='log', max_iter=1000, tol=1e-4)
log_reg_small_clf = LogisticRegression()
lin_svc_small_clf = SVC(kernel='linear', probability=True)
forest_small_clf = RandomForestClassifier(n_estimators=100, random_state=0)

multinomial_small_clf = multinomial_small_clf.fit(phrases_small_tfidf, intent)
sgdc_small_clf = sgdc_small_clf.fit(phrases_small_tfidf, intent)
log_reg_small_clf = log_reg_small_clf.fit(phrases_small_tfidf, intent)
lin_svc_small_clf = lin_svc_small_clf.fit(phrases_small_tfidf, intent)
forest_small_clf = forest_small_clf.fit(phrases_small_tfidf, intent)

save_to_pickle(count_small_vect,
               pickels_dir + 'count_small_vect.pkl')
save_to_pickle(tfidf_small_transformer,
               pickels_dir + 'tfidf_small_transformer.pkl')
save_to_pickle(multinomial_small_clf,
               pickels_dir + 'multinomial_small_model.pkl')
save_to_pickle(sgdc_small_clf,
               pickels_dir + 'sgdc_small_model.pkl')
save_to_pickle(log_reg_small_clf,
               pickels_dir + 'log_reg_small_model.pkl')
save_to_pickle(lin_svc_small_clf,
               pickels_dir + 'lin_svc_small_model.pkl')
save_to_pickle(forest_small_clf,
               pickels_dir + 'forest_small_clfmodel.pkl')
