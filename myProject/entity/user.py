class User(object):
    def __init__(self, usernames, first_name=None, last_name=None):
        self.usernames = usernames
        self.first_name = first_name
        self.last_name = last_name

    def get_username(self):
        return self.usernames

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def _is_valid_username(self):
        if len(self.usernames) < 50:
            if not (",", "@", "+", "." ",") or i.isdigit() or i.isalpha():
                return True
            return False
        else:
            False

if __name__ =='__mail__':
    user = [Uset(usernames="dfhdfhsdfhht"),
            Uset(usernames="fwefefwfefefwfewf"),
            Uset(usernames="fewefffeeffef,.efwfwe,"),
            Uset(usernames="r3r32r23r3fewf")]