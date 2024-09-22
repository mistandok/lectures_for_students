# pip install python-dateutil

"""Стандартный пакет datetime предоставляет абстрактрную сущность tzinfo, но не дает конкретные сущности для работы
с той или иной таймзоной. Для этого есть сторонний пакет python-dateutil"""
import datetime

from dateutil import tz


def add_timezone():
    now = datetime.datetime.now(tz=tz.tzlocal())
    print("Now in local TZ", now)

    london_tz = tz.gettz("Europe/London")
    now = datetime.datetime.now(tz=london_tz)
    print("Now in london TZ", now)
    
    now = datetime.datetime.now(tz=tz.tzutc())
    print("Now in UTC TZ", now)


if __name__ == '__main__':
    add_timezone()