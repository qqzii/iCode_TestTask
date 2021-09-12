from models import *

with db:
    db.create_tables([Human, Teacher, Student, Group, Subject])

print('gotovo')
