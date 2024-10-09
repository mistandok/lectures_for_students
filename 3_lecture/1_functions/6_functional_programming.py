from functools import reduce


def map_example():
    users = ["Anton", "Artem", "Victor", "Ilya", "Olya", "Nastya"]
    users = list(map(lambda name:  name.lower(), users))
    print("Функциональное программироване", users)

    users = [user.lower() for user in users]
    print("Аналог с comprehansion", users)


def reduce_example():
    users_balance = {
        "Anton": 100,
        "Nastya": 300,
        "Ivan": 200,
    }

    result = reduce(lambda cur_amount, next_amount: cur_amount + next_amount, users_balance.values(), 0)
    print("Функциональное программирование", result)

    result = sum([amount for amount in users_balance.values()])

    print("Аналог ", result)


def filter_example():
    users_balance = {
        "Anton": 100,
        "Nastya": 300,
        "Ivan": 200,
        "Nikolay": 150,
    }

    result = dict(filter(lambda info: info[1] > 100 and info[0].lower().startswith("n"), users_balance.items()))
    print("Функциональное программирование", result)

    result = {
        name: balance
        for name, balance in users_balance.items()
        if name.lower().startswith("n") and balance > 100
    }

    print("Аналог с comprehansion", result)


if __name__ == '__main__':
    filter_example()
