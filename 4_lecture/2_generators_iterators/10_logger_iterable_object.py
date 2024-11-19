from logger.logger_iterable_object import LoggerIterableObject
from logger.storage import MemSotrage

if __name__ == "__main__":
    storage = MemSotrage()
    logger = LoggerIterableObject(storage)

    logger.info("Some log with information")

    for log in logger:
        print(log)

    for log in logger:
        print(log)
