import pickle
import os

def add_word(word, file_name):

    f = open(file_name, "rb")
    words = pickle.load(f)
    f.close()
    if word not in words:
        words.append(word)
    f = open(file_name, "wb")
    pickle.dump(words, f)
    f.close()


def init_words(file_name):

    f = open(file_name, "wb")
    words = []
    pickle.dump(words, f)
    f.close()

fname = "words.data"

if not os.path.isfile(fname):
    init_words(fname)

for i in range(int(input("How many words do you want to add?"))):

    add_word(input("word :"), fname)
