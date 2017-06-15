# -*- coding: utf-8 -*-
# s = "tekst"
# print type(s)
# s = u"tekst"
# print type(s)
# s = 1
# print type(s)
# s = '1a'
# print type(s)
# print u"tekst" == "tekst"
# print type("tekst") == type("tekst")
# print type("tekst") == type(u"tekst")
# print "1" == 1
# s = "012345678945"
# print s[1], s[-2]
# print s[0:-2], s[:-2], s[-2:]
# print s[0:4], s[0:4:2], s[::2]
# print s[::-1]
# print s
# print dir(s)
# print s.find('45')
# print s.find('46')
# print s.count('45')
# print "ghasvdhfj1".isalpha()

# print "name %s age %f" % ("Roma", 25)
# print "name {} age {}".format("Roma", 25)
# print "name {1} age {0}".format("Roma", 25)
# print "name {1} age {2}".format(3, "Roma", 25)
# print "name {1} age {2}{0}{1}{2}".format(3, "Roma", 25)

# i = 10
# print i
# i = 010
# print i
# i = 0x10
# print i
# i = int("10")
# i = int("AA",16)
# print type(i), i
# i = len(str(int(2**31)**10000))
# print type(i), i

# i = 10
# print type(i), i
# i = 10L
# print type(i), i
# a = 2**20
# b = 2**20
# print a is b, a == b
# a = 2
# b = 2
# a +=1
# print a is b, a == b
# print b

# i = float(0.5)
# i = 0.5
# i = .5
# print (float(0.5), 0.5, .5)
# print (float(5), 5.0, 5.)
# print (-1.54E-21)
# print (-154E-23)

# a, b = 8, 3
# print a/b
# print round(2.123456789, 5), round(2.5), round(2.99), round(-2.99)
# print a//b
# print a%b
print 9**2
print 9**0.5
print 9**-0.5
print 0.5**-0.5
# print (-10)**0.5
# print (-10)**2.5
def f(a):
    a *= 2 
    print a
    

c = 10
b = f(c)
print c, b