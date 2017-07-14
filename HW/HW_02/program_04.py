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




