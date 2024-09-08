import json
from collections import namedtuple
from pprint import pprint
from typing import TypeVar

UserInfo = namedtuple("UserInfo", "age skills")
UserID = TypeVar("UserID", bound=str)

def get_users_info() -> dict[str, int]:
    # Предположим, что тут запрос на сервис user_info_service
    with open("./jsons/age.json", mode="r") as f:
        data = json.load(f)
        return data


def get_users_skills() -> dict[str, list[str]]:
    # Предположим, что тут запрос на сервис user_skills_service
    with open("./jsons/skills.json", mode="r") as f:
        data = json.load(f)
        return data


def collect_users() -> dict[UserID, UserInfo]:
    user_info = get_users_info()
    user_skills = get_users_skills()

    users = {}
    for user_id, age in user_info.items():
        skills = user_skills.get(user_id)
        if skills is None:
            continue

        users[user_id] = UserInfo(age=age, skills=skills)

    return users


if __name__ == '__main__':
    users = collect_users()
    pprint(users, width=1)
