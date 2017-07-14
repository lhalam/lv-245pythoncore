x = str(input('x = '))

if len(x) != 4:
    print 'Your number must contain four characters'
else:
     sum = 1
     for i in str(x):
        sum *= int(i)
     print 'sum = ' , sum

