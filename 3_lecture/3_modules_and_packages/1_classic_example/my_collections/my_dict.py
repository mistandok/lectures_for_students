import dataclasses
from typing import Any, Hashable

print("Выполняется код в my_dict")


@dataclasses.dataclass
class Element:
    key: Hashable
    value: Any


class MyDict:
    def __init__(self):
        self._storage = [[] for _ in range(100)]

    def add(self, key: Hashable, value: Any):
        current_idx = self._get_idx_for_key(key)
        for idx in range(len(self._storage[current_idx])):
            if self._storage[current_idx][idx].key == key:
                self._storage[current_idx][idx].value = value
                break
        else:
            self._storage[current_idx].append(Element(key, value))

    def get(self, key: Hashable):
        current_idx = self._get_idx_for_key(key)
        for element in self._storage[current_idx]:
            if element.key == key:
                return element.value

    def remove(self, key: Hashable):
        current_idx = self._get_idx_for_key(key)
        element = None
        for idx, element in enumerate(self._storage[current_idx]):
            if key == element.key:
                break

        if element is not None:
            self._storage[current_idx].remove(element)

    def _get_idx_for_key(self, key: Hashable):
        return abs(hash(key) % len(self._storage))


if __name__ == '__main__':
    my_dict = MyDict()
    my_dict.add("hello", 1)
    my_dict.add("hello", 1)
    my_dict.add("world", 2)
    my_dict.add("Anton", 3)

    my_dict.remove("world")

    print(my_dict.get("Anton"))
