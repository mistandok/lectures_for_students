from logger.logger import Logger
from logger.storage import MemSotrage

if __name__ == "__main__":
    storage = MemSotrage()
    logger = Logger(storage)

    logger.info("Some log with information")

    for log in logger.walk():
        print(log)

    for log in logger.walk():
        print(log)
