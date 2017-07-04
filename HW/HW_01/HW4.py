
k = int(input("vedit kilkist sukynd:    "))
if k >=0:
    s = k % 60
    m = ((k - s) // 60) % 60
    h = k // 60 // 60
    print(h, m, s)
