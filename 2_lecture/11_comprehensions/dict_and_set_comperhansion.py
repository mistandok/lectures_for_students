from itertools import zip_longest
from pprint import pprint

from utils.strings import random_string


def comprehension_example():
    user_ids = list(range(10))
    user_names = [random_string(10) for _ in range(10)]

    users_info = {user_id: user_name for user_id, user_name in zip(user_ids, user_names)}
    print("users_info")
    pprint(users_info, width=1)

    user_names = user_names[:-2]
    users_info = {user_id: user_name for user_id, user_name in zip(user_ids, user_names)}
    print("users_info")
    pprint(users_info, width=1)

    users_info = {user_id: user_name for user_id, user_name in zip_longest(user_ids, user_names)}
    print("users_info")
    pprint(users_info, width=1)


if __name__ == '__main__':
    comprehension_example()
