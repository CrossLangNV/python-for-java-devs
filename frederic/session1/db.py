import logging
from sentence import Sentence
from ngram import Ngram


class Db(object):

    def __init__(self):
        self.__sentences = []

    @property
    def sentences(self):
        return self.__sentences

    @sentences.setter
    def sentences(self, value):
        self.__sentences = value

    def print_sentence_ngrams(self):
        for s in self.__sentences:
            for n in s.ngrams:
                print(n)    
