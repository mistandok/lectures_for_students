def correct_default(element: int = 10):
    print(element)


def dangerous_with_mutable_default(default_list: list = []):
    """Присваивается значение на этапе считывания кода интерпретатором.

    Далее default list по умолчанию ссылается на эту созданную область памяти и при каждом вызове работает с ней."""
    default_list.append(10)
    print(default_list)


def call_dangerous_with_mutable_default():
    dangerous_with_mutable_default()
    dangerous_with_mutable_default([15])
    dangerous_with_mutable_default()
    dangerous_with_mutable_default([20])
    dangerous_with_mutable_default()


def correct_with_mutable_default(default_list: None | list = None):
    if default_list is None:
        default_list = []

    default_list.append(10)
    print(default_list)


def call_correct_with_mutable_default():
    correct_with_mutable_default()
    correct_with_mutable_default()
    correct_with_mutable_default()


if __name__ == '__main__':
    call_dangerous_with_mutable_default()