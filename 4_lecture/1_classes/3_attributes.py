class Logger:
    logger_names = []

    def __init__(self, name: str):
        self.name = name
        self.logger_names.append(name)


if __name__ == "__main__":
    logger_main = Logger("main")
    logger_support = Logger("support")

    print(f"logger_names in main logger_main {logger_main.logger_names}")
    print(f"logger_names in main logger_support {logger_support.logger_names}")

    # Тут переопределили атрибут класса атрибутом инстанса.
    # Теперь мы найдем этот атрибут в локальном неймспейсе инстанса.
    # Мы не будем искать его в неймспейсе класса. Вспоминайте LEGB, примрно тоже самое, только под другим углом
    logger_support.logger_names = []

    logger_default = Logger("logger_default")

    print(f"logger_names in logger_main {logger_main.logger_names}")
    print(f"logger_names in logger_support {logger_support.logger_names}")
    print(f"logger_default in logger_support {logger_default.logger_names}")

    # Вот тут делаем плохие дела, не повторяйте в своем коде. Просто надо понимать, что в питоне так можно
    logger_default.new_attr = 10

    try:
        print(f"new_attr in logger_main {logger_main.new_attr}")
    except AttributeError:
        print("new_attr is missing")

    print(f"new_attr in logger_default {logger_default.new_attr}")
