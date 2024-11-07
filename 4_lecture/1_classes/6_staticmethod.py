from __future__ import annotations

import dataclasses
from abc import ABC, abstractmethod
from enum import Enum, auto


@dataclasses.dataclass
class User:
    name: str
    age: int


class StorageType(Enum):
    TXT = auto()
    CSV = auto()


class Storage(ABC):
    @abstractmethod
    def save(self, user: User):
        raise NotImplementedError

    @staticmethod
    def get_storage_by_type(storage_type: StorageType) -> Storage:
        storages = {
            StorageType.CSV: CsvStorage,
            StorageType.TXT: TxtStorage,
        }

        return storages[storage_type]()


class TxtStorage(Storage):
    def save(self, user: User):
        pass


class CsvStorage(Storage):
    def save(self, user: User):
        pass


if __name__ == "__main__":
    storage = Storage.get_storage_by_type(StorageType.TXT)
    print(f"current storage is {type(storage)}")
