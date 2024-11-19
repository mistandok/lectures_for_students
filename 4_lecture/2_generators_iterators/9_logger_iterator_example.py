from logger.logger_iterator import LoggerIterator
from logger.storage import MemSotrage

if __name__ == "__main__":
    storage = MemSotrage()
    logger = LoggerIterator(storage)

    my_list = []

    try:
        a = 10 / 0
    except ZeroDivisionError as err:
        logger.error(str(err), True)

    try:
        _ = my_list[10]
    except IndexError as err:
        logger.error(str(err), True)

    logger.info("Some log with information")

    for log in logger:
        print(log)

    for log in logger:
        print(log)
