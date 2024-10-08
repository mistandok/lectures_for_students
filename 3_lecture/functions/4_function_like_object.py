"""Функция в Python - объект первого порядка.

Это значит, что:
    - может быть создана во время выполнения
    - может быть присвоена переменной или полю структуры данных
    - может быть передан функции в качестве аргумента
    - может быть возвращен функцией в качестве результата
"""
from typing import Callable


def get_formatted_user_id(user_id: int) -> str:
    """Вызвать call_get_formatted_user_id.

    Рассказать про то, что функция - это такой же объект как и все в питоне.
    """
    """Форматирует ID пользователя."""
    return f"id_{user_id}"


def call_get_formatted_user_id():
    print("Результат работы функции:", get_formatted_user_id(100))
    print("Функция имеет собственные атрибуты, ее документация:", get_formatted_user_id.__doc__)
    print("Тип функции:", type(get_formatted_user_id))
    print(issubclass(type(get_formatted_user_id), object))
    print(issubclass(type("string"), object))
    print(issubclass(type(int), object))


def created_in_time_execute(is_need_new_function: bool = False):
    """может быть создана во время выполнения"""
    if is_need_new_function:
        def new_function():
            print("hello, i'm in new function")

        new_function()
    else:
        print("do nothing")


def call_created_in_time_execute():
    created_in_time_execute()
    created_in_time_execute(True)


def assign_to_variable(user_name: str):
    """может быть присвоена переменной или полю структуры данных"""
    print(f"Hello, {user_name}")


def call_assign_to_variable():
    assign_to_variable("Anton")
    new_variable = assign_to_variable

    new_variable("Anton")


def send_like_argument():
    """может быть передан функции в качестве аргумента."""
    def summator(a, b):
        print("Результат сложения", a+b)

    def divider(a, b):
        print("Результат деления", a/b)

    def pairs_action_execute(*number_pairs: tuple[int, int], action: Callable[[int, int], None]):
        for left, right in number_pairs:
            action(left, right)

    pairs = [(1, 2), (3, 4), (5, 6), (100, 20)]

    pairs_action_execute(*pairs, action=summator)
    pairs_action_execute(*pairs, action=divider)


if __name__ == '__main__':
    send_like_argument()
