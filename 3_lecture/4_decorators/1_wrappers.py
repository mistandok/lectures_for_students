"""
Декоратор - это структурный паттерн проектирования, который позволяет добавлять поведение к классу или функции.
При этом код самих классов или функций остается без изменений.
"""
from typing import Callable

# Вспомним замыкание функций

def is_palindrome(text: str):
    formatted_text = "".join(ch for ch in text.lower() if ch.isalpha())
    return formatted_text == "".join(reversed(formatted_text))


def add(x: int, y: int) -> int:
    return x + y


def printer[T](
        text_before_action: str,
        text_after_action: str,
        action: Callable[[...], T],
        *args,
        **kwargs,
) -> T:
    print(text_before_action)
    result = action(*args, **kwargs)
    print(text_after_action)
    print("Результат работы: ", result)
    return result


def call_function_without_wrapper():
    sentence = "never odd or even"
    print("Проверяем, является ли текст палиндромом:", is_palindrome(sentence))
    print("Результат сложения двух чисел:", add(10, 15))


def call_function_with_wrapper():
    """Обернули наши функции принтером.

    В итоге выполнения мы получим результат работы наших функций и дополнительное поведение,
    но работаем мы уже с новой сущностью printer.
    При этом нам приходится посылать дополнительные параметры в не очень удобном формате:
    посылаем текст, посылаем саму функцию в качестве действия, посылаем параметры, которые надо передать в функцию.
    Можем ли как-то упросить этот формат?
    """
    sentence = "never odd or even"
    printer(
        "Проверим, является ли текст палиндромом",
        "Проверили, что текст является палиндромом",
        is_palindrome,
        sentence
    )

    print("\n-------------------\n")

    printer(
        "Сложим несколько чисел",
        "Сложили несколько чисел",
        add,
        1,
        y=2,
    )


def new_printer[T](
    text_before_action: str,
    text_after_action: str,
    action: Callable[[...], T]
) -> Callable[..., T]:
    def func(*args, **kwargs) -> T:
        print(text_before_action)
        result = action(*args, **kwargs)
        print(text_after_action)
        print("Результат работы: ", result)
        return result

    return func


def call_function_with_new_wrapper():
    """Создали new_printer. Использовали в замыкание и new_printer теперь возвращает другую функцию.

    Эта функция принимает параметры, которые должна была бы принять исходная функция.
    Далее мы создаем новые объекты:
    wrapped_is_palindrome, wrapped_add

    Они - это результат работы функции new_printer. То есть эти переменные ссылаются на функцию func,
    которая содержит в себе замыкание на переденной действие.
    Как мы можем заметить - мы посылаем в new_printer какие-то параметры,
    которые важны для дополнительного поведения и само действие.
    Можем ли мы изменить это поведение? Да, можем.
    """
    sentence = "never odd or even"
    wrapped_is_palindrome = new_printer(
        "Проверим, является ли текст палиндромом",
        "Проверили, что текст является палиндромом",
        is_palindrome,
    )

    print("Тип и значение:", type(wrapped_is_palindrome), wrapped_is_palindrome)

    wrapped_is_palindrome(sentence)

    print("\n-------------------\n")

    wrapped_add = new_printer(
        "Проверим, является ли текст палиндромом",
        "Проверили, что текст является палиндромом",
        add,
    )

    print("Тип и значение:", type(wrapped_add), wrapped_add)

    wrapped_add(10, 15)


def the_newest_printer[T](text_before_action: str, text_after_action: str) -> Callable[..., Callable[..., T]]:
    """Тут у нас двойное замыкание.

    Оно позволяет передавать действие\функцию в качестве отдельного аргумента возвращаемой функции.
    Эта концепция важна для изучения параметризированных декораторов. По сути мы с вами только что его написали.
    """
    def closure(func: Callable[..., T]) -> Callable[..., T]:
        def wrapped_func(*args, **kwargs) -> T:
            print(text_before_action)
            result = func(*args, **kwargs)
            print(text_after_action)
            print("Результат работы: ", result)
            return result

        return wrapped_func

    return closure


def call_function_with_the_newest_wrapper():
    sentence = "never odd or even"
    wrapped_is_palindrome = the_newest_printer(
        "Проверим, является ли текст палиндромом",
        "Проверили, что текст является палиндромом",
    )(is_palindrome)

    print("Тип и значение:", type(wrapped_is_palindrome), wrapped_is_palindrome)

    wrapped_is_palindrome(sentence)

    print("\n-------------------\n")

    wrapped_add = the_newest_printer(
        "Проверим, является ли текст палиндромом",
        "Проверили, что текст является палиндромом",
    )(add)

    print("Тип и значение:", type(wrapped_add), wrapped_add)

    wrapped_add(10, 15)


if __name__ == '__main__':
    call_function_with_the_newest_wrapper()
