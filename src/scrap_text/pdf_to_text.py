#!/usr/bin/python3
#pip install tika

from tika import parser

FILE_NAME = "/home/ani-ho/Downloads/Software_Quality.pdf"
RESULT_FILE = "pdf_text.txt"

print("\n >>> Preparing to read PDF.")
raw = parser.from_file(FILE_NAME)

def generate_result_file(fileName, fileContent):
    f = open(fileName, "a")
    f.write(fileContent)
    f.close()
    print("\n <<< Script succeeded!")


generate_result_file(RESULT_FILE, raw['content'])
