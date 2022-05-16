#!/usr/bin/python3
#pip install PyPDF2

#TODO: Not working properly, collected https aren't enough
import PyPDF2

FILE_NAME = "/home/ani-ho/Downloads/Software_Quality.pdf"
RESULT_FILE = "pdf_text.txt"

def parse_pdf(pdf_file):
    print("\n >>> Preparing to read PDF.")
    pdfReader = PyPDF2.PdfFileReader(pdf_file)
    pages = pdfReader.numPages
    c = 0
    for i in range(pages):
        pageObj = pdfReader.getPage(i)
        #print("Page No: ",i)
        text = pageObj.extractText().split("  ")
        for i in range(len(text)):
                c = c + 1
                #print(c, "-", text[i], end="\n\n")
    print("Counted:", c, "times.")
    return text

def get_weblinks(text):
    links = []
    #import pdb; pdb.set_trace()
    for i in text:
        if "https" in i:
            #print("Found https in:", i)
            links.append(i)
            #print("Links:", links[i])
    return links

def generate_result_file(fileName, fileContent):
    f = open(fileName, "a")
    f.write(fileContent)
    f.close()
    print("\n <<< Script succeeded!")

#Get PDF data
pdfText = parse_pdf(FILE_NAME)
#exit()
linksText = str(get_weblinks(pdfText))
generate_result_file(RESULT_FILE, linksText)


