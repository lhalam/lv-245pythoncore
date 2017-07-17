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
# print 9**2
# print 9**0.5
# print 9**-0.5
# print 0.5**-0.5
# # print (-10)**0.5
# # print (-10)**2.5
# def f(a):
#     a *= 2
#     print a
#
#
# c = 10
# b = f(c)
# print c, b
# print help(list)


# class MyClass:
#     i = 123
#
#     def f(self):
#         return 'hello'
#
# print(MyClass.f)
# x = MyClass()
# print(x)

# class Complex:
#     def __init__(self, r, i):
#         self.r = r
#         self.i = i
# x = Complex(3, 4)
# x.r, x.i
# x.counter = 1
# while x.counter < 10:
#     x.counter *= 2
#     print(x.counter)
# print(x.counter)
# del x.counter
# print(dir(x))

# x.f()
# print(x.f())
# print(MyClass.f(x))
# class C:
#     pass
#
# class Dog(C):
#     # kind = 'canine'
#     tricks = []
#     def __init__(self, name):
#         self.name = name
#     def add_trick(self, trick):
#         self.tricks.append(trick)
# f=  2
# d = Dog('Fibo')
# e = Dog('Buddy')
# d.add_trick('roll over')
# # print(dir(d))
#
# print(isinstance(d, Dog))
# print(issubclass(C, Dog))

# s = 'asd'
# it = iter(s)
# # print(it)
#
# print(next(it))

# class Reverse:
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index -= 1
#         return self.data[self.index]
#
# for i in Reverse('asdf'):
#     print(i)

# def reverse(data):
#     for i in range(len(data)-1, -1, -1):
#         yield data[i]
#
# print(reverse('asd'))

# print(sum(i*i for i in range(10)))
