#!/usr/bin/env python

#This file scraps text from url and stores words in JSON file.
import requests
from bs4 import BeautifulSoup
import re
import json
import os
#import dataset_controller

#Constants
CONFIG_FILE = "./config/websites.json"
DATASET_PATH = "../dataset/news_am/"
CORPUS_TXT_FILE = ".txt"

#Globals
configs = {}

def is_clear_paragraph(par):
    if par and not par.isspace() \
        and not par.isdecimal() \
        and not re.match(r'^[_\W]+$', par):
        return True
    else:
        return False

def get_cleared_paragraphs(text):
    #print(text)
    #TEMPORARY RETURINING TO COLLECT FRESH RAW DATA
    return text

    par = text.split("\n")
    par_length = len(par)
    cleared_text = []
    for i in range(par_length):
        if is_clear_paragraph(par[i]):
            cleared_text.append(par[i])
    #print(">>> Found about: ", i, " text paragraphs out from:", par_length)
    print(">>> Found par length is:", par_length)
    #dataset_controller.prepare_par(cleared_text)
    #DOESNT work well unremove if fixed in dataset_controller.py
    return cleared_text

def scrap_url(header, url, tag, sid, fn):
    page = requests.get(url, headers={"User-Agent": header})
    print("\n>>> Loaded webpage:", url, ", status is:", page.status_code)
    soup = BeautifulSoup(page.content, "html.parser")
    object = soup.find(tag, {"class": sid})
    if object:
        text = object.get_text()
        cleared_paragraphs = get_cleared_paragraphs(text)
        write_into_file(fn, cleared_paragraphs)

def write_into_file(fn, c):
    print("Writing into file:", fn)
    f = open(fn, mode="w")
    f.write(c)
    f.close()

def load_configs():
    f = open(CONFIG_FILE)
    data = json.load(f)
    f.close()
    return data

def main():
    #Loading website text scraping configs
    configs = load_configs()
    #Fetching
    for site in configs["websites"]:
        #print(site)
        if "news_am" == site["title"]:
            site["min"] = "642" # Remove after interrupted cycle
            for i in range(int(site["min"]), int(site["max"])):
                url = site["url"].replace("000000", str(i))
                fn = os.path.join(DATASET_PATH, site["title"] + "_" + str(i) + CORPUS_TXT_FILE)
                scrap_url(configs["browser_agent"], url, site["tag"], site["id"], fn)

if __name__ == "__main__":
    main()

#Connecting to website to request data
#TODO: Make function to call various websites by passing find class/id

