#This file scraps text from url and stores words in JSON file.
import requests
from bs4 import BeautifulSoup

url = "https://hy.wikipedia.org/wiki/Parov_Stelar"
page = requests.get(url)
print("Loaded page:", url, "status", page.status_code)
soup = BeautifulSoup(page.content, "html.parser")
object = soup.find("div", {"class": "mw-parser-output"})
text = object.get_text()
print("Text is:", text)
