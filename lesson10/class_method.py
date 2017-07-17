class MyClass(object):
    name = "name"

    def __init__(self, arg=None):
        self.arg = arg

    def print_self(self):
        print[i
        for i in dir(self) if i[0] != "_"]

    @classmethod
    def print_cls(cls):
        print[i
        for i in dir(cls) if i[0] != "_"]

    @staticmethod
    def static_print(_str=""):
        print
        _str

    @classmethod
    def class_method(cls):
        print
        cls

    @classmethod
    def add_new_method(cls, func):
        cls.new_method = func


l = [MyClass(), MyClass(), MyClass()]
# for i in range(len(l)):
#     print i,
#     l[i].print_self()
#     l[i].print_cls()
l[0].arg2 = 1
MyClass.arg3 = 1


# for i in range(len(l)):
#     print i,
#     l[i].print_self()
#     l[i].print_cls()

def my_f(self):
    print
    "my_f",
    print
    self


# l[0].f = my_f

# for i in range(len(l)):
#     print i,
#     l[i].print_self()
#     l[i].print_cls()
# l[0].f(1)
MyClass.f = my_f
# for i in range(len(l)):
#     print i,
#     l[i].print_self()
#     l[i].print_cls()

l[0].f()

MyClass.add_new_method(my_f)
for i in range(len(l)):
    print
    i,
    l[i].print_self()
    l[i].print_cls()

l[0].new_method()

from ppp import __MyClass

c = __MyClass()
print
c
print
c.x
print
c._x
print
c._MyClass__x
