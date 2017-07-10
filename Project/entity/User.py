class User(object):
    def __init__(self, username, first_name=None, last_name=None):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name

    def get_username(self):
        return self.username

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def _is_valid_username(self):
        if len(self.username) < 50:
            return True
        else:
            return False

    if len(self.username) < 50:
        for i in self.username:
            if i in ("_", "-", "@", ".", "+") or i.isdigit() or i.isalpha()
                return True
            return False
        else:
            return False

if __name__ == '__name__':
    user = [User(username=),






