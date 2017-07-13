class User(object):
    def __init__(self, name="string"):
        super(User, self).__init__()
        self.name = name
    def __str__(self):
        return "name: {}".format(self.name)
