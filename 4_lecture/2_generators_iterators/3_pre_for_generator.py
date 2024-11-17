def generator():
    print("start generator and stop before first yield")
    print("------------------------")
    yield
    print("start after first yield")
    print("stop generator before second yield")
    print("------------------------")
    yield
    print("finish function")
    print("------------------------")


if __name__ == "__main__":
    print(generator)
    print(generator())

    gen = generator()

    try:
        while True:
            next(gen)
    except StopIteration:
        print("generator was finished")
