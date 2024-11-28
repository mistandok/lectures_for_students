import datetime
import os
import traceback
from typing import Protocol

from logger.entity import LogContent, LogType

# ====================================
# formatter
# ====================================


class TextFormatter(Protocol):
    def format(self, text: str) -> str:
        raise NotImplementedError


class UpperCaseFormatter:
    def format(self, text: str) -> str:
        return text.upper()


class CapitalizeFormatter:
    def format(self, text: str) -> str:
        return text.capitalize()


class TitleFormatter:
    def format(self, text: str) -> str:
        return text.title()


# ====================================
# Storage
# ====================================


class Storage(Protocol):
    def save(self, log_content: LogContent):
        raise NotImplementedError

    def show_last_n(self, n: int) -> list[LogContent]:
        raise NotImplementedError


class MemStorage:
    def __init__(self):
        self._data: list[LogContent] = []

    def show_last_n(self, n: int) -> list[LogContent]:
        return self._data[-n:][::-1]

    def save(self, log_content: LogContent):
        self._data.append(log_content)


class TxtStorage:
    def __init__(self, file_path: str):
        create_file_if_not_exists(file_path)
        self._path = file_path

    def show_last_n(self, n: int) -> list[LogContent]:
        result: list[LogContent] = []
        split_symbol = "----"
        with open(self._path, mode="r") as file:
            tb = ""
            params = {}
            for line in file:
                if line.startswith("log_type: "):
                    log_type = line.replace("log_type: ", "").rstrip("\n")
                    params["log_type"] = LogType(log_type)
                    continue

                if line.startswith("msg: "):
                    msg = line.replace("msg: ", "").rstrip("\n")
                    params["msg"] = msg
                    continue

                if line.startswith("cur_time: "):
                    cur_time_str = line.replace("cur_time: ", "").rstrip("\n")
                    #  cur_time: 2024-11-27 22:43:14.383325
                    format_str = "%Y-%m-%d %H:%M:%S.%f"
                    cur_time = datetime.datetime.strptime(cur_time_str, format_str)
                    params["cur_time"] = cur_time
                    continue

                if line.startswith("traceback: "):
                    tb += line.replace("traceback: ", "")
                    continue

                if line.startswith(split_symbol):
                    params["traceback"] = tb[:-2]
                    log_content = LogContent(**params)
                    result.append(log_content)
                    params.clear()
                    tb = ""
                    continue

                if tb:
                    tb += line

        return result[-n:][::-1]

    def save(self, log_content: LogContent):
        with open(self._path, mode="a") as file:
            file.write(f"log_type: {log_content.log_type.value}\n")
            file.write(f"msg: {log_content.msg}\n")
            file.write(f"cur_time: {log_content.cur_time}\n")
            file.write(f"traceback: {log_content.traceback}\n")
            file.write(f"----\n")


# ====================================
# Logger
# ====================================


class Logger:
    def __init__(
        self, storage: Storage, message_formatter: TextFormatter | None = None
    ):
        self._storage = storage
        self._message_formatter = message_formatter

    def error(self, msg: str, with_tb: bool = False):
        self._add_log(LogType.ERROR, msg, with_tb)

    def info(self, msg: str):
        self._add_log(LogType.INFO, msg)

    def critical(self, msg: str, with_tb: bool = False):
        self._add_log(LogType.CRITICAL, msg, with_tb)

    def warning(self, msg: str, with_tb: bool = False):
        self._add_log(LogType.WARNING, msg, with_tb)

    def show_last_n(self, n: int) -> list[LogContent]:
        return self._storage.show_last_n(n)

    def _add_log(self, log_type: LogType, msg: str, with_tb: bool = False):
        msg = self._message_formatter.format(msg) if self._message_formatter else msg

        params = {
            "log_type": log_type,
            "msg": msg,
        }
        if with_tb:
            params["traceback"] = traceback.format_exc()

        self._storage.save(LogContent(**params))


def is_file_exists(file_path: str) -> bool:
    return os.path.isfile(file_path)


def create_file_if_not_exists(file_path: str):
    if is_file_exists(file_path):
        return

    with open(file_path, mode="w+"):
        pass


if __name__ == "__main__":
    storage = TxtStorage("./logs.log")
    formatter = TitleFormatter()
    logger = Logger(storage, formatter)
    logger.info("hello world")
    logger.info("another message for log")
    logger.info("get one more message")
    print(logger.show_last_n(2))
