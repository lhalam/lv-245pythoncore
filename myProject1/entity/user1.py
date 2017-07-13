from validate_email import validate_email
from hashlib import md5
from datetime import date

class User(object):

    def __init__(self, username, first_name=None, last_name=None, email=None, password=None):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set(self, username=None, first_name=None, last_name=None, email=None, password=None):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        if password:
            self.set_password(password)
        else:
            self.password = None

    def get_username(self):
        return self.username

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name

    def get_email(self):
        return self.email

    def _is_valid_username(self):
        if len(self.username) < 50:
            for i in self.username:
                if i in ("_", "@", "+", ".", "-") or i.isdigit() or i.isalpha():
                    return True
                else:
                    return False
        else:
            return False

    def _is_valid_first_name(self):
        for i in self.first_name:
            if len(self.first_name) < 30:
                return True
            else:
                return False

    def _is_valid_last_name(self):
        for i in self.last_name:
            if len(self.last_name) < 30:
                return True
            else:
                return False

    def _is_valid_email(self):
        for i in self.email:
            if validate_email(self.email):
                return True
            else:
                return False

    def set_password(self, password):
        self.password = md5(password.encode())


    def check_password(self, password):
        return self.password == md5(password.encode())

    def _is_valid_password(self):
        return True if self.password else False

    def is_valid(self):
        errors = []
        if not self._is_valid_username():
            errors.append("usernames")
        if not self._is_valid_first_name():
            errors.append("first_name")
        if not self._is_valid_last_name():
            errors.append("last_name")
        if not self._is_valid_email():
            errors.append("email")
        if not self._is_valid_password():
            errors.append("password")

        return errors
#

class Profaile(User):

    def __init__(self, sex=None, date_of_birth=None, avatar=None):
        self.sex=sex
        self.date_of_birth=date_of_birth
        self.avatar=avatar

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
        prof = {"Username:  " : self.username,
                "Full Name: " : self.first_name,
                #"Age:       " : self.get_age(),
                "Email:     " : self.email,}
                #"Sex:       " : self.sex,
                #"Birth:     " : self.date_of_birth,
                #"Avatar:    " : self.avatar}
        return prof




               #
               #"Birth:     " : self.date_of_birth,
               #"Avatar:    " : self.avatar

    def get_age(self):
        if len(self.date_of_birth)<=3:
            y=0
            m=0
            d=0
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
            years = today.year - birth_date.year
            if (today.month - birth_date.month) > 0:
                return years
            elif (today.day - birth_date.day) > 0:
                return years
            else:
                return years -1








if __name__ == '__main__':


    users = [User(username="user_YURIY", first_name="YURIY", last_name="last_YURIY",
                  email="yuriy.semesyuk@yahoo.com", password="abcd12344"),
             User(username="user_TANYA", first_name="TANYA", last_name="last_TANYA",
                  email="yuriy.semesyuk@yahoo.com", password="abcd12344"),
             User(username="user_IHOR", first_name="IHOR", last_name="last_IHOR",
                  email="IHOR@yahoo.com", password="abcd12344"),
             User(username="user_KATYA", first_name="KATYA", last_name="last_KATYA",
                  email="KATYA@yahoo.com", password="bhrt")]

    profailes = [Profaile(sex="men1", date_of_birth="20.04.1991", avatar="foto1"),
                 Profaile(sex="men2", date_of_birth="20.04.1992", avatar="foto2"),
                 Profaile(sex="men3", date_of_birth="20.04.1993", avatar="foto3"),
                 Profaile(sex="men4", date_of_birth="20.04.1994", avatar="foto4")]

    ihor = Profaile(sex="men", date_of_birth="29323923923", avatar="sfssff")
    print(ihor.get_sex())
    print(ihor.get_birth())
    print(ihor.get_avatar())

    ihor = User(username="user_44YURIY", first_name="YUR44IY", last_name="last_Y44URIY", email="yuriy.semesyuk@y44ahoo.com", password="abc44d12344")
    print(ihor.username, ihor.first_name, ihor.last_name, ihor.email, ihor.password)

    for user in users:
        print(user.get_username())
        print(user.is_valid())
        # print(user.get_full_name())
        # print(user.get_short_name())
        # print(user._is_valid_email())
        # print(user._is_valid_username())
        # print(user._is_valid_first_name())
        # print(user._is_valid_last_name())

    for profaile in profailes:
        print(profaile.get_sex(), profaile.get_birth(), profaile.get_avatar())

    print("++++++++++++++++++++++++++++++++++++")
