def range_example():
    print("simple range")
    for idx in range(10):
        print(idx, end=" ")
    print()
    print("with step range")
    for idx in range(0, 10, 2):
        print(idx, end=" ")
    print()
    print("reversed step range")
    for idx in range(10, 0, -1):
        print(idx, end=" ")


def range_for_iterable_objects():
    sentence = "hello world, my name is Anton ぁ"
    b_sentence = b"hello world, my name is Anton"
    encoded_sentence = sentence.encode(encoding="utf-8")
    array = [1, 2, 3, 4, 5]
    hash_map = {1: "anton", 2: "ivan", 3: "kolya"}
    set_users = {"anton", "ivan", "kolya"}

    iterable_objects = [sentence, b_sentence, encoded_sentence, array, hash_map, set_users]

    for obj in iterable_objects:
        print(f"\nExample for iterable object {type(obj)}")
        for element in obj:
            print(element, end=" ")


def enumerate_example():
    array = [1, 2, 3, 4, 5]
    for idx, element in enumerate(array):
        print(idx, element, end=";")

    print()

    array = [1, 2, 3, 4, 5]
    for idx, element in enumerate(array, start=1):
        print(idx, element, end=";")


def for_else_example():
    info = ["good data", "good data", "critical error in data", "good data"]
    idx = 0
    for idx, data in enumerate(info):
        if data == "critical error in data":
            break
        # some operations with data...
    else:
        print("all data was processed")

    print(f"We are processed only {idx} data from {len(info)}")


if __name__ == '__main__':
    for_else_example()
