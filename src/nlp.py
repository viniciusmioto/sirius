import nltk
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy as np
import tflearn as tfl
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
        docs_x.append(words)
        docs_y.append(intent['tag'])

        if intent['tag'] not in labels:
            labels.append(intent['tag'])

phrases = [stemmer.stem(w.lower()) for w in phrases if  w not in '?']
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

tf.compat.v1.reset_default_graph()

net = tfl.input_data(shape=[None, len(training[0])])
net = tfl.fully_connected(net, 8)
net = tfl.fully_connected(net, 8)
net = tfl.fully_connected(net, len(output[0]), activation='softmax')
net = tfl.regression(net)

model = tfl.DNN(net)
model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
model.save('./output/model.tflearn')