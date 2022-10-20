class Student:
    def __init__(self, name):
        self.name = name
        self.assignments = Assignments()


class Assignments:
    def __init__(self):
        self.assignment_list = []

    def make_assignment(self, name, total_grade, earned_grade):
        self.assignment_list.append([ name, [earned_grade, total_grade]])
    
    def final_grade(self):
        for i in self.assignment_list:
            grade = i[1][0] / i[1][1] * 100
        print(grade)

bob = Student('Bob')
bob.assignments.make_assignment('test 1', 100, 90)
bob.assignments.make_assignment('test 2', 100, 100)
bob.assignments.final_grade()



#def create_student():
#    name = input('What is the students name?\n')
 #   assignment_points_earned = 0
  #  assignment_points_available = 0
   # res1 = (input('What is the name of this assignment?\n')).capitalize()
    #res2 = float(input('Available Points: '))
    #res3 = float(input('Earned Points: '))
    #assignment_points_available += res2
    #assignment_points_earned += res3
    #assignment_maker(name, assignment_points_earned, assignment_points_available)
        