import random
import time

from decorators.timer import timer

from utils.strings import random_string


def func_with_random_latency() -> int:
    time.sleep(random.randint(1, 3))
    return random.randint(1, 100500)


func_with_random_latency = timer(func_with_random_latency)


def update_text(text: str) -> str:
    time.sleep(random.randint(1, 3))
    return text.lower().capitalize()


update_text = timer(update_text)


def call_decorated_functions():
    for _ in range(3):
        result = func_with_random_latency()
        print("Результат работы:", result)

    print("\n------------------\n")

    for _ in range(3):
        result = update_text(" ".join([random_string(5).upper() for _ in range(4)]))
        print("Результат работы:", result)


if __name__ == '__main__':
    call_decorated_functions()
