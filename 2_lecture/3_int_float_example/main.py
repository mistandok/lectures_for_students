def standard_int_operations():
    print("Operation +", 1 + 1)
    print("Operation *", 2 * 2)
    print("Operation //", 10 // 2)
    print("Operation /", 10 / 2, isinstance((10 / 2), float))
    print("Operation %", 7 % 3, 10 % 2)


def standard_float_operations():
    print("Operation +", 1.0 + 1.0)
    print("Operation *", 2.0 * 2.0)
    print("Operation //", 10.0 // 2.0, 10.0 // 2)
    print("Operation /", 10.0 / 2.0)
    print("Operation %", 7.0 % 3.0, 10.0 % 2.0)


if __name__ == "__main__":
    standard_int_operations()
    print()
    standard_float_operations()
