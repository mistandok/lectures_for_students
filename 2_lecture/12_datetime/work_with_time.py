import datetime
import time


def time_example():
    now = time.time()
    print("С момента начала отсчета UTC прошло", now)


def modules_example():
    now_date = datetime.date.today()
    now_datetime = datetime.datetime.now()
    now_time = datetime.time()

    print("Date", now_date)
    print("Date and time", now_datetime)
    print("Time", now_time)


def setup_modules_example():
    print("Setup date", datetime.date(2022, 1, 1))
    print("Setup datetime", datetime.datetime(2022, 1, 1, 00, 00, 00, 00, datetime.UTC))

    date = datetime.date.today()
    set_time = datetime.time(00, 00, 00)
    print(
        "Combine results",
        datetime.datetime.combine(date, set_time),
        "\n",
        datetime.datetime.combine(date, set_time, datetime.UTC),
    )


def from_str_iso_format_example():
    print("Date", datetime.date.fromisoformat("2020-01-31"))
    print("Date and time", datetime.datetime.fromisoformat("2020-01-31 00:00:00"))


def from_str_custom_format():
    date_str = "01-31-2020 14:45:37+0000"
    format_str = "%m-%d-%Y %H:%M:%S%z"
    date = datetime.datetime.strptime(date_str, format_str)
    print("Date and time", date)


def operations_with_date():
    new_year = datetime.datetime(
        year=2025, month=1, day=1, hour=0, minute=0, microsecond=0, tzinfo=datetime.UTC
    )
    time_to_new_year = new_year - datetime.datetime.now(tz=datetime.UTC)
    print("Time to New Year", time_to_new_year)
    print("What is type?", type(time_to_new_year))

    print("\n-------Next week-------\n")
    now = datetime.datetime.now()
    one_week_delta = datetime.timedelta(days=7)

    for _ in range(4):
        now = now + one_week_delta
        print("Next week", now)
        print("Type", type(now))


if __name__ == "__main__":
    operations_with_date()
