import sys
from typing import Iterable


def even_numbers(numbers: Iterable[int]):
    for num in numbers:
        if num % 2 == 0:
            yield num


def list_even_numbers(numbers: Iterable[int]):
    return [num for num in numbers if num % 2 == 0]


if __name__ == "__main__":
    for num in even_numbers(range(10)):
        print(num)

    for num in list_even_numbers(range(10)):
        print(num)

    gen = even_numbers(range(10_000_000))
    print("size generator", sys.getsizeof(gen))

    numbers = list_even_numbers(range(10_000_000))
    print("size list", sys.getsizeof(numbers))
