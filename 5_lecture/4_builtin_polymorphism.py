from typing import Iterable


def pow(obj: Iterable) -> list[int]:
    result = []
    for element in obj:
        result.append(element**2)

    return result


if __name__ == "__main__":
    objects: Iterable = [
        (1, 2, 3),
        [1, 2, 3],
        {1, 2, 3},
        {1: 1, 2: 2, 3: 3},
        (i for i in range(3)),
    ]

    for obj in objects:
        print(pow(obj))
        print(len(obj))
