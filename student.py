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
                grade += i[1][0] 
                total += i[1][1]

        if total == 0:
            return -1
        return grade / total * 100

bob = Student('Bob')
bob.assignments.make_assignment('test 1', 90, 100)
bob.assignments.make_assignment('test 2', 100, 100)

joe = Student('Joe')
joe.assignments.make_assignment('quiz 1', 20, 25)
joe.assignments.make_assignment('test 1', 100, 100)
joe.assignments.make_assignment('quiz 2', 25, 25)

mary = Student('Mary')
mary.assignments.make_assignment('quiz 1', 23, 25)
mary.assignments.make_assignment('test 1', 95, 100)
mary.assignments.make_assignment('quiz 2', 25, 25)

sue = Student('Sue')
sue.assignments.make_assignment('test 1', 95, 100)
sue.assignments.make_assignment('test 2', 96, 100)

students1 = Students()
students1.add_student(bob)
students1.add_student(joe)
students1.add_student(mary)
students1.add_student(sue)