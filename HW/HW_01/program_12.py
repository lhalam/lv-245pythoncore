a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

d = (b**2) - (4*a*c)
if d > 0:
    print 'x1 = ', (-b + (d**0.5)) / (2 * a)
    print 'x2 = ', (-b - (d**0.5)) / (2 * a)
elif d == 0:
    print 'x = ', (-b)/(2*a)
else:
    print 'No solution'
