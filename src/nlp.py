import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy as np
import tflearn
import tensorflow as tf
import random
import json

with open("../data/intents.json") as file:
    data = json.load(file)

phrases = []
labels = []
docs_x = []
docs_y = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        words = nltk.word_tokenize(pattern)
        phrases.extend(words)
        docs_x.append(pattern)
        docs_y.append(intent['tag'])

        if intent['tag'] not in labels:
            labels.append(intent['tag'])

phrases = [stemmer.stem(w.lower()) for w in phrases]
phrases = sorted(list(set(phrases)))

labels = sorted(labels)

training = []
output = []

out_empty = [0 for _ in range(len(labels))]

for x, doc in enumerate(docs_x):
    bag = []
    words = [stemmer.stem(w) for w in doc]

    for w in phrases:
        if w in words:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)

training = np.array(training)
output = np.array(output)