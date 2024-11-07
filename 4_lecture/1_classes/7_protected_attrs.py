"""Нужно понимать, что в питоне нет таких понятий как защищенные и приватные атрибуты.
Я использую эти понятия только для наглядности.
"""


class Test:
    def __init__(self) -> None:
        self.attr = "i'm open attr"
        self._attr = "i'm protected attr"
        self.__attr = "i'm private attr"


if __name__ == "__main__":
    t = Test()
    print(t.attr)
    print(t._attr)
    try:
        print(t.__attr)
    except AttributeError:
        print("we are catch AttributeError")
        print(t._Test__attr)
