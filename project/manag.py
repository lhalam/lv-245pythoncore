from entity.user import User

users = [User(username="Ihor", first_name="Ihor", last_name="Kapiy", password="nksm21", email="kapi@.ua"),
         User(username="Olehovuch", first_name="Oleh", last_name="Kalinich", password="123", email="sara09@mail.ru"),
         User(username="Sasha", first_name="Oleksandr", last_name="Danuliv", password="sd23-+w", email="dina@m.com"),
         User(username="Katerine", first_name="Kate", last_name="Kislova", email="oleh.@gmail.com", password="psd._")]
for user in users:
    print user.get_username()
    print user.is_valid()


# 1)ств клас профайл який є похідним від класу юзер і містить поля:
# -дата нар
# -стать
# -аватар(стрінга нейм)
#
# Визн методи:
# -get_age
# -get_sax
# -1 property
# -get_avatar
# -get_birthday
#
#
#
#
# 2)Ств профайли для 2-х користувачів. Вивести First i Lastname тих хто неповнолітні