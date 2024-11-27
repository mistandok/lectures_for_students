import json
import pickle
from typing import Protocol


class Writer(Protocol):
    def write(self, data: dict):
        raise NotImplementedError()


class Reader(Protocol):
    def read(self) -> dict:
        raise NotImplementedError()


class PickleStorage:
    def __init__(self, file_path: str) -> None:
        self._file_path = file_path

    def write(self, data: dict) -> None:
        with open(self._file_path, "wb") as file:
            pickle.dump(data, file)

    def read(self) -> dict:
        with open(self._file_path, "rb") as file:
            return pickle.load(file)


class JsonStorage:
    def __init__(self, file_path: str) -> None:
        self._file_path = file_path

    def write(self, data: dict) -> None:
        with open(self._file_path, "w") as file:
            json.dump(data, file)

    def read(self) -> dict:
        with open(self._file_path, "r") as file:
            return json.load(file)


def load_object(writer: Writer):
    obj = {"hello": 123}
    writer.write(obj)


def get_object(reader: Reader):
    print(reader.read())


if __name__ == "__main__":
    # storage = PickleStorage("./data.pickle")
    storage = JsonStorage("./data.json")
    load_object(storage)
    get_object(storage)
