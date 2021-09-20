import time
import re
from text_base import text_base
from models import *


def selection_check(answer, key, qty):
    try:
        if (int(answer) > 0) and (int(answer) < qty + 1):
            answer = int(answer)
            key = False
        else:
            print(text_base('errors', 0))
    except ValueError:
        print(text_base('errors', 0))
    return answer, key


def choice(request, qty):
    key = True
    answer = ''
    while key:
        print(request)
        answer = input(text_base('choices', 0))
        answer, key = selection_check(answer, key, qty)
    return answer


def main_menu():
    out = False
    table = 0
    action = 0
    request = text_base('choices', 1)
    passage = choice(request, 3)
    if passage == 1:
        action = action_choice()
        if action != 4:
            table = table_choice()
    elif passage == 2:
        table = table_choice()
        if table != 6:
            action = action_choice()
    elif passage == 3:
        out = True
    return action, table, out


def action_choice():
    request = text_base('choices', 2)
    return choice(request, 4)


def table_choice():
    request = text_base('choices', 3)
    return choice(request, 6)


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
    print(text_base('views', 0))

    model = [GroupSubjects, 'group', 'subject']
    columns = {'Group': 60, 'Subject': 52}
    draw_table(columns, model)


def student_group():
    print(text_base('views', 1))

    model = [StudentGroup, 'group', 'student']
    columns = {'Group': 60, 'Student': 40}
    draw_table(columns, model)


def student_subject():
    print(text_base('views', 2))

    model = [StudentSubject, 'student', 'subject']
    columns = {'Student': 40, 'Subject': 52}
    draw_table(columns, model)


def view(table, key_for_view=True):

    print(text_base('views', 3))

    if table == 1:
        model = [Group, 'id', 'title', 'headman_name', 'curator', 'end_date']
        columns = {'ID': 6, 'Title': 60, 'Headman': 40, 'Curator': 40, 'End Date': 16}
        draw_table(columns, model)

        if key_for_view:

            request = text_base('choices', 4)
            answer = choice(request, 3)

            if answer == 1:
                student_group()

                request = text_base('choices', 5)
                answer = choice(request, 2)

                if answer == 1:
                    subject_group()

                    request = text_base('choices', 6)
                    choice(request, 1)

            elif answer == 2:
                subject_group()

                request = text_base('choices', 7)
                answer = choice(request, 2)

                if answer == 1:
                    student_group()

                    request = text_base('choices', 6)
                    choice(request, 1)

    if table == 2:
        model = [Student, 'id', 'full_name', 'birth_date', 'headman', 'rating']
        columns = {'ID': 6, 'Full Name': 40, 'Birth Date': 16, 'Headman': 11, 'Rating': 8}
        draw_table(columns, model)

        if key_for_view:

            request = text_base('choices', 8)
            answer = choice(request, 2)

            if answer == 1:
                student_subject()

                request = text_base('choices', 6)
                choice(request, 1)

    if table == 3:
        model = [Teacher, 'id', 'full_name', 'birth_date', 'subject']
        columns = {'ID': 6, 'Full Name': 40, 'Birth Date': 16, 'Subject Title': 52}
        draw_table(columns, model)

        if key_for_view:
            request = text_base('choices', 6)
            choice(request, 1)

    if table == 4:
        model = [Subject, 'id', 'title']
        columns = {'ID': 6, 'Title': 52}
        draw_table(columns, model)

        if key_for_view:
            request = text_base('choices', 6)
            choice(request, 1)

    if table == 5:
        model = [Human, 'id', 'full_name', 'birth_date']
        columns = {'ID': 6, 'Full Name': 40, 'Birth Date': 16}
        draw_table(columns, model)

        if key_for_view:
            request = text_base('choices', 6)
            choice(request, 1)


def validation(field_type, count, message):

    if field_type == 'int' or field_type == 'boolean' or field_type == 'float':
        while True:
            inp = input(message)
            if field_type == 'int':
                if inp.isdigit() and count >= int(inp) > 0:
                    res = int(inp)
                    break
                else:
                    print(text_base('errors', 1) + str(count))
            elif field_type == 'boolean':
                if inp.isdigit() and count >= int(inp) >= 0:
                    res = int(inp)
                    break
                else:
                    print(text_base('errors', 2))
            elif field_type == 'float':
                try:
                    if count >= float(inp) > 0:
                        res = round(float(inp), 1)
                        break
                    else:
                        print(text_base('errors', 3) + str(count))
                except ValueError:
                    print(text_base('errors', 3) + str(count))
        return res

    elif field_type == 'name' or field_type == 'title' or field_type == 'title_subject':
        while True:
            inp = input(message)
            front = '^'
            back = '$'
            body = ''
            regular = ''
            for i in range(count):
                body += text_base('re', 0)
                if i+1 != count:
                    body += text_base('re', 1)
            if field_type == 'name':
                regular = front + body + back
            elif field_type == 'title':
                regular = front + text_base('re', 2) + back
            elif field_type == 'title_subject':
                regular = front + text_base('re', 3) + back
            if re.match(regular, inp):
                res = inp
                break
            else:
                if field_type == 'name':
                    print(text_base('errors', 4))
                elif field_type == 'title':
                    print(text_base('errors', 5))
                elif field_type == 'title_subject':
                    print(text_base('errors', 6))
        return res

    elif field_type == 'date':
        while True:
            inp = input(message)
            try:
                time.strptime(inp, '%Y/%m/%d')
                year, month, day = inp.split('/')
                year, month, day = int(year), int(month), int(day)
                if year > 2021 and count != 'Group':
                    print(text_base('errors', 7))
                elif year < 2020 and count == 'Group':
                    print(text_base('errors', 8))
                elif year > 2031 and count == 'Group':
                    print(text_base('errors', 9))
                elif year < 1915:
                    print(text_base('errors', 10))
                elif 2021 > year > 1997 and count == 'Teacher':
                    print(text_base('errors', 11))
                elif 1915 < year < 1951 and count == 'Teacher':
                    print(text_base('errors', 12))
                elif year > 2006 and count == 'Student':
                    print(text_base('errors', 13))
                elif year < 2000 and count == 'Student':
                    print(text_base('errors', 14))
                elif (1951 > year or 2006 < year) and count == 'Human':
                    print(text_base('errors', 15))
                else:
                    res = (str(year) + '-' + str(month) + '-' + str(day))
                    break
            except ValueError:
                print(text_base('errors', 16))
        return res

    elif field_type == 'list':
        list_res = []
        while True:
            try:
                inp = input(message)
                regular = text_base('re', 4)
                if re.match(regular, inp):
                    list_id = inp.split(' ')
                    list_id = list(map(int, list_id))
                    for i in list_id:
                        if count >= i > 0:
                            list_res.append(i)
                        else:
                            print(text_base('views', 4) + str(count) + text_base('views', 5))
                    list_res = list(set(list_res))
                    break
            except ValueError:
                print(text_base('errors', 17) + str(count) + text_base('errors', 18))
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


def removal(model, model_name, table):
    key_for_view = False
    view(table, key_for_view)

    data = prepare_fields({
        text_base('choices', 9) + model_name + text_base('choices', 10):
        ['int', model.filter(model.id > 0).count()]
                           })

    request = text_base('choices', 11) + model_name + text_base('choices', 12) + str(data[0]) + text_base('choices', 13)
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
            print(text_base('views', 6))
        else:
            print(text_base('views', 7) + model_name + text_base('views', 8))


def redirect(action, table):
    if action == 1:
        view(table)

    elif action == 2:
        if table == 1:
            print(text_base('attentions', 0))

            data = prepare_fields({text_base('fields', 0): ['title', 0],
                                   text_base('fields', 1): ['int', Teacher.filter(Teacher.id > 0).count()],
                                   text_base('fields', 2): ['int', Student.filter(Student.id > 0).count()],
                                   text_base('fields', 3): ['date', 'Group']
                                   })

            print(text_base('views', 9))

            data_support = prepare_fields({
                text_base('fields', 4): ['list', Subject.filter(Subject.id > 0).count()],
                text_base('fields', 5): ['list', Student.filter(Student.id > 0).count()]
            })

            Group.create(title=data[0], curator_id=data[1], headman_name_id=data[2], end_date=data[3]).save()

            count_group = Group.filter(Group.id > 0).count()
            for i in data_support[0]:
                GroupSubjects.create(group_id=count_group, subject_id=i).save()
            for i in data_support[1]:
                StudentGroup.create(group_id=count_group, student_id=i).save()

            print(text_base('views', 10))

        elif table == 2:
            print(text_base('attentions', 1))

            data = prepare_fields({
                text_base('fields', 6): ['name', 3],
                text_base('fields', 7): ['date', 'Student'],
                text_base('fields', 8): ['int', Group.filter(Group.id > 0).count()],
                text_base('fields', 9): ['boolean', 1],
                text_base('fields', 10): ['float', 10.0]
            })

            print(text_base('views', 11))

            data_support = prepare_fields({
                text_base('fields', 11): ['list', Subject.filter(Subject.id > 0).count()]
            })

            Student.create(full_name=data[0], birth_date=data[1], headman=data[3], rating=data[4]).save()
            StudentGroup.create(group_id=data[2], student_id=Student.filter(Student.id > 0).count()).save()
            Human.create(full_name=data[0], birth_date=data[1])

            count_student = Student.filter(Student.id > 0).count()
            for i in data_support[0]:
                StudentSubject.create(student_id=count_student, subject_id=i).save()

            print(text_base('views', 12))

        elif table == 3:
            print(text_base('attentions', 2))

            data = prepare_fields({
                text_base('fields', 12): ['name', 3],
                text_base('fields', 13): ['date', 'Teacher'],
                text_base('fields', 14): ['int', Subject.filter(Subject.id > 0).count()]
            })

            Teacher.create(full_name=data[0], birth_date=data[1], subject=data[2]).save()
            Human.create(full_name=data[0], birth_date=data[1])

            print(text_base('views', 13))

        elif table == 4:
            print(text_base('attentions', 3))

            data = prepare_fields({
                text_base('fields', 15): ['title_subject', 0]
            })

            Subject.create(title=data[0]).save()

            print(text_base('views', 14))

        elif table == 5:
            print(text_base('views', 15))

            request = text_base('choices', 14)
            answer = choice(request, 2)

            if answer == 1:
                print(text_base('attentions', 4))

                data = prepare_fields({
                    text_base('fields', 16): ['name', 3],
                    text_base('fields', 17): ['date', 'Human']
                })

                Human.create(full_name=data[0], birth_date=data[1]).save()

                print(text_base('views', 16))

    elif action == 3:
        if table == 1:
            removal(Group, 'Group', table)

        elif table == 2:
            removal(Student, 'Student', table)

        elif table == 3:
            removal(Teacher, 'Teacher', table)

        elif table == 4:
            removal(Subject, 'Subject', table)

        elif table == 5:
            print(text_base('views', 17))

            request = text_base('choices', 15)
            answer = choice(request, 2)

            if answer == 1:
                removal(Human, 'Pass-Card', table)


def main_loop():
    print('\nWelcome to our database!\n')
    while True:
        action, table, out = main_menu()
        if out:
            break
        redirect(action, table)
    print('\nBye!\n')


if __name__ == "__main__":
    main_loop()
