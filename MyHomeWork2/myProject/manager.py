from entity.user import User

users = [User(username="421563gfhjdesuif"),
          User(username="421563gfhjdesuif!!!!+.fbjds"),
          User(username="421563gfhjdesuif!!!!+.fbjdsfbgdjhbgdhjbghfdbgbdfkjgbdfkjgbdfkj"),
          User(username="421563gfhj?desuif!!!!+.fbjds")]
for user in users:
    # print user._is_valid_username()
    print user.is_valid()