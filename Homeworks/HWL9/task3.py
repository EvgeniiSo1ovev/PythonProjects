"""
Создать метакласс для паттерна Синглтон (см. конец вебинара)
"""


class MyMetaClass(type):
    obj = None

    def __new__(mcs, clsname, bases, clsdict):
        return super(MyMetaClass, mcs).__new__(mcs, clsname, bases, clsdict)

    def __init__(cls, clsname, bases, clsdict):
        super(MyMetaClass, cls).__init__(clsname, bases, clsdict)

    def __call__(cls, *args, **kwargs):
        if cls.obj is None:
            cls.obj = super(MyMetaClass, cls).__call__(*args, **kwargs)
        return cls.obj


class MyClass(metaclass=MyMetaClass):
    pass


obj_1 = MyClass()
obj_2 = MyClass()
print(obj_1 is obj_2)
