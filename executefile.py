import datetime
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


with db:

    Human.delete().where(Human.id == 1000).execute()

print('ok')
