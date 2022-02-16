from abc import ABC, abstractmethod
import string


class Box(ABC):
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def empty(self):
        pass

    @abstractmethod
    def count(self):
        pass


class Item():

    def __init__(self, name, value):
        self.name = name
        self.value = value


class ListBox(Box):

    def __init__(self):
        self.boxList = []

    def add(self, items):
        self.boxList.extend(items)

    def empty(self):
        self.boxList = []

    def count(self):
        return len(self.boxList)


class DictBox(Box):
    def __init__(self):
        self.boxDict = {}

    def add(self, items):
        self.boxDict.update(items)

    def empty(self):
        self.boxDict = {}

    def count(self):
        return len(self.boxDict)


box1 = ListBox()
box1.add([Item(alphabet, i) for i, alphabet in enumerate(list(string.ascii_lowercase))])

box2 = DictBox()
box2.add(dict((alphabet, Item(alphabet, i)) for i, alphabet in enumerate(list(string.ascii_lowercase))))
