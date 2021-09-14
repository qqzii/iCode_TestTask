import datetime
from prettytable import PrettyTable
from models import *


def create_human(full_name, birth_year, birth_month, birth_day):
    return Human(full_name=full_name, birth_date=datetime.date(birth_year, birth_month, birth_day)).save()


def create_subject(title):
    return Subject(title=title).save()


def create_teacher(full_name, birth_year, birth_month, birth_day, subject_id):
    create_human(full_name, birth_year, birth_month, birth_day)
    return Teacher(
        full_name=full_name, birth_date=datetime.date(birth_year, birth_month, birth_day), subject_id=subject_id
    ).save()


def create_student(full_name, birth_year, birth_month, birth_day, add_subjects_id, headman, rating):
    create_human(full_name, birth_year, birth_month, birth_day)
    return Student(
        full_name=full_name, birth_date=datetime.date(birth_year, birth_month, birth_day),
        add_subjects_id=add_subjects_id, headman=headman, rating=rating
    ).save()


def create_group(
        students_id, headman_id, curator_id, main_subjects_id, title, end_date_year, end_date_month, end_date_day):
    end_date = datetime.date(end_date_year, end_date_month, end_date_day)
    return Group(students_id=students_id, headman_id=headman_id, curator_id=curator_id,
                 main_subjects_id=main_subjects_id, title=title, end_date=end_date).save()


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


def action_choice():
    key = True
    answer = ''
    while key:
        print('Please select the function you want to perform:\n1. View data\n2. Adding data\n'
              '3. Change data\n4. Delete data')
        answer = input('Your choice: ')
        answer, key = selection_check(answer, key, 4)
    return answer


def table_choice():
    key = True
    answer = ''
    while key:
        print('Please select table:\n1. Groups\n2. Students\n'
              '3. Teachers\n4. Subjects\n5. Pass Cards')
        answer = input('Your choice: ')
        answer, key = selection_check(answer, key, 5)
    return answer


def view(table):
    print('Your table:')
    if table == 1:
        print('id'.ljust(5), 'Title'.ljust(60), 'Students'.ljust(35), 'Headman'.ljust(35), 'Curator'.ljust(35),
              'Main Subjects'.ljust(7), 'End Date'.ljust(12))
        print('-' * 197)
        all_table = Group.select().where(Group.id > 0)
        for i in all_table:
            print(str(i.id).ljust(5), str(i.title).ljust(60), 'OOO'.ljust(35), str(i.headman.full_name).ljust(35),
                  str(i.curator.full_name).ljust(35), 'OOO'.ljust(7), str(i.end_date).ljust(12))

    if table == 2:
        print('id'.ljust(5), 'Full Name'.ljust(35), 'Birth Date'.ljust(12), 'Additional Subjects'.ljust(40),
              'Headman'.ljust(7), 'Average Rating'.ljust(14))
        print('-' * 118)
        all_table = Student.select().where(Student.id > 0)
        for i in all_table:
            print(str(i.id).ljust(5), str(i.full_name).ljust(35), str(i.birth_date).ljust(12), 'OOO'.ljust(40),
                  'OOO'.ljust(7), str(i.rating).ljust(14))

    if table == 3:
        print('id'.ljust(5), 'Full Name'.ljust(35), 'Birth Date'.ljust(12), 'Subject Title'.ljust(55))
        print('-' * 107)
        all_table = Teacher.select().where(Teacher.id > 0)
        for i in all_table:
            print(str(i.id).ljust(5), str(i.full_name).ljust(35), str(i.birth_date).ljust(12),
                  str(i.subject.title).ljust(55))

    if table == 4:
        print('id'.ljust(5), 'Title'.ljust(55))
        print('-' * 60)
        all_table = Subject.select().where(Subject.id > 0)
        for i in all_table:
            print(str(i.id).ljust(5), str(i.title).ljust(55))

    if table == 5:
        print('id'.ljust(5), 'Full Name'.ljust(35), 'Birth Date'.ljust(12))
        print('-' * 52)
        all_table = Human.select().where(Human.id > 0)
        for i in all_table:
            print(str(i.id).ljust(5), str(i.full_name).ljust(35), str(i.birth_date).ljust(12))


def add():
    pass


def change():
    pass


def delete():
    pass


def redirect(table, action):
    if action == 1:
        view(table)
    if action == 2:
        add(table)
    if action == 3:
        change(table)
    if action == 4:
        delete(table)


def main():

    greetings()
    redirect(table_choice(), action_choice())

main()
