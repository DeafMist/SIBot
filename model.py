import joblib

from dataset import get_dataset
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neural_network import MLPClassifier

X, Y, data = get_dataset()

vectorizer = CountVectorizer()
vectorizer.fit(X)

X_vec = vectorizer.transform(X)

model = MLPClassifier()
model.fit(X_vec, Y)

model_filename = 'saved_obj/model.sav'
joblib.dump(model, model_filename)

vectorizer_filename = 'saved_obj/vectorizer.sav'
joblib.dump(vectorizer, vectorizer_filename)

data_filename = 'saved_obj/data.sav'
joblib.dump(data, data_filename)
