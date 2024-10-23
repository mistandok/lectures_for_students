from my_collections import MyDict
from my_collections.my_set import MySet

if __name__ == '__main__':
    my_dict = MyDict()
    my_dict.add("hello", 1)
    my_dict.add("hello", 1)
    my_dict.add("world", 2)
    my_dict.add("Anton", 3)

    my_dict.remove("world")

    print("Значение для ключа 'Anton':", my_dict.get("Anton"))
    print("Значение для ключа 'hello':", my_dict.get("hello"))
    print("Значение для ключа 'world':", my_dict.get("world"))

    my_set = MySet()

    my_set.insert("Anton")
    my_set.insert("Dima")
    my_set.insert("Nastya")

    my_set.remove("Dima")

    print("Элемент 'Anton' есть в множестве:", my_set.has("Anton"))
    print("Элемент 'Dima' есть в множестве:", my_set.has("Dima"))
    print("Элемент 'Nastya' есть в множестве:", my_set.has("Nastya"))


