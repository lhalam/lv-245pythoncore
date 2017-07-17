class __MyClass(object):
    name = "name"

    def __init__(self, y=1, _y=2, __y=3):
        self.x = y
        self._x = _y
        self.__x = __y

    def __str__(self):
        return "x:{} _x:{} __x:{}".format(self.x, self._x, self.__x)


a = __MyClass()
print
a
print
a.x
print
a._x
print
a._MyClass__x
print
dir(a)
