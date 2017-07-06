class User(object):
    # Fields:
    # username(Required.
    # 50
    # characters or fewer.Usernames
    # may
    # contain
    # alphanumeric, _,
    #
    # @
    #
    # , +,.and - characters.)
    # first_name(Optional.
    # 30
    # characters or fewer.)
    # last_name(Optional.
    # 30
    # characters or fewer.)
    # email(Optional.Email
    # address.)
    # password(Required.
    # 50
    # characters or fewer.Password
    # must
    # contain
    # Letters, numbers, symbols(_, @, +,.-))
    # Methods:
    # get_username()(Returns
    # the
    # username
    # for the user)
    # get_full_name()(Returns
    # the
    # first_name
    # plus
    # the
    # last_name,
    # with a space in between.)
    # get_short_name()(Returns
    # the
    # first_name.)
    # set_password(raw_password)(Sets
    # the
    # user’s
    # password)
    # check_password(raw_password)(Returns
    # True if the
    # given
    # raw
    # string is the
    # correct
    # password
    # for the user.)
    # is_valid()(Returns
    # True,
    # if all the fields are valid.)
    # Protected
    # methods:
    # _is_valid_username()
    # _is_valid_first_name()
    # _is_valid_last_name()
    # _is_valid_email()
    # _is_valid_password()
    def __init__(self, name="string"):
        super(User, self).__init__()
        self.name = name
    def __str__(self):
        return "name: {}".format(self.name)
        