x = str(input('sum = '))

s = 0
for i in str(x):
    s += int(i)

if  len(x) == 3 and (int(x)**2 == int(s)**3):
    print 'Equal'
else:
    print 'Not equal or your number contain more than three characters'