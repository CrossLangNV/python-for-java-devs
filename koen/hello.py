import logging

logging.basicConfig(level=logging.DEBUG)

def say_hello(name):
  logging.info("hello " + name)

stringy = "koen"

if __name__=="__main__":
  say_hello(stringy);
else:
  logging.info("NOT called from hello")
