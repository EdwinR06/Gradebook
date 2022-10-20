class Students:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append([student, student.assignments.final_grade()])

class Student:
    def __init__(self, name):
        self.name = name
        self.assignments = Assignments()


class Assignments:
    def __init__(self):
        self.assignment_list = []

    def make_assignment(self, name, earned_grade, total_grade):
        self.assignment_list.append([ name, [earned_grade, total_grade]])
    
    def final_grade(self):
        for i in self.assignment_list:
            grade = i[1][0] / i[1][1] * 100
        return grade

bob = Student('Bob')
bob.assignments.make_assignment('test 1', 100, 90)
bob.assignments.make_assignment('test 2', 100, 100)

students = Students()
students.add_student(bob)