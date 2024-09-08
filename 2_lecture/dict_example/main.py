from pprint import pprint


def visual_demonstration():
    user_info = {
        "name": "Anton",
        "age": 30,
        "skills": ["go", "sql", "python"],
    }

    pprint(user_info, compact=False, width=1)

    name = user_info["name"]
    print("Name:", name)

    name = user_info.get("name")
    print("Name:", name)

    # unexpected key
    try:
        _ = user_info["unexpected"]
    except KeyError as e:
        print("error:", e)

    something = user_info.get("unexpected", "default value")
    print("something:", something)

    print("length:", len(user_info))


def iterable_object():
    user_info = {
        "name": "Anton",
        "age": 30,
        "skills": ["go", "sql", "python"],
    }

    for key in user_info.keys():
        print("key:", key)

    for key in user_info:
        print("key:", key)

    for key, value in user_info.items():
        print(f"{key}: {value}")


def sorting():
    user_info = {
        "name": "Anton",
        "age": 30,
        "skills": ["go", "sql", "python"],
    }

    result = sorted(user_info)
    print(result)

    class_scores = {
        "anton": 10,
        "dima": 5,
        "vitya": 40,
        "kolya": 30,
    }

    result = sorted(class_scores, key=lambda key: class_scores[key])
    print(result)


if __name__ == '__main__':
    sorting()
