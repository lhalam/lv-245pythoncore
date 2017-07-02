x = "abcd"
y = "bcad"


def fun(x,y):
    a = 0
    for i in range(len(x)):
        for j in range(len(x)):
            if x[j] is y[i]:
                a += 1
                if a == len(x):
                    return x

print fun(x,y)
