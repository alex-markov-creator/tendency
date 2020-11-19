#-*- coding: utf-8 -*-
"""
Реализация шаблона "Одиночка" через декоратор
"""
def singleton(class_):
    """
    Функция декоратор
    """
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

if __name__ == '__main__':
    @singleton
    class MyClass(object):
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