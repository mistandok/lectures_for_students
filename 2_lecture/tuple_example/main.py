from collections import namedtuple


def what_is_tuple():
    user = ("Anton", "Artikov", 30)
    print("user info:", user)


def with_mutable_elements():
    user = ("Anton", "Artikov", 30, ["go", "python", "sql", "docker"])
    name, *_, skills = user
    print("current tuple:", user)
    print(f"User: {name}. Skills: {skills}")

    skills.append("asyncio")
    print("current tuple:", user)
    print(f"User: {name}. Skills: {skills}")


def named_tuple():
    User = namedtuple("User", "name last_name age, skills")
    user = User(name="Anton", last_name="Artikov", age=30, skills=["go", "python", "sql", "docker"])
    print(f"User: {user.name}")

    print(f"User: {user[0]}")


if __name__ == '__main__':
    named_tuple()
