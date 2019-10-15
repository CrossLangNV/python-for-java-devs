# Python 3.6+ example

class Printer:
    def print(self):
        pass

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        self._items = items

class YamlPrinter(Printer):
    def __init__(self, items = {}):
        # assume this is a dict
        self._items = items

    def print(self):
        print('--- # YAML printer')
        for item in self._items:
            print(f'- {item}: {self._items[item]}')

    def __repr__(self):
        return "YamlPrinter %s" % self._items

    def __str__(self):
        return "Instance of YamlPrinter with the following items %s" % self._items

class CSVPrinter(Printer):
    def __init__(self, items = {}):
        # assume this is a dict
        self._items = items

    def print(self):
        for item in self._items:
            print(f'{item}, {self._items[item]}')
    
    def __repr__(self):
        return "CSVPrinter %s" % self._items

    def __str__(self):
        return "Instance of CSVPrinter with the following items %s" % self._items

if __name__ == '__main__':
    items = {
        'color': 'blue',
        'amount': 3,
        'enabled': True
    }
    y = YamlPrinter()
    c = CSVPrinter()

    y.print()

    y.items = items

    y.print()
    print(y)