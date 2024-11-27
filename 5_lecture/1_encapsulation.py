import traceback

from logger.entity import LogContent, LogType


class Logger:
    def __init__(self):
        self._storage: list[LogContent] = []

    def error(self, msg: str, with_tb: bool = False):
        self._add_log(LogType.ERROR, msg, with_tb)

    def info(self, msg: str):
        self._add_log(LogType.INFO, msg)

    def critical(self, msg: str, with_tb: bool = False):
        self._add_log(LogType.CRITICAL, msg, with_tb)

    def warning(self, msg: str, with_tb: bool = False):
        self._add_log(LogType.WARNING, msg, with_tb)

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


if __name__ == "__main__":
    logger = Logger()
    logger.info("hello world")
    logger.info("amazing log")
    print(logger.show_last_n(1))
