# import sys
# import data
# for i in sys.path:
#     print i

# print data.users

# if __name__ == '__main__':
#    pass
######################################
# import sys
# from data import users, profiles as p
# for i in sys.path:
#     print i

# print users
# print p

# if __name__ == '__main__':
#    pass

#############################

import sys
from data import users, profiles as p
for i in sys.path:
    print i

from entity.user import User
# from entity import user
u = User()

print u


if __name__ == '__main__':
   pass