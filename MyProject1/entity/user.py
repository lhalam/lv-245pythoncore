# -*- coding: utf-8 -*-

class User(object):
    def __init__(self, username, password,  first_name=None, last_name=None, email=None):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def get_username(self):
        return self.username

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_email(self):
        return self.email

    def set_password(self, raw_password):
        self.fr_password = raw_password
        self.fr = []
        self.leng = len(self.fr_password)
        for i in self.fr_password:
            self.temp = ord(i) +(ord(i) % self.temp)
            self.code.append(chr(self.temp))
        return ''.join(self.code)

    def check_password(self, raw_password):
        self.raw_password = raw_password
        if  set_password(self.raw_password) == set_password(self.password):
            return True
        else:
            return False


    def _is_valid_username(self):
        if len(self.username) < 50:
            for i in self.username:
                if not( i in ("_", "@", "+", ".", "-") or i.isdigit() or i.isalpha()):
                    return False
            return True
        else:
            return False

    def is_valid(self):
        errors = []
        if self._is_valid_username():
            errors.append("username")
        return errors