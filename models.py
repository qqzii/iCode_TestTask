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


class StudentGroup(Model):

    group = IntegerField()
    student = IntegerField()

    class Meta:
        database = db
        db_table = 'student-group'


class GroupSubject(Model):

    group = IntegerField()
    subject = IntegerField()

    class Meta:
        database = db
        db_table = 'group-subject'


class StudentSubject(Model):

    student = IntegerField()
    subject = IntegerField()

    class Meta:
        database = db
        db_table = 'student-subject'


class Student(Human):

    add_subjects = ManyToManyField(Subject)
    headman = BooleanField()
    rating = FloatField()

    class Meta:
        db_table = 'students'


class Group(BaseModel):

    students = ManyToManyField(Student)
    headman = ForeignKeyField(Student)
    curator = ForeignKeyField(Teacher)
    main_subjects = ManyToManyField(Subject)
    title = CharField()
    end_date = DateField()

    class Meta:
        db_table = 'groups'
