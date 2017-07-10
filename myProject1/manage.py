from entity.user1 import User

users = [User(usernames="user.YURIY", first_name="YURIY", last_name="last.YURIY",
              email="yuriy.semesyuk@yahoo.com", password="abcd12344"),
         User(usernames="user.TANYA", first_name="TANYA", last_name="last.TANYA",
              email="yuriy.semesyuk@yahoo.com", password="abcd12344"),
         User(usernames="user.IHOR", first_name="IHOR", last_name="last.IHOR",
              email="IHOR@yahoo.com", password="abcd12344"),
         User(usernames="user.KATYA", first_name="KATYA", last_name="last.KATYA",
              email="KATYA@yahoo.com", password="")]

for user in users:
    print(user.get_username())
    print(user.is_valid())
    # print(user.get_full_name())
    # print(user.get_short_name())
    # print(user._is_valid_email())
    # print(user._is_valid_username())
    # print(user._is_valid_first_name())
    # print(user._is_valid_last_name())
