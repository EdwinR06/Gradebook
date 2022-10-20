from student import Student
from teacher import assignment_maker
from student import students1

res = input('Are you a teacher or student? \n[a] Teacher \n[b] Student \n')
if res == 'a':
    res_name = input("What is the student's name? \n")
    student = Student(res_name)
    assignment_maker(student)
if res == 'b':
    res_name = input("What is your name? \n")
    for i in students1.students:
        if res_name == i[0].name:
            print("{} has a {}% in class.".format(i[0].name, i[1]))

