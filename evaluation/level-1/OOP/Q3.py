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

    def add(self, *items):
        self.boxList.extend(items)

    def empty(self):
        items = self.boxList
        self.boxList = []
        return items

    def count(self):
        return len(self.boxList)


class DictBox(Box):
    def __init__(self):
        self.boxDict = {}

    def add(self, *items):
        self.boxDict.update(dict((str(i), i) for i in items))

    def empty(self):
        items = list(self.boxDict.values())
        self.boxDict = {}
        return items

    def count(self):
        return len(self.boxDict)


def repack_boxes(boxes):
    items = []

    for box in boxes:
        items.extend(box.empty())

    while items:
        for box in boxes:
            try:
                box.add(items.pop())
            except IndexError:
                break


box1 = ListBox()
for i in range(20):
    box1.add(Item(str(i), i))

box2 = ListBox()
for i in range(9):
    box2.add(Item(str(i), i))

box3 = DictBox()
for i in range(5):
    box3.add(Item(str(i), i))


repack_boxes([box1, box2, box3])

print(box1.count())
print(box2.count())
print(box3.count())
