import datetime

from dateutil.relativedelta import relativedelta


def example():
    now = datetime.datetime(2024, 2, 1)

    next_month_timedelta = now + datetime.timedelta(days=30)
    next_month_relativdelta = now + relativedelta(months=1)

    print(next_month_timedelta)
    print(next_month_relativdelta)


if __name__ == '__main__':
    example()
