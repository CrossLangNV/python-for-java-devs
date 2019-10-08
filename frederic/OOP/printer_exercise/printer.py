# Python 3.6+ example

class Printer:
    def print(self):
        pass

class YamlPrinter(Printer):
    def __init__(self, items):
        # assume this is a dict
        self._items = items

    def print(self):
        print('--- # YAML printer')
        for item in self._items:
            print(f'- {item}: {self._items[item]}')

class CSVPrinter(Printer):
    def __init__(self, items):
        # assume this is a dict
        self._items = items

    def print(self):
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