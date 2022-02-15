from abc import ABC, abstractmethod


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

    def add(self, name, value):
        self.boxList.append(Item(name, value))

    def empty(self):
        self.boxList = []

    def count(self):
        return len(self.boxList)


class DictBox(Box):
    def __init__(self):
        self.dictList = {}

    def add(self, name, value):
        self.dictList[name] = Item(name, value)

    def empty(self):
        self.dictList = {}

    def count(self):
        return len(self.dictList)
