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

    add_subjects = ManyToManyField(Subject, backref='subject-student')
    headman = BooleanField()
    rating = FloatField()

    class Meta:
        db_table = 'students'


class Group(BaseModel):

    students = ManyToManyField(Student, backref='student-group')
    headman_name = ForeignKeyField(Student)
    curator = ForeignKeyField(Teacher)
    main_subjects = ManyToManyField(Subject, backref='subject-group')
    title = CharField()
    end_date = DateField()

    class Meta:
        db_table = 'groups'


StudentGroup = Group.students.get_through_model()
StudentSubject = Student.add_subjects.get_through_model()
GroupSubjects = Group.main_subjects.get_through_model()

# with db:
#     db.create_tables([GroupSubjects, StudentGroup, StudentSubject, Group, Subject, Student, Teacher, Human])
