from entity.user import User

users = [User(username="421563gfhjdesuif", password="bhjvbhv", first_name = "Vasja1"),
            User(username="421563gfhjdesuif!!!!+.fbjds", password="bhjv@341bhv"),
            User(username="421563gfhjdesuif!!!!+.fbjdsfbgdjhbgdhjbghfdbgbdfkjgbdfkjgbdfkj", password="bh9&(6jvbhv"),
            User(username="421563gfhj+_gh", password="bhj_ui5v)bhv", first_name = "Vasja45", last_name = "Vasichkin", email = "vasja45_sd@tesr.com")]
for user in users:
    print (user.is_valid())