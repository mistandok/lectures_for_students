def generator_example():
    generator = (i for i in range(10))
    print(type(generator))


if __name__ == '__main__':
    generator_example()
