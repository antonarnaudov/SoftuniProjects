class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        if len(self.students) < self.__students_count:
            self.students.append(name)
            self.students.append(grade)

    def get_average_grade(self):
        return round(sum(self.grades) / len(self.grades), 2) # round 1.00

    def __repr__(self):
        students_str = ', '.join(self.students)
        average = self.get_average_grade()
        return f"The students in {self.name}: {students_str}. Average grade: {average}"
