from datetime import datetime
import time
import re
from models import *


def greetings():

    print('Welcome to our database!')


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


def validation(var_mean, count, message):

    if var_mean == 'int':
        while True:
            inp = input(message)
            if inp.isdigit() and count >= int(inp) > 0:
                res = int(inp)
                break
            else:
                print('Error, please enter a number from 1 to ' + str(count))
        return res

    elif var_mean == 'name' or var_mean == 'title':
        while True:
            inp = input(message)
            front = '^'
            back = '$'
            body = ''
            regular = ''
            for i in range(count):
                body += '\w+'
                if i+1 != count:
                    body += '\s'
            if var_mean == 'name':
                regular = front + body + back
            elif var_mean == 'title':
                regular = front + 'Departament\s[\w+\s]{,50}' + back
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if re.match(regular, inp):
                res = inp
                break
            else:
                if var_mean == 'name':
                    print('Error, please enter full name in three words (First Name, Father Name, Last Name) separated '
                          'by spaces')
                elif var_mean == 'title':
                    print('Error, enter a title of at least two and no more than fifty characters with the first word '
                          '"Department" separated by a spaces')
        return res

    elif var_mean == 'date':
        while True:
            inp = input(message)
            try:
                time.strptime(inp, '%Y/%m/%d')
                year, month, day = inp.split('/')
                year, month, day = int(year), int(month), int(day)
                if year > 2021 and count != 'Group':
                    print('Our university does not recruit people from the future, please call the NSA they will be '
                          'more interested')
                elif year < 2020 and count == 'Group':
                    print('This database can only contain groups that have not completed education')
                elif year > 2031 and count == 'Group':
                    print('Students study at our university only for 5 years, and we admit groups only for 3 years in '
                          'advance')
                elif year < 1915:
                    print('There are no dead souls in our university')
                elif 2021 > year > 1997 and count == 'Teacher':
                    print('Our university does not employ such young teachers')
                elif 1915 < year < 1951 and count == 'Teacher':
                    print('You are about to retire or you are already retired, so we cannot recruit you')
                else:
                    res = (str(year) + '-' + str(month) + '-' + str(day))
                    break
            except ValueError:
                print('Invalid date, please try again')
        return res

    elif var_mean == 'list':
        list_res = []
        while True:
            inp = input(message)
            regular = '[\d+\s]{,30}'
            if re.match(regular, inp):
                list_id = inp.split(' ')
                list_id = list(map(int, list_id))
                for i in list_id:
                    if count >= i > 0:
                        list_res.append(i)
                    else:
                        print('Numbers greater than ' + str(count) + ' have been automatically removed')
                break
            else:
                print('Error, please enter several (no more than 10) or one number from 1 to ' + str(count) +
                      'separated by a spaces')
        return list_res


def teacher_add():
    print('\nATTENTION: model Teacher has fields: Full Name, Date of Birth, ID of the taught Subject\n')

    count_words = 3
    message = 'Enter the full name of the teacher: '
    full_name = validation('name', count_words, message)

    who = 'Teacher'
    message = 'Enter the teacher date of birth in the format year/month/day: '
    birth_date = validation('date', who, message)

    subject_count = Subject.filter(Subject.id > 0).count()
    message = 'Enter the ID of the taught subject: '
    subject = validation('int', subject_count, message)

    Teacher.create(full_name=full_name, birth_date=birth_date, subject=subject).save()

    print('\nModel object Teacher created successfully\n')


def group_add():
    print('\nATTENTION: model Group has fields: Title, ID of Curator, ID of Headman, End Date\n')

    count_words = 0
    message = 'Enter group title: '
    title = validation('title', count_words, message)

    teacher_count = Teacher.filter(Teacher.id > 0).count()
    message = 'Enter the ID of group curator: '
    curator_id = validation('int', teacher_count, message)

    student_count = Student.filter(Student.id > 0).count()
    message = 'Enter the ID of group headman: '
    headman_name_id = validation('int', student_count, message)

    who = 'Group'
    message = 'Enter year of end education in the format year/month/day: '
    end_date = validation('date', who, message)

    print('\nYou also need to enter the ID of the Students who will study in this group and ID of main subjects of '
          'this group\n')

    subject_count = Subject.filter(Subject.id > 0).count()
    message = 'Enter the ID of subjects that will be the main for this group, separated by a space: '
    subjects_id_list = validation('list', subject_count, message)

    student_count = Student.filter(Student.id > 0).count()
    message = 'Enter the ID of the students who will study in this group, separated by a space: '
    students_id_list = validation('list', student_count, message)

    Group.create(title=title, curator_id=curator_id, headman_name_id=headman_name_id, end_date=end_date).save()

    count_group = Group.filter(Group.id > 0).count()
    for i in subjects_id_list:
        GroupSubjects.create(group_id=count_group, subject_id=i).save()
    for i in students_id_list:
        StudentGroup.create(group_id=count_group, student_id=i).save()

    print('\nModel object Group created successfully\n')


def add(table):
    if table == 1:
        group_add()

    if table == 2:
        pass

    if table == 3:
        teacher_add()

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
