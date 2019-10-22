# *Pythonification* of Java code

## Python classes

Class names should follow the UpperCaseCamelCase convention. In case you want to define a class, but leave its implementation open for now, make sure to declare `pass` in the body:
```python
class SomeExampleClass(object):
    pass
```

## Class variables and instance variables

```python
class SomeExample(object):
    some_class_var = 'red'

    def __init__(self, value):
        self._some_instance_var = value
    
    def get_instance_var(self):
        return self._some_instance_var
```
In the example above `some_class_var` can be accessed by invoking `SomeExample.some_class_var`, it belongs to the class. Whereas `_some_instance_var` belongs to a specific instance of this class: 
```python
    e = SomeExample()
    print e.get_instance_var()
```

## Factory pattern instead of constructor overloading

Use the `@classmethod` decorator. With a classmethod the class of the object instance is implicitly passed as the first argument instead of `self`. In the example below `return cls(text)` invokes the regular constructor to return a new instance.
```python
class SomeExample(object):
    def __init__(self, text):
        self.__text = text

    @classmethod
    def from_list(cls, l):
        text = ' '.join(l)
        return cls(text)
```
Usage:
```python
s1 = SomeExample('ab') # regular instantiation
s2 = SomeExample.from_list(['a', 'b']) # instantiation by classmethod
```

## Static methods

## Interfaces in Python

*For Python 3*, from: http://masnun.rocks/2017/04/15/interfaces-in-python-protocols-and-abcs/

### Informal interfaces: protocols / duck typing

There’s no `interface` keyword in Python. The Java / C# way of using interfaces is not available here. In the dynamic language world, things are more implicit. We’re more focused on how an object behaves, rather than it’s type/class.

> If it talks and walks like a duck, then it is a duck.

So if we have an object that can fly and quack like a duck, we consider it as a duck. This called "duck typing". In runtime, instead of checking the type of an object, we try to invoke a method we expect the object to have. If it behaves the way we expected, we’re fine and move along. But if it doesn’t, things might blow up. To be safe, we often handle the exceptions in a `try..except` block or use `hasattr` to check if an object has the specific method.

In the Python world, we often hear “file like object” or “an iterable” - if an object has a read method, it can be treated as a file like object, if it has an `__iter__` magic method, it is an iterable. So any object, regardless of it’s class/type, can conform to a certain interface just by implementing the expected behavior (methods). These informal interfaces are termed as __protocols__. Since they are informal, they can not be formally enforced. They are mostly illustrated in the documentations or defined by convention. All the cool magic methods you have heard about - `__len__`, `__contains__`, `__iter__` - they all help an object to conform to some sort of protocols.

```python
class Team:
    def __init__(self, members):
        self.__members = members

    def __len__(self):
        return len(self.__members)

    def __contains__(self, member):
        return member in self.__members

    def __iter__(self):
        return iter(self.__members)


justice_league_fav = Team(["batman", "wonder woman", "flash"])

# Sized protocol
print(len(justice_league_fav))

# Container protocol
print("batman" in justice_league_fav)
print("superman" in justice_league_fav)
print("cyborg" not in justice_league_fav)

# Iterable protocol
for member in justice_league_fav:
    print(member)
```

### Formal Interfaces: ABCs

While protocols work fine in many cases, there are situations where informal interfaces or duck typing in general can cause confusion. For example, a `Bird` and `Aeroplane` both can `fly()`. But they are not the same thing even if they implement the same interfaces / protocols. __Abstract Base Classes__ or __ABCs__ can help solve this issue.

The concept behind ABCs is simple - we define base classes which are abstract in nature. We define certain methods on the base classes as abstract methods. So any objects deriving from these bases classes are forced to implement those methods. And since we’re using base classes, if we see an object has our class as a base class, we can say that this object implements the interface. That is now we can use types to tell if an object implements a certain interface. Let’s see an example.

```python
from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass
```

There’s the `abc` module which has a metaclass named `ABCMeta`. ABCs are created from this metaclass. So we can either use it directly as the metaclass of our ABC (something like this - `class Bird(metaclass=abc.ABCMeta):`) or we can subclass from the `abc.ABC` class which has the `abc.ABCMeta` as it’s metaclass already.

Then we have to use the `abc.abstractmethod` decorator to mark our methods abstract. Now if any class derives from our base `Bird` class, it must implement the `fly` method too. The following code would fail:

```python
class Parrot(Bird):
    pass

p = Parrot()
```

We see the following error:
```
TypeError: Can't instantiate abstract class Parrot with abstract methods fly
```

Let's fix that:
```python
class Parrot(Bird):
    def fly(self):
        print("Flying")


p = Parrot()
```
Also note:
```python
>>> isinstance(p, Bird)
True
```
Since our parrot is recognized as an instance of `Bird` ABC, we can be sure from it’s type that it definitely implements our desired interface.

Now let’s define another ABC named `Aeroplane` like this:
```python
class Aeroplane(ABC):
    @abstractmethod
    def fly(self):
        pass


class Boeing(Aeroplane):
    def fly(self):
        print("Flying!")

b = Boeing()
```
Now if we compare:
```python
>>> isinstance(p, Aeroplane)
False
>>> isinstance(b, Bird)
False
```
We can see even though both objects have the same method `fly` but we can now differentiate easily which one implements the `Bird` interface and which implements the `Aeroplane` interface.

We saw how we can create our own, custom ABCs. But it is often discouraged to create custom ABCs and rather use/subclass the built in ones. The Python standard library has many useful ABCs that we can easily reuse. We can get a list of useful built in ABCs in the `collections.abc` module - https://docs.python.org/3/library/collections.abc.html#module-collections.abc. Before writing your own, please do check if there’s an ABC for the same purpose in the standard library.

## Abstract methods

## Properties

## Abstract properties

## Strings and Unicode

## toString() vs str()

## Multi-dimensional arrays

