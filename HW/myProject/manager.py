# створити  створити в коренні проекту файл manage.py
# імпортевати в нього класс User

from entity.user import Profile

# створити масив з 4 юзерів
# Usernames may contain alphanumeric, _, @, +, . and - characters

user_1 = Profile(
    '1the-best-musician',
    first_name='Bob',
    last_name='Jonson',
    email='Bob@ukr.net',
    password='Bob_musician+@1',
    date_of_birth='1985-08-06',
    sex='male',
    avatar='foto.jpg')

user_2 = Profile(
    'senator+@2',
    first_name='Arnold',
    last_name='Schwarzenegger',
    email='Arnold@ukr.net',
    password='Strong_Arny',
    date_of_birth='1965-08-06',
    sex='male',
    avatar='foto.jpg')

user_3 = Profile(
    'my+not_good_mechanic',
    first_name='Vasya',
    last_name='Holyb',
    email='Vasya@ukr.net',
    password='renault+mechanic',
    date_of_birth='2000-08-06',
    sex='male',
    avatar='foto.jpg')

user_4 = Profile(
    'traveler+.+',
    first_name='Natali',
    last_name='Holybovych',
    email='Holybovych@ukr.net',
    password='Natali_95@+traveler',
    date_of_birth='2001-08-06',
    sex='female',
    avatar='foto.jpg')


def get_not_adult():
    not_adults = []
    users = [user_1,
             user_2,
             user_3,
             user_4]
    for user in users:
        if user.get_age() < 18:
            not_adults.append(user.get_full_name())
    return '{} and {} are not adults'. \
        format(not_adults[0], not_adults[1])


print(get_not_adult())


def input_invalid_data():
    users_invalid_data = {}
    users = [user_1,
             user_2,
             user_3,
             user_4]
    for user in users:
        if len(user.is_valid()) != 0:
            users_invalid_data[user.get_username()] = user.is_valid()
    if len(users_invalid_data) == 0:
        return 'All input data are valid'
    else:
        print('There are input data which are invalid')
        return users_invalid_data


print(input_invalid_data())

if __name__ == '__main__':
    pass
