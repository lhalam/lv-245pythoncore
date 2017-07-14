x = str(input('x = '))

if len(x) != 3:
    print 'Your number must contain three characters'
else:
     sum = 1
     for i in str(x):
        sum *= int(i)
     print 'sum = ' , sum

