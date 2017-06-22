k = int(input('k = '))

if 0<k<8:
    print k
elif 0< k % 7 == 0:
    print '7'
elif 7<k<356:
    print k % 7
else:
    print 'You entered the wrong number, enter the number from 1 to 365'
