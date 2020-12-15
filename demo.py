from unittest import TestCase


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Hello I am {self.name} and i am {self.age} years old!'


class TestHello(TestCase):
    def test_init(self):
        person = Person('Anton', 19)
        self.assertEqual(person.name, 'Anton')
        self.assertEqual(person.age, 19)

    def test_repr(self):
        person = Person('Anton', 19)
        self.assertEqual(person.__repr__(), f'Hello I am {person.name} and i am {person.age} years old!')