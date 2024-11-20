import time
from random import randint


class AppError(Exception):
    """Базовый класс наших ошибок приложения"""


class UserNotFoundError(AppError):
    """Пользователя не существует"""


class EmptyUserBalanceError(AppError):
    """Пустой баланс пользователя"""


def action_without_err():
    print("action")


def action_with_app_err_1():
    raise UserNotFoundError("пользователя не существует")


def action_with_app_err_2():
    raise EmptyUserBalanceError("пустой баланс пользователя")


def action_with_unexpected_error():
    i = randint(1, 3)
    if i == 2:
        raise IndexError("пу-пу-пу, что-то делаем не так в приложении")


def main():
    actions = [
        action_without_err,
        action_with_app_err_1,
        action_with_app_err_2,
        action_with_unexpected_error,
    ]

    while True:
        for action in actions:
            try:
                action()
                time.sleep(1)
            except AppError as err:
                print(
                    "у нас бизнесовая ошибка, залогируем, но не будем останавливать приложение"
                )
                print(err)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("У нас произошла неожиданная ошибка, залогируем ее и завершим приложение")
