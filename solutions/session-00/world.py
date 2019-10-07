import hello

if __name__=='__main__':
    print hello.get_hello()
   #  h = HelloSayer() will not work unless you import the HelloSayer class explicitly
    from hello import HelloSayer
    h = HelloSayer()
