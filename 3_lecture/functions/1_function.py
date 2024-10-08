def empty_function() -> None:
    """Пример функции, которая ничего не делает. Если в функции явно не указан результат возврата, то это будет None"""
    pass


def function_with_return() -> int:
    return 10


if __name__ == '__main__':
    print(empty_function())
    print(function_with_return())
