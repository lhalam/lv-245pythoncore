# -*- coding: utf-8 -*-

l = []
print type(l), l
l = list()
print type(l), l
l = [1,2,3]
print type(l), l
l = list((1,2,3,4))
print type(l), l
l = list("str")
print type(l), l
print [i for i in dir(l) if not i[:2] == "__"]
l.append(5)
print type(l), l
for i in l:
    print i, type(i)
l = [str(i) for i in l]
print type(l), l
print l.count("5")
l.append((5, 6, 7))
print type(l), l
for i in l:
    print i, type(i)
l.extend((1,2,3,4,5,5,5))
print type(l), l
for i in l:
    print i, type(i)
l.remove(5)
l.sort(lambda a, b: a<b)
print "l1", l
l.reverse()
print "l1", l, l[::-1]
print l
l[1], l[3] = "ST", "END"
print l

l = ()
print type(l), l
l = tuple()
print type(l), l
print [i for i in dir([]) if not i[:2] == "__"]
print [i for i in dir(()) if not i[:2] == "__"]
l = (1,2,3,"vgdsf")
print l
# l[1], l[3] = "ST", "END"
l = l+l 
print l
t = [5, 'ST', 4, 'END', 2, 1, (5, 6, 7), '5', 'r', 't', 's']
l = tuple(t)
print t.__sizeof__()
print l.__sizeof__()


# print help(list)
l = {}
print type(l), l
l = dict()
print type(l), l

print [i for i in dir([]) if not i[:2] == "__"]
print [i for i in dir(()) if not i[:2] == "__"]
print [i for i in dir({}) if not i[:2] == "__"]
l = {10: "str", "1":{"a":1,"b":1},(1,2,3):[1,2,3] }
print l[10]
print l["1"]
print l.get("12")
for i in l:
    print i, l[i]
print l
l.update({10:1234})
print l
l[10] = "dgfkjd"
print l
l[11] = 12
l.update({33:1234})
print l
t = {i:chr(i) for i in range(200)}
c=0
for i in t:
    print i, t[i], '\t',
    if not c % 10:
        print
    c +=1

