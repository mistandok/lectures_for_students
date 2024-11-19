import traceback

from .entity import LogContent, LogType
from .storage import Storage


class LoggerIterator:
    def __init__(self, storage: Storage):
        self._storage = storage
        self._iter_idx = None

    def __iter__(self):
        return self

    def __next__(self):
        if self._iter_idx is None:
            self._iter_idx = 0

        try:
            cur_log = self._storage.get_by_id(self._iter_idx)
        except IndexError:
            raise StopIteration

        self._iter_idx += 1
        return cur_log

    def error(self, msg: str, with_tb: bool = False):
        self._add_log(LogType.ERROR, msg, with_tb)

    def info(self, msg: str, with_tb: bool = False):
        self._add_log(LogType.INFO, msg, with_tb)

    def critical(self, msg: str, with_tb: bool = False):
        self._add_log(LogType.CRITICAL, msg, with_tb)

    def warning(self, msg: str, with_tb: bool = False):
        self._add_log(LogType.WARNING, msg, with_tb)

    def _add_log(self, log_type: LogType, msg: str, with_tb: bool = False):
        params = {
            "log_type": log_type,
            "msg": msg,
        }
        if with_tb:
            params["traceback"] = traceback.format_exc()

        self._storage.save(LogContent(**params))
