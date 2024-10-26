import random

from decorators.error_handler import error_handler


def fallback_calculate_area() -> int:
    return 0


@error_handler((Exception,), fallback=fallback_calculate_area)
def calculate_area() -> int:
    data = random.randint(1, 3)
    if data == 3:
        raise ValueError("ошибка в рассчетах")

    return random.randint(1, 100500)


if __name__ == '__main__':
    for _ in range(10):
        print(f"результат выполнения: {calculate_area()}")
        print("\n-------------------\n")
