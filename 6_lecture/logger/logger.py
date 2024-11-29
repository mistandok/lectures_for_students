import traceback

from .entity import LogContent, LogType


class Logger:
    def __init__(self):
        self._storage: list[LogContent] = []

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

        self._storage.append(LogContent(**params))
