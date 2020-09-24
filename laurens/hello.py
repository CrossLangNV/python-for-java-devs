def hello_world(name: str):
    """
    Greets you by your name!

    :param name: Your lovely name
    :return: my greetings

    """

    s = f'Hello {name}! I hope you are well.'
    print(s)
    return s


class Hello(object):
    """ A simple class without any use """

    def __init__(self,
                 creator: str,
                 age: int = 0,
                 ):
        """I haven't thought what this can create, but let's give the creater and it's age

        :param creator: Please enter your name
        :param age: We advise to use non-negative ages
        """

        self.creator = creator
        self.age = age

    def get_older(self, delta_year: int = 1):
        """
        We'll set the age one year older

        :param delta_year: amount of years to increase
        :return: the new age counter
        """

        self.age += delta_year
        return self.age
