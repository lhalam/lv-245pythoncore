class User(object):
    def __init__(self, username='fdsfsdf', first_name=None, last_name=None, email=None, password='dfsfs'):
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

    def set_password(self):
        self.password += "12345"

    def check_password(self):
        if self.password:
            return True
        else:
            return False

    def _is_valid_username(self):

        if len(self.username) <= 50:
            for i in self.username:
                if not (i in ("_", "@", "+", ".", "-") or i.isdigit() or i.isalpha()):
                    return False
            return True
        else:
            return False

    def _is_valid_first_name(self):

        if self.first_name and len(self.first_name) < 30:
            return True
        else:
            return False

    def _is_valid_last_name(self):

        if self.last_name and len(self.last_name) < 30:
            return True
        else:
            return False

    def _is_valid_email(self):
        pass

    def _is_valid_password(self):
        digit = False
        alpha = False
        symbol = False
        if len(self.password) <= 50:
            for x in self.password:
                if x in map(chr, range(ord('0'), ord('9'))):
                    digit = True
                if x in map(chr, range(ord('a'), ord('z'))):
                    alpha = True
                if x in ('_', '@', '+', '.', '-'):
                    symbol = True
        return digit and alpha and symbol

    def is_valid(self):
        errors = []
        if self._is_valid_username():
            errors.append("username")
        if self._is_valid_first_name():
            errors.append("first name")
        if self._is_valid_last_name():
            errors.append("last name")
        if self._is_valid_email():
            errors.append("email")
        if self._is_valid_password():
            errors.append("password")

        return errors

    





