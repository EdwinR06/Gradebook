from teacher import assignment_maker

class Student:
    def __init__(self, name, assignment_points_available, assignment_points_earned):
        self.grade = (assignment_points_earned / assignment_points_available) * 100
        self.name = name


def create_student():
    name = input('What is the students name?\n')
    assignment_points_earned = 0
    assignment_points_available = 0
    res1 = (input('What is the name of this assignment?\n')).capitalize()
    res2 = float(input('Available Points: '))
    res3 = float(input('Earned Points: '))
    assignment_points_available += res2
    assignment_points_earned += res3
    assignment_maker(name, assignment_points_earned, assignment_points_available)
        