from entity.user1 import User

users = [User(usernames="YURIY", first_name="eredfberew", last_name="efwefdf"),
         User(usernames="TANYA", first_name="gfefveeregsda", last_name="cdsdfew"),
         User(usernames="IHOR", first_name="gfefvergrga", last_name="ewcec"),
         User(usernames="KATYA", first_name="ssssss", last_name="cwecw"), ]

for user in users:
    print(user.get_username())
    print(user.is_valid())
    #print(user._is_valid_username())
    #print(user._is_valid_first_name())
    #print(user._is_valid_last_name())
    #print(user.get_full_name())
    #print(user.get_short_name())