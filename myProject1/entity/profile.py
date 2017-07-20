from entity.user1 import User
from datetime import date

class Profile(User):
    def __init__(self, username=None, password=None, first_name=None, last_name=None,
                 email=None, date_of_birth=None, sex=None, avatar=None):
        super(Profile, self).__init__(username, password, first_name, last_name, email)

        self.date_of_birth = date_of_birth
        self.sex = sex
        self.avatar = avatar

    def set(self, username=None, first_name=None, last_name=None, email=None, password=None,
            sex=None, date_of_birth=None, avatar=None):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        if password:
            self.set_password(password)
        else:
            self.password = None
        self.sex = sex
        self.date_of_birth = date_of_birth
        self.avatar = avatar

    def get_sex(self):
        return self.sex

    def get_date_of_birth(self):
        return self.date_of_birth

    def get_avatar(self):
        return self.avatar

    def get_profile(self):
        prof = {"Username:  ": self.username,
                "Full Name: ": self.first_name,
                "Age:       ": self.get_age(),
                "Email:     ": self.email,
                "Sex:       ": self.sex,
                "Birth:     ": self.date_of_birth,
                "Avatar:    ": self.avatar}
        return prof

    def get_age(self):
        if len(self.date_of_birth)<=3:
            z=0
            for i in self.date_of_birth:
                if z == 0:
                    year = i
                if z == 1:
                    month = i
                if z == 2:
                    day = i
                z += 1
            birth_date = date(year, month, day)
            today = date.today()
            age = today.year - birth_date.year
            if (today.month - birth_date.month) > 0:
                return age
            elif (today.day - birth_date.day) > 0:
                return age
            else:
                return age -1