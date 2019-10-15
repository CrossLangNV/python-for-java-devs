# Python 3.6+ example

class Printer:
    def print(self):
        pass

class YamlPrinter(Printer):
    def __init__(self, items=None):
        # assume this is a dict
        self._items = items

    def print(self):
        print('--- # YAML printer')
        for item in self._items:
            print(f'- {item}: {self._items[item]}')

    @property
    def items(self):
        print("getter of items called")
        return self._items

    @items.setter
    def items(self, value):
        print("setter of items called")
        self._items = value

    def __repr__(self):
        return "YamlPrinter items=%s" % self._items

class CSVPrinter(Printer):
    def __init__(self, items={}):
        # assume this is a dict
        self._items = items

    def print(self):
        for item in self._items:
            print(f'{item}, {self._items[item]}')

    @property
    def items(self):
        print("getter of items called")
        return self._items


    @items.setter
    def items(self, value):
       print("setter of items called")
       self._items = value

    def __repr__(self):
        return "CSVPrinter items=%s" % self._items

if __name__ == '__main__':
    items = {
        'color': 'red',
        'amount': 5
    }
    y = YamlPrinter(items)
    c = CSVPrinter(items)

    y.print()
    c.print()

    y.items = {'color':'blue', 'amount':3, 'enabled':True}  # setter called
    items = y.items    # getter called

    print(y)
