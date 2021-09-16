import datetime
from models import *


def greetings():

    print('Welcome to our database!')
    return True


def selection_check(answer, key, qty):

    try:
        if (int(answer) > 0) and (int(answer) < qty + 1):
            answer = int(answer)
            key = False
        else:
            print('Incorrect input, try again')
    except ValueError:
        print('Incorrect input, try again')
    return answer, key


def choice(request, qty):
    key = True
    answer = ''

    while key:
        print(request)
        answer = input('Your choice: ')
        answer, key = selection_check(answer, key, qty)
    return answer


def action_choice():
    request = '\nPlease select the function you want to perform:\n1. View data\n2. Adding data\n3. Change data\n' \
              '4. Delete data'
    return choice(request, 4)


def table_choice():
    request = '\nPlease select table:\n1. Groups\n2. Students\n3. Teachers\n4. Subjects\n5. Pass Cards'
    return choice(request, 5)


def draw_table(columns, model):
    head = ''
    summa = 0

    for i in columns:
        head += str(i.ljust(columns[i]))
        summa += columns[i]
    print(head)
    print('-' * (summa-2))

    all_table = model[0].select()
    model = model[1:]

    for rows in all_table:
        body = ''

        for cols, width in zip(model, columns):

            if cols == 'subject':
                val = getattr(getattr(rows, cols), 'title')

            elif cols == 'headman':
                if getattr(rows, cols):
                    val = 'Headman'
                else:
                    val = ' '

            elif cols == 'headman_name':
                val = getattr(getattr(rows, cols), 'full_name')

            elif cols == 'curator':
                val = getattr(getattr(rows, cols), 'full_name')

            elif cols == 'group':
                val = getattr(getattr(rows, cols), 'title')

            elif cols == 'student':
                val = getattr(getattr(rows, cols), 'full_name')

            else:
                val = getattr(rows, cols)
            body += str(val).ljust(columns[width])
        print(body)


def subject_group():
    print('\nList of subjects by group')

    model = [GroupSubjects, 'group', 'subject']
    columns = {'Group': 60, 'Subject': 52}
    draw_table(columns, model)


def student_group():
    print('\nList of students by group')

    model = [StudentGroup, 'group', 'student']
    columns = {'Group': 60, 'Student': 40}
    draw_table(columns, model)


def student_subject():
    print('\nList of additional subjects for each student')

    model = [StudentSubject, 'student', 'subject']
    columns = {'Student': 40, 'Subject': 52}
    draw_table(columns, model)


def view(table):

    print('\nYour table:')

    if table == 1:
        model = [Group, 'id', 'title', 'headman_name', 'curator', 'end_date']
        columns = {'ID': 6, 'Title': 60, 'Headman': 40, 'Curator': 40, 'End Date': 16}
        draw_table(columns, model)

        request = '\nWould you like to see additional data?\n1. View a list of students in groups\n' \
                  '2. View the main subjects of groups\n3. I don’t want to watch additional data'
        answer = choice(request, 3)

        if answer == 1:
            student_group()

            request = '\nWould you like to see additional data?\n1. View the main subjects of this group\n' \
                      '2. I don’t want to watch additional data'
            answer = choice(request, 2)

            if answer == 1:
                subject_group()

                request = '\n1. To the main menu'
                answer = choice(request, 1)

                if answer == 1:
                    print('glavv')

            elif answer == 2:
                print('glavv')

        elif answer == 2:
            subject_group()

            request = '\nWould you like to see additional data?\n1. View a list of students in groups\n' \
                      '2. I don’t want to watch additional data'
            answer = choice(request, 2)

            if answer == 1:
                student_group()

                request = '\n1. To the main menu'
                answer = choice(request, 1)

                if answer == 1:
                    print('glavv')

            elif answer == 2:
                print('glavv')

        elif answer == 3:
            print('glavv')

    if table == 2:
        model = [Student, 'id', 'full_name', 'birth_date', 'headman', 'rating']
        columns = {'ID': 6, 'Full Name': 40, 'Birth Date': 16, 'Headman': 11, 'Rating': 8}
        draw_table(columns, model)

        request = '\nWould you like to see additional data?\n1. View a list of additional subjects for each student\n' \
                  '2. I don’t want to watch additional data'
        answer = choice(request, 2)

        if answer == 1:
            student_subject()

            request = '\n1. To the main menu'
            answer = choice(request, 1)

            if answer == 1:
                print('glavv')

        elif answer == 2:
            print('glavv')

    if table == 3:
        model = [Teacher, 'id', 'full_name', 'birth_date', 'subject']
        columns = {'ID': 6, 'Full Name': 40, 'Birth Date': 16, 'Subject Title': 52}
        draw_table(columns, model)

    if table == 4:
        model = [Subject, 'id', 'title']
        columns = {'ID': 6, 'Title': 52}
        draw_table(columns, model)

    if table == 5:
        model = [Human, 'id', 'full_name', 'birth_date']
        columns = {'ID': 6, 'Full Name': 40, 'Birth Date': 16}
        draw_table(columns, model)


def add(table):
    if table == 1:
        pass

    if table == 2:
        pass

    if table == 3:
        print('\nATTENTION: model Teacher has fields: Full Name, Date of Birth, ID of the taught Subject\n')
        full_name = input('Enter the full name of the Teacher: ')
        birth_date = int(input('Enter the Teacher date of birth in the format year/month/day: '))
        subject = int(input('Enter the id of the taught subject: '))
        Teacher.create(full_name=full_name, birth_date=birth_date, subject=subject).save()

    if table == 4:
        pass

    if table == 5:
        pass


def change(table):
    pass


def delete(table):
    pass


def redirect(action, table):
    if action == 1:
        view(table)

    elif action == 2:
        add(table)

    elif action == 3:
        change(table)

    elif action == 4:
        delete(table)


def main():

    greetings()
    redirect(action_choice(), table_choice())


main()
