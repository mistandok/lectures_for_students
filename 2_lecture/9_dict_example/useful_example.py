import json
from collections import namedtuple
from copy import copy, deepcopy  # noqa: F401
from pprint import pprint
from typing import TypeVar

UserInfo = namedtuple("UserInfo", "age skills")
UserID = TypeVar("UserID", bound=str)


def _get_users_info() -> dict[str, int]:
    # Предположим, что тут запрос на сервис user_info_service
    with open("./jsons/age.json", mode="r") as f:
        data = json.load(f)
        return data


def _get_users_skills() -> dict[str, list[str]]:
    # Предположим, что тут запрос на сервис user_skills_service
    with open("./jsons/skills.json", mode="r") as f:
        data = json.load(f)
        return data


def collect_users() -> dict[UserID, UserInfo]:
    user_info = _get_users_info()
    user_skills = _get_users_skills()

    users = {}
    for user_id, age in user_info.items():
        skills = user_skills.get(user_id)
        if skills is None:
            continue

        users[user_id] = UserInfo(age=age, skills=skills)

    return users


def merge_two_dicts():
    common_users = {
        "anton": 30,
        "dima": 30,
        "kolya": 40,
        "vitya": 40,
        "nastya": 20,
        "vika": 60,
    }

    vip_users = {
        "oleg": 40,
        "nastya": 30,
        "vika": 70,
    }

    new_users = {**common_users, **vip_users}
    print(new_users)

    common_users.update(vip_users)
    print(common_users)


def copy_dicts():
    user_info = {
        "name": "Vitya",
        "age": 20,
        "skills": ["go", "python"],
        "other_info": {
            "favorite_movie": "spider-man",
            "favorite_cuisine": "italian",
            "games_achievements_percents": {
                "cyberpunk": 50,
            }
        }
    }

    copy_user_info = copy(user_info)
    # copy_user_info = deepcopy(user_info)

    print("copied object")
    pprint(copy_user_info, width=1)
    print("deep change in copied object")
    copy_user_info["other_info"]["games_achievements_percents"]["cyberpunk"] = 100
    print("one level change")
    copy_user_info["age"] = 40

    print("results:")
    print("copy")
    pprint(copy_user_info, width=1)
    print("original")
    pprint(user_info, width=1)


if __name__ == '__main__':
    copy_dicts()
