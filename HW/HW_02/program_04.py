a = [ [1,2,3,4,5], [9,8,7,6,5], [1,43,6,8,3], [4,7,5,1,3], [3,4,10,4,7] ]
b = [ [1,2,3,-3,5], [9,-30,7,6,5], [1,5,6,44,3], [4,7,5,33,100], [3,4,10,4,8] ]



def fun(x):
    n = 0
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j] > n:
                n = x[i][j]


    return n



print fun(a)
print fun(b)



