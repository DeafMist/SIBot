import random

import joblib


def get_intent(text):
    model_filename = 'saved_obj/model.sav'
    model = joblib.load(model_filename)

    vectorizer_filename = 'saved_obj/vectorizer.sav'
    vectorizer = joblib.load(vectorizer_filename)

    text_vec = vectorizer.transform([text])
    intent = model.predict(text_vec)[0]
    return intent


def get_response(intent):
    data = joblib.load('saved_obj/data.sav')
    return random.choice(data[intent]['responses'])


def bot(text):
    intent = get_intent(text)
    answer = get_response(intent)
    return answer
