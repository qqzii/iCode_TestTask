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


def view(table, key_for_view=True):

    print('\nYour table:')

    if table == 1:
        model = [Group, 'id', 'title', 'headman_name', 'curator', 'end_date']
        columns = {'ID': 6, 'Title': 60, 'Headman': 40, 'Curator': 40, 'End Date': 16}
        draw_table(columns, model)

        if key_for_view:

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

        if key_for_view:

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


def validation(field_type, count, message):

    if field_type == 'int' or field_type == 'boolean' or field_type == 'float':
        while True:
            inp = input(message)
            if field_type == 'int':
                if inp.isdigit() and count >= int(inp) > 0:
                    res = int(inp)
                    break
                else:
                    print('Error, please enter a number from 1 to ' + str(count))
            elif field_type == 'boolean':
                if inp.isdigit() and count >= int(inp) >= 0:
                    res = int(inp)
                    break
                else:
                    print('Error, please enter 1 or 0')
            elif field_type == 'float':
                try:
                    if count >= float(inp) > 0:
                        res = round(float(inp), 1)
                        break
                    else:
                        print('Error, please enter a float number from 0 to ' + str(count))
                except ValueError:
                    print('Error, please enter a float number from 0 to ' + str(count))
        return res

    elif field_type == 'name' or field_type == 'title' or field_type == 'title_subject':
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
            if field_type == 'name':
                regular = front + body + back
            elif field_type == 'title':
                regular = front + 'Departament\s[\w+\s]{,50}' + back
            elif field_type == 'title_subject':
                regular = front + '[\w+\s]{,60}' + back
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if re.match(regular, inp):
                res = inp
                break
            else:
                if field_type == 'name':
                    print('Error, please enter full name in three words (First Name, Father Name, Last Name) separated '
                          'by spaces')
                elif field_type == 'title':
                    print('Error, enter a title of at least two words and no more than fifty characters with the first '
                          'word "Department" separated by a spaces')
                elif field_type == 'title_subject':
                    print('Error, enter a title with at least one word and no more than sixty characters, with words '
                          'separated by a space')
        return res

    elif field_type == 'date':
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
                elif year > 2006 and count == 'Student':
                    print('We do not accept such young students')
                elif year < 2000 and count == 'Student':
                    print('You are too old to study at our university')
                elif (1951 > year or 2006 < year) and count == 'Human':
                    print("By age, you don't fall into any category")
                else:
                    res = (str(year) + '-' + str(month) + '-' + str(day))
                    break
            except ValueError:
                print('Invalid date, please try again')
        return res

    elif field_type == 'list':
        list_res = []
        while True:
            try:
                inp = input(message)
                regular = '[\d+\s]{,30}'
                if re.match(regular, inp):
                    list_id = inp.split(' ')
                    list_id = list(map(int, list_id))
                    for i in list_id:
                        if count >= i > 0:
                            list_res.append(i)
                        else:
                            print('Number greater than ' + str(count) + ' and repetitive have been automatically '
                                                                        'removed')
                    list_res = list(set(list_res))
                    break
            except ValueError:
                print('Error, please enter several (no more than 10) or one number from 1 to ' + str(count) +
                      ' separated by a spaces')
        return list_res


def prepare_fields(data):
    response = []
    for i in data:
        response.append(validation(data[i][0], data[i][1], i))
    return response


def human_definition(model_name, name):
    response = False
    id_found = 0
    for i in model_name.select():
        if i.full_name == name:
            id_found = i.id
            response = True
    return response, id_found


def removal(model, model_name, table, key_for_view=True):
    view(table, key_for_view)

    data = prepare_fields({
        '\nEnter the ID of the ' + model_name + ' you want to remove: ': ['int', model.filter(model.id > 0).count()]
    })

    request = '\nConfirm DELETE ' + model_name + ' with ID - ' + str(data[0]) + ':\n1. Confirm\n2. Do not delete. To' \
                                                                                ' the main menu'
    answer = choice(request, 2)

    if answer == 1:

        if model == Teacher or model == Student or model == Human:

            object_model = model.select().where(model.id == data[0])
            full_name = ''
            for i in object_model:
                full_name = i.full_name

            if model == Human:
                is_student, student_id = human_definition(Student, full_name)
                is_teacher, teacher_id = human_definition(Teacher, full_name)

                if is_student:
                    for i in StudentGroup.select().where(StudentGroup.student == student_id):
                        i.delete_instance()
                    for i in StudentSubject.select().where(StudentSubject.student == student_id):
                        i.delete_instance()
                    Student.get(Student.id == student_id).delete_instance()

                elif is_teacher:
                    Teacher.get(Teacher.id == teacher_id).delete_instance()

            Human.get(Human.full_name == full_name).delete_instance()

        if model == Group:
            for i in StudentGroup.select().where(StudentGroup.group == data[0]):
                i.delete_instance()
            for i in GroupSubjects.select().where(GroupSubjects.group == data[0]):
                i.delete_instance()

        if model == Student:
            for i in StudentGroup.select().where(StudentGroup.student == data[0]):
                i.delete_instance()
            for i in StudentSubject.select().where(StudentSubject.student == data[0]):
                i.delete_instance()

        if model == Subject:
            for i in GroupSubjects.select().where(GroupSubjects.subject == data[0]):
                i.delete_instance()
            for i in StudentSubject.select().where(StudentSubject.subject == data[0]):
                i.delete_instance()

        if model != Human:
            model.get(model.id == data[0]).delete_instance()

        if model == Human:
            print('\nPass-Card and Model deleted successfully\n')
        else:
            print('\nModel object ' + model_name + ' deleted successfully\n')

    elif answer == 2:
        print('glavv')


def add(table):
    if table == 1:
        print('\nATTENTION: model Group has fields: Title, ID of Curator, ID of Headman, End Date\n')

        data = prepare_fields({'Enter group title: ': ['title', 0],
                               'Enter the ID of group curator: ': ['int', Teacher.filter(Teacher.id > 0).count()],
                               'Enter the ID of group headman: ': ['int', Student.filter(Student.id > 0).count()],
                               'Enter year of end education in the format year/month/day: ': ['date', 'Group']
                               })

        print('\nYou also need to enter the ID of the Students who will study in this group and ID of main subjects of '
              'this group\n')

        data_support = prepare_fields({
            'Enter the ID of subjects that will be the main for this group, separated by a space: ':
                ['list', Subject.filter(Subject.id > 0).count()],
            'Enter the ID of the students who will study in this group, separated by a space: ':
                ['list', Student.filter(Student.id > 0).count()]
        })

        Group.create(title=data[0], curator_id=data[1], headman_name_id=data[2], end_date=data[3]).save()

        count_group = Group.filter(Group.id > 0).count()
        for i in data_support[0]:
            GroupSubjects.create(group_id=count_group, subject_id=i).save()
        for i in data_support[1]:
            StudentGroup.create(group_id=count_group, student_id=i).save()

        print('\nModel object Group created successfully\n')

    elif table == 2:
        print(
            '\nATTENTION: model Student has fields: Full Name, Date of Birth, Group ID, status Headman or not, '
            'Rating\n')

        data = prepare_fields({
            'Enter the full name of the student: ': ['name', 3],
            'Enter the student date of birth in the format year/month/day: ': ['date', 'Student'],
            'Enter the ID of the group, where will the student study: ': ['int', Group.filter(Group.id > 0).count()],
            'Enter 1 if the student is applying for the role of headman and 0 if not: ': ['boolean', 1],
            'Enter the average student rating: ': ['float', 10.0]
        })

        print('\nYou also need to enter the ID of the subjects that will be additional for this student\n')

        data_support = prepare_fields({
            'Enter the ID of subjects that will be additional for this student, separated by a space: ':
                ['list', Subject.filter(Subject.id > 0).count()]
        })

        Student.create(full_name=data[0], birth_date=data[1], headman=data[3], rating=data[4]).save()
        StudentGroup.create(group_id=data[2], student_id=Student.filter(Student.id > 0).count()).save()
        Human.create(full_name=data[0], birth_date=data[1])

        count_student = Student.filter(Student.id > 0).count()
        for i in data_support[0]:
            StudentSubject.create(student_id=count_student, subject_id=i).save()

        print('\nModel object Student created successfully\n')

    elif table == 3:
        print('\nATTENTION: model Teacher has fields: Full Name, Date of Birth, ID of the taught Subject\n')

        data = prepare_fields({
            'Enter the full name of the teacher: ': ['name', 3],
            'Enter the teacher date of birth in the format year/month/day: ': ['date', 'Teacher'],
            'Enter the ID of the taught subject: ': ['int', Subject.filter(Subject.id > 0).count()]
        })

        Teacher.create(full_name=data[0], birth_date=data[1], subject=data[2]).save()
        Human.create(full_name=data[0], birth_date=data[1])

        print('\nModel object Teacher created successfully\n')

    elif table == 4:
        print('\nATTENTION: model Subject has fields: Title\n')

        data = prepare_fields({
            'Enter subject title: ': ['title_subject', 0]
        })

        Subject.create(title=data[0]).save()

        print('\nModel object Subject created successfully\n')

    elif table == 5:
        print('\nPlease note that this table contains only information for pass-card. If you want to create a Student'
              ' or Teacher, you can create them by selecting the appropriate option in the previous menu. If you want'
              ' to create a position for a university employee, then you should continue')

        request = '\nPlease select the function you want to perform:\n1. Create pass-card\n2. To the main menu'
        answer = choice(request, 2)

        if answer == 1:
            print('\nATTENTION: model Pass-Card has fields: Full Name, Date of Birth\n')

            data = prepare_fields({
                'Enter the full name: ': ['name', 3],
                'Enter the student date of birth in the format year/month/day: ': ['date', 'Human']
            })

            Human.create(full_name=data[0], birth_date=data[1]).save()

            print('\nPass-Card created successfully\n')

        elif answer == 2:
            print('glavv')


def delete(table):
    if table == 1:
        removal(Group, 'Group', table, False)

    elif table == 2:
        removal(Student, 'Student', table, False)

    elif table == 3:
        removal(Teacher, 'Teacher', table)
    elif table == 4:
        removal(Subject, 'Subject', table)

    elif table == 5:
        print('\nPlease note if you delete a Student or Teacher, they will be deleted from all tables')

        request = '\nPlease select the function you want to perform:\n1. Continue\n2. To the main menu'
        answer = choice(request, 2)

        if answer == 1:
            removal(Human, 'Pass-Card', table)

        elif answer == 2:
            print('glavv')


def change(table):
    if table == 1:
        pass

    elif table == 2:
        pass

    elif table == 3:
        pass

    elif table == 4:
        pass

    elif table == 5:
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
