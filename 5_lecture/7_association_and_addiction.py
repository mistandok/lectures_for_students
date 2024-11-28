"""
Зависимость - базовая связь между классами, которая показывает, что один класс склоее всего придется менять, при изменении
названия или сигнаруты методов второго. Если использовать абстракции, а не конкретные классы, то зависимости можно избежать.

Ассоциация - это когда один объект взаимодействует с другим объектом. Строгий вариант зависимости,
при котором один объект всегда имеет доступ к объекту, с которым он взаимодействует. Пример - один класс имеет поле-ссылку на другой класс.
"""

from typing import Protocol


class Student:
    def __init__(self):
        self._brain = []

    def remember(self, information: dict):
        self._brain.append(information)


class Book:
    def data(self) -> dict:
        return {}


class Professor:
    def __init__(self):
        """Тут профессор ассоциирован со студентом.
        Профессор управляет жизненным циклом студента, любые изменения в методах студента приведут к изменениям в профессоре
        """
        self.student: Student = Student()

    def teach_via_book(self, book: Book):
        """Тут профессор зависит от книги, он принимает ее в качестве аргумента.
        Если у Book изменится метод data, или само название, то нам придется изменять код в профессоре.
        """
        self.student.remember(book.data())


class LearningMaterial(Protocol):
    def data(self) -> dict:
        raise NotImplementedError


class DoctorOfScience:
    def __init__(self):
        """Тут профессор ассоциирован со студентом.
        Профессор управляет жизненным циклом студента, любые изменения в методах студента приведут к изменениям в профессоре
        """
        self.student: Student = Student()

    def teach_via_learning_material(self, learning_material: LearningMaterial):
        """Тут доктор наук ассоциирован с интерфейсом LearningMaterial.
        Book сейчас подходит под этот интерфейс, если и может использоватьс в качестве учебных материалов.
        Да, если у Book изменится сигнатура метода, то наш класс DoctorOfScience никак не изменится, но Book действительно нельзя будет тут использовать.
        """
        self.student.remember(learning_material.data())
