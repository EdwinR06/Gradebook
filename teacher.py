import student

def assignment_maker(name, assignment_points_earned, assignment_points_available):
    res = input('Would you like to add another assignment? \n[a] Yes \n[b] No \n')
    if res == 'a':
        res1 = (input('What is the name of this assignment?\n')).capitalize()
        res2 = float(input('Available Points: '))
        res3 = float(input('Earned Points: '))
        assignment_points_available += res2
        assignment_points_earned += res3
        assignment_maker(name, assignment_points_earned, assignment_points_available)
    else:
        student1 = student.Student(name, assignment_points_available, assignment_points_earned)
        print('{} earned a {}% in this class.'.format((student1.name).capitalize(), str(student1.grade)))