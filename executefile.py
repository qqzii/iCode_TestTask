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
            inp = input(message)
            regular = '[\d+\s]{,30}'
            if re.match(regular, inp):
                list_id = inp.split(' ')
                list_id = list(map(int, list_id))
                for i in list_id:
                    if count >= i > 0:
                        list_res.append(i)
                    else:
                        print('Number greater than ' + str(count) + ' have been automatically removed')
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
    Human.create(full_name=full_name, birth_date=birth_date)

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


def student_add():
    print('\nATTENTION: model Student has fields: Full Name, Date of Birth, status Headman or not, Rating\n')

    count_words = 3
    message = 'Enter the full name of the student: '
    full_name = validation('name', count_words, message)

    who = 'Student'
    message = 'Enter the student date of birth in the format year/month/day: '
    birth_date = validation('date', who, message)

    true_false = 1
    message = 'Enter 1 if the student will be the headman or enter 0 if not: '
    headman = validation('boolean', true_false, message)

    rating = 10.0
    message = 'Enter the average student rating: '
    rating = validation('float', rating, message)

    print('\nYou also need to enter the ID of the subjects that will be additional for this student\n')

    subject_count = Subject.filter(Subject.id > 0).count()
    message = 'Enter the ID of subjects that will be additional for this student, separated by a space: '
    subjects_id_list = validation('list', subject_count, message)

    Student.create(full_name=full_name, birth_date=birth_date, headman=headman, rating=rating).save()
    Human.create(full_name=full_name, birth_date=birth_date)

    count_student = Student.filter(Student.id > 0).count()
    for i in subjects_id_list:
        StudentSubject.create(student_id=count_student, subject_id=i).save()

    print('\nModel object Student created successfully\n')


def subject_add():
    print('\nATTENTION: model Subject has fields: Title\n')

    count_words = 0
    message = 'Enter subject title: '
    title = validation('title_subject', count_words, message)

    Subject.create(title=title).save()

    print('\nModel object Subject created successfully\n')


def human_add():
    print('\nPlease note that this table contains only information for pass-card. If you want to create a Student or '
          'Teacher, you can create them by selecting the appropriate option in the previous menu. If you want to create'
          ' a position for a university employee, then you should continue')

    request = '\nPlease select the function you want to perform:\n1. Create pass-card\n2. To the main menu'
    answer = choice(request, 2)

    if answer == 1:
        print('\nATTENTION: model Pass-Card has fields: Full Name, Date of Birth\n')

        count_words = 3
        message = 'Enter the full name: '
        full_name = validation('name', count_words, message)

        who = 'Human'
        message = 'Enter the student date of birth in the format year/month/day: '
        birth_date = validation('date', who, message)

        Human.create(full_name=full_name, birth_date=birth_date).save()

        print('\nPass-Card created successfully\n')

    elif answer == 2:
        print('glavv')


def teacher_delete():

    view(3)

    teacher_count = Teacher.filter(Teacher.id > 0).count()
    message = '\nEnter the ID of the Teacher you want to remove: '
    teacher_id = validation('int', teacher_count, message)

    object_model = Teacher.select().where(Teacher.id == teacher_id)

    teacher_name = ''
    for i in object_model:
        teacher_name = i.full_name

    request = '\nConfirm DELETE Teacher with ID - ' + str(teacher_id) + ':\n1. Confirm\n2. Do not delete. To the main' \
                                                                        ' menu'
    answer = choice(request, 2)

    if answer == 1:
        Teacher.get(Teacher.id == teacher_id).delete_instance()
        Human.get(Human.full_name == teacher_name).delete_instance()

        print('\nModel object Teacher deleted successfully\n')

    elif answer == 2:
        print('glavv')


def group_delete():

    print('\nYour table:')
    model = [Group, 'id', 'title', 'headman_name', 'curator', 'end_date']
    columns = {'ID': 6, 'Title': 60, 'Headman': 40, 'Curator': 40, 'End Date': 16}
    draw_table(columns, model)

    group_count = Teacher.filter(Teacher.id > 0).count()
    message = '\nEnter the ID of the Group you want to remove: '
    group_id = validation('int', group_count, message)

    request = '\nConfirm DELETE Group with ID - ' + str(group_id) + ':\n1. Confirm\n2. Do not delete. To the main menu'
    answer = choice(request, 2)

    if answer == 1:
        StudentGroup.get(StudentGroup.group == group_id).delete_instance()
        GroupSubjects.get(GroupSubjects.group == group_id).delete_instance()
        Group.get(Group.id == group_id).delete_instance()

        print('\nModel object Group deleted successfully\n')

    elif answer == 2:
        print('glavv')


def student_delete():

    print('\nYour table:')
    model = [Student, 'id', 'full_name', 'birth_date', 'headman', 'rating']
    columns = {'ID': 6, 'Full Name': 40, 'Birth Date': 16, 'Headman': 11, 'Rating': 8}
    draw_table(columns, model)

    student_count = Student.filter(Student.id > 0).count()
    message = '\nEnter the ID of the Student you want to remove: '
    student_id = validation('int', student_count, message)

    object_model = Student.select().where(Student.id == student_id)

    student_name = ''
    for i in object_model:
        student_name = i.full_name

    request = '\nConfirm DELETE Student with ID - ' + str(student_id) + ':\n1. Confirm\n2. Do not delete. To the ' \
                                                                        'main menu'
    answer = choice(request, 2)

    if answer == 1:
        # for i in StudentGroup.select().where(StudentGroup.student == student_id):
        #     i.delete_instance()
        for i in StudentSubject.select().where(StudentSubject.student == student_id):
            i.delete_instance()
        Student.get(Student.id == student_id).delete_instance()
        Human.get(Human.full_name == student_name).delete_instance()

        print('\nModel object Student deleted successfully\n')

    elif answer == 2:
        print('glavv')


def subject_delete():

    view(4)

    subject_count = Subject.filter(Subject.id > 0).count()
    message = '\nEnter the ID of the Subject you want to remove: '
    subject_id = validation('int', subject_count, message)

    request = '\nConfirm DELETE Subject with ID - ' + str(subject_id) + ':\n1. Confirm\n2. Do not delete. To the main' \
                                                                        ' menu'
    answer = choice(request, 2)

    if answer == 1:
        GroupSubjects.get(GroupSubjects.subject == subject_id).delete_instance()
        StudentSubject.get(StudentSubject.subject == subject_id).delete_instance()
        Subject.get(Subject.id == subject_id).delete_instance()
        print('\nModel object Subject deleted successfully\n')

    elif answer == 2:
        print('glavv')


def human_definition(model_name, name):
    response = False
    id_found = 0
    for i in model_name.select():
        if i.full_name == name:
            id_found = i.id
            response = True
    return response, id_found


def human_delete():
    print('\nPlease note if you delete a Student or Teacher, they will be deleted from all tables')

    request = '\nPlease select the function you want to perform:\n1. Continue\n2. To the main menu'
    answer = choice(request, 2)

    if answer == 1:
        view(5)

        human_count = Human.filter(Human.id > 0).count()
        message = '\nEnter the ID of the Pass-Card you want to remove: '
        human_id = validation('int', human_count, message)

        object_model = Human.select().where(Human.id == human_id)

        human_name = ''
        for i in object_model:
            human_name = i.full_name

        request = '\nConfirm DELETE Pass-Card with ID - ' + str(human_id) + ':\n1. Confirm\n2. Do not delete. To the' \
                                                                            ' main menu'
        answer = choice(request, 2)

        if answer == 1:
            is_student, student_id = human_definition(Student, human_name)
            is_teacher, teacher_id = human_definition(Teacher, human_name)
            if is_student:
                # for i in StudentGroup.select().where(StudentGroup.student == student_id):
                #     i.delete_instance()
                for i in StudentSubject.select().where(StudentSubject.student == student_id):
                    i.delete_instance()
                Student.get(Student.id == student_id).delete_instance()

            elif is_teacher:
                Teacher.get(Teacher.id == teacher_id).delete_instance()

            Human.get(Human.id == human_id).delete_instance()

            print('\nPass-Card and Model deleted successfully\n')

        elif answer == 2:
            print('glavv')

    elif answer == 2:
        print('glavv')


def add(table):
    if table == 1:
        group_add()

    elif table == 2:
        student_add()

    elif table == 3:
        teacher_add()

    elif table == 4:
        subject_add()

    elif table == 5:
        human_add()


def delete(table):
    if table == 1:
        group_delete()

    elif table == 2:
        student_delete()

    elif table == 3:
        teacher_delete()

    elif table == 4:
        subject_delete()

    elif table == 5:
        human_delete()


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
