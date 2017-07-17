class A(object):
    def __init__(self, x):
        self._x = x

    def getx(self):  # method to obtain the value
        print
        "get"
        return self._x

    def setx(self, value):  # method to obtain the value
        print
        "set"
        self._x = value

    def delx(self):  # delete attribute
        del self._x
        # define x as the property

    x = property(getx, setx, delx, "property x")


a = A(99)
# # print a.x
# print a.getx()
# a.setx(88)
# print a.getx()
# # a.delx()
# print a.getx()
print
a.x
a.x = 10
print
a.x
