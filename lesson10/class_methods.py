class MyClass:
    def __init__(self, arg=None):
        self.arg = arg

    def my_print(self):
        print(self)

    @staticmethod
    def static_print(_str=''):
        print(_str)

    @classmethod
    def class_method(cls):
        print(cls)


obj = MyClass('test_1')
obj.my_print()
MyClass.static_print('aa')
obj.static_print('bb')
MyClass.class_method()
