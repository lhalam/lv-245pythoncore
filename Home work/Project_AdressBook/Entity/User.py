import hashlib

class User():
    def __init__(self, username = None,
                     first_name = None,
                      last_name = None,
                          email = None,
                       password = None):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def get_username(self):
        return self.username

    def get_full_name(self):
        return(self.first_name + "" + self.last_name)

    def get_short_name(self):
        return(self.first_name)

    def set_password(self, raw_password):
        self.password = hashlib.md5(raw_password)

    def check_password(self, raw_password):
        return self.password == hashlib.md5(raw_password)

    def is_valid(self):
        if self.username


