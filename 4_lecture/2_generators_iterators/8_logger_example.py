from logger.logger import Logger
from logger.storage import MemSotrage

if __name__ == "__main__":
    storage = MemSotrage()
    logger = Logger(storage)

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

    info = logger._storage.get()
    print(info[0])
    print(info[1])
    print(info[2])
