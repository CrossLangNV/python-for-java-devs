import logging

def say_hello():
   logging.basicConfig(level=logging.DEBUG)
   logging.info("Hello world")

say_hello()

'''
multiline-comment
yet another line
'''
if __name__=="__main__":
  say_hello()
