k = '4132'
q = 0
a = k[2]
b = k[3]
c = k[2] + k[3]
for i in str(c):
    q += int(i)
# print (q)
w = 0
d = k[0]
e = k[1]
f = (k[0] + k[1])
for i in str(f):
    w += int(i)
# print (w)
if q == w:
    print ('It`s the same number! = ', (q) or (w))
else:
    print "Error"