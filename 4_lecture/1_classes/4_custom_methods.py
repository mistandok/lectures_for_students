class Logger:
    def __init__(self, name: str):
        self.name = name
        self.storage = []

    def size(self):
        return len(self.storage)

    def info(self, message: str):
        self.storage.append(message)


if __name__ == "__main__":
    logger = Logger("main")
    print(f"current size {logger.size()}")

    for _ in range(10):
        logger.info("some info")

    print(f"current size {logger.size()}")
    print(f"elements in loggeer {logger.storage}")
