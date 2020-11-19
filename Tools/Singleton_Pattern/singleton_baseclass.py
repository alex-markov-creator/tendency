#-*- coding: utf-8 -*-
"""
Реализация шаблона "Одиночка" через базовый класс
"""
class Singleton(object):
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

if __name__ == '__main__':

    class MyClass(Singleton, object):
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