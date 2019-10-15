# Python 3.6+ example

class Printer:
    def print(self):
        pass


class YamlPrinter(Printer):
    def __init__(self, items=None):
        # assume this is a dict
        self.__items = items

    def print(self):
        print('--- # YAML printer')
        for item in self.__items:
            print(f'- {item}: {self.__items[item]}')

    def __repr__(self):
        string_repr = str()
        for x in self.__items:
            string_repr.join(x)
        return "YamlPrinter __items=" + string_repr

    def __str__(self):
        string_repr = str()
        for x in self.__items:
            string_repr.join(x)
        return "I am a dictionary of YamlPrinter items" + string_repr

    @property
    def items(self):
        print("getter of items called")
        return self.__items

    @items.setter
    def items(self, value):
        print("setter of items called")
        self.__items = value


class CSVPrinter(Printer):
    def __init__(self, items="color : blue, amount : 3, enabled : True"):
        # assume this is a dict
        self._items = items

    def print(self):
        for item in self._items:
            print(f'{item}, {self._items[item]}')

    def __repr__(self):
        string_repr = str()
        for x in self._items:
            string_repr.join(x)
        return string_repr

    def __str__(self):
        string_repr = str()
        for x in self.__items:
            string_repr.join(x)
        return "I am a dictionary of CSVPrinter items" + string_repr

    @property
    def items(self):
        print("getter of items called")
        return self._items

    @items.setter
    def items(self, value):
        print("setter of items called")
        self._items = value


if __name__ == '__main__':
    items = {
        'color': 'red',
        'amount': 5
    }
    y = YamlPrinter(items)
    c = CSVPrinter()
    print(c)
    c.__repr__()
    c.__str__()
    y.__repr__()
    y.__str__()

    c.items = {1: 'csv'}
    y.items = {2: 'yaml'}
    csv_printer = c.items
    yaml_printer = y.items

