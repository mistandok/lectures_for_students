from typing import Hashable

print("Выполняется код в my_set")

class MySet:
    def __init__(self):
        self._set = dict()

    def insert(self, element: Hashable):
        self._set[element] = None

    def has(self, element: Hashable):
        return element in self._set.keys()

    def remove(self, element: Hashable):
        try:
            del self._set[element]
        except KeyError:
            return
