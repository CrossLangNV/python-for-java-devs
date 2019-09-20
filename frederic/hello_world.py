import logging

def say():
  logging.basicConfig(level=logging.DEBUG)
  logging.info("Hello world")

say()

if __name__=="__main__":
  say()
