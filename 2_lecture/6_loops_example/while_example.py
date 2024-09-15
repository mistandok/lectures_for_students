def simple_example():
    idx = 10
    while idx >= 0:
        print(idx)
        idx -= 1


def walrus_example_1():
    while not (name := input("Input name: ")):
        continue
    print(f"Name is: {name}")


def walrus_example_2():
    idx = 10
    while idx := idx - 1:
        print(idx)


def while_else_example():
    idx = 10
    while idx := idx - 1:
        if idx == 11:
            break
    else:
        print("finish without break")


def liveness_while_else_example():
    info = ["good data", "good data", "critical error in data", "good data"]
    idx = 0
    while (idx := idx + 1) <= len(info):
        data = info[idx]
        if data == "critical error in data":
            break
        # some operations with data...
    else:
        print("all data was processed")

    print(f"We are processed only {idx} data from {len(info)}")


def alternative_liveness_while_else_example():
    info = ["good data", "good data", "critical error in data", "good data"]
    idx = 0
    error_founded = False
    while (idx := idx + 1) <= len(info):
        data = info[idx]
        if data == "critical error in data":
            error_founded = True
            break
        # some operations with data...

    if error_founded:
        print(f"We are processed only {idx} data from {len(info)}")
    else:
        print("all data was processed")


if __name__ == '__main__':
    liveness_while_else_example()
    alternative_liveness_while_else_example()
