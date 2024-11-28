"""
Агрегация - это специализированная разновидность ассоциации, которая
описывает отношение один ко многим, многие ко многим, часть-целое между несколькими объектами.
Обычно при агрегации один объект содержит другие обхекты, то есть выступает контейнером или коллекцией. Компоненты вполне могут 
существовать отдельно от контейнера.
Жизненные циклы объектов не зависят друг от друга.
"""


class Book:
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author


class Library:
    def __init__(self):
        self._books: list[Book] = []

    def add_books(self, *books: Book):
        self._books.extend(books)


if __name__ == "__main__":
    book_1 = Book("Преступление и наказание", "Достоевский")
    book_2 = Book("Лабиритны Ехо", "Макс Фрай")

    library = Library()

    library.add_books(book_1, book_2)
