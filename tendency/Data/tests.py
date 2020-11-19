# -*- coding: utf-8 -*-
"""
tests.py - таблица переменных
"""
import sys
import os

import matplotlib.pyplot as plt # библиотека для построения графиков
from prettytable import PrettyTable # импорт библиотеки для вывода табличных данных в консоли(терминале)

try:
    sys.path.append(os.path.realpath('..')) # субродительский каталог в sys.path, для импорта из субродителского каталога
    import Tools.Abstract_Parents as Abstract # универсальный модуль для выполнения контракта
except Exception:
    print("Ошибка при импорте абстрактных классов!!!")

try:
    print('Загрузка...pandas.DataFrame объектов')
    from data_for_tests import *
except Exception:
    print ('Ошибка при импорте БД!!!')

class FirstGraphic(Abstract.Graphic):
    """
    Класс тестового графика
    """
    def __init__(self, data):
        super().__init__(data)
        pass

if __name__ == '__main__':
# НЕОБХОДИМ РЕФАКТОРИНГ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    score = 0
    for i in info_name.keys():
        score += 1
    print('Количество показателей: {}'.format(score))
    ident = [i for i in range(score)]
    x = PrettyTable()
    field_names = ['Идентификатор','Показатель','Переменная']
    a = [i +'...' for i in list(info_name.values())]
    x.add_column(field_names[0], list(ident))
    x.add_column(field_names[1],a)
    #x.add_column(field_names[2],list(info_name.keys()))
    print(x)
    d = dict(zip(range(score), lst_name))
    print('Загрузка завершена!')
    while True:
        try:
            v = input("Укажите идентификатор(выход - 'exit'): ")
            if v == 'exit':
                break
            else:
                print(d[int(v)])
                g = FirstGraphic(d[int(v)]) # экземпляр класса второго графика
                g.test_graphic() # Построение "Тест-графика""
                plt.show()
        except:
            print("Такого идентификатора не существует")


