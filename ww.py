

class Man:

    def __init__(self, id, full_name, birth_date):
        self.id = id
        self.full_name = full_name
        self.birth_date = birth_date

    def info(self):
        print('3')


class Teacher(Man):

    def __init__(self, id, full_name, birth_date, group_curator, subject):
        super().__init__(id, full_name, birth_date)
        self.group_curator = group_curator
        self.subject = subject

    def info(self):
        print('5')


class Student(Man):

    def __init__(self, id, full_name, birth_date, group, subjects, additional_subjects, reputation, average_score, end):
        super().__init__(id, full_name, birth_date)
        self.group_curator = group
        self.subject = subjects
        self.additional_subjects = additional_subjects
        self.reputation = reputation
        self.average_score = average_score
        self.end = end

    def info(self):
        print('7')


class Group:

    def __init__(self, id, speciality, curator, headman, subjects, reputation, end):
        self.id = id
        self.speciality = speciality
        self.curator = curator
        self.headman = headman
        self.subject = subjects
        self.reputation = reputation
        self.end = end

    def info(self):
        print('9')


class Subject:

    def __init__(self, id, title, teacher, groups, additional_students):
        self.id = id
        self.title = title
        self.teacher = teacher
        self.groups = groups
        self.additional_students = additional_students

    def info(self):
        print('1')


artem = Student(
    1, 'MorozovAD', '01.11.2000', 1, ('math', 'physic', 'programming'), ('bel', 'eng'), 9.8, 5.6, '1.07.2022'
)
print(artem.full_name)