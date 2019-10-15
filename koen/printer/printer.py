# Python 3.6+ example
class Printer:

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    def __init__(self, items):
        # assume this is a dict
        self._items = items

    def print(self):
        pass


class YamlPrinter(Printer):

    def __init__(self, items={}):
        self._items = items

    def print(self):
        print('--- # YAML printer')
        for item in self._items:
            print(f'- {item}: {self._items[item]}')

    def __repr__(self):
        return f'YamlPrinter({len(self._items)} items)'

    def __str__(self):
        return f'I am an object of class YamlPrinter. The size of my _items is {len(self._items)}.'


class CSVPrinter(Printer):
    def print(self):
        print('--- # CSV printer')
        for item in self._items:
            print(f'{item}, {self._items[item]}')


if __name__ == '__main__':
    items = {
        'color': 'red',
        'amount': 5
    }
    y = YamlPrinter(items)
    c = CSVPrinter(items)

    y.print()
    c.print()

    # Create object without items
    y1 = YamlPrinter()
    y1.print()

    # Set items on object
    items = {
        'color': 'blue',
        'amount': 2,
        'enabled': True
    }
    y1.items = items
    y1.print()

    # print as string
    print(y1)
