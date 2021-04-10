import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy as numpy
import tflearn
import tensorflow as tf
import random
import json

with open("../data/intents.json") as file:
    data = json.load(file)

phrases = []
labels = []
docs = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        words = nltk.word_tokenize(pattern)
        phrases.extend(words)
        docs.append(pattern)

        if intent['tag'] not in labels:
            labels.append(intent['tag'])