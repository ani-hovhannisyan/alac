#!/usr/bin/env python
# This file is responsible for dealing with dataset. Here initial data is one
# paragraph, which will be decomposed and cut into words.

import pdb

DATASET_PATH = "../dataset/"
test_txt_file = "Harry Potter and the Deathly Hallows.txt"

punctuation = {
  "hy": ["։", "․" , "֊", " ", "՞", "՜", "՛", "՝", "«", "»", ";", "*", "―", "(", ")", '"'],
  "en": [" "]
  #"en": [" ", "." , "-", ":", "?", "~", ";", "*", "―", "(", ")", '"', "'", "<", ">", "_"]
}

def prepare_par(par):
    cat_paragraph(par)
    return false

def get_data():
    return false

def load_dataset(path):
    file = open(DATASET_PATH + path, mode="r")
    data = file.read()
    file.close()
    return data

def split_words(text):
    c = 0
    #for t in text:
    for p in punctuation["en"]:
        c = c + 1
        print(c, "Spliting text by:", p)
        pdb.set_trace()
        text = text.split(p)
    #text_part = 
    # TODO: doesnlt work well now, should fix splitted words.
    return text

text = load_dataset(test_txt_file)
words = split_words(text)

file = open(DATASET_PATH + "words_hp.txt", mode="w")
file.writelines(words)
file.close()
print(words)
