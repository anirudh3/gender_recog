#!/usr/bin/env python

# '''
# Name : genderClassifier.py
# Desc : A simple classifier to identify gender from short voice snippets.
# Author : Anirudh Mani
#
# '''

import sys, os
import numpy as np
from getFeatures import SpeechFeatures # our feature extractor
from matplotlib import pyplot as plt
from sklearn.svm import SVC
import random



# get features

features = SpeechFeatures()
features.load_data()

m = [] # holds the non zero pitch values for men
for k in features.men_pitches.keys():
    temp = [v for v in features.men_pitches[k] if v > 0.0]
    m.extend(temp)

w = [] # holds the non zero pitch values for women
for k in features.women_pitches.keys():
    temp = [v for v in features.women_pitches[k] if v > 0.0]
    w.extend(temp)


# Preparing input for the classifier
inp_train = []
label_train = []
inp_test = []
label_test = []

# 80% train set, 20% test set
random.shuffle(m)
random.shuffle(w)


for v in m[:int(len(m) * 0.8)]:
    inp_train.append([v])
    label_train.append(1)

for v in w[:int(len(w) * 0.8)]:
    inp_train.append([v])
    label_train.append(2)

for v in m[int(len(m) * 0.8):]:
    inp_test.append([v])
    label_test.append(1)

for v in w[int(len(w) * 0.8):]:
    inp_test.append([v])
    label_test.append(2)

# classifying using SVM

clf = SVC(kernel='poly', degree=2, verbose=True)
clf.fit(inp_train, label_train)

print clf.score(inp_test, label_test)





# plt.plot(m, 'go', w, 'rs')
# plt.ylabel('pitch')
# plt.show()
