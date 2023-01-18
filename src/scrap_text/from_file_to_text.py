# This file reads dataset folder and unions each 1000 .txt files into one

import os

DATASET_PATH = "../dataset/news_am/"
POST_TXT_FILE = ".txt"
NEWS_1000_POSTS = "1000_news_posts.txt"

def main():
    siteTitle = "news_am" # TODO: replace to all websites loop
    for k in range(1, 7):

        for i in range((k-1)*1000, k*1000):

            print("Working with:", k, i)
            fn = os.path.join(DATASET_PATH, siteTitle + "_" + str(i) + POST_TXT_FILE)

            if os.path.exists(fn):
                text = read_data(fn)
                print("Writing into file:", fn)
                write_into_file(str(k) + "_" + NEWS_1000_POSTS, text)


def read_data(fn):
    f = open (fn, 'r', encoding='utf-8')
    text = f.read()
    f.close()
    return text

def write_into_file(fn, c):
    f = open(fn, mode="a")
    f.write(c)
    f.close()


if __name__ == "__main__":
    main()
