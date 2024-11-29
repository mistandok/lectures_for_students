import sqlite3
from contextlib import contextmanager
from typing import Generator


class UserNotFoundError(Exception):
    pass


@contextmanager
def sqlite_connection(db_name: str) -> Generator[sqlite3.Connection, None, None]:
    con = None
    try:
        con = sqlite3.connect(db_name)
        yield con
    finally:
        if con is not None:
            con.close()


class Storage:
    def __init__(self, con: sqlite3.Connection):
        self._con = con

    def create_table(self):
        cursor = self._con.cursor()
        cursor.execute(
            """
            create table if not exists users (
                id integer primary key autoincrement,
                username text not null,
                email text not null,
                age integer
            )
        """
        )
        self._con.commit()

    def insert_data(self):
        cursor = self._con.cursor()
        cursor.execute(
            """
            insert into users (username, email, age)
            values
                ('anton', 'email@yandex.ru', 13)
        """
        )
        self._con.commit()

    def select_data(self):
        cursor = self._con.cursor()
        cursor.execute(
            """
            select id, username, email, age from users
        """
        )
        users = cursor.fetchall()

        return users


class Application:
    def __init__(self, storage: Storage):
        self._storage = storage

    def get_last_user(self):
        users = self._storage.select_data()
        if users:
            return users[-1]

        raise UserNotFoundError()

    def create_user(self):
        self._storage.insert_data()

    def init_app(self):
        self._storage.create_table()

    def run(self):
        for _ in range(10):
            self.create_user()

        print(self.get_last_user())


if __name__ == "__main__":
    try:
        with sqlite_connection("database.db") as con:
            storage = Storage(con)
            app = Application(storage)
            app.init_app()
            app.run()
    except Exception:
        print("unexpected error, sorry")
