x = 'abcd'
y = 'abcd'

def mysort(x,y):
    if sorted(x) == sorted(y):
        return x
    else:
        return 'False'

print mysort(x,y)

