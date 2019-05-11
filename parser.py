from nltk import *
from nltk.corpus import stopwords
from directory import directory

def parse(inp):

    parsed_sen = word_tokenize(inp)
    stop_words = list(stopwords.words("english"))

    parsed_inp = []
    for word in parsed_sen:
        if word not in stop_words:
            parsed_inp.append(word)

    parsed_inp = ",".join(parsed_inp)

    #print(parsed_inp)
    if "directory" in parsed_inp or "folder" in parsed_inp:
        directory(parsed_inp)
