def try_work_with_file():
    file = None
    try:
        file = open("./ctx_file.txt", mode="w")
        file.write("hello world")
    except Exception:
        print("something wrong")
    finally:
        if file is not None:
            file.close()


def try_work_with_file_with_ctx_manager():
    with open("./ctx_file.txt", mode="w") as file:
        file.write("hello world")


if __name__ == "__main__":
    try_work_with_file_with_ctx_manager()
