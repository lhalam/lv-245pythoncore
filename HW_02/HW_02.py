# № 1

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





# № 2
m = int(input("m = "))
n = int(input("n = "))

def f(x):
    if x == 0:
        return 1
    else:
        return x * f(x-1)

print (f(n) * f(m)) / f((n + m))






# № 3
x = 'abcd'
y = 'abcd'

def mysort(x,y):
    if sorted(x) == sorted(y):
        return x
    else:
        return 'False'

print mysort(x,y)






# № 4
a = [ [1,2,3,4,5], [9,8,7,6,5], [1,10000,6,8,3], [4,7,5,1,3], [3,4,10,4,7] ]
b = [ [1,2,3,-3,5], [9,-30,7,6,5], [1,5,6,44,3], [4,7,5,33,20000], [3,4,10,4,8] ]
def fun(x):
    n = 0
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j] > n:
                n = x[i][j]
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j] == n:
                return i,j
            else:
                continue


num1 = fun(a)
num2 = fun(b)

print a[num1[0]][num1[1]]
print b[num2[0]][num2[1]]

a[num1[0]][num1[1]],b[num2[0]][num2[1]] = b[num2[0]][num2[1]],a[num1[0]][num1[1]]
print a
print b




# № 5
x = [3, 14, 0, -1, 20, 141, 56]
y = [-10, 100, -12, 5, 38, 13, 60]

def mysort(x):
    my_list = len(x) - 1
    for a in range(0, my_list):
        for i in range(0, my_list - a):
            if x[i] < x[i + 1]:
                x[i], x[i + 1] = x[i + 1], x[i]
    return x

print mysort(x)
print mysort(y)

