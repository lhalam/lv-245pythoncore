from validate_email import validate_email
from hashlib import md5


class User(object):
    def __init__(self, usernames, first_name=None, last_name=None, email=None, password=None):
        self.usernames = usernames
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        if password:
            self.set_password(password)
        else:
            self.password = None

    def get_username(self):
        return self.usernames

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name

    def _is_valid_username(self):
        if len(self.usernames) < 50:
            for i in self.usernames:
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
            errors.append("lirst_name")
        if not self._is_valid_first_name():
            errors.append("last_name")
        if not self._is_valid_email():
            errors.append("email")
        if not self._is_valid_password():
            errors.append("password")

        return errors


if __name__ == '__main__':

    users = [User(usernames="user.YURIY", first_name="YURIY", last_name="last.YURIY",
                  email="yuriy.semesyuk@yahoo.com"),
             User(usernames="user.TANYA", first_name="TANYA", last_name="last.TANYA",
                  email="yuriy.semesyuk@yahoo.com"),
             User(usernames="user.IHOR", first_name="IHOR", last_name="last.IHOR",
                  email="IHOR@yahoo.com"),
             User(usernames="user.KATYA", first_name="KATYA", last_name="last.KATYA",
                  email="KATYA@yahoo.com")]

    for user in users:
        print(user.get_username())
        print(user.is_valid())
        # print(user._is_valid_email())
        # print(user._is_valid_username())
        # print(user._is_valid_first_name())
        # print(user._is_valid_last_name())
        # print(user.get_full_name())
        # print(user.get_short_name())
