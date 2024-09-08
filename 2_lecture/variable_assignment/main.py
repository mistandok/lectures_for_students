# simple assignment
def simple():
    name = "Anton"
    age = 10

    print(name, age)


# assignment in one row
def in_a_row():
    name, age = "Anton", 10

    print(name, age)


# swap variables
def swap():
    name = "Anton"
    age = 10

    name, age = age, name

    print(name, age)


# unpacking from tuple
def unpacking_from_tuple():
    name, age = ("Anton", 10)

    print(name, age)


# unpacking from list
def unpacking_from_list():
    name, age = ["Anton", 10]

    print(name, age)

    name_1, name_2, name_3, name_4 = ["Anton", "Ivan", "Dima", "Kolya"]

    print(name_1, name_2, name_3, name_4)


# hard unpacking from list
def hard_unpacking_from_list():
    first, *_, last = ["Anton", "Ivan", "Dima", "Daria", "Katya", "Kolya"]

    print(first, last)

    # hard unpacking from list
    first, second, *_, last = ["Anton", "Ivan", "Dima", "Daria", "Katya", "Kolya"]

    print(first, second, last)

    # hard unpacking from list
    _, *meaningful_names, _ = ["Anton", "Ivan", "Dima", "Daria", "Katya", "Kolya"]

    print(meaningful_names)

    # hard unpacking from list
    *names, _, _, _, _, last_name = ["Anton", "Ivan", "Dima", "Daria", "Katya", "Kolya"]

    print(names, last_name)

    # hard unpacking from list
    _, _, _, _, _, _, *names = ["Anton", "Ivan", "Dima", "Daria", "Katya", "Kolya"]

    print(names)


if __name__ == '__main__':
    simple()
    in_a_row()
    swap()
    unpacking_from_tuple()
    unpacking_from_list()
    hard_unpacking_from_list()
