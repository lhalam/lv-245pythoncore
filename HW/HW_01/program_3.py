k = str(input('k = '))

if len(k) < 3:
    print 'Your number must contain more than three characters'
else:
     s = 0
     for i in str(k):
        s += int(i)
     print 's = ' , s
while
