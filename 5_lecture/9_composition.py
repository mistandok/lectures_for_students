"""
Композиция  - это более сильный тип отношения часть-целое, где дочерний объект напрямую зависит от родительского.
Дочерний объект не может существовать отдельно от родительского.
Жизненные циклы дочернего оъекта и родительского - совпадают.
Это более тесная связь и зависимость, чем агрегация.
"""

import traceback
from enum import Enum
from typing import Protocol


class LogType(Enum):
    CRITICAL = "critical"
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


class LogContent:
    def __init__(self):
        pass


class Storage(Protocol):
    def save(self, log_content: LogContent):
        raise NotImplementedError


class MemStorage:
    def save(self, log_content: LogContent):
        pass


class PgStorage:
    def save(self, log_content: LogContent):
        pass


class Logger:
    def __init__(self, storage: Storage):
        """Тут Logger содержит Storage. Storage у нас, по задумке, вне Logger существовать не будет. Мы не будем пользоваться им вне Logger.
        Мы помещаем его в Logger через init, чтобы нам в коде, где происходит инициализация, можно было легко заменить конкретную реализацию хранилища
        на новую. При этом мы не будем менять код самого Logger, что очень удобно.
        """
        self._storage = storage

    def error(self, msg: str, with_tb: bool = False):
        self._add_log(LogType.ERROR, msg, with_tb)

    def _add_log(self, log_type: LogType, msg: str, with_tb: bool = False):
        params = {
            "log_type": log_type,
            "msg": msg,
        }
        if with_tb:
            params["traceback"] = traceback.format_exc()

        self._storage.save(LogContent(**params))


if __name__ == "__main__":
    storage = MemStorage()
    # storage = PgStorage()
    logger = Logger(storage)
