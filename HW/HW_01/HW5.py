g1 = 360 / 60
g2 = 360 / 12
g3 = 30 / 60
h = 11
m = 30
s = 30

if (0 <= h <= 11 and 0 <= m <= 59 and 0 <= s <=59 ):
    s1 = s * g1
    m1 = m * g1 + (s1/60)
    h1 = h * g2 +((m1 / g1) * g3)
    print ("h:",int(h1),"\nm:",int(m1),"\ns:",int(s1))