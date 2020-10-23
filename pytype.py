import time
import pickle
import random
import os


fname = "words.data"
letters = 0


def load_words(file_name):
    
    f = open(file_name, "rb")
    words = pickle.load(f)
    return words


def rand_word(words):
    
    randword = random.choice(words)
    return randword


def check(word):

    if word == input("type...\n"):
        return True
    return False

   

def screen(number):

    global fname
    global letters
    words  = load_words(fname)
    for i in range(number):
        w = rand_word(words)
        print(w)
        letters += len(w)
        while not check(w):
            print("oh no! repeat...\n")

        os.system("clear")

def main():

    global letters
    w = int(input("how many word ?"))
    start = time.time()
    screen(w)
    end = time.time()
    print("time              : ", end-start)
    print("time per word     : ", (end-start)/w)
    print("all letters typed : ", letters )
    print("time per letter   : ", (end-start)/letters)
 

if __name__ == "__main__":
    main()
