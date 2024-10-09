from collections import namedtuple

UserInfo = namedtuple("UserInfo", ["id", "name", "age", "skills"])


def get_user_info(user_id: int) -> UserInfo:
    """Пример функции, которая принимает один аргумент и возвращает какое-то значение"""
    return UserInfo(id=user_id, name="Anton", age=20, skills=["go", "python"])


def foo(user_id: int, user_name: str = "Anton"):
    """Вызвать call_foo, показать разные способы вызова одной и той же функции"""
    return f'ID: {user_id}, Name: {user_name}'


def call_foo():
    print(foo(1), '\n')
    print(foo(2, "Victor"), '\n')
    print(foo(user_name="Anton", user_id=10), '\n')
    print(foo(user_id=10, user_name="Anton"), '\n')
    params = {"user_id": 10, "user_name": "Anton"}
    print(foo(**params), '\n')
    params = [1, "Anton"]
    print(foo(*params), '\n')


def foo_with_args_kwargs(*args, **kwargs):
    """Вызвать call_foo_with_args_kwargs, рассказать про args, kwargs"""
    print("Тип args:", type(args))
    print("Тип kwargs:", type(kwargs))

    for arg in args:
        print(f"arg: {arg}")

    for arg_name, arg_value in kwargs.items():
        print(f"arg_name: {arg_name}, arg_value: {arg_value}")

    print('\n-------------\n')


def call_foo_with_args_kwargs():
    foo_with_args_kwargs(1, 2, 3)
    foo_with_args_kwargs(1)
    foo_with_args_kwargs(a=1, b=2, c=3)
    foo_with_args_kwargs(1, 2, 3, a=1, b=2, c=3)
    position = [4, 5, 6]
    named = {"a": 7, "b": 8, "c": 9}
    foo_with_args_kwargs(*position, **named)


def only_named_argument(a, *, b):
    """В этой функции b - это чисто именованные аргумент. Мы не можем передать его позиционно, только по имени"""
    return a, b


def call_only_named_argument():
    print(only_named_argument(1, b=2))
    try:
        only_named_argument(1, 2)
    except TypeError as e:
        print("b - чисто именованные аргумент, нужно явно его передать.", e)


def only_position_argument(a, b, /, c, d):
    """Функция, в которой параметры нельзя передавать по имени. Их можно передавать только позиционно"""
    print(a, b, c, d)


def call_only_position_argument():
    try:
        only_position_argument(a=1, b=2, c=3, d=4)
    except TypeError as e:
        print("a и b - позиционные аргументы.", e)

    only_position_argument(1, 2, c=3, d=4)


def tag(name: str, *content: str, class_: None | str = None, **attrs: str) -> str:
    """Функция генерирует тэг HTML документа по переданным параметрам."""
    if class_ is not None:
        attrs['class'] = class_

    attr_pairs = (f'{attr}="{value}"' for attr, value in sorted(attrs.items()))
    attr_str = ' '.join(attr_pairs)

    if content:
        elements = (f'<{name} {attr_str}>{c}</{name}>' for c in content)
        return '\n'.join(elements)

    return f'<{name} {attr_str}/>'


def call_tag():
    """Абсолютно по разному можем вызывать функцию.

    Позиционные аргументы
    Именованные аргументы
    Позиционные и именованные аргументы
    """
    print(tag('br'), '\n')
    print(tag('p', 'hello'), '\n')
    print(tag('p', 'hello', 'world'), '\n')
    print(tag('p', 'hello', id="33"), '\n')
    print(tag('p', 'hello', 'world', class_='sidebar'), '\n')
    print(tag(content='testing', name='img'), '\n')

    my_tag = {
        'name': 'img',
        'title': 'Sunset Boulevard',
        'src': 'sunset.jpg',
        'class': 'framed'
    }
    print(tag(**my_tag), '\n')


if __name__ == '__main__':
    call_only_position_argument()
