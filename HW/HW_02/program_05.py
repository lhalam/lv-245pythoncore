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



