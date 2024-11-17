from typing import Iterable


def even_numbers(numbers: Iterable[int]):
    for num in numbers:
        if num % 2 == 0:
            yield num


if __name__ == "__main__":
    for num in even_numbers(range(100)):
        print(num)
