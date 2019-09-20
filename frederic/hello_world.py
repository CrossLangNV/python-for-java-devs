import logging

def say(n):
  logging.basicConfig(level=logging.DEBUG)
  for i in range(n):
    logging.info(str(i) + ": Hello world")

say(1)

if __name__=="__main__":
  say(3)
