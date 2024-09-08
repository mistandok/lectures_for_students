from typing import TypeVar

T = TypeVar("T")


class StackIsEmptyError(Exception):
    def __init__(self):
        super().__init__("stack is empty")


class Stack:
    def __init__(self):
        self._data: list[T] = []

    def push(self, element: T):
        self._data.append(element)

    def pop(self) -> T:
        try:
            return self._data.pop(-1)
        except IndexError:
            raise StackIsEmptyError

    def is_empty(self) -> bool:
        return not bool(self._data)


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    while not stack.is_empty():
        print(stack.pop())

    try:
        stack.pop()
    except StackIsEmptyError as e:
        print(f"incorrect action: {e}")
