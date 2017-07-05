x = 'abcd'
y = 'abcd'

def fun(x,y):
    a = False
    if len(x) == len(y):
        for i in range(len(x)):
            if x[i] in y:
                a = True
            else:
                a = False
                break
    if a:
        return x
    else:
        return 'False'

print fun(x,y)