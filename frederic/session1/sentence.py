import logging
from ngram import Ngram


class Sentence(object):

    def __init__(self):
        self.__ngrams = []

    @property
    def ngrams(self):
        return self.__ngrams

    @ngrams.setter
    def ngrams(self, value):
        self.__ngrams = value