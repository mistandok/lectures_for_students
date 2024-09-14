import time


def visual_demonstration():
    list_user_ids = []
    set_user_ids = set()
    for idx in range(10_000_000):
        list_user_ids.append(idx)
        set_user_ids.add(idx)

    # searched_id = 1
    searched_id = 9_999_999

    start = time.time()
    print(searched_id in list_user_ids)
    print("result time:", time.time() - start)

    start = time.time()
    print(searched_id in set_user_ids)
    print("result time:", time.time() - start)

    # start = time.time()
    # for idx in range(10_000_000):
    #     find = idx in list_user_ids
    # print("result time:", time.time() - start)

    # start = time.time()
    # for idx in range(10_000_000):
    #     find = idx in set_user_ids
    # print("result time:", time.time() - start)


def iterable_object():
    set_user_ids = {1, 2, 3, 4, 5, 6, 7}
    print(set_user_ids)

    for user_id in set_user_ids:
        print(user_id)


def sorting():
    set_user_ids = {1, 2, 3, 4, 5, 6, 7}
    print(set_user_ids)

    sorted_set = sorted(set_user_ids, reverse=True)
    print(sorted_set)


if __name__ == '__main__':
    sorting()
