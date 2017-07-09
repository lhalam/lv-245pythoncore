class User(object):
    def __init__(self, usernames, first_name=None, last_name=None,):
        self.usernames = usernames
        self.first_name = first_name
        self.last_name = last_name

    def __set__(self, instance, value):

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

    def _is_valid_email(self)




    #_is_valid_password()


    def is_valid(self):
        errors = []
        if not self._is_valid_username():
            errors.append("usernames")
        if not self._is_valid_first_name():
            errors.append("lirst_name")
        if not self._is_valid_first_name():
            errors.append("last_name")
        return errors



if  __name__ =='__main__':
    users = [User(usernames="767g95//==  ", first_name="eredfbgbdsbdbdfbdrerwerewrwerweewrwerew"),
             User(usernames="Tannya", first_name="gfefe"),
             User(usernames="IHOR", first_name="ffefe"),
             User(usernames="KATYA", first_name="ssssss"), ]

    for user in users:
        print(user._is_valid_username())

        print(user._is_valid_first_name())
        print(user.is_valid())