x = str(input('x = '))

if len(x) != 3:
    print 'Your number must contain three characters'
else:
     print x[::-1]