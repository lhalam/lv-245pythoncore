k = 1162165
h = str(k)[-3]
print (k, h)

#--------------

x = 65.72
x1 = str(x)
d = x1[x1.find(".") + 1]
print (d)

#--------------

k=853
s=k//100+((k%100)//10)+((k%100)%10)//1
print (s, k)

#--------------

k=13257
h=k//3600
m=(k%3600)//60
print (h, m)

#-------------

h=3
m=0
s=0
f=(h*30)+(m/2)+(s/120)
print (f)

#--------------

f=359.58
h=int(f//30)
m=int(f%60)
print (h, m)

#--------------

k=1
dicday={1:"Mo", 2:"Tu", 3:"We", 4:"Th", 5:"Fr", 6:"St", 0:"Sa"}
dofweek=dicday[k%7]
print (dofweek)

#--------------

x=4
y=7
x, y = y, x
print (x, y)

#-----------------
import math
r=4
l=2*math.pi*r
s = math.pi*(r**2)
v=(4*math.pi*(r**3))/3
print (l, s, v)