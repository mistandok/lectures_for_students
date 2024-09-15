def sort():
    user_ids = [1, 4, 5, 6, 8, 9, 15, 2, 3, 145, 17]
    copy_user_ids = user_ids[:]

    print("unsorted", user_ids)

    res = user_ids.sort()

    print("sorted: ", user_ids, "result: ", res)

    sorted_user_ids = sorted(copy_user_ids)
    print("sorted: ", sorted_user_ids, "copy_user_ids: ", copy_user_ids)


def sort_with_key():
    user_ids = [1, 4, 5, 6, 8, 9, 15, 2, 3, 145, 17]
    # copy_user_ids = user_ids[:]

    print("unsorted", user_ids)

    user_ids.sort(reverse=True)
    print(f"reversed sort: {user_ids}")

    sentence = "This is a test string from Andrew".split()
    sentence.sort(key=str.casefold)
    # sentence.sort()

    print("sorted insensitive case", sentence)

    student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
    ]

    sorted_students = sorted(student_tuples, key=lambda student: student[2])
    print("sorted students by age:", sorted_students)


if __name__ == '__main__':
    sort_with_key()


