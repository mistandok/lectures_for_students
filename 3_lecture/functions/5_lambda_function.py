def example():
    square = lambda x: x**2  # noqa: E731

    print(square(3))


if __name__ == '__main__':
    example()
