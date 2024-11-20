def catch_root_exception():
    try:
        _ = 10 / 0
    except Exception as err:
        print("Отловили ошибку-родителя")
        print("Какой на самом деле тип у ошибки?", type(err))
        print("Текст ошибки:", err)
        print(
            "ZeroDivisionError это subclass для Exception:",
            issubclass(type(err), Exception),
        )


def catch_zero_exception():
    try:
        _ = 10 / 0
    except ZeroDivisionError as err:
        print("Какой на самом деле тип у ошибки?", type(err))
        print("Текст ошибки:", err)
        print(
            "ZeroDivisionError это subclass для Exception:",
            issubclass(type(err), Exception),
        )


if __name__ == "__main__":
    catch_root_exception()
    print("-----------------")
    catch_zero_exception()
