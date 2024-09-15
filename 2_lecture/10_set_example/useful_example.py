def search():
    user_ids = [1, 2, 3, 4, 5, 6, 7]
    seen_ids = [4, 5, 6]

    set_seen_ids = set(seen_ids)
    uniq_ids = []
    for user_id in user_ids:
        if user_id not in set_seen_ids:
            uniq_ids.append(user_id)

    print(uniq_ids)


def uniq_elements():
    many_elements_string = "fdfjdklfjlkdafjkldsfj kljkljklfjkfajkldfj lkdjf lkfjkldjf lkaf jdjf lafjkdaf"
    uniq_string = set(many_elements_string)
    # random order
    print("uniq symbols:", "".join(uniq_string))


if __name__ == '__main__':
    uniq_elements()
