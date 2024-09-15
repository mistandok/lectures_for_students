import random
import string


def strings():
    name = "Anton"
    second_name = "Artikov"
    full_name = name + second_name
    print("Full name", full_name)

    by_char = list(full_name)
    print("By char", by_char)

    sentence = "hello, my name is Anton"
    print("Capitalise", sentence.capitalize())
    print("Title", sentence.title())

    for char in sentence:
        print("char in for loop", char)

    print("startswith", sentence.startswith("hello"))
    print("endswith", sentence.endswith("hello"))

    print("split", sentence.split())
    print("join", "__".join(sentence.split()))
    print("replace", sentence.replace(" ", "__"))

    print("index", sentence[0])
    print("slice, even characters", sentence[::2])

    print("sorting", "".join(sorted(sentence)))
    print("sorting", sorted(sentence))
    print("reverse", sentence[::-1])

    print("title", sentence.title())
    print("capitalize", sentence.capitalize())


def unicode_example():
    japan_symbol = "ぁ"
    alphabet = {char: ord(char) for char in string.ascii_lowercase}
    alphabet_uppercase = {char: ord(char) for char in string.ascii_uppercase}
    print("Unicode alphabet lowercase", *alphabet.items(), sep=" ")
    print("Unicode alphabet uppercase", *alphabet_uppercase.items(), sep=" ")
    print()
    print("japan symbol", ord(japan_symbol))


def utf8_example():
    japan_symbol = "ぁ"
    alphabet = {char: (char.encode(), len(char.encode())) for char in string.ascii_lowercase}
    alphabet_uppercase = {char: (char.encode(), len(char.encode())) for char in string.ascii_uppercase}
    print("Unicode alphabet lowercase", *alphabet.items(), sep=" ")
    print("Unicode alphabet uppercase", *alphabet_uppercase.items(), sep=" ")
    print()
    print("japan symbol encoded len", japan_symbol.encode(encoding="utf-8"))
    print("japan symbol encoded len", len(japan_symbol.encode(encoding="utf-8")))
    print("japan symbol decoded", japan_symbol.encode(encoding="utf-8").decode(encoding="utf-8"))


def f_string_example():
    user_name = "amazing_user"
    print(f"User name: {user_name}")


def format_string_example():
    template = "Hello, {username}! Your age is {age}"
    age = random.randint(1, 60)
    username = "Anton"
    print(template.format(age=age, username=username))


if __name__ == "__main__":
    utf8_example()
