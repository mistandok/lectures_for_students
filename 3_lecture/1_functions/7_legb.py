"""Правила разрешения имен - LEGB

1) Local - сначала смотрим в локальное области видимости
2) Enclosing - если не нашли в локальной, то в объемлющей
3) Global - если нет в объемлющей, то в глобальной
4) Builtin - если нет в глобальной, то в builtin

Если нет нигде - ошибка.
"""


name = "Anton"


def enclosing_name_printer():
    print("Берем глобальную переменную name:", name)
    second_name = "Artikov"

    def inner_name_printer():
        name = "Victor"
        print("Затенили глобальную переменную name локальной, берем ее:", name)
        print("Берем second_name из объемлющей области видимости:", second_name)
        print("Берем функцию set из builtin области видимости:", set.__doc__)

    inner_name_printer()


def enclosing_func():
    global name

    print("Изменили глобальную переменную из функции")
    name = "New Anton"

    print("Объявили локальную переменную second_name для enclosing_func")
    second_name = "Victor"

    def inner_func():
        nonlocal second_name

        print("Для inner_func задали second_name из объемлющей области видимости и изменили ее")
        second_name = "New Victor"

    inner_func()

    print("Новое значение second_name", second_name)


if __name__ == '__main__':
    enclosing_func()
    print("Новое значение global name", name)
