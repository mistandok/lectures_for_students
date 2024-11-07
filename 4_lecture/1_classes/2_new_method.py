class Logger:
    # Создание экземпляра
    def __new__(cls, name: str) -> "Logger":
        print("Inside __new__ method")
        print(f"Cls is it {type(cls)} {cls}")
        instance = super().__new__(cls)
        print(f"Instance is {instance} with type {type(instance)}")
        return instance

    # Инициализация созданного экземпляра
    def __init__(self, name: str):
        print(f"Inside __init__ method {name}")
        print(f"Self it is {type(self)} with id {id(self)}")
        self.name = name


if __name__ == "__main__":
    logger_1 = Logger("1")
    logger_2 = Logger("2")

    print(f"Loggeer with id {id(logger_1)}")
    print(f"Logger with id {id(logger_2)}")

    print(logger_1.name)
    print(logger_2.name)
