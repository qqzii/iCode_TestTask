from peewee import *

db = SqliteDatabase('DataBase.db')


class BaseModel(Model):

    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'


class Human(BaseModel):

    full_name = CharField()
    birth_date = DateField()

    class Meta:
        db_table = 'pass_cards'


class Subject(BaseModel):

    title = CharField()

    class Meta:
        db_table = 'subjects'


class Teacher(Human):

    subject = ForeignKeyField(Subject)

    class Meta:
        db_table = 'teachers'


class Student(Human):

    add_subjects = ForeignKeyField(Subject)
    headman = BooleanField()
    rating = FloatField()

    class Meta:
        db_table = 'students'


class Group(BaseModel):

    students = ForeignKeyField(Student)
    headman = ForeignKeyField(Student)
    curator = ForeignKeyField(Teacher)
    main_subjects = ForeignKeyField(Subject)
    title = CharField()
    end_date = DateField()

    class Meta:
        db_table = 'groups'
