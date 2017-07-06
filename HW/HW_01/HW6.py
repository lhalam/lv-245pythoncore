n = float(input("Vvedit chuslo float:   "))

if 0 <= n <= 360:

    m1 = n * 2
    h = m1 // 60
    m2 = m1 - (60 * h)

    print ("h-",int(h), "   m-",int(m2))
