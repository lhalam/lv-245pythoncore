# -*- coding: utf-8 -*-

class User(object):
    def __init__(self, username, password, first_name=None, last_name=None, email=None):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def get_username(self):
        return self.username

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name

    def set_password(self, raw_password):
<<<<<<< HEAD
        self.password = raw_password[::-1]
        

    def check_password(self, raw_password):
        if self.password == raw_password[::-1]:
=======
        self.password = raw_password
        

    def check_password(self, raw_password):
        if self.password == raw_password:
>>>>>>> master
            return True
        else:
            return False

    def _is_valid_username(self):
        """
        Required. 50 characters or fewer. /t
        Usernames may contain alphanumeric, _, @, +, . and - characters.
        """
        if len(self.username) <= 50:
            for i in self.username:
                if not (i in ("_", "@", "+", ".", "-") or i.isdigit() or i.isaipha()):
                    return False
            return True
        else:
            return False

    def _is_valid_first_name(self):
        if self.first_name and len(self.first_name) <= 30:
            return True
        else:
            return False


    def _is_valid_last_name(self):
        if self.last_name and len(self.last_name) <= 30:
            return True
        else:
            return False

    def _is_valid_email(self):
<<<<<<< HEAD
        #l@l.l
        b1, a1 = self.email.split('@')
        if len(b1) > 0:
            b2, a2 = a1.split(".")
            if len(b2) > 0 and len(a2) > 0:
                return True
        return False
        # if self.email == "." and "@" in self.email:
        #     return True
        # else:
        #     return False
=======
        if self.email == "." and "@" in self.email:
            return True
        else:
            return False
>>>>>>> master
    # !Завжди виходить False


    def _is_valid_password(self):
        digit = False
        alpha = False
        symbol = False
        if len(self.password) <= 50:
            for i in self.password:
                if i.isdigit():
                    digit = True
                elif i.isalpha():
                    alpha = True
                elif i in ("_", "@", "+", ".", "-", ")"):
                    symbol = True
                else:
                    print "Incorrect password"
            return digit and alpha and symbol
        else:
            return False


    def is_valid(self):
        errors = []
        if not self._is_valid_username():
            errors.append("username")
        if not self._is_valid_first_name():
            errors.append("first_name")
        if not self._is_valid_last_name:
            errors.append("last_name")
        if not self._is_valid_email():
            errors.append("email")
        if not self._is_valid_password():
            errors.append("password")
        return errors


if __name__ == '__main__':
    users = [User(username="Ihor", first_name="Ihor", last_name="Kapiy", password="nksm21", email="kapi@.ua"),
             User(username="Olehovuch", first_name="Oleh", last_name="Kalinich", password="123", email="sara09@mail.ru"),
             User(username="Sasha", first_name="Oleksandr", last_name="Danuliv", password="sd23-+w", email="dina@m.com"),
             User(username="Katerine", first_name="Kate", last_name="Kislova", email="oleh.@gmail.com", password="psd._")]
    for user in users:
        print user.get_username()
        # print user.get_short_name()
        # print user.get_full_name()
        # print user.check_password("nksm21")
        # print user.check_password("nksm21")
<<<<<<< HEAD
        # print user._is_valid_password()
=======
        print user._is_valid_password()
>>>>>>> master

        # t = "?"
        # print t in ("_", "@", "+", ".", "-")
        # print t.isdigit()
        # print t.isalpha()
