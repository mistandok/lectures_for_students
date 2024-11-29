class FileCtxManager:
    def __init__(self, file_path: str, mode: str) -> None:
        self._file_path = file_path
        self._mode = mode
        self._file = None

    def __enter__(self):
        self._file = open(self._file_path, self._mode)
        return self._file

    def __exit__(self, type, value, traceback):
        print("type is", type)
        print("value is", value)
        print("traceback is", traceback)

        if self._file is not None:
            print("close file")
            self._file.close()

        # return True # если возвращаем True - то ошибка не выбрасывается в основном коде приложения
        return False  # если возвращаем False - то ошибка выбрасывается в основном коде приложения


if __name__ == "__main__":
    with FileCtxManager("./ctx_file.txt", mode="w") as file:
        file.write("our context manager is work")
