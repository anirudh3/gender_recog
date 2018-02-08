#!/usr/bin/env python


import sys, os
# import librosa
import re
import numpy as np
import random

class SpeechFeatures:

    dir_data_men = './Data/Men'
    dir_data_women = './Data/Women'
    dir_pitch_men = './pitches/men'
    dir_pitch_women = './pitches/women'


    # create a list of all audio files
    def listAudioFiles(self, dir_folder):
        list_audio_files = []
        for file in os.listdir(dir_folder):
            if file.endswith(".wav") or file.endswith(".txt"):
                directory = "%s/%s" % (dir_folder, file)
                list_audio_files.append(directory)

        return list_audio_files


    def get_features(self, list_audio_files):

        for i, file in enumerate(list_audio_files):
            y, sr = librosa.load(file)


    def get_pitches(self, dir_folder):
        pitches = {}

        # for each file
        for file in os.listdir(dir_folder):
            pitches[file[:-4]] = []

            # open that file and go through the pitch values
            with open(dir_folder + "/" + file, 'r') as f:

                # go through the values
                for n in f.readlines():
                    pitches[file[:-4]].append(float(n.strip()))

        return pitches





    def seg_data(self):

        # test data for men - 80 percent
        indices = random.sample(xrange(len(self.data_men_list)), int(len(self.data_men_list) * 0.8))
        self.data_men_train = [self.data_men_list[i] for i in indices]
        self.data_men_test = [self.data_men_list[i] for i in xrange(len(self.data_men_list)) if i not in indices]

        # test data for women - 80 percent
        indices = random.sample(xrange(len(self.data_women_list)), int(len(self.data_women_list) * 0.8))
        self.data_women_train = [self.data_women_list[i] for i in indices]
        self.data_women_test = [self.data_women_list[i] for i in xrange(len(self.data_women_list)) if i not in indices]



    def load_data(self):

        # load men lists = data, pitches
        self.data_men_list = self.listAudioFiles(self.dir_data_men)
        self.pitch_men_list = self.listAudioFiles(self.dir_pitch_men)

        # load women lists - data, pitches
        self.data_women_list = self.listAudioFiles(self.dir_data_women)
        self.pitch_women_list = self.listAudioFiles(self.dir_pitch_women)

        # get actual pitches
        self.men_pitches = self.get_pitches(self.dir_pitch_men)
        self.women_pitches = self.get_pitches(self.dir_pitch_women)









# yes = SpeechFeatures()
# yes.load_data()
