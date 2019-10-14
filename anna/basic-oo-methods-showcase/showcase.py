class C(object):
    def __init__(self):
        self.__x = None

    #def __init__(self, x):
    #    self.__x = x

    #def __init__(self, x=None):
    #    self.__x = x

    #def __init__(self, x="something"):
    #    self.__x = x

    #@property
    #def x(self):
    #    print("getter of x called")
    #    return self.__x

    #@x.setter
    #def x(self, value):
    #    print("setter of x called")
    #    self.__x = value

    #def __repr__(self):
    #    return "C x=" + self.__x

    #def __str__(self):
    #    return "I am an object of class C. The value of my x property is " + self.__x

c = C()

#c.x = 'foo'  # setter called
#foo = c.x    # getter called

#c.__repr__()
#c.__str__()
