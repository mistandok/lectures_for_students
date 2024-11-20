def look_for_order_first_exception():
    try:
        _ = 10 / 0
    except Exception:
        print("Отлоивили исключение, которое идет выше в объявлении")
    except ZeroDivisionError:
        print("Сюда не попадем")


def look_for_order_first_zero(with_another_error: bool = False):
    try:
        if with_another_error:
            my_list = []
            _ = my_list[12]
        else:
            _ = 10 / 0
    except ZeroDivisionError:
        print("Отлоивили исключение, которое идет выше в объявлении")
    except Exception:
        print("Попадем только в том случае, если выше не поймали конкретные ошибки")


def look_for_order_multiexcept(with_another_error: bool = False):
    try:
        if with_another_error:
            my_list = []
            _ = my_list[12]
        else:
            _ = 10 / 0
    except (ZeroDivisionError, IndexError) as err:
        print("Отлоивили исключение, которое идет выше в объявлении")
        print(err)
    except Exception:
        print("Попадем только в том случае, если выше не поймали конкретные ошибки")


if __name__ == "__main__":
    look_for_order_multiexcept(with_another_error=False)
