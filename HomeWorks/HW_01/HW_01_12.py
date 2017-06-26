a = 3
b = 6
c = 2

D = int(b ** 2) - int(4) * int(a) * int(c)
print("D = ", D)

if D > 0:
    D = (int(D) ** 0.5)
    print("D = ", D)
    x1 = (-b + D) / (2 * a)
    print("x1 = ", x1)
    x2 = (-b - D) / (2 * a)
    print("x2 = ", x2)
elif D == 0:
    D = -b / (2 * a)
    print("Hight x = ", D)
else:
    print("Dont have")
