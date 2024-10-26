def visualiser():
    print("Зашел в visualiser")

    def decorator(func):
        print("Зашел в decorator")

        def wrapper(*args, **kwargs):
            print("Зашел во wrapper")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@visualiser()
def function():
    return 0


# function = visualiser()(function)
