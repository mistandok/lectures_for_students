def standard_logic_operation():
    user_ids = [1, 2, 3]
    name = "Anton"
    user_id = 1
    users_name = {
        1: "Anton",
        2: "Ivan",
    }

    print("list compare", bool(user_ids))
    print("string compare", bool(name))
    print("numbers compare", bool(user_id))
    print("hash map compare", bool(users_name))

    user_ids = []
    name = ""
    user_id = 0
    users_name = {}

    print("list compare", bool(user_ids))
    print("string compare", bool(name))
    print("numbers compare", bool(user_id))
    print("hash map compare", bool(users_name))


def is_user_exists(user_id: int):
    if user_id:
        return True

    return False


def int_example():
    print("Isinstance int for true", isinstance(True, int))
    print("Isinstance int false", isinstance(False, int))
    print("Issubclass for int", issubclass(bool, int))
    print("Compare true with 1", True == 1)
    print("Compare true with 15", True == 15)
    print("Compare true with 0", True == 0)
    print("Compare false with 1", False == 1)
    print("Compare false with 0", False == 0)


if __name__ == "__main__":
    standard_logic_operation()
    print(is_user_exists(1))
    print(is_user_exists(0))  # be careful with int values
    int_example()
