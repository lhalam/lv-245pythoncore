
#-------1-------

k = 1162165
h = str(k)[-3]
print (k, h)

#-------2-------

x = 65.72
x1 = str(x)
d = x1[x1.find(".") + 1]
print (d)

#-------3-------

k = 853
s= k // 100 + ((k % 100) // 10) + ((k % 100) % 10) // 1
print (s, k)

#-------4-------

k = 13257
h = k // 3600
m = (k % 3600) // 60
print (h, m)

#-------5------

h = 3
m = 0
s = 0
f = (h * 30) + (m / 2) + (s / 120)
print (f)

#-------6-------

f = 359.58
h = int(f // 30)
m = int(f % 60)
print (h, m)

#-------7-------

k = 1
dicday = {1:"Mo", 2:"Tu", 3:"We", 4:"Th", 5:"Fr", 6:"St", 0:"Sa"}
dofweek = dicday[k % 7]
print (dofweek)

#-------8-------

x = 4
y = 7
x, y = y, x
print (x, y)

#---------9--------
import math
r = 4
l = 2 * math.pi * r
s = math.pi * (r ** 2)
v = (4 * math.pi * (r ** 3)) / 3
print (l, s, v)

#--------10--------

k = 2456
ch = str(k)
s = int(ch[0])+int(ch[1])+int(ch[2])+int(ch[3])
print (s)

#---------11----------

a = 745
b = str(a)[::-1]
print (b)

#---------12-----------

a = 5
b = 7
c = 1
d = b ** 2 - (4 * a * c)
if d > 0:
	x = (-b + d ** 0.5) / (2 * a)
	y = (-b - d ** 0.5) / (2 * a)
	print (x, y)
elif d == 0:
	x = (-b) / (2 * a)
	print (x)
else:
	print ("Has no solution")

#----------13----------

k = 3526
l = str(k)
if (int(l[0]) + int(l[1])) == (int(l[2]) + int(l[3])):
	print (int(l[0]) + int(l[1]))

#----------14-----------

k = 734
if k ** 2 == (k // 100 + (k % 100) // 10 + ((k % 100) % 10) // 1) ** 3:
	print (True)

#---------15-----------

k = 355
a = str(k)
if a[0] == a[1]:
	print (a[0], a[1])
elif a[0] == a[2]:
	print (a[0], a[2])
elif a[1] == a[2]:
	print (a[1], a[2])

#--------16----------

x = 5 # координати цілі
y = 3 # координати цілі
x1 = 7 # координати ходу
y1 = 4 # координати ходу
flag = False
if x1 != x and y1 != y and 1 <= x1 <= 8 and 1 <= y1 <= 8:
	if (x1 - 1) == x and (y1 - 2) == y:
		flag = True
	elif (x1 + 1) == x and (y1 + 2) == y:
		flag = True
	elif (x1 - 2) == x and (y1 - 1) == y:
		flag = True
	elif (x1 + 2) == x and (y1 - 1) == y:
		flag = True
print (flag)

#---------17---------

k = 654
s = (k // 100) * ((k % 100) // 10) * (((k % 100) % 10) // 1)
print (s)