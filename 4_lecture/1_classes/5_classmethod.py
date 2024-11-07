from __future__ import annotations


class User:
    _users: list[User] = []

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self._users.append(self)

    @classmethod
    def from_str(cls, user_info: str) -> User:
        try:
            name, age = user_info.split("-")
            return cls(name, int(age))
        except ValueError:
            raise ValueError("incorrect user_info. correct template 'name-15'")

    @classmethod
    def count_users(cls):
        return len(cls._users)

    @classmethod
    def the_oldes_user(cls) -> User | None:
        min_age = 0
        target_user = None
        for user in cls._users:
            if user.age > min_age:
                target_user = user

        return target_user

    def __str__(self):
        return f"User {self.name} {self.age}"


if __name__ == "__main__":
    anton = User("anton", 15)
    nastya = User.from_str("nastya-20")
    print(anton)
    print(nastya)

    try:
        error_user = User.from_str("faf")
    except Exception:
        print("can't create user")

    print(f"count users: {User.count_users()}")
    print(f"the oldes user: {User.the_oldes_user()}")
