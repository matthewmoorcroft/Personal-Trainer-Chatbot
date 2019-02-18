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

intents = {}
intents['salute'] = 0
codigo_intent={}


phrases = []
intent = []
snow = SnowballStemmer('english')

file = Path(os.path.dirname(os.path.abspath(__file__))+"/data/input.data").absolute()
pickels_dir = Path(os.path.dirname(os.path.abspath(__file__))+"/pickels/").absolute()


with open(file,'r') as inp:
	for row in csv.reader(inp,delimiter=';'):
		phrases.append(row[0])
		intent.append(intents[row[1]])

phrases = [" ".join([snow.stem(word) for word in sentence.split(" ")]) for sentence in phrases]

###Training with stop_words
count_vect = CountVectorizer(stop_words='english')
phrases_train_counts = count_vect.fit_transform(phrases)
tfidf_transformer = TfidfTransformer()
phrases_train_tfidf = tfidf_transformer.fit_transform(phrases_train_counts)

multinomial_clf = MultinomialNB(alpha=0.01).fit(phrases_train_tfidf, intent)
sgdc_clf = SGDClassifier(loss='log',max_iter=1000,tol=1e-4).fit(phrases_train_tfidf, intent)
log_reg_clf = LogisticRegression().fit(phrases_train_tfidf, intent)
lin_svc_clf = SVC(kernel='linear',probability=True).fit(phrases_train_tfidf, intent)
forest_clf = RandomForestClassifier(n_estimators=100,random_state=0).fit(phrases_train_tfidf, intent)

pickle.dump(count_vect, open(pickels_dir + 'count_vect.pkl', 'wb'))
pickle.dump(tfidf_transformer, open(pickels_dir + 'tfidf_transformer.pkl', 'wb'))
pickle.dump(multinomial_clf, open(pickels_dir + 'multinomial_model.pkl', 'wb'))
pickle.dump(sgdc_clf, open(pickels_dir + 'sgdc_model.pkl', 'wb'))
pickle.dump(log_reg_clf, open(pickels_dir + 'log_reg_model.pkl', 'wb'))
pickle.dump(lin_svc_clf, open(pickels_dir + 'lin_svc_model.pkl', 'wb'))
pickle.dump(forest_clf, open(pickels_dir + 'forest_model.pkl', 'wb'))

###Training with no stop_words
count_small_vect = CountVectorizer()
phrases_small_counts = count_small_vect.fit_transform(phrases)
tfidf_small_transformer = TfidfTransformer()
phrases_small_tfidf = tfidf_small_transformer.fit_transform(phrases_small_counts)

multinomial_small_clf = MultinomialNB(alpha=0.01).fit(phrases_small_tfidf, intent)
sgdc_small_clf = SGDClassifier(loss='log',max_iter=1000,tol=1e-4).fit(phrases_small_tfidf, intent)
log_reg_small_clf = LogisticRegression().fit(phrases_small_tfidf, intent)
lin_svc_small_clf = SVC(kernel='linear',probability=True).fit(phrases_small_tfidf, intent)
forest_small_clf = RandomForestClassifier(n_estimators=100,random_state=0).fit(phrases_small_tfidf, intent)

pickle.dump(count_small_vect, open(pickels_dir + 'count_small_vect.pkl', 'wb'))
pickle.dump(tfidf_small_transformer, open(pickels_dir + 'tfidf_small_transformer.pkl', 'wb'))
pickle.dump(multinomial_small_clf, open(pickels_dir + 'multinomial_small_model.pkl', 'wb'))
pickle.dump(sgdc_small_clf, open(pickels_dir + 'sgdc_small_model.pkl', 'wb'))
pickle.dump(log_reg_small_clf, open(pickels_dir + 'log_reg_small_model.pkl', 'wb'))
pickle.dump(lin_svc_small_clf, open(pickels_dir + 'lin_svc_small_model.pkl', 'wb'))
pickle.dump(forest_small_clf, open(pickels_dir + 'forest_small_clfmodel.pkl', 'wb'))
