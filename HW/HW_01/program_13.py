k = str(input('sum = '))

if len(k) != 4:
    print 'Your number must contain four characters'
elif k[0]+k[1]==k[2]+k[3]:
    print 'sum = ', int(k[0])+int(k[1])+int(k[2])+int(k[3])
else:
    print 'Not equal'
