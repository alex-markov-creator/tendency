#-*- coding: utf-8 -*-
"""
Реализация шаблона "Одиночка" через метакласс
"""
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

if __name__ == '__main__':
    class MyClass(object, metaclass=Singleton):
        pass

    class Spam(object):
        pass

    a = MyClass()
    b = MyClass()
    c = Spam()
    d = Spam()
    print(a)
    print(b)
    print(c)
    print(d)
