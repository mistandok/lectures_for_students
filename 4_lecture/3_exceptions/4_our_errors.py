from dataclasses import dataclass
from http import HTTPStatus


class EmptyUserBalanceError(Exception):
    """Ошибки при отсутствии баланса у пользователя"""


@dataclass
class User:
    name: str
    balance: int


@dataclass
class Responce:
    user: User | None
    http_status: HTTPStatus


class UserClient:
    def __init__(
        self,
        result_status: HTTPStatus = HTTPStatus.OK,
        without_balance: bool = False,
        with_timeout: bool = False,
    ) -> None:
        self._result_status = result_status
        self._without_balance = without_balance
        self._witn_timeout = with_timeout

    def get(self) -> Responce:
        if self._witn_timeout:
            raise TimeoutError

        if self._result_status in (HTTPStatus.NOT_FOUND, HTTPStatus.UNAUTHORIZED):
            return Responce(None, self._result_status)

        return Responce(
            User("Anton", 0 if self._without_balance else 100), self._result_status
        )


def get_user_description(user_client: UserClient) -> str:
    try:
        responce = user_client.get()
    except TimeoutError:
        print("ручка начала таймаутить")
        return ""

    if responce.http_status == HTTPStatus.UNAUTHORIZED:
        print("у нас опять проблема с сертификатами")
        return ""

    if responce.http_status == HTTPStatus.NOT_FOUND:
        print("у нас хранятся кривые пользователи")
        return ""

    if responce.user is None:
        print("какая-то ошибка на стороне сервиса пользователей")
        return ""

    if responce.user.balance == 0:
        raise EmptyUserBalanceError(
            "какая-то ужасная ситуация, пользователь без баланса"
        )

    return f"Пользователь: {responce.user.name}, баланс: {responce.user.balance}"


if __name__ == "__main__":
    user_client = UserClient(without_balance=True)

    try:
        desc = get_user_description(user_client)
        print(desc)
    except EmptyUserBalanceError:
        print("залогировали информацию о том, что денег нет")
    except Exception:
        print("ловим то, что не обработали, чего не ожидали")
