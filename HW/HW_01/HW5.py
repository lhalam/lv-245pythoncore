
#g1 = 360 / 60
#g2 = 360 / 12
#g3 = 30 / 60#
#  #
#if (0 <= h <= 11 and 0 <= m <= 59 and 0 <= s <=59 ):
#    s1 = s * g1
#    m1 = m * g1 + (s1 / 60)
#    h1 = h * g2 + ((m1 / g1) * g3)
#    print ("h:",h1,"\nm:",m1,"\ns:",s1)

h = 7
m = 15
s = 30

if(0 <= h <= 11 and 0 <= m <= 59 and 0 <= s <=59 ):
    hou = (h * 30) + (m * 0.5)
    min = (m * 6) + (s * 0.1)
    sec = s * 6

    print (hou, min, sec)