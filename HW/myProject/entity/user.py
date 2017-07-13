class User:
    def __init__(self, username, first_name=None,
                 last_name=None, email=None, password=None):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def get_username(self):
        return self.username

    def get_full_name(self):
        # Returns the first_name plus the last_name, with a space in between
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        # Returns the first_name
        return self.first_name

    def set_password(raw_password):
        # Sets the user’s password
        return raw_password

    def check_password(self):
        # Returns True if the given raw string is the correct password for the user
        if self.set_password() == self.password:
            return True
        else:
            return False

    def is_valid(self):
        # Returns True, if all the fields are valid
        errors = []
        if self._is_valid_username() == False:
            errors.append("username")
        if self._is_valid_first_name() == False:
            errors.append("first_name")
        if self._is_valid_last_name() == False:
            errors.append("last_name")
        if self._is_valid_email() == False:
            errors.append("email")
        if self._is_valid_password() == False:
            errors.append("password")
        return errors

    # Protected methods:
    def _is_valid_username(self):
        # Required. 50 characters or fewer.
        # Usernames may contain alphanumeric, _, @, +, . and - characters
        if len(self.username) > 50:
            return False
        for i in self.username:
            if not ((i in ('_', '@', '+', '.', '-') or
                         i.isalnum())):
                return False
        else:
            return True

    def _is_valid_first_name(self):
        # Optional. 30 characters or fewer
        if len(self.first_name) <= 30:
            return True
        else:
            return False

    def _is_valid_last_name(self):
        # Optional. 30 characters or fewer
        if len(self.last_name) <= 30:
            return True
        else:
            return False

    def _is_valid_email(self):
        # Optional. Email address
        if self.email.count('.') > 2:
            return False
        elif self.email.count('@') >= 2:
            return False
        elif (('..' in self.email or
                       ' ' in self.email) or
                  self.email.startswith(('.', '@')) or
                  self.email.endswith(('.', '@')) or
                  not '@' in self.email):
            return False
        else:
            return True

    def _is_valid_password(self):
        # Required. 50 characters or fewer.
        # Password must contain Letters, numbers, symbols ( _, @, +, . -)
        if len(self.password) > 50:
            return False
        elif not ('_' in self.password or
                          '@' in self.password or
                          '+' in self.password or
                          '.' in self.password or
                          '-' in self.password):
            return False
        for i in self.password:
            if i.isalnum():
                return True
        else:
            return False


class Profile(User):
    def __init__(self,
                 username, first_name=None,
                 last_name=None, email=None, password=None,
                 date_of_birth=None, sex=None, avatar=None):
        super(Profile, self).__init__(username, first_name,
                                      last_name, email, password)
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.avatar = avatar

    def get_age(self):
        from datetime import date
        today = date.today()
        self.date_of_birth = date(
            int(self.date_of_birth[:4]),
            int(self.date_of_birth[5:7]),
            int(self.date_of_birth[8:])
        )
        age = today.year - self.date_of_birth.year
        return age

    def get_sex(self):
        return '{}'.format(self.sex)

    def get_avatar(self):
        return '{}'.format(self.avatar)

    def get_birthday(self):
        return '{}'.format(self.date_of_birth)
