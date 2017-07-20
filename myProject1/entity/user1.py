from hashlib import md5
from validate_email import validate_email

class User(object):

    def __init__(self, username, password, first_name=None, last_name=None, email=None):
        self.username = username
        if password:
            self.set_password(password)
        else:
            self.password = None
        self.first_name = first_name
        self.last_name = last_name
        self.email = email


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


if __name__ == '__main__':
    users = [User(username="user_YURIY", first_name="YURIY", last_name="last_YURIY",
                  email="yuriy.semesyuk@yahoo.com", password="abcd12344"),
             User(username="user_TANYA", first_name="TANYA", last_name="last_TANYA",
                  email="yuriy.semesyuk@yahoo.com", password="abcd12344"),
             User(username="user_IHOR", first_name="IHOR", last_name="last_IHOR",
                  email="IHOR@yahoo.com", password="abcd12344"),
             User(username="user_KATYA", first_name="KATYA", last_name="last_KATYA",
                  email="KATYA@yahoo.com", password="bhrt")]

    profiles = [Profile(sex="men1", date_of_birth=(1993, 4, 29), avatar="foto1"),
                Profile(sex="men2", date_of_birth=(1993, 7, 29), avatar="foto2"),
                Profile(sex="men3", date_of_birth=(1993, 1, 29), avatar="foto3"),
                Profile(sex="men4", date_of_birth=(1993, 12, 28), avatar="foto4")]

    ihor = Profile()
    ihor.set(username="user_YURIY", first_name="YURIY", last_name="last_YURIY",
             email="yuriy.semesyuk@yahoo.com", password="abcd12344",
             sex="men", date_of_birth=(2000, 4, 29), avatar="foto")

    for i in ihor.get_profile():
        print(i, ihor.get_profile()[i])

        # for user in users:
        # print(user.get_username())
        # print(user.is_valid())
        # print(user.get_full_name())
        # print(user.get_short_name())
        # print(user._is_valid_email())
        # print(user._is_valid_username())
        # print(user._is_valid_first_name())(1993, 5, 24)
        # print(user._is_valid_last_name())

    for profile in profiles:
        print(profile.get_sex())
        print(profile.get_date_of_birth())
        print(profile.get_age())
    print("++++++++++++++++++++++++++++++++++++")