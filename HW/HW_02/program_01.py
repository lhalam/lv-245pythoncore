a = 1
b = 1
c = 1
x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))

def fun(a,x):
    n = 0
    while n < 31:
        n += 1
        a += 1
        c = a*(x**n)
    return c

print (((fun(a,x) + a)**2) - (fun(b,y) + b))/(fun(c,(x + z)) + c)




