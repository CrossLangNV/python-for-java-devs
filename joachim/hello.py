import logging

def say_hello():
  logging.basicConfig(level=logging.DEBUG)
  logging.info("Hello world")

say_hello()

# Single line comment
'''
In java we have /**
                **/
'''
if __name__=="__main__":
  say_hello()
