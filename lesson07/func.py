# -*- coding: utf-8 -*-
# def my_func():
#     print "temp"

# my_func()
# print my_func()

# def my_func(a=1, c=1, b=10):
#     print "a:{} b:{} c:{}".format(a,b,c)
#     result = a+b+c
#     return result

# d = my_func(5, 9)
# print d
# print my_func(7, 12)
# print my_func(1,1)
# print my_func(1, 2)
# print my_func(c=1, a=2)
# print my_func(b=1, a=1, c=2)
# aa, bb, cc= 9, 8, 7
# print my_func(aa, bb, cc)

# def my_func(a=1, c=1, b=10, *ar, **di):
#     print "a:{} b:{} c:{} arg:{} dict:{}".format(a,b,c,ar, di)
#     result = a+b+c
#     return result
# print my_func(1,2,3,4,5,5)
# print my_func(1,2,3,4,5,5,k=12,p=10)
# l = (9,8,7)
# print my_func(a=l[0], b=l[1], c=l[2])
# print my_func(*l)
# d = {"c":12, "b":10, "a":5,"t":1}
# print d
# print my_func(a=d["a"], b=d["b"], c=d["t"])
# print my_func(*d)
# print my_func(**d)

# def my_sum(arg1, arg2):
#     total = arg1 + arg2
#     print "Inside the function : ", total
#     return total
#     print "After operator the return "

# print my_sum(9,10)
print dir()
for i in range(1):
    t = [1,2,3]
    print dir()
    print i
print dir()
b = [1,2,3]
def my_func(a=1, d=1):
    g = 10
    b.append("a")
    print "in ", dir()
    print "b: ", b
    return g+a

print dir()
print my_func(5)
print "b", b
print dir()