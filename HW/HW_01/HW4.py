
sec = int(input("vedit kilkist sukynd:    "))
if sec >=0:
    s = sec % 60
    m = ((sec - s) // 60) % 60
    h =sec // 60 // 60
    print(h, m, s)