#!/usr/bin/env python
# This file is responsible for dealing with dataset. Here initial data is one
# paragraph, which will be decomposed and cut into words.

import pdb

DATASET_PATH = "../dataset/news_am/"
test_txt_file = "Harry Potter and the Deathly Hallows.txt"
test_file = "test.txt"

punctuation = {
  "hy": ["։", "․" , "֊", " ", "՞", "՜", "՛", "՝", "«", "»", ";", "*", "―", "(", ")", '"'],
  "en": [" ", "." , "-", ":", "?", "~", ";", "*", "―", "(", ")", '"', "'", "<", ">", "_"],
  "space": " "
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

def get_words_by(text, delimiter):
    words_list = text.split(delimiter)
    #print("-> Amount of words splitted by delimiter:", delimiter, "is:", len(words_list))
    return words_list

def split_words(text):
    all_words = []

    spaced_text = text.split(punctuation["space"])
    print("----> spaced text length is:", len(spaced_text))
    for i in spaced_text:
        print("Spliting by:", i)
        #pdb.set_trace()
        delimiter = punctuation["en"]
        for d in delimiter:
            all_words.extend(get_words_by(text, d))
            print("----> spaced text length is:", len(all_words), all_words)

    # TODO: doesn't work well now, should fix splitted words.
    return text

#text = load_dataset(test_txt_file)
## COmmented not to call
#database_text = load_dataset(test_file)
#words = split_words(database_text)
#
#file = open(DATASET_PATH + "words_hp.txt", mode="w")
#file.writelines(words)
#file.close()
#print(words)
