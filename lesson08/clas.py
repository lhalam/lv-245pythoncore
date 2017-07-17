# class ClassName():
#     pass
<< << << < HEAD
#
# a = ClassName()
#
# print(dir(a))
# print(type(ClassName))
#
# class Point():
== == == =
# a = ClassName()
# print dir(a)
# print type(ClassName)
# class ClassName(object):
#     pass
# a = ClassName()
# # print dir(a)
# print type(ClassName)

# class Point(object):
>> >> >> > 808
d968da48f83399b6e92d39325732b4a3786a6
#     x = 0
#     y = 0
#     def __init__(self, z=0):
#         self.z = z
<< << << < HEAD
#     def __str__(self):
#         return 'x: {}, y: {}'.format(self.x, self.y)
#     def my_f(self):
#         return self.x + self.y
#
# p = Point()
# p.x = 10
# p.y = 140
# print(p)
# # print(p.x, p.y)
#
# p2 = Point()
# print(p2)
# print(p)
# p.x = 10
# print(p, p.my_f())
# print(p.__dict__)

print('name: ', __name__)


class Exp():
    x = 12
    y = [1, 2]

    def __init__(self):
        self.s_x = 99
        self.s_y = [2, 2]

    def __str__(self):
        return 'x: {}, y: {}, s_x; {}, s_y: {}'.format(self.x, self.y, self.s_x, self.s_y)

== == == =
#     def __str__(a):
#         return "x:{} y:{}".format(a.x, a.y)

#     def my_f(self):
#         return self.x + self.y

# p = Point()
# p.x = 10
# p.y = 140
# print p
# # print p.x, p.y
# p2 = Point()
# print p2
# print p
# p.x = 10
# print p
# print p, p.my_f()

# print p.__dict__
# # print dir(p)
# print Point.__dict__
# # print my_f()
# # print dir(p)


class Exp(object):
    x = 12
    y = [1, 2]

    def __init__(self):
        self.s_x = 99
        self.s_y = [2, 2]
        # print dir()

    def __str__(self):
        return "x:{} y:{} s_x:{} s_y{}".format(
            self.x, self.y, self.s_x, self.s_y)

    def __repr__(self):
        return "({} {} {} {})".format(
            self.x, self.y, self.s_x, self.s_y)

    def __eq__(self, other):
        print
        "__eq__"
        if self.s_x == other.s_x:
            return True
        else:
            return False

    def sum(self):
        return self.x + self.s_x

>> >> >> > 808
d968da48f83399b6e92d39325732b4a3786a6


e1 = Exp()
e2 = Exp()
<< << << < HEAD

print(e1)
print(e2)

e1.x = 1
print(e1)
print(e2)

e1.y.append(1)
print(e1)
print(e2)


# class Point():
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#     def __repr__(self):
#         return 'x: {}, y: {}'.format(self.x, self.y)
#     def distance(self):
#         result = ((self.x ** 2) + (self.y ** 2)) ** 0.5
#         return result
#     def __eq__(self, other):
#         if self.x == other.x and self.y == other.y:
#             return True
#         else:
#             return False
#
# obj1 = Point()
# obj1.x = 1
# obj1.y = 1
# print(obj1)
# print(obj1.distance())
#
# obj2 = Point()
# obj2.x = 2
# obj2.y = 1
# print(obj2)
# print(obj2.distance())
# # print(obj1 == obj2)
# print(obj1.__eq__(obj2))
# # print(obj1.eqval(obj2))

class Person:
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print('Hello', self.name)

# p = Person('Olexandr')
# p.sayHi()

# class Robot:
#     population = 0
#     def __init__(self, name):
#         self.name = name
#         print(self.name)
#         Robot.population += 1
#     def __del__(self):
#         print('del')
#         Robot.population -= 1
#         if Robot.population == 0:
#             print(self.name, 'was last')
#         else:
#             print('there are', Robot.population, 'robots')
#     def sayHi(self):
#         print('Hello, I am', self.name)
#     def howMany():
#         print('population is: ', Robot.population)
#     howMany = staticmethod(howMany)
#
# dron1 = Robot('Alex')
# dron1.sayHi()
# Robot.howMany()
# dron2 = Robot('Vasil')
# dron2.sayHi()
# Robot.howMany()
# del dron1
# del dron2
# Robot.howMany()
# print(Robot.__doc__)

# from abc import *
#
# class SchoolMember(metaclass=ABCMeta):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('create schoolmember ', self.name)
#     def tell(self):
#         print('Name {}, age {}'.format(self.name, self.age, end=' '))
#
# class Teacher(SchoolMember):
#     def __init__(self, name, age, salary):
#         SchoolMember.__init__(self, name, age)
#         self.salary = salary
#         print('create teacher {}'.format(self.name))
#     def tell(self):
#         SchoolMember.tell(self)
#         print('Salary {}'.format(self.salary))
#
# class Student(SchoolMember):
#     def __init__(self, name, age, marks):
#         SchoolMember.__init__(self, name, age)
#         self.marks = marks
#         print('create student {}'.format(self.name))
#     def tell(self):
#         SchoolMember.tell(self)
#         print('Marks {}'.format(self.marks))
#
# t = Teacher('Zhytenko', 32, 4000)
# s = Student('student1', 20, 50)
#
# print()
# members = [t, s]
# for i in members:
#     i.tell()


# class First:
#     color = 'red'
#     form = 'circle'
#     def changecolor(self, newcolor):
#         self.color = newcolor
#     def changeform(self, newform):
#         self.form = newform
#
# obj1 = First()
# obj2 = First()
#
# print(obj1.color, obj1.form)
# obj1.changecolor('green')
# print(obj1.color)
# obj1.changeform('oval')
# print(obj1.form)

# class YesInit:
#     def __init__(self, one, two):
#         self.fname = one
#         self.sname = two
#
# obj1 = YesInit('peter', 'ok')
# print(obj1.fname, obj1.sname)
#
# class NoInit:
#     def names(self, one, two):
#         self.fname = one
#         self.sname = two
#
# obj2 = NoInit()
# obj2.names('peter', 'ok')
# print(obj2.fname, obj2.sname)

# class Building:
#     def __init__(self, w, c, n=0):
#         self.what = w
#         self.color = c
#         self.numbers = n
#         self.mwhere(n)
#     def mwhere(self, n):
#         if n <= 0:
#             self.where = 'vidsytni'
#         elif 0 < n < 100:
#             self.where = 'maliy vklad'
#         else:
#             self.where = 'osnovnuy vklad'
#     def plus(self, p):
#         self.numbers = self.numbers + p
#         self.mwhere(self.numbers)
#     def minus(self, m):
#         self.numbers = self.numbers - m
#         self.mwhere(self.numbers)
#
# m1 = Building('doski', 'color1', 50)
# m2 = Building('doski', 'color2', 300)
# m3 = Building('kirpich', 'color1')
#
# print(m1.what, m1.color, m1.where)
# m1.plus(50)
# print(m1.numbers, m2.where)
# class Things:
#     def __init__(self, n, t):
#         self.namething = n
#         self.total = t
#
# th1 = Things('table', 5)
# th2 = Things('computer', 7)
#
# print(th1.namething, th1.total)
#
# th1.color = 'green'
#
# print(th1.color)

# class Table:
#     def __init__(self, l, w, h):
#         self.long = l
#         self.width = w
#         self.height = h
#     def outing(self):
#         print(self.long, self.width, self.height)
#
# class Kitchen(Table):
#     def howplaces(self, n):
#         if n < 2:
#             print('It is not kitchen table')
#         else:
#             self.places = n
#     def outplaces(self):
#         print(self.places)
#
# t_room1 = Kitchen(2, 1, 0.5)
# t_room1.outing()
# t_room1.howplaces(5)
# t_room1.outplaces()

# class T1:
#     n = 10
#     def total(self, N):
#         self.total = int(self.n) + int(N)
#
# class T2:
#     def total(self, s):
#         self.total = len(str(s))
#
# t1 = T1()
# t2 = T2()
# t1.total(34)
# print(t1.total)
# t2.total(34)
# print(t2.total)

# input_number = int(input('enter number'))
# class Number:
#     def __init__(self, input_number):
#         self.input_number = input_number
#     def math_operation(self):
#         if -100 < input_number < 100:
#             return input_number ** 2
#         else:
#             input_number * 2
#
# number = Number(input_number)
# print(number.math_operation())

# class One:
#     def __init__(self, a):
#         self.a = a ** 2
#
# class Two:
#     def __init__(self, a):
#         self.a = a * 2
#
# a = input_number
# if  -100 < a < 100:
#     obj = One(a)
# else:
#     obj = Two(a)
# print(obj.a)

# day1 = 1
# hour1 = 0
# min1 = 0
# sec1 = 0
# day2 = 2
# hour2 = 3
# min2 = 4
# sec2 = 5
# all_sec1 = sec1 + (min1 * 60) + (hour1 * 60 * 60) + (day1 * 12 * 60 * 60)
# print(all_sec1)
# all_sec2 = sec2 + (min2 * 60) + (hour2 * 60 * 60) + (day2 * 12 * 60 * 60)
# print(all_sec2)
# diff= all_sec2 - all_sec1
# print('diff', diff)
# diff_day = diff // (12*60*60)
# print('diff_day', diff_day)
# diff = diff - (diff_day * 12 * 60 * 60)
# print(diff)
# diff_hour = diff // (60 * 60)
# print(diff_hour)
# diff = diff - (diff_hour * 60 * 60)
# print(diff)
# diff_min = diff // 60
# print(diff_min)
# diff = diff - diff_min * 60
# print(diff)

# a = open('q.txt', 'w')
# a.close()
# answer = ''
# with open('q.txt', 'r') as imput_time:
#     test_numbers = int(imput_time.readline())
#     for i in range(test_numbers):
#         data = imput_time.readline().split()
#         start_day = int(data[0])
#         start_hour = int(data[1])
#         start_min = int(data[2])
#         start_sec = int(data[3])
#         end_day = int(data[4])
#         end_hour = int(data[5])
#         end_min = int(data[6])
#         end_sec = int(data[7])
#         all_sec_start = start_sec + (start_min * 60) + (start_hour * 60 * 60) + (start_day * (12 * 60 * 60))
#         all_sec_end = end_sec + (end_min * 60) + (end_hour * 60 * 60) + (end_day * (12 * 60 * 60))
#         diff = all_sec_end - all_sec_start
#         print('diff', diff)
#         diff_day = diff // (12 * 60 * 60)
#         print('day', diff_day)
#         diff = diff - (diff_day * 12 * 60 * 60)
#         diff_hour = diff // (60 * 60)
#         print('hour', diff_hour)
#         diff = diff - (diff_hour * 60 * 60)
#         diff_min = diff // 60
#         diff_sec = diff - diff_min * 60
#         if diff_day < 0:
#             diff_day = 0
#         a= ('({} {} {} {})'.format(diff_day, diff_hour, diff_min, diff_sec))
#         answer += a
# print(answer)

# class Base:
#     def __init__(self, N):
#         self.numb = N
#     def out(self):
#         self.numb /= 2
#         print(self.numb)
#
# class Subclass(Base):
#     def out(self):
#         print('\n-----')
#         Base.out(self)
#         print('-----\n')
#
# i = 0
# while i < 10:
#     if 4 < i < 7:
#         obj = Subclass(i)
#     else:
#         obj = Base(i)
#     i += 1
#     obj.out()


# class Win_Door:
#     def __init__(self, x, y):
#         self.square = x * y
#
# class Room:
#     def __init__(self, x, y, z):
#         self.square = 2 * z * (x + y)
#     def win_door(self, d, e, f, g, m=1, n=1):
#         self.window = Win_Door(d, e)
#         self.door = Win_Door(f, g)
#         self.numb_w = m
#         self.numb_d = n
#     def wallpapers(self):
#         self.wallpapers = self.square -\
#             self.window.square * self.numb_w -\
#             self.door.square * self.numb_d
#     def printer(self):
#         print("Square walls = ", str(self.square))
#         print('possible square = ', str(self.wallpapers))
#
# labor34 = Room(5, 4, 2)
# labor34.win_door(1.5, 1.5, 2, 1, 2)
# labor34.wallpapers()
# labor34.printer()
# print(labor34.window.square)
# print(labor34.door.square)

# class Newclass:
#     def __init__(self, base):
#         self.base = base
#     def __add__(self, a):
#         self.base = self.base + a
#     def __str__(self):
#         return '{} !!!'.format(self.base)
#
# a = Newclass(10)
# print(a)
# a + 20
# print(a)
# b = Newclass('asd')
# print(b)
# b + 'ssssss'
# print(b)
# c = Newclass([2,5,8])
# c + [2,6]
# print(c)

# class Changeable:
#     def __init__(self, color):
#         self.color = color
#     def __call__(self, newcolor):
#         self.color = newcolor
#     def __str__(self):
#         return '{}'.format(self.color)
#
# c = Changeable('green')
# print(c)
# f = Changeable('blue')
# print(f)
# c('red')
# print(c)
# f('yellow')
# print(f)

# class Information:
#     def __init__(self, info):
#         self.info = info
#     def extract(self, i):
#         self.current = self.info[i]
#         return '{}'.format(self.current)
#
# class Teacher:
#     def into(self, phrase):
#         self.phrase = phrase
#     def out(self):
#         return '{}'.format(self.phrase)
#
# class Pupil:
#     def __init__(self):
#         self.know = []
#     def take(self, i):
#         self.know.append(i)
#
# inform = Information(['> (bigger)', '< smaller',\
#                       '== equal', '!= not equal'])
# t = Teacher()
# p1 = Pupil()
# p2 = Pupil()
#
# t.into(inform.extract(2))
# p1.take(t.out())
# print(p1.know)
#
# t.into(inform.extract(0))
# p1.take(t.out())
# print(p1.know)
# p2.take((t.out()))
# print(p2.know)


# class A:
#     pass
#
# a = A()
# print(a)
# a.arg = 1
# print(a.arg)


# class MyClass:
#     i = 123456
#
#     def f(self):
#         return 'hello'
# x = MyClass()
# print(x)
# x.f()
# print(x.f())
# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart
#
# x = Complex(3, -4)
# print(x.r, x.i)
#
# x.counter = 1
# print(x.r, x.i, x.counter)
#
# while x.counter < 10:
#     x.counter = x.counter * 2
#     print(x.counter)
# del x.counter
# print(x.r, x.i)






# class Dog:
#     kind = 'canine'
#     def __init__(self, name):
#         self.name = name
#
# d = Dog('fido')
# e = Dog('buddy')
#
# print(d.kind)
# print(d.name)

# class Dog:
#     def __init__(self, name):
#         self.name = name
#     def add_trick(self, trick):
== == == =
# print e1.x
# print e1
# print e2
# e1.x = 1
# print e1
# print e2
# e1.y.append(1)
# print e1
# print e2
# e1.s_x = 1
# print e1
# print e2
# e1.s_y.append(1)
# print e1
# print e2
# print e1.__dict__
# e1.x = 1
# print e1.__dict__
# print e1
# print e2
# Exp.x = 10
# print e1
# print e2
# print Exp.__dict__
# print e1
# print e2
# Exp.x = 8
# print e1
# print e2
# e1.x = 7
# print e1
# print e2
# Exp.x = 88
# print e1
# print e2
# print Exp.s_x
print
e1
print
e2
print
e1.sum()


def myf(self):
    return self.x - self.s_x


Exp.sum = myf
print
e1.sum()

es = [Exp(), Exp()]
print
es

print
e1 == e2

print
"clas name: ", __name__
>> >> >> > 808
d968da48f83399b6e92d39325732b4a3786a6
