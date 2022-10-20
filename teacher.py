import student



def assignment_maker(student):
    res = input('Would you like to add an assignment? \n[a] Yes \n[b] No \n')
    if res == 'a':
        res1 = (input('What is the name of this assignment?\n')).capitalize()
        res2 = float(input('Available Points: '))
        if res2 <= 0:
            print("Invalid response: please input a value greater than zero")
            res2 = float(input('Available Points: '))
        res3 = float(input('Earned Points: '))
        if res3 < 0:
            print("Invalid response: please input a value greater than or equal to zero")
            res3 = float(input('Earned Points: '))
        student.assignments.make_assignment(res1, res3, res2)
        assignment_maker(student)
    else:
        if student.assignments.final_grade() == - 1:
            print("{} has no grades in the class.".format(student.name))
        if student.assignments.final_grade() > -1:
            print("{} has a {}% in class.".format(student.name, student.assignments.final_grade()))