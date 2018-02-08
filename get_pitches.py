import sys
import os

dir_data_men = './Data/Men'
dir_data_women = './Data/Women'


# Men

for file in os.listdir(dir_data_men):
    if file.endswith(".wav"):
        # directory = "%s/%s" % (dir_folder, file)

        # list_audio_files.append(directory)

        # extract pitch, run executable
        os.system("./histopitch -in Data/Men/%s.wav -out pitches/men/%s.txt -srate 8000 -lopitch 50 -hipitch 300 -winlen 0.06 -frate 200" % (file[:-4], file[:-4]))


# Women
for file in os.listdir(dir_data_women):
    if file.endswith(".wav"):
        # directory = "%s/%s" % (dir_folder, file)

        # list_audio_files.append(directory)

        # extract pitch, run executable
        os.system("./histopitch -in Data/Women/%s.wav -out pitches/women/%s.txt -srate 8000 -lopitch 50 -hipitch 300 -winlen 0.06 -frate 200" % (file[:-4], file[:-4]))
