from student import Student
from teacher import assignment_maker
from student import students1


def login():
    res = input('Are you a teacher or student? \n[a] Teacher \n[b] Student \n')
    if res == 'a':
        res_name = input("What is the student's name? \n")
        in_students = False
        for i in students1.students:
            if res_name == i[0].name:
                in_students = True
                assignment_maker(i[0])

        if (in_students == False):
            student = Student(res_name)
            assignment_maker(student)

    elif res == 'b':
        res_name = input("What is your name? \n")
        in_students = False
        for i in students1.students:
            if res_name == i[0].name:
                in_students = True
                res_choice = input("Would you like to check your final grade or an assignment grade?\n[a] Final Grade \n[b] Assignment Grade \n")
                if res_choice == 'a':
                    if i[1] == -1:
                        print("{} has no grades in the class.".format(i[0].name))
                    if i[1] > -1:
                        print("{} has a {}% in class.".format(i[0].name, i[1]))
                elif res_choice == 'b':
                    res_assignment = input("Which assignment?\n")
                    for j in i[0].assignments.assignment_list:
                        if j[0] == res_assignment:
                            print("{} got a {}% on {}.".format(i[0].name, j[1][0]/j[1][1]*100, j[0]))

        if (in_students == False):
            print("Student does not exist.")

    else:
        print("Invalid input")
        login()



login()