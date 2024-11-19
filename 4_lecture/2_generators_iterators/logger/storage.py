from typing import Protocol

from .entity import LogContent


class Storage(Protocol):
    def save(self, log: LogContent):
        pass

    def get(self) -> list[LogContent]:
        pass

    def get_by_id(self, idx: int) -> LogContent:
        pass


class MemSotrage:
    def __init__(self):
        self._data: list[LogContent] = []

    def save(self, log: LogContent):
        self._data.append(log)

    def get(self) -> list[LogContent]:
        return self._data

    def get_by_id(self, idx: int) -> LogContent:
        return self._data[idx]
