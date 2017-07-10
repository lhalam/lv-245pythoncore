import datetime
from user import User

class Profile(User):	
	def __init__(self, date_birthday, sex, avatar, username, password, first_name=None, last_name=None, email=None):
		super(Profile, self).__init__( username, password, first_name, last_name, email)
		self.date_birthday = date_birthday
		self.sex = sex
		self.avatar = avatar

	def get_age(self):
		today = datetime.date.today()
		# delta = today - datetime.date(*map(int,(self.date_birthday.split(','))))
		y, m, d = map(int,(self.date_birthday.split(',')))
		delta = today - datetime.date(y, m, d)
		
		return delta.days/365 # self.today.year - self.date_birthday.year

	def get_sex(self):
		return self.sex

	def get_avatar(self):
		return self.avatar

	def get_birthday(self):
		return self.date_birthday

	def adult(self):
		if self.get_age() > 18:
		    print self.first_name, self.last_name

if __name__ == '__main__':
    users = [Profile(username="421563gfhj+_gh", password="bhj_ui5v)bhv", first_name = "Vasja45", last_name = "Vasichkin",\
             email = "vasja45_sd@tesr.com", date_birthday = "1980, 07, 14", sex = "Men", avatar = "adress"),
             Profile(username="alisa+_gh", password="25bhj_ui5v)bhv", first_name = "Alisa", last_name = "Lvivska",\
             email = "alisa12_sd@tesr.com", date_birthday = "2005, 06, 25", sex = "Women", avatar = "adress")]
    for user in users:
    	if user.adult():
    		print user