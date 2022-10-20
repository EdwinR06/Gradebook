import student



def assignment_maker(student):
    res = input('Would you like to add an assignment? \n[a] Yes \n[b] No \n')
    if res == 'a':
        res1 = (input('What is the name of this assignment?\n')).capitalize()
        res2 = float(input('Available Points: '))
        res3 = float(input('Earned Points: '))
        student.assignments.make_assignment(res1, res3, res2)
        assignment_maker(student)
    else:
        print("{} has a {}% in class.".format(student.name, student.assignments.final_grade()))