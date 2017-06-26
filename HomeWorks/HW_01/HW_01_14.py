# -*- coding: utf-8 -*-
k = '413'
q = 0
c = k[0] + k[1] + k[2]
# print c

for i in str(c):
    q += int(i)
# print q
q1 = q**3
# print q1

k = int(k)
w = k**2
# print w

if q == w:
    print ('It`s the same number! = ', (q) or (w))
else:
    print " The square of the k  is not equal  of cube of the sum number of digits of the k!"