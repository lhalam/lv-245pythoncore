# -*- coding: utf-8 -*-
import datetime
from user import User

class Profile(object):

    def __init__(self, username, password, first_name=None, last_name=None,
                email=None, date_of_birthday=None, sex=None, avatar=None):
        super(Profile, self).__init__(username, password, first_name, last_name, email)

        self.date_of_birthday = date_of_birthday
        self.sex = sex
        self.avatar = avatar


    def get_age(selfself):
        today = datetime.date.today()
        age = today - datetime.date.today()
        return age

    def get_sex(self):
        return self.sex

    def get_avatar(self):
        return self.avatar

    def get_birthday(self):
        return self.date_of_birthday

    def _is_adult(self):
        if self.get_age() < 18:
            print self.first_name, self.last_name
        else:
            return False


    if __name__== '__main__':
        users = [Profile(username="Sasha", password="sd23-+w", first_name="Oleksandr", last_name="Danuliv",
                 email="dina@m.com", date_of_birthday="1989, 10, 03", sex="men", avatar="dcsl"),
                 Profile(username="Katerine", password="psd._", first_name="Kate", last_name="Kislova",
                 email="oleh.@gml.com", date_of_birthday="1999, 06, 12", sex="women", avatar="adress")]
        for User in users:
            if user.adult():
                print user






