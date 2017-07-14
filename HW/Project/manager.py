from Entity.User import User

users = [User(username="gdfggd%f",password="dssddfsd"),
          User(username="1123",password="dssddf11sd"),
          User(username="sdfds",password="dssdd@fsd"),
          User(username="@dds33",password="dssddf34@sd")]


for user in users:
     print user._is_valid_username()
     print user._is_valid_first_name()
     print user._is_valid_last_name()
     print user._is_valid_email()
     print user._is_valid_password()
     print "------------------------"

