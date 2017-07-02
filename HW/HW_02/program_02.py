m = int(input("m = "))
n = int(input("n = "))

def f(x):
    if x == 0:
        return 1
    else:
        return x * f(x-1)

print (f(n) * f(m)) / f((n + m))
