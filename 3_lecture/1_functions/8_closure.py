"""Замыкания.

Это функция, назовем ее f, с расширенной областью видимости, которая охватывает переменные,
на которые есть ссылки в теле f, но которые не являются ни глобальными, ни локальными переменными f.
Такие переменные должны происходить из локальной области видимости врешней функции, объемлющей f.

Это функции, которые ссылаются на переменные из объемлющей области видимости и используют их в своих рассчетах.
Получается, что внешние функции хранят состояние для внутренней функции f, а она его использует в своих целях.
"""
from enum import Enum
from functools import partial
from typing import Callable


def make_averager() -> Callable[[int], float]:
    series = []  # локальная переменная для make_averager

    def averager(element: int) -> float:
        series.append(element)  # ссылаемся на переменную из enclosing и используем ее в своих целях
        return sum(series) / len(series)

    return averager  # возвращаем функцию, в которой есть замыкание на series.


def example_make_averager():
    avg = make_averager()

    print(avg(10))
    print(avg(11))
    print(avg(15))


class AmountType(Enum):
    RUB = "rub"
    DOLLAR = "$"


def amount_formatter(amount_type: AmountType) -> Callable[[int], str]:
    def format_amount(amount: int) -> str:
        return f"{amount} {amount_type.value}"

    return format_amount


def example_amount_formatter():
    rub = amount_formatter(AmountType.RUB)
    dollar = amount_formatter(AmountType.DOLLAR)

    print(rub(100))
    print(dollar(200))


def example_with_partial():
    def format_amount(amount: int, amount_type: AmountType) -> str:
        return f"{amount} {amount_type.value}"

    rub = partial(format_amount, amount_type=AmountType.RUB)
    dollar = partial(format_amount, amount_type=AmountType.DOLLAR)

    print(rub(100))
    print(dollar(200))


if __name__ == '__main__':
    example_with_partial()
