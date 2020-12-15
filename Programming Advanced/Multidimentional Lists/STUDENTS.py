class Student:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

students =[Student(f'Student #{i}') for i in range(5)]
print(', '.join(str(s) for s in students))

