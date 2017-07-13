from datetime import date

from user import User


class Profile(User):
    def __init__(self, birthdate=None,
                 avatar=None,
                 sex=None,
                 username=None,
                 first_name=None,
                 last_name=None,
                 password=None,
                 email=None):
        super(Profile, self).__init__(username,
                                      first_name,
                                      last_name,
                                      password,
                                      email)

        self.birthdate = birthdate
        self.sex = sex
        self.avatar = avatar

    def get_age(self):
        today = date.today()
        age = today.year - self.birthday.year
        if today.month < self.birthday.month:
            age -= 1
        elif today.month == self.birthday.month and today.day < self.birthday.day:
            age -= 1
        return age

    def get_birthdate(self):
        return self.birthdate

    def get_sex(self):
        return self.sex

    def get_avatar(self):
        return

    def _is_adult(self):
        years = self.get_age()
        if years < 18:
            return False
        else:
            return True
