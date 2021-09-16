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


def action_choice():
    key = True
    answer = ''
    while key:
        print('Please select the function you want to perform:\n1. View data\n2. Adding data\n3. Change data\n'
              '4. Delete data')
        answer = input('Your choice: ')
        answer, key = selection_check(answer, key, 4)
    return answer


def table_choice():
    key = True
    answer = ''
    while key:
        print('Please select table:\n1. Groups\n2. Students\n3. Teachers\n4. Subjects\n5. Pass Cards')
        answer = input('Your choice: ')
        answer, key = selection_check(answer, key, 5)
    return answer


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
            else:
                val = getattr(rows, cols)
            body += str(val).ljust(columns[width])
        print(body)


def view(table):
    columns = {}
    model = []
    print('Your table:')
    if table == 1:
        model = [Group, 'id', 'title', 'headman_name', 'curator', 'end_date']
        columns = {'ID': 6, 'Title': 60, 'Headman': 40, 'Curator': 40, 'End Date': 16}

        # for i in all_table:
        #     names = []
        #     for j in i.students:
        #         names.append(j.full_name)

    if table == 2:
        model = [Student, 'id', 'full_name', 'birth_date', 'headman', 'rating']
        columns = {'ID': 6, 'Full Name': 40, 'Birth Date': 16, 'Headman': 11, 'Rating': 8}

    if table == 3:
        model = [Teacher, 'id', 'full_name', 'birth_date', 'subject']
        columns = {'ID': 6, 'Full Name': 40, 'Birth Date': 16, 'Subject Title': 51}

    if table == 4:
        model = [Subject, 'id', 'title']
        columns = {'ID': 6, 'Title': 51}

    if table == 5:
        model = [Human, 'id', 'full_name', 'birth_date']
        columns = {'ID': 6, 'Full Name': 40, 'Birth Date': 16}

    draw_table(columns, model)


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
