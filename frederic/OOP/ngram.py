from abc import ABCMeta, abstractmethod, abstractproperty


class Db(object):

    def __init__(self):
        self.__sentences = list()

    def add_sentence(self, sentence):
        self.__sentences.append(sentence)

    def get_sentences(self):
        return self.__sentences

    def print_sentence_ngrams(self):
        for sentence in self.__sentences:
            for ngram in sentence.ngrams:
                assert isinstance(ngram, NGram)
                print ngram


class NGram(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_order(self):
        pass

    @abstractproperty
    def text(self):
        pass


class Unigram(NGram):

    def __init__(self, text):
        self.__text = text

    def get_order(self):
        return 1

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        self.__text = text

    def __repr__(self):
        return "Unigram (%d, %s)" % (self.get_order(), self.__text)


class Bigram(NGram):
    def __init__(self, text):
        self.__text = text

    def get_order(self):
        return 2

    @property
    def text(self):
        return self.__text

    def __repr__(self):
        return "Bigram (%d, %s)" % (self.get_order(), self.__text)


class Sentence(object):

    def __init__(self):
        self.__ngrams = list()

    def add_ngram(self, ngram):
        self.__ngrams.append(ngram)

    @property
    def ngrams(self):
        return self.__ngrams


if __name__ == '__main__':
    s1 = Sentence()
    n1 = Unigram('Hello')
    s1.add_ngram(n1)

    s2 = Sentence()
    n2 = Bigram('Hello World')
    s2.add_ngram(n2)

    db = Db()
    db.add_sentence(s1)
    db.add_sentence(s2)
    db.print_sentence_ngrams()
