from entity.user1 import User
from entity.user1 import Profaile


users = [Profaile(username="user_YURIY", first_name="YURIY", last_name="last_YURIY",
                  email="yuriy.semesyuk@yahoo.com", password="abcd12344"),
         Profaile(username="user_TANYA", first_name="TANYA", last_name="last_TANYA",
              email="yuriy.semesyuk@yahoo.com", password="abcd12344"),
         Profaile(username="user_IHOR", first_name="IHOR", last_name="last_IHOR",
              email="IHOR@yahoo.com", password="abcd12344"),
         Profaile(username="user_KATYA", first_name="KATYA", last_name="last_KATYA",
              email="KATYA@yahoo.com", password="bhrt")]

profailes = [Profaile(sex="men1", date_of_birth=(1993, 4, 29), avatar="foto1"),
             Profaile(sex="men2", date_of_birth=(1993, 7, 29), avatar="foto2"),
             Profaile(sex="men3", date_of_birth=(1993, 1, 29), avatar="foto3"),
             Profaile(sex="men4", date_of_birth=(1993, 12, 28), avatar="foto4")]

ihor=Profaile()
ihor.set(username="user_YURIY", first_name="YURIY", last_name="last_YURIY",
         email="yuriy.semesyuk@yahoo.com", password="abcd12344",
         sex="men", date_of_birth=(2000, 4, 29), avatar="foto")
#print(ihor.username)
#print(ihor.get_username())
#print(ihor.get_profile())
#print("++++++++++++++++++++++++++++++++++++++++",
#      "\nUsername:  ", ihor.get_username(),
#      "\nFull Name: ", ihor.get_full_name(),
#      "\nAge:       ", ihor.get_age(),
#      "\nEmail:     ", ihor.get_email(),
#      "\nSex:       ", ihor.get_sex(),
#      "\nBirth:     ", ihor.get_date_of_birth(),
#      "\nAvatar:    ", ihor.get_avatar(),
#      "\n++++++++++++++++++++++++++++++++++++++++")
for profaile in profailes:
    for i in profaile.get_profile():
        #print(i, ihor.get_profile()[i])
        print(i, profaile.get_profile()[i])


#for user in users:
    #print(user.get_username())
    #print(user.is_valid())
    #print(user.get_full_name())
    #print(user.get_short_name())
    #print(user._is_valid_email())
    #print(user._is_valid_username())
    #print(user._is_valid_first_name())(1993, 5, 24)
    #print(user._is_valid_last_name())


#for profaile in profailes:
#    print(profaile.get_sex())
#    print(profaile.get_age())
#    print(profaile.get_date_of_birth())
#
#
#
#print("++++++++++++++++++++++++++++++++++++")




