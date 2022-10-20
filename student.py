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

        self.counter = 0

    def make_assignment(self, name, earned_grade, total_grade):
        self.assignment_list.append([ name, [earned_grade, total_grade] ])
        self.counter += 1
    
    def final_grade(self):
        grade = 0
        total = 0
        if self.counter >= 1:
            for i in self.assignment_list:
                grade += i[1][0] / i[1][1] * 100
                total += i[1][1]
        return grade / total * 100

bob = Student('Bob')
bob.assignments.make_assignment('test 1', 90, 100)
bob.assignments.make_assignment('test 2', 100, 100)

students1 = Students()
students1.add_student(bob)