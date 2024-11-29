import sqlite3
from contextlib import contextmanager
from typing import Generator


def create_table(con: sqlite3.Connection):
    cursor = con.cursor()
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
    con.commit()


def insert_data(con: sqlite3.Connection):
    cursor = con.cursor()
    cursor.execute(
        """
        insert into users (username, email, age)
        values
            ('anton', 'email@yandex.ru', 13)
    """
    )
    con.commit()


def select_data(con: sqlite3.Connection):
    cursor = con.cursor()
    cursor.execute(
        """
        select id, username, email, age from users
    """
    )
    users = cursor.fetchall()

    for user in users:
        print(user)


def casual_variant():
    connection = None
    try:
        connection = sqlite3.connect("database.db")
        create_table(connection)
        insert_data(connection)
        select_data(connection)
    finally:
        if connection is not None:
            connection.close()


@contextmanager
def sqlite_connection(db_name: str) -> Generator[sqlite3.Connection, None, None]:
    con = None
    try:
        con = sqlite3.connect(db_name)
        yield con
    finally:
        if con is not None:
            con.close()


def modern_variant():
    with sqlite_connection("database.db") as con:
        create_table(con)
        insert_data(con)
        select_data(con)


if __name__ == "__main__":
    modern_variant()
