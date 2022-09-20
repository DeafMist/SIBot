import json
import urllib.request


def get_json():
    url = "https://drive.google.com/uc?export=view&id=1u4sNekGHaDzgkOVzCOAbyWpFTEMfu95Z"
    filename = "intents_dataset.json"
    urllib.request.urlretrieve(url, filename)

    return filename


def get_dataset():
    filename = get_json()

    with open(filename, 'r', encoding='UTF-8') as file:
        data = json.load(file)

    X = []
    Y = []
    for intent_name in data:
        for phrase in data[intent_name]['examples']:
            X.append(phrase)
            Y.append(intent_name)

        for phrase in data[intent_name]['responses']:
            X.append(phrase)
            Y.append(intent_name)

    return [X, Y, data]
