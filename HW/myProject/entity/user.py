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
        """
        Required. 50 characters or fewer.
        Usernames may contain alphanumeric, _, @, +, . and - characters.
        """
        if len(self.username) < 50:
            for i in self.username:
                if not (i in ("_", "@", "+", ".", "-") or i.isdigit() or i.isalpha()):
                    return False
            return True
        else:
            return False

    def is_valid(self) -> object:
        """

        :rtype: object
        """
        errors = []
        if self._is_valid_username():
            errors.append("username")

        return errors


if __name__ == '__main__':
    users = [User(username="421563gfhjdesuif"),
             User(username="421563gfhjdesuif!!!!+.fbjds"),
             User(username="421563gfhjdesuif!!!!+.fbjdsfbgdjhbgdhjbghfdbgbdfkjgbdfkjgbdfkj"),
             User(username="421563gfhj?desuif!!!!+.fbjds")]
    for user in users:
        # print user._is_valid_username()
        print
        user.is_valid()
        # t = "?"
        # print t in ("_", "@", "+", ".", "-")
        # print t.isdigit()
        # print t.isalpha()
