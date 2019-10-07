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

## Abstract methods

## Properties

## Abstract properties

## Strings and Unicode

## toString() vs str()

## Multi-dimensional arrays

