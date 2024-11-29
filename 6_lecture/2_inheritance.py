import datetime
import os
import traceback
from abc import ABC, abstractmethod

from logger.entity import LogContent, LogType


class Logger(ABC):
    def error(self, msg: str, with_tb: bool = False):
        self._add_log(LogType.ERROR, msg, with_tb)

    def info(self, msg: str):
        self._add_log(LogType.INFO, msg)

    def critical(self, msg: str, with_tb: bool = False):
        self._add_log(LogType.CRITICAL, msg, with_tb)

    def warning(self, msg: str, with_tb: bool = False):
        self._add_log(LogType.WARNING, msg, with_tb)

    @abstractmethod
    def show_last_n(self, n: int) -> list[LogContent]:
        pass

    @abstractmethod
    def _add_log(self, log_type: LogType, msg: str, with_tb: bool = False):
        pass


class MemLogger(Logger):
    def __init__(self):
        super().__init__()
        self._storage: list[LogContent] = []

    def show_last_n(self, n: int) -> list[LogContent]:
        return self._storage[-n:][::-1]

    def _add_log(self, log_type: LogType, msg: str, with_tb: bool = False):
        params = {
            "log_type": log_type,
            "msg": msg,
        }
        if with_tb:
            params["traceback"] = traceback.format_exc()

        self._storage.append(LogContent(**params))


def is_file_exists(file_path: str) -> bool:
    return os.path.isfile(file_path)


def create_file_if_not_exists(file_path: str):
    if is_file_exists(file_path):
        return

    with open(file_path, mode="w+"):
        pass


class TxtLogger(Logger):
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

    def _add_log(self, log_type: LogType, msg: str, with_tb: bool = False):
        params = {
            "log_type": log_type,
            "msg": msg,
        }
        if with_tb:
            params["traceback"] = traceback.format_exc()

        log_content = LogContent(**params)

        with open(self._path, mode="a") as file:
            file.write(f"log_type: {log_content.log_type.value}\n")
            file.write(f"msg: {log_content.msg}\n")
            file.write(f"cur_time: {log_content.cur_time}\n")
            file.write(f"traceback: {log_content.traceback}\n")
            file.write(f"----\n")


if __name__ == "__main__":
    logger = TxtLogger("./logs.log")
    logger.info("hello world")
    logger.info("amazing log")
    try:
        _ = 10 / 0
    except Exception:
        logger.error("error", with_tb=True)

    logger.info("next info")

    try:
        raise ValueError("wow")
    except ValueError:
        logger.error("wow error", with_tb=True)

    print(logger.show_last_n(2))
