def foo(with_error: bool = False):
    try:
        print("Блок выполнения кода")
        if with_error:
            raise ValueError("Я сам выбросил ошибку")
        print("Блок выполнения кода после потенциальной ошибки")
    except Exception:
        print("Попадем, если поймали ошибку")
    else:
        print("Попадем, если успешно отработал блок выполнения кода")
    finally:
        print("Попадем в любом случае")


if __name__ == "__main__":
    foo()
