class User(object):
    def __init__(self, username, password, first_name=None, last_name=None, email=None):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    
    def get_username(self):
        return self.username

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name

    def set_password(self, raw_password):
        self.code_password = raw_password
        self.code = []
        self.l = len(self.code_password)
        for i in self.code_password:
            self.k = ord(i) + (ord(i) % self.l)
            self.code.append(chr(self.k))
        return ''.join(self.code)

    def check_password(self, raw_password):
        self.raw_password = raw_password
        if set_password(self.raw_password) == set_password(self.password):
            return True
        else:
            return False

    def _is_valid_username(self):
        if len(self.username) <= 50:
            for i in self.username:
                if not( i in ("_", "@", "+", ".", "-") or i.isdigit() or i.isalpha()):
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
        if self.email and self.email[-1].isalpha() and self.email[-2].isalpha() and self.email[-3].isalpha() and \
        self.email[-4] == "." and "@" in self.email:
            return True
        else:
            return False

    def _is_valid_password(self):
        self.check_v_pas = [0,0,0]
        if len(self.password) <= 50:
            for i in self.password:
                if i.isalpha():
                    self.check_v_pas[0] = 1
                elif i.isdigit():
                    self.check_v_pas[1] = 1
                elif i in ("_", "@", "+", ".", "-", ")"):
                    self.check_v_pas[2] = 1
                else:
                    return False
            if self.check_v_pas[0] and self.check_v_pas[1] and self.check_v_pas[2]:
                return True
            else:
                return False
        else:
            return False

    def is_valid(self):
        errors = []
        if not(self._is_valid_username()):
            errors.append("username")
        if not(self._is_valid_first_name()):
            errors.append("first_name")
        if not(self._is_valid_last_name()):
            errors.append("last_name")
        if not(self._is_valid_email()):
            errors.append("email")
        if not(self._is_valid_password()):
            errors.append("password")
        return errors


if __name__ == '__main__':
    users = [User(username="421563gfhjdesuif", password="bhjvbhv", first_name = "Vasja1"),
             User(username="421563gfhjdesuif!!!!+.fbjds", password="bhjv@341bhv"),
             User(username="421563gfhjdesuif!!!!+.fbjdsfbgdjhbgdhjbghfdbgbdfkjgbdfkjgbdfkj", password="bh9&(6jvbhv"),
             User(username="421563gfhj+_gh", password="bhj_ui5v)bhv", first_name = "Vasja45", last_name = "Vasichkin", email = "vasja45_sd@tesr.com")]
    for user in users:
        # print user._is_valid_username()
        print (user.is_valid())
    # t = "?"
    # print t in ("_", "@", "+", ".", "-") 
    # print t.isdigit()
    # print t.isalpha()