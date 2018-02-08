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



# declaring globally useful variables




# get features

features = SpeechFeatures()
features.load_data()

# m = [v for v in features.men_pitches[k] for k in features.men_pitches.keys()]
# f = [features.women_pitches[k] for k in features.women_pitches.keys()]
m = []
for k in features.men_pitches.keys():
    temp = [v for v in features.men_pitches[k] if v > 0.0]
    m.extend(temp)

w = []
for k in features.women_pitches.keys():
    temp = [v for v in features.women_pitches[k] if v > 0.0]
    w.extend(temp)


mean_m = sum(m)/len(m)
mean_w = sum(w)/len(w)


print m

plt.plot(m, 'go', w, 'rs')
plt.ylabel('pitch')
plt.show()
