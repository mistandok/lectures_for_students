class Logger:
    def __init__(self, name: str):
        self.name = name


if __name__ == "__main__":
    logger_main = Logger("main_logger")
    print(f"What it is: {type(logger_main)}")
    print(f"Logger name is: {logger_main.name}")

    logger_support = Logger("support_logger")
    print(f"What it is: {type(logger_support)}")
    print(f"Logger name is: {logger_support.name}")

    print(f"Is it same? {logger_support is logger_main}")
