class Man:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def info(self):
        self.say_hello()
        self.my_strength()

    def say_hello(self):
        print(f"hello, my name is {self.name}")

    def my_strength(self):
        print(f"my strength is {self.age * 0.5}")


class WeakMan(Man):
    def my_strength(self):
        print(f"my strength is {self.age * 0.2}")


class SuperMan(Man):
    def __init__(self, name: str, age: int, with_glasses: bool = True) -> None:
        super().__init__(name, age)
        self._with_glasses = with_glasses

    def toggle_glasses(self):
        self._with_glasses = not self._with_glasses

    def say_hello(self):
        if self._with_glasses:
            return super().say_hello()

        print("hello, my name is Super Man!")

    def my_strength(self):
        if self._with_glasses:
            return super().my_strength()

        print(f"my strength is {self.age * 1000}")


if __name__ == "__main__":
    anton = Man("anton", 20)
    igor = WeakMan("igor", 20)
    clark_kent = SuperMan("clark", 20)

    anton.info()
    print("--------")
    igor.info()
    print("--------")
    clark_kent.info()
    clark_kent.toggle_glasses()
    print("clark without glasses")
    clark_kent.info()
