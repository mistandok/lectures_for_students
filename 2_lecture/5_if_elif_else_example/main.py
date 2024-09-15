from types import NoneType


def examples():
    user_ids = [1, 2, 3]

    if user_ids:
        print("if statement is True")

    print("-------------")
    user_ids = []
    super_user = 123

    if user_ids:
        print("if statement is True")
    elif super_user:
        print("elif statement is True")
    else:
        print("all previous statement was false")

    print("-------------")
    user_ids = []
    super_user = None

    if user_ids:
        print("if statement is True")
    elif super_user:
        print("elif statement is True")
    else:
        print("all previous statement was false")


def what_is_none():
    # None - это буквально ничего, альтернатива null из sql, nil из go
    user_id = None
    if user_id is None:
        print("user is None", user_id)

    if user_id:
        print("user in bool format is False")

    print("bool for None", bool(None))

    types_for_check = (int, bool, str, NoneType)
    for t in types_for_check:
        print(f"isinstance None for {t}", isinstance(None, t))


def all_and_example():
    any_result = any([True, True, False, False])
    print("Any example", any_result)

    any_result = any([True, True, None, False])
    print("Any example  with None", any_result)

    any_result = any([[1, 2, 3], "hello", None, False])
    print("Any example  with diff types", any_result)

    any_result = any([[], "", None, False])
    print("Any example  with diff types", any_result)

    all_result = all([True, True, True, True])
    print("All example", all_result)

    all_result = all([True, True, None, False])
    print("All example  with None", all_result)

    all_result = all([[1, 2, 3], "hello", True, 1])
    print("All example  with diff types", all_result)


def hard_expressions_examples():
    user_id = 1
    user_bills = [1, 2, 3, 4]
    external_bills = [1, 2, 3, 4]
    is_external_user = True

    if (user_id or user_bills
            and (is_external_user or external_bills)):
        print("Success")


def and_or_example_for_simplify_code():
    user_age_from_api = 20
    user_age_from_database = None

    user_age = user_age_from_database or user_age_from_api
    print("User age", user_age)

    user_age_from_api = 20
    user_age_from_database = 25

    user_age = user_age_from_database or user_age_from_api
    print("User age", user_age)

    user_id = 1

    # first variant
    result = user_id and hard_operation_with_user(user_id)
    print("Hard operation result:", result)

    # second variant
    if user_id:
        result = hard_operation_with_user(user_id)
        print("Hard operation result:", result)

    user_id = None

    # first variant
    result = user_id and hard_operation_with_user(user_id)
    print("Hard operation result:", result)

    # second variant
    if user_id:
        result = hard_operation_with_user(user_id)
        print("Hard operation result:", result)


def hard_operation_with_user(user_id: int) -> str:
    if user_id is None:
        raise Exception("pu-pu-pu")

    return "operation complete"


def ternary_operator():
    score = 20
    result_by_score = "bad result" if score < 25 else "good result"
    print(result_by_score)


if __name__ == '__main__':
    examples()
    what_is_none()
    all_and_example()
    hard_expressions_examples()
    and_or_example_for_simplify_code()
