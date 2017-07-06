# class ClassName():
#     pass
# a = ClassName()
# print dir(a)
# print type(ClassName)
# class ClassName(object):
#     pass
# a = ClassName()
# # print dir(a)
# print type(ClassName)


# class Point(object):
#     x = 0
#     y = 0
#     def __init__(self, z=0):
#         self.z = z
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
    y = [1,2]
    def __init__(self):
        self.s_x = 99
        self.s_y = [2,2]
        # print dir()
    def __str__(self):
        return "x:{} y:{} s_x:{} s_y{}".format(
            self.x, self.y, self.s_x, self.s_y)
    def __repr__(self):
        return "({} {} {} {})".format(
            self.x, self.y, self.s_x, self.s_y)
    def __eq__(self, other):
        print "__eq__"
        if self.s_x == other.s_x:
            return True
        else:
            return False
    def sum(self):
        return self.x + self.s_x


e1 = Exp()
e2 = Exp()
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
print e1
print e2
print e1.sum()
def myf(self):
    return self.x - self.s_x
Exp.sum = myf
print e1.sum()

es = [Exp(), Exp()]
print es

print e1 == e2

print "clas name: ", __name__