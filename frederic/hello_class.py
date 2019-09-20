import logging
logging.basicConfig(level=logging.DEBUG)


class Hello(object):

  @staticmethod
  def create_user(name):
    h = Hello()
    h.__name = name
    return h

  def __init__(self):
    self.__name = None

  @staticmethod
  def say_static():
    logging.info("Hello from Hello")

  def say(self):
    logging.info("Hello " + self.__name)
