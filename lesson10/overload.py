class A(object):
    def __init__(self, x):
        self.x = x

    def my_print(self):
        print[i
        for i in dir(self) if i[0] != "_"]

    def sum(self):
        return self.x


class B(A):
    def __init__(self, x, y):
        super(B, self).__init__(x)
        self.y = y

    def my_print(self):
        print
        self.x, self.y

    def sum(self):
        return self.x + self.y


a = A(1)
a.my_print()
b = B(1, 2)
b.my_print()
print
a.sum()
print
b.sum()
