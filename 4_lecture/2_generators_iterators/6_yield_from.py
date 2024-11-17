from typing import Iterable


def odd_numbers(numbers: Iterable[int]):
    for num in numbers:
        if num % 2 != 0:
            yield num


def even_numbers(numbers: Iterable[int]):
    for num in numbers:
        if num % 2 == 0:
            yield num

    yield from odd_numbers(numbers)


if __name__ == "__main__":
    for num in even_numbers(range(10)):
        print(num)
