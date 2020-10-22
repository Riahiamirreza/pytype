import time
import pickle
import random
import os


fname = "words.data"


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
    words  = load_words(fname)
    for i in range(number):
        w = rand_word(words)
        print(w)
        while not check(w):
            print("oh no! repeat...\n")

        os.system("clear")

def main():
    w = int(input("how many word ?"))
    start = time.time()
    screen(w)
    end = time.time()
    print("time : ", end-start)
 

if __name__ == "__main__":
    main()
