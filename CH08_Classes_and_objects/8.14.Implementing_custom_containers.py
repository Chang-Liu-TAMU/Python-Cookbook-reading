import collections

class A(collections.Iterable):
    pass


import collections
import bisect


class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []
    # Required sequence methods

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    # Method for adding an item in the right location
    def add(self, item):
        bisect.insort(self._items, item)

# items = SortedItems([5, 1, 3])
# print(list(items))
# print(items[0])
# items.add(2)
# print(list(items))
# print(1 in items)
# print(items[-1])

items = SortedItems()
import collections
# print(isinstance(items, collections.Iterable))

# >>> isinstance(items, collections.Sequence)
# True
# >>> isinstance(items, collections.Container)
# True
# >>> isinstance(items, collections.Sized)
# True
# >>> isinstance(items, collections.Mapping)

class Items(collections.MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is not None else []
    # Required sequence methods
    def __getitem__(self, index):
        print('Getting:', index)
        return self._items[index]
    def __setitem__(self, index, value):
        print('Setting:', index, value)
        self._items[index] = value
    def __delitem__(self, index):
        print('Deleting:', index)
        del self._items[index]

    def insert(self, index, value):
        print('Inserting:', index, value)
        self._items.insert(index, value)

    def __len__(self):
        print('Len')
        return len(self._items)

a = Items([1, 2, 3])
print(len(a))
a.append(4)
a.append(100)
a.append(888)
print(a.count(1))
a.remove(3) #remove value at index
print(a)
print(list(a))
