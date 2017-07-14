h = int(input('hour = '))
m = int(input('mimute = '))
s = int(input('second = '))

if (0 <= h <= 11) and (0 <= m <= 59) and (0 <= s <= 59 ):
    h1 = h * 30
    m1 = m * 0.5
    s1 = s * 0.008
    x = h1 + m1 + s1
    print '%.3f' % x
