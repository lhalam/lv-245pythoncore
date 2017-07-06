#!/usr/bin/python

k = input('Vedit chuslo:    ')
s = 0
i = 0
while i < len(k):
    s = s + int(k[i])
    i = i + 1
print (s)