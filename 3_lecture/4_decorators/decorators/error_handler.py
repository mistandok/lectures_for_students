from functools import wraps
from typing import Callable


def error_handler[T](
        errors: tuple[type(Exception)],
        *,
        fallback: Callable[..., T] | None = None
) -> Callable[..., Callable[..., T]]:
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> T:
            try:
                return func(*args, **kwargs)
            except errors as e:
                print(f"error in time function: {e}")
                if fallback is not None:
                    print(f"сработал фоллбэк: {fallback.__name__}")
                    return fallback(*args, **kwargs)
                raise

        return wrapper

    return decorator
