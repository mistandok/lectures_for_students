import json
import pickle
from abc import ABC, abstractmethod


class ObjectStorage(ABC):
    def __init__(self, file_path: str) -> None:
        self._file_path = file_path

    @abstractmethod
    def write(self, data: dict) -> None:
        pass

    @abstractmethod
    def read(self) -> dict:
        pass


class PickleObjectStorage(ObjectStorage):
    def write(self, data: dict) -> None:
        with open(self._file_path, "wb") as file:
            pickle.dump(data, file)

    def read(self) -> dict:
        with open(self._file_path, "rb") as file:
            return pickle.load(file)


class JsonObjectStorage(ObjectStorage):
    def write(self, data: dict) -> None:
        with open(self._file_path, "w") as file:
            json.dump(data, file)

    def read(self) -> dict:
        with open(self._file_path, "r") as file:
            return json.load(file)


if __name__ == "__main__":
    storage = PickleObjectStorage("./data.pickle")
    storage.write({"hello": 123})
    print(storage.read())

    storage = JsonObjectStorage("./data.json")
    storage.write({"hello": 123})
    print(storage.read())
