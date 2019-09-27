import logging


class Ngram(object):

    def __init__(self):
        self.__order = 0
        self.__text = ""

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, value):
        self.__order = value

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value

    def __repr__(self):
        return "(%d, %s)" % (self.__order, self.__text)