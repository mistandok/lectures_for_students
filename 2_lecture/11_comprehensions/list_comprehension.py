if __name__ == '__main__':
    user_ids = [user_id for user_id in range(10)]
    print("user_ids:", user_ids)

    even_user_ids = [user_id for user_id in range(10) if user_id % 2 == 0]
    print("even_user_ids:", even_user_ids)

    users = {1: "Anton", 2: "Vitya", 3: "Dima"}
    formatted_users_id = [f"{key}_{value}" for key, value in users.items()]
    print("formatted_users_id:", formatted_users_id)
    