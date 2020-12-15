class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Hello, my name is {self.name} and im {self.age}'


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        # super(Student, self).__init__(name, age)
        # Person.__init__(self, name, age)
        self.grade = grade

    def __repr__(self):
        return f'{super().__repr__()} Im a {self.__class__.__name__} and my grade is {self.grade}'


class Worker(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def __repr__(self):
        return f'{super().__repr__()} Im a {self.__class__.__name__} and my salary is {self.salary}'


person = Person('Bebe Ivan', 12)
student = Student('Bebe Ivan', 12, 6)
worker = Worker('Tati Ivan', 24, 600)

print(person)
print(student)
print(worker)
print(Worker.mro())
# MRO -> в какъв ред се изпълнява кода
