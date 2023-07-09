import nltk
import numpy as np
# print(nltk.__version__)
# nltk.download('punkt)
from nltk.stem.porter import PorterStemmer

# object of the package PortStemmer
stemmer = PorterStemmer()
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence,all_words):
    # sentence = ['hello','how','are','you']
    # words = ['hi','hello','I','bye','thank','you','cool']
    # bag = ['0','1','0','0','0','1','0']

    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words),dtype=np.float32)

    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0

    return bag



# practice
# a = "How are you doing?"
# print(a)
# b = tokenize(a)
# print(b)
# words = ["Organize","organizes","organized"]
# stemmed_words  = [stem(w) for w in b]
# print(stemmed_words)
# stemmed_words = [stem(w) for w in words]
# print(stemmed_words)
# sentence = ['hello','how','are','you']
# words = ['hi','hello','I','bye','thank','you','cool']
# bag = bag_of_words(sentence,words)
# print(bag)
