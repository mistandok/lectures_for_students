from __future__ import annotations


class AppError(Exception):
    pass


class UserInputError(AppError):
    pass


def atoi(string: str) -> int:
    try:
        return int(string)
    except ValueError:
        raise UserInputError("вы ввели не число, попробуйте еще раз")


def main():
    while True:
        try:
            print("выбери команду")
            print("1 - деление 10 на заданное число\n")

            user_input = input("введи номер команды: ")

            command = atoi(user_input)

            if command != 1:
                raise UserInputError("вы ввели некорректную команду, попробуйте снова")

            user_input = input("введи число, на которое мы будем делить 10: ")

            number = atoi(user_input)

            try:
                print(10 / number)
            except ZeroDivisionError:
                raise UserInputError("вы пытаетесь делить на ноль, попробуйте еще раз")

        except AppError as e:
            print(f"{e}\n")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("что-то пошло не так, мы уже решаем проблему")
