#!/usr/bin/env python

#This file scraps text from url and stores words in JSON file.
import requests
from bs4 import BeautifulSoup
import re
import json

#Constants
CONFIG_FILE = "./config/websites.json"
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
    par = text.split("\n")
    par_length = len(par)
    cleared_text = []
    for i in range(par_length):
        if is_clear_paragraph(par[i]):
            cleared_text.append(par[i])
    print(">>> Found about: ", i, " text paragraphs out from:", par_length)
    return cleared_text

def scrap_url(header, url, tag, id):
    page = requests.get(url, headers={"User-Agent": header})
    print("\n>>> Loaded webpage:", url, ", status is:", page.status_code)
    soup = BeautifulSoup(page.content, "html.parser")
    object = soup.find(tag, {"class": id})
    text = object.get_text()
    cleared_paragraphs = get_cleared_paragraphs(text)

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
        #TODO: Add a logic to parse each site specifc urls, now static links for testing
        scrap_url(configs["browser_agent"], site["url"], site["tag"], site["id"])
        #return

if __name__ == "__main__":
    main()

#Connecting to website to request data
#TODO: Make function to call various websites by passing find class/id
#TODO: Make main to call downloading data and storing in file

