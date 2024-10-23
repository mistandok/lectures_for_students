from typing import Any, Hashable

print("Выполняется код в my_dict")

class MyDict:
    def __init__(self):
        self._storage = [[] for _ in range(100)]

    def add(self, key: Hashable, value: Any):
        current_idx = self._get_idx_for_key(key)
        for idx in range(len(self._storage[current_idx])):
            if self._storage[current_idx][idx][0] == key:
                self._storage[current_idx][idx][1] = value
                break
        else:
            self._storage[current_idx].append((key, value))

    def get(self, key: Hashable):
        current_idx = self._get_idx_for_key(key)
        for saved_key, value in self._storage[current_idx]:
            if saved_key == key:
                return value

    def remove(self, key: Hashable):
        current_idx = self._get_idx_for_key(key)
        key_value = None
        for idx, key_value in enumerate(self._storage[current_idx]):
            if key == key_value[0]:
                break

        if key_value is not None:
            self._storage[current_idx].remove(key_value)

    def _get_idx_for_key(self, key: Hashable):
        return abs(hash(key) % len(self._storage))


if __name__ == '__main__':
    my_dict = MyDict()
    my_dict.add("hello", 1)
    my_dict.add("world", 2)
    my_dict.add("Anton", 3)

    my_dict.remove("world")

    print(my_dict.get("Anton"))
