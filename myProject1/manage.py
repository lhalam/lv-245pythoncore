from entity.user1 import User
from entity.profile import Profile

users = [User(username="user_YURIY", first_name="YURIY", last_name="last_YURIY",
              email="yuriy.semesyuk@yahoo.com", password="abcd12344"),
         User(username="user_TANYA", first_name="TANYA", last_name="last_TANYA",
              email="yuriy.semesyuk@yahoo.com", password="abcd12344"),
         User(username="user_IHOR", first_name="IHOR", last_name="last_IHOR",
              email="IHOR@yahoo.com", password="abcd12344"),
         User(username="user_KATYA", first_name="KATYA", last_name="last_KATYA",
              email="KATYA@yahoo.com", password="bhrt")]

profiles = [Profile(sex="men1", date_of_birth=(1993, 4, 29), avatar="foto1"),
             Profile(sex="men2", date_of_birth=(1993, 7, 29), avatar="foto2"),
             Profile(sex="men3", date_of_birth=(1993, 1, 29), avatar="foto3"),
             Profile(sex="men4", date_of_birth=(1993, 12, 28), avatar="foto4")]

ihor=Profile()
ihor.set(username="user_YURIY", first_name="YURIY", last_name="last_YURIY",
         email="yuriy.semesyuk@yahoo.com", password="abcd12344",
         sex="men", date_of_birth=(2000, 4, 29), avatar="foto")


for i in ihor.get_profile():
    print(ihor.get_profile()[i])

#for user in users:
    #print(user.get_username())
    #print(user.is_valid())
    #print(user.get_full_name())
    #print(user.get_short_name())
    #print(user._is_valid_email())
    #print(user._is_valid_username())
    #print(user._is_valid_first_name())(1993, 5, 24)
    #print(user._is_valid_last_name())


for profile in profiles:
    print(profile.get_sex())
    print(profile.get_date_of_birth())
    print(profile.get_age())
print("++++++++++++++++++++++++++++++++++++")




