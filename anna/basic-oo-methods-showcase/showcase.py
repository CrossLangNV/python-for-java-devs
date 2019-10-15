class C(object):

    # Voorbeelden van verschillende mogelijke constructors:

    #def __init__(self):
    #    self.__x = None

    #def __init__(self, x):
    #    self.__x = x

    #def __init__(self, x=None):
    #    self.__x = x

    def __init__(self, x="something"):
        self.__x = x

    # Getters en setters:

    @property
    def x(self):
        print("getter of x called")
        return self.__x

    # een getter is ook op de volgende manier mogelijk:
    def get_x(self):
        return self.__x

    @x.setter
    def x(self, value):
        print("setter of x called")
        self.__x = value

    # Methodes om classeobject als string weer te geven:

    def __repr__(self):
        return "C __x=" + self.__x

    def __str__(self):
        return "I am an object of class C. The value of my x property is " + self.__x

c = C()
c2 = C("bla")

c.x = 'foo'  # setter called
bar = c.x    # getter called

print(c.__repr__())
print(c.__str__())

print(c)

