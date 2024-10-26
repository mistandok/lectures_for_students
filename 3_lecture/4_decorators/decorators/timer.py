import time
from functools import wraps
from typing import Callable


def timer[T](func: Callable[..., T]) -> Callable[..., Callable[..., T]]:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable[[...], T]:
        print("Начали выполнение функции")
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"На выполнение функции потребовалось {time.time() - start_time} времени")
        return result

    return wrapper
