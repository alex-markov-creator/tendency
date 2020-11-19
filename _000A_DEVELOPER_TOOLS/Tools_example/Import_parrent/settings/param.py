#-*- coding: utf-8 -*-
with open(r'C:\Users\a.bezzubov\Desktop\Example\DATA\settings.txt', mode ='r') as file_settings:
    for line in file_settings:
        S = line.split(';')
        screen = '\n'.join(S)

screen = S[0]
color = S[1]

if __name__ == '__main__':
    #Для импортирования модуля из родительского каталога есть несколько вариантов
    #решений этой проблемы: модуль setup.py с импортированием setuptools,
    #путь в sys.path, sys.path(хаки),...

    import os,sys,inspect
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0,parentdir)
    import main

    print(main.x)
