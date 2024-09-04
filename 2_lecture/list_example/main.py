import time
from typing import TypeVar

T = TypeVar('T')


def assignment():
    names = ["Anton", "Kolya", "Dima", "Ivan"]
    age = list((30, 20, 10, 15))
    symbol_codes = list("abcd")

    print(names, age, symbol_codes)


def safely_indexing(obj: list[T], idx: int) -> T:
    try:
        return obj[idx]
    except IndexError as e:
        print(e, end="; ")
        return None


def indexing():
    names = ["Anton", "Kolya", "Dima", "Ivan"]
    print(names[0])
    print(names[1])
    print(names[2])
    print(names[3])
    print(safely_indexing(names, 4))


def reverse_indexing():
    names = ["Anton", "Kolya", "Dima", "Ivan"]
    print(names[-1])
    print(names[-2])
    print(names[-3])
    print(names[-4])
    print(safely_indexing(names, -5))


def slice_example():
    names = ["Anton", "Kolya", "Dima", "Ivan", "Petr", "Slava"]
    print("All names", names[:])  # for create list copy
    print("3 names", names[:3])
    print("3 names", names[0:3])
    print("even names", names[::2])
    print("reverse names", names[::-1])  # for reverse list
    print("reverse even names", names[::-2])
    print("with border", names[1:3])
    print("interesting border", names[1:-1])


def naming_for_slice():
    names = ["Anton", "Kolya", "Dima", "Ivan", "Petr", "Slava"]
    even_elements = slice(0, len(names), 2)
    print("even names", names[even_elements])


def interesting_example():
    names = ["Anton", "Kolya", "Dima", "Ivan", "Petr", "Slava"]
    another_names = names

    print("names", names)
    print("another names", another_names)

    names[0] = "Victor"
    print("names", names)
    print("another names", another_names)

    print("names id", id(names))
    print("another_names id", id(another_names))
    print("names is another_names", names is another_names)


def pow_elements(elements: list[int]):
    for idx, element in enumerate(elements):
        elements[idx] = element ** 2


def operations():
    names = ["Anton", "Kolya", "Dima", "Ivan", "Petr", "Slava"]
    another_names = ["Dima", "Svetlana"]

    print("concatenate +", names + another_names)  # return new list
    print("concatenate extend", names.extend(another_names))  # return None
    print("concatenate extend", names)  # source names was changed

    names.append("new_name")
    print("with new element", names)  # source names was changed

    names.pop(-1)
    print("extract last element", names)

    names.pop(0)
    print("extract first element", names)

    big_array = [1 for _ in range(100_000_000)]

    start = time.time()
    big_array.pop(-1)
    print("Time for pop last element: ", time.time() - start)

    big_array = [1 for _ in range(100_000_000)]

    start = time.time()
    big_array.pop(0)
    print("Time for pop last element: ", time.time() - start)

    names.insert(1, "Anton")
    print("insert after 0 element: ", names)


if __name__ == '__main__':
    operations()
