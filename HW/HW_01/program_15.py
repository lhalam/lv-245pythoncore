x = str(input('x = '))

if len(x) != 3:
   print 'Your number contain more than three characters'
elif x[0] == x[1]:
    print x[0]
elif x[1] == x[2]:
    print x[1]
elif x[2] == x[0]:
    print x[2]
else:
    print 'There are no identical characters'

