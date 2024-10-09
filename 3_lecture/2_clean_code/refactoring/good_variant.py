import dataclasses
import json
import os
from collections import namedtuple

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FILE_DIR = os.path.join(BASE_DIR, "refactoring", "data")
USER_FILES_DIR = [
    os.path.join(FILE_DIR, f"users_{idx}.json")
    for idx in range(1, 4, 1)
]
TARGET_FILE_DIR = os.path.join(FILE_DIR, "pairs.txt")


@dataclasses.dataclass
class User:
    id: int
    name: str
    skills: list[str]
    salary: int
    superhero: bool = False


Pair = namedtuple("Pair", ["first", "second"])


def save_user_pairs_from_files():
    users = get_users_from_many_files(*USER_FILES_DIR)
    update_users_info(users)
    pairs = make_pairs(users)
    save_pairs_to_file(pairs, TARGET_FILE_DIR)


def get_users_from_many_files(*files_dir: str) -> list[User]:
    users: list[User] = []
    for file_dir in files_dir:
        users.extend(get_users_from_file(file_dir))

    return users


def update_users_info(users: list[User]):
    for user in users:
        if is_user_superhero(user):
            user.superhero = True
            user.salary += 100


def make_pairs(users: list[User]) -> list[Pair]:
    pairs: list[Pair] = []
    for idx in range(0, len(users), 2):
        first_user = users[idx]
        second_user = users[idx+1] if idx+1 < len(users) else None
        pairs.append(Pair(first_user, second_user))

    return pairs


def save_pairs_to_file(pairs: list[Pair], target_file_dir: str):
    with open(target_file_dir, mode="w") as f:
        for pair in pairs:
            f.write(description_for_pair(pair))


def get_users_from_file(file_dir: str) -> list[User]:
    users: list[User] = []

    with open(file_dir) as f:
        raw_data: dict = json.load(f)

    raw_users = raw_data.get("users")
    for user in raw_users:
        users.append(User(**user))

    return users


def is_user_superhero(user: User):
    return len(user.skills) >= 2


def description_for_pair(pair: Pair) -> str:
    if is_full_pair(pair):
        return (f'User {pair.first.name} and {pair.second.name} in pair.'
                f'Count superhero: {count_superhero_in_pair(pair)}\n\n')

    return f'User {pair.first.name} solo. Count superhero: {count_superhero_in_pair(pair)}\n\n'


def is_full_pair(pair: Pair):
    return pair.first and pair.second


def count_superhero_in_pair(pair: Pair):
    if is_full_pair(pair):
        return sum([int(user.superhero) for user in pair])

    return int(pair.first.superhero)


if __name__ == '__main__':
    save_user_pairs_from_files()
