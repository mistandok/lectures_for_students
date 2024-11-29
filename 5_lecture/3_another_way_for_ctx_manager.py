from contextlib import contextmanager


@contextmanager
def file_open(file_path: str, mode: str):
    file = None
    try:
        file = open(file_path, mode)
        yield file
    finally:
        if file is not None:
            file.close()


if __name__ == "__main__":
    with file_open("./ctx_file.txt", mode="w") as file:
        file.write("one more variant for contextmanager")
