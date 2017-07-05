n = float(input("Vvedit chuslo:   "))

if 0 <= n <= 360:
    h = 30
    m = 6
    h1 = n // h
    h2 = h % 30
    m1 = h2 // m
    print (n , h1, m1,)