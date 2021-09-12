import sqlite3

with sqlite3.connect('db/DataBase.db') as db:
    cursor = db.cursor()
    query = """CREATE TABLE IF NOT EXISTS teachers(name VARCHAR , id INTEGER)"""
    query1 = """INSERT INTO teachers(name,id) VALUES('Iliya', 3)"""
    query2 = """INSERT INTO teachers(name,id) VALUES('Kate', 2)"""
    query3 = """INSERT INTO teachers(name,id) VALUES('Artemy', 1)"""

    cursor.execute(query)
    cursor.execute(query1)
    cursor.execute(query2)
    cursor.execute(query3)

    db.commit()

students_list = [
        ('Renat', 1),
        ('Dima', 2),
        ('Max', 3),
        ('Jenya', 4)
    ]

with sqlite3.connect('db/DataBase.db') as db:
    cursor = db.cursor()
    query = """CREATE TABLE IF NOT EXISTS students(
    name VARCHAR,
    id INTEGER
    )"""
    query1 = """INSERT INTO students(name, id) VALUES(?, ?)"""

    cursor.executemany(query1, students_list)

    db.commit()

with sqlite3.connect('db/DataBase.db') as db:
    cursor = db.cursor()
    query = """SELECT  FROM teachers JOIN teachers ON teachers.id = students.id WHERE id = 2"""

    cursor.execute(query)
    for i in cursor:
        print(i)
    print('Завершено\n\n')

    db.commit()
