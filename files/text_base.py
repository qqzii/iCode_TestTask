
def text_base(category, n):
    errors = [
        'Incorrect input, try again',
        'Error, please enter a number from 1 to ',
        'Error, please enter 1 or 0',
        'Error, please enter a float number from 0 to ',
        'Error, please enter full name in three words (First Name, Father Name, Last Name) separated by spaces',
        'Error, enter a title of at least two words and no more than fifty characters with the first word "Department" separated by a spaces',
        'Error, enter a title with at least one word and no more than sixty characters, with words separated by a space',
        'Our university does not recruit people from the future, please call the NSA they will be more interested',
        'This database can only contain groups that have not completed education',
        'Students study at our university only for 5 years, and we admit groups only for 3 years in advance',
        'There are no dead souls in our university',
        'Our university does not employ such young teachers',
        'You are about to retire or you are already retired, so we cannot recruit you',
        'We do not accept such young students',
        'You are too old to study at our university',
        "By age, you dont fall into any category",
        'Invalid date, please try again',
        'Error, please enter several (no more than 10) or one number from 1 to ',
        ' separated by a spaces'
    ]
    choices = [
        'Your choice: ',
        '\nPlease select the function you want to perform:\n1. Select action\n2. Select table\n3. EXIT',
        '\nPlease select the function you want to perform:\n1. View data\n2. Adding data\n3. Delete data\n4. To the main menu',
        '\nPlease select table:\n1. Groups\n2. Students\n3. Teachers\n4. Subjects\n5. Pass Cards\n6. To the main menu',
        '\nWould you like to see additional data?\n1. View a list of students in groups\n2. View the main subjects of groups\n3. I don’t want to watch additional data',
        '\nWould you like to see additional data?\n1. View the main subjects of this group\n2. I don’t want to watch additional data',
        '\n1. To the main menu',
        '\nWould you like to see additional data?\n1. View a list of students in groups\n2. I don’t want to watch additional data',
        '\nWould you like to see additional data?\n1. View a list of additional subjects for each student\n2. I don’t want to watch additional data',
        '\nEnter the ID of the ',
        ' you want to remove: ',
        '\nConfirm DELETE ',
        ' with ID - ',
        ':\n1. Confirm\n2. Do not delete. To the main menu',
        '\nPlease select the function you want to perform:\n1. Create pass-card\n2. To the main menu',
        '\nPlease select the function you want to perform:\n1. Continue\n2. To the main menu'
    ]
    views = [
        '\nList of subjects by group',
        '\nList of students by group',
        '\nList of additional subjects for each student',
        '\nYour table:',
        'Number greater than ',
        ' and repetitive have been automatically removed',
        '\nPass-Card and Model deleted successfully\n',
        '\nModel object ',
        ' deleted successfully\n',
        '\nYou also need to enter the ID of the Students who will study in this group and ID of main subjects of this group\n',
        '\nModel object Group created successfully\n',
        '\nYou also need to enter the ID of the subjects that will be additional for this student\n',
        '\nModel object Student created successfully\n',
        '\nModel object Teacher created successfully\n',
        '\nModel object Subject created successfully\n',
        '\nPlease note that this table contains only information for pass-card. If you want to create a Student or Teacher, you can create them by selecting the appropriate option in the previous menu. If you want to create a position for a university employee, then you should continue',
        '\nPass-Card created successfully\n',
        '\nPlease note if you delete a Student or Teacher, they will be deleted from all tables'
    ]
    fields = [
        'Enter group title: ',
        'Enter the ID of group curator: ',
        'Enter the ID of group headman: ',
        'Enter year of end education in the format year/month/day: ',
        'Enter the ID of subjects that will be the main for this group, separated by a space: ',
        'Enter the ID of the students who will study in this group, separated by a space: ',
        'Enter the full name of the student: ',
        'Enter the student date of birth in the format year/month/day: ',
        'Enter the ID of the group, where will the student study: ',
        'Enter 1 if the student is applying for the role of headman and 0 if not: ',
        'Enter the average student rating: ',
        'Enter the ID of subjects that will be additional for this student, separated by a space: ',
        'Enter the full name of the teacher: ',
        'Enter the teacher date of birth in the format year/month/day: ',
        'Enter the ID of the taught subject: ',
        'Enter subject title: ',
        'Enter the full name: ',
        'Enter the student date of birth in the format year/month/day: '
    ]
    attentions = [
        '\nATTENTION: model Group has fields: Title, ID of Curator, ID of Headman, End Date\n',
        '\nATTENTION: model Student has fields: Full Name, Date of Birth, Group ID, status Headman or not, Rating\n',
        '\nATTENTION: model Teacher has fields: Full Name, Date of Birth, ID of the taught Subject\n',
        '\nATTENTION: model Subject has fields: Title\n',
        '\nATTENTION: model Pass-Card has fields: Full Name, Date of Birth\n'
    ]
    regular = [
        '\w+',
        '\s',
        'Departament\s[\w+\s]{,50}',
        '[\w+\s]{,60}',
        '[\d+\s]{,30}'
    ]
    if category == 'errors':
        return errors[n]
    elif category == 'choices':
        return choices[n]
    elif category == 'views':
        return views[n]
    elif category == 'fields':
        return fields[n]
    elif category == 'attentions':
        return attentions[n]
    elif category == 're':
        return regular[n]
