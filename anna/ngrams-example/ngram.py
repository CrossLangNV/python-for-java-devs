from abc import ABC, abstractmethod

class NGram(ABC):
    @abstractmethod
    def get_order(self):
        pass
    @abstractmethod
    def get_text(self):
        pass

class Unigram(NGram):
    def __init__(self, text):
        self.__text = text
    def get_order(self):
        return 1
    def get_text(self):
        return self.__text
    def __str__(self):
        return "unigram " + self.__text
    def __repr__(self):
        return "unigram " + self.__text

class BiGram(NGram):
    def __init__(self, text):
        self.__text = text
    def get_order(self):
        return 2
    def get_text(self):
        return self.__text
    def __str__(self):
        return "bigram " + self.__text
    def __repr__(self):
        return "bigram " + self.__text

class Sentence():
    def __init__(self):
        self.__n_grams = []
    def add_ngram(self, n_gram):
        if isinstance(n_gram, NGram):
            self.__n_grams.append(n_gram)
        else:
            print("Error: this is not an ngram.")
    def get_n_grams(self):
        return self.__n_grams
    def __str__(self):
        return "sentence"
    def print_n_gram_count(self):
        print(len(self.__n_grams))
    def print_n_grams(self):
        print(self.__n_grams)

class DB():
    def __init__(self):
        self.__sentences = []
    def add_sentence(self, sentence):
        if isinstance(sentence, Sentence):
            self.__sentences.append(sentence)
        else:
            print("Error: this is not a sentence.")
    def get_sentences(self):
        return self.__sentences
    def print_sentence_n_grams(self):
        for sentence in self.__sentences:
            print(sentence)
            for n_gram in sentence.get_n_grams():
                print(str(n_gram.get_order()) + ": " + str(n_gram))

x = Unigram("rain")
print(x.get_order())
print(x.get_text())
print(x)

y = BiGram("Spain plain")
print(y.get_order())
print(y.get_text())
print(y)

z = Sentence()
print(z)

z.print_n_gram_count()
z.add_ngram(x)
z.print_n_gram_count()
z.add_ngram(y)
z.print_n_gram_count()

z.print_n_grams()

db = DB()
db.add_sentence(z)
db.print_sentence_n_grams()