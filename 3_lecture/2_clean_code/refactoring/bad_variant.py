import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def execute():
    data = []
    with open(os.path.join(BASE_DIR, "refactoring", "data", "users_1.json")) as f:
        data.append(json.load(f))
    with open(os.path.join(BASE_DIR, "refactoring",  "data", "users_2.json")) as f:
        data.append(json.load(f))
    with open(os.path.join(BASE_DIR, "refactoring", "data", "users_3.json")) as f:
        data.append(json.load(f))
    r = []
    for element in data:
        us = element.get("users")
        for u in us:
            if len(u.get("skills")) >= 2:
                u["superhero"] = True
                u["salary"] += 100
            else:
                u["superhero"] = False
            r.append(u)
    p = []
    for i in range(0, len(r), 2):
        u = r[i]
        if i+1 < len(r):
            nu = r[i+1]
        else:
            nu = None
        p.append((u, nu))
    with open(os.path.join(BASE_DIR, "refactoring", "data", "pairs.txt"), mode="w") as f:
        for x in p:
            if x[0] and x[1]:
                f.write(f'User {x[0].get("name")} and {x[1].get("name")} in pair.'
                        f' Count superhero: {sum([1 if u.get("superhero") else 0 for u in x])}\n\n')
            else:
                f.write(f'User {x[0].get("name")} solo'
                        f' Count superhero: {1 if x[0].get("superhero") else 0}\n\n')


if __name__ == '__main__':
    execute()