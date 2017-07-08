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
            for i in self.usernames:
                if not (i in ("_", "@", "+", ".", "-") or i.isdigit() or i.isalpha()):
                    return False
            return True
        else:
            return False


if  __name__ =='__main__':
    users= [User(usernames="r4553235rrt"),
            User(usernames="fefef"),
            User(usernames="ffefe"),
            User(usernames="r3fewf")]
    for user in users:
        print (user._is_valid_username())