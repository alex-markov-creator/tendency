# -*- coding: utf-8 -*-
# version 0.1a
# author: andrew.bezzubov - 27/10/2020 year
"""
=============================================================================
adhaesio.py - модуль обработки данных по показателям качества характеризующих адгезию.
=============================================================================

Показатели:
-----------
1 Адгезия ленты к праймированной стальной поверхности при температуре
(20 "плюс минус 3" градусов по Цельсию), Н/см, не менее 15-20 Н/см,
обозначение в таблице - "к стали";
2 Адгезия ленты к праймированной стальной поверхности с подплавлением мастичного слоя при температуре (20 "плюс минус 3" градусов по Цельсию), Н/см, не менее 15-20 Н/см,;
обозначение в таблице - "с подплавл"
3 Адгезия ленты к ленте в нахлесте при температуре
(20 "плюс минус 3" градусов по Цельсию), Н/см, не менее 7-15 Н/см,
обозначение в таблице - "в нахлест".

Критерии значений по наименованию соответственно:
-------------------------------------------------
ПИРМА-З - 20 Н/см, 20 Н/см, 15 Н/см;
ПИРМА-Л - 20 Н/см, 20 Н/см, 15 Н/см;
ЛИТКОР-З_газ - 20 Н/см, 20 Н/см, 15 Н/см;
ЛИТКОР-З_тр_нефть - 20 Н/см, 20 Н/см, 15 Н/см;
ЛИТКОР-Л_газ - 20 Н/см, 20 Н/см, 15 Н/см;
ЛИТКОР-Л_тр_нефть - 20 Н/см, 20 Н/см, 15 Н/см;
ЛИТКОР-НН толщина 1.9 мм. - 20 Н/см, 20 Н/см, 15 Н/см;
ЛИТКОР-НН толщина 2.0 мм. - 20 Н/см, 20 Н/см, 15 Н/см;
ЛИТКОР-НН толщина 1.7 мм. - 20 Н/см, 20 Н/см, 15 Н/см;
БПИ толщина 1.7 мм. - 20 Н/см, 20 Н/см, 7 Н/см;
БПИ толщина 2.0 мм - 20 Н/см, 20 Н/см, 7 Н/см;

Выполняет следующие задачи:
---------------------------
- Редактирование pandas.DataFrame объектов для построения графиков;
- Построение графиков;
- Расчёт и вывод статистических данных;
- Сохранение результатов в файл.

Исходные данные:
----------------
+---------------+---------------------------+---------------------------------+
| Идентификатор |     Наименования лент     |     Наименование переменных*    |
+---------------+---------------------------+---------------------------------+
|      001      |          ПИРМА-З          |         pz, _pz, __pz           |
|      002      |          ПИРМА-Л          |         pl, _pl, __pl           |
|      003      |        ЛИТКОР-З_газ       |    lz_gaz, _lz_gaz, __lz_gaz    |
|      004      |     ЛИТКОР-З_тр_нефть   |lz_tr_neft,_lz_tr_neft,__lz_tr_neft|
|      005      |        ЛИТКОР-Л_газ       |    ll_gaz,_ll_gaz,__ll_gaz      |
|      006      |     ЛИТКОР-Л_тр_нефть   |ll_tr_neft,_ll_tr_neft,__ll_tr_neft|
|      007      | ЛИТКОР-НН толщина 1.9 мм. |    lnn_1_9,_lnn_1_9, __lnn_1_9  |
|      008      | ЛИТКОР-НН толщина 2.0 мм. |   lnn_2_0,_lnn_2_0,__lnn_2_0    |
|      009      | ЛИТКОР-НН толщина 1.7 мм. |   lnn_1_7,_lnn_1_7,__lnn_1_7    |
|      010      |    БПИ толщина 1.7 мм.    |   bpi_1_7,_bpi_1_7,__bpi_1_7    |
|      011      |     БПИ толщина 2.0 мм    |   bpi_2_0,_bpi_2_0,__bpi_2_0    |
+---------------+---------------------------+---------------------------------+
* - Переменная с одним подчеркиванием отформатированные данные для построения графиков в Н/см, с двойным подчеркиванием данные в кг.

Инструкции при импорте:
-----------------------
import pandas as pd
import matplotlib.pyplot as plt
import adhaesio as ad

Построение графиков:
--------------------
a = ad.LinearGraphic(ad._pz) # экземпляр класса линейного графика
a.middle_value_text() # Aср
a.regres_graphic() # построение графика линейной регресии
b = ad.DistributionDiagramm(ad._pz) # экземпляр класса диаграммы распределения
c = ad.DistributionHistogramm(ad._pz) # экземпляр класса гистограммы распределения
d = ad.ErrorGraphic(ad._pz) # экземпляр класса графика погрешностей
e = ad.TableGraphic(ad.pz) # экземпляр класса выборки последних значений
f = ad.DependenceGraphic(ad._lz_gaz)
plt.show()#график на экран

Данные статистических расчетов
--------------------------------
y = ad.Statistic_Table(ad._pz)
print(y.score())
print(y.middle())
print(y.max_min())
print(y.k_cor())
print(y.st_d())
print(y.s_val())
print(y.data_mode())

Вывод исходных данных в виде файла и таблицы
---------------------------------------------
x = ad.Data_Table(ad.pz)
print(x)
x.open_data()

СОХРАНЕНИЕ графиков и результатов
---------------------------------
for i in ad._lst_adhaesio:
    ad.Save_Data(i)

СОХРАНЕНИЕ данных за квартал
----------------------------
for i in ad.lst_adhaesio:
    ad.Save_add_Data(i)

"""
import sys
import os
import subprocess
import time
sys.path.append(os.path.realpath('../..'))
#субродительский каталог в sys.path

from abc import ABC, abstractmethod

import pandas as pd
from pandas.plotting import table # данные в таблице
import numpy as np
import statistics # модуль используется для определния средних значений
import matplotlib.pyplot as plt
import seaborn as sb
from scipy.stats import linregress # модуль для построения линейной регрессии
from tabulate import tabulate
import Tools.Abstract_Parents as Abstract
#универсальный модуль для выполнения контракта

from Data import pz, pl, lz_gaz, lz_tr_neft, ll_gaz, ll_tr_neft, lnn_1_9,lnn_2_0, lnn_1_7, bpi_1_7, bpi_2_0, lst_adhaesio
#импорт DataFrame объектов с исходными данными

from prettytable import PrettyTable # импорт библиотеки для вывода табличных данных в консоли(терминале)

# ИСХОДНЫЕ ДАННЫЕ (ДОПОЛНИТЕЛЬНОЕ ФОРМАТИРОВАНИЕ):
##################################################
try:
    #Список наименований продукции
    LENTA_NAME = [
                    'ПИРМА-З','ПИРМА-Л','ЛИТКОР-З_газ','ЛИТКОР-З_тр_нефть',
                    'ЛИТКОР-Л_газ', 'ЛИТКОР-Л_тр_нефть',
                    'ЛИТКОР-НН толщина 1.9 мм.', 'ЛИТКОР-НН толщина 2.0 мм.',
                    'ЛИТКОР-НН толщина 1.7 мм.', 'БПИ толщина 1.7 мм.',
                    'БПИ толщина 2.0 мм'
                 ]#запись наименований

    _pz = pz.iloc[:,1:4]
    _pl = pl.iloc[:,1:4]
    _lz_gaz = lz_gaz.iloc[:,1:4]
    _lz_tr_neft = lz_tr_neft.iloc[:,1:4]
    _ll_gaz = ll_gaz.iloc[:,1:4]
    _ll_tr_neft = ll_tr_neft.iloc[:,1:4]
    _lnn_1_9 = lnn_1_9.iloc[:,1:4]
    _lnn_2_0 = lnn_2_0.iloc[:,1:4]
    _lnn_1_7 = lnn_1_7.iloc[:,1:4]
    _bpi_1_7 = bpi_1_7.iloc[:,1:4]
    _bpi_2_0 = bpi_2_0.iloc[:,1:4]
    _lst_adhaesio = [
                    _pz, _pl, _lz_gaz, _lz_tr_neft, _ll_gaz,
                    _ll_tr_neft, _lnn_1_9, _lnn_2_0, _lnn_1_7,
                    _bpi_1_7, _bpi_2_0]

    #Итерирование с присвоением наименования индекса pandas.DataFrame объектам
    n = -1
    for i in _lst_adhaesio:
        n+=1
        i.index.name = LENTA_NAME[n]
    #Словарь нименований идентификаторов
    NAME_INPUT_ORIGIN = {
                '001':pz, '002':pl, '003':lz_gaz, '004':lz_tr_neft,
                '005':ll_gaz, '006':ll_tr_neft, '007':lnn_1_9,
                '008':lnn_2_0, '009':lnn_1_7, '010':bpi_1_7,
                '011':bpi_2_0,
                } #идентификатор c с исходными данными

    NAME_INPUT = {
                '001':_pz, '002':_pl, '003':_lz_gaz, '004':_lz_tr_neft,
                '005':_ll_gaz, '006':_ll_tr_neft, '007':_lnn_1_9,
                '008':_lnn_2_0, '009':_lnn_1_7, '010':_bpi_1_7,
                '011':_bpi_2_0,
                } #идентификатор


    # Расчёт значений в кг
    __pz = _pz.apply(lambda x: x/9.80665)
    __pl = _pl.apply(lambda x: x/9.80665)
    __lz_gaz = _lz_gaz.apply(lambda x: x/9.80665)
    __lz_tr_neft = _lz_tr_neft.apply(lambda x: x/9.80665)
    __ll_gaz = _ll_gaz.apply(lambda x: x/9.80665)
    __ll_tr_neft = _ll_tr_neft.apply(lambda x: x/9.80665)
    __lnn_1_9 = _lnn_1_9.apply(lambda x: x/9.80665)
    __lnn_2_0 = _lnn_2_0.apply(lambda x: x/9.80665)
    __lnn_1_7 = _lnn_1_7.apply(lambda x: x/9.80665)
    __bpi_1_7 = _bpi_1_7.apply(lambda x: x/9.80665)
    __bpi_2_0 = _bpi_2_0.apply(lambda x: x/9.80665)
    __lst_adhaesio = [
                    __pz, __pl, __lz_gaz, __lz_tr_neft, __ll_gaz,
                    __ll_tr_neft, __lnn_1_9, __lnn_2_0, __lnn_1_7,
                    __bpi_1_7, __bpi_2_0]

except Exception:
    print(time.ctime(), 'Benchmark_Data_Error: ', sys.exc_info()[:2], file = open('log.txt', 'a'))

try:
    class LinearGraphic(Abstract.Graphic):
        """
        Линейный график со значениеями адгезии, критериями и средними значениями показателей.
        #############################################################
        Пример запуска:
        ---------------
        _pz = _pz.tail(10)
        #10 значений
        gr = LinearGraphics(_pz)
        plt.show()
        """
        def __init__(self, data: pd.DataFrame, name='Название графика', critery_1 = 20, critery_2 = 15, critery_3 = 7):
            """
            Параметры:
            ----------
            data - нименование переменной (см.таблицу выше);
            name - название графика;
            critery_1 - Критерий оценки "к стали";
            critery_2 - Критерий оценки "в нахлест";
            critery_3 - Критерий оценки "в нахлест" - БПИ.
            """
            super().__init__(data)
            self.name = name
            self.critery_1 = critery_1
            self.critery_2 = critery_2
            self.critery_3 = critery_3
            self.data.plot(linestyle='solid', linewidth=2, alpha=1, figsize=(12,8))
            plt.gcf().canvas.set_window_title('Линейный график')
            plt.axhline(critery_1, color ='red', linestyle=':')
            plt.axhline(data.mean().iloc[0], color ='blue', linestyle='dashdot')
            plt.axhline(critery_2, color ='blue', linestyle=':')
            plt.axhline(data.mean().iloc[2], color ='green', linestyle='dashdot')
            plt.axhline(critery_3, color ='black', linestyle=':')
            plt.xlabel('Номер испытания', fontsize=12)
            plt.ylabel("Значение адгезии, Н/см", fontsize=12)
            plt.legend(fontsize=8, shadow=True, framealpha=1,  edgecolor='r', title='', loc='best')
            plt.grid(axis='both', color='black', linestyle=':',linewidth=0.5, alpha=0.7)
            plt.title(data.index.name, fontsize=16, y=1.05)

        def middle_value_text(self):
            """
            Среднее значение функций
            """
            middle_value_1 = self.data.mean().iloc[0]
            middle_1 = statistics.mean(self.data.index.tolist())
            middle_value_2 = self.data.mean().iloc[2]
            middle_2 = statistics.mean(self.data.index.tolist())
            plt.annotate(
                        "Аср 'к стали' = {}".format(round(self.data.mean().iloc[0], 3)), xy=(middle_1, middle_value_1),
                        xytext=(middle_1, middle_value_1+1), fontsize=9, bbox=dict(facecolor='blue', alpha=0.1)
                        ) # надпись
            plt.annotate(
                        "Аср 'в нахлест'= {}".format(round(self.data.mean().iloc[2], 3)), xy=(middle_2, middle_value_2),
                        xytext=(middle_2, middle_value_2-1), fontsize=9, bbox=dict(facecolor='green', alpha=0.1)
                        ) # надпись
            plt.annotate(
                        ('Критерий оценки "к стали"'), xy=(middle_2, self.critery_1), xytext=(middle_2, self.critery_1),
                        fontsize=9, bbox=dict(facecolor='red', alpha=0.1)
                        ) # надпись
            plt.annotate(
                        ('Критерий оценки "в нахлест"'), xy=(middle_2, self.critery_2), xytext=(middle_2, self.critery_2),
                        fontsize=9, bbox=dict(facecolor='blue', alpha=0.1)
                        ) # надпись
            plt.annotate(
                        ('Критерий оценки "в нахлест" - БПИ'), xy=(middle_2, self.critery_3), xytext=(middle_2, self.critery_3),
                        fontsize=9, bbox=dict(facecolor='black', alpha=0.1)
                        ) # надпись

        def regres_graphic(self, name = r'Линейная регрессия значений адгезии'):
            """
            Точечный график с линейной регрессией.
            object.regres_graphic(name), где name - название графика
            :name: str
            """
            fig, (ax1, ax2) = plt.subplots(2,1)
            fig.canvas.set_window_title('График линейной регресии значений адгезии')
            x = self.data.index.tolist()
            x = np.array(x)
            y: pd.DataFrame = self.data.transpose().iloc[0]
            y2: pd.DataFrame = self.data.transpose().iloc[2]
            y = np.array(y)
            y2 = np.array(y2)
            stats = linregress(x, y)
            stats2 = linregress(x, y2)
            m = stats.slope
            m2 = stats2.slope
            b = stats.intercept
            b2 = stats2.intercept
            ax1.set_title(self.data.index.name, fontsize=16, y=1.05)
            ax1.scatter(x,y,marker='*',label='Значение показателя "к стали"', color="orange")
            ax2.scatter(x,y2,marker='^',label='Значение показателя "в нахлест"', color="blue")
            ax1.plot(x, b + m * x , color="blue", label='Линия регрессии "к стали"')
            ax2.plot(x, b2 + m2 * x , color="orange", label='Линия регрессии "в нахлест"')
            plt.xlabel('Ось - X')
            ax1.set_ylabel('Значение показателя')
            ax2.set_ylabel('Значение показателя')
            ax1.legend(fontsize=8, shadow=True, framealpha=1, facecolor='w', edgecolor='r', title='', loc='upper right')
            ax2.legend(fontsize=8, shadow=True, framealpha=1, facecolor='w', edgecolor='r', title='', loc='upper right')
            ax1.grid(axis='both', color='black', linestyle='dotted',linewidth=1)
            ax2.grid(axis='both', color='black', linestyle='dotted',linewidth=1)

    class DistributionDiagramm(Abstract.Graphic):
        """
        Класс построения диаграммы распределения
        ########################################
        Пример запуска:
        ---------------
        _pz = _pz.tail(50)
        #50 значений
        dg = DistributionDiagramm(_pz)
        plt.show()
        """
        def __init__(self, data: pd.DataFrame, name='Название графика', critery_1 = 20, critery_2 = 15, critery_3 = 7):
            """
            Параметры:
            ----------
            data - нименование переменной (см.таблицу выше);
            name - название графика;
            critery_1 - Критерий оценки "к стали";
            critery_2 - Критерий оценки "в нахлест";
            critery_3 - Критерий оценки "в нахлест" - БПИ.
            """
            super().__init__(data)
            self.critery_1 = critery_1
            self.critery_2 = critery_2
            self.critery_3 = critery_3
            fig, ax = plt.subplots()
            fig.canvas.set_window_title('Ящик "с усами"')
            sb.boxplot(data=self.data)
            plt.ylabel("Значение адгезии, Н/см", fontsize=12)
            plt.axhline(critery_1, color ='red', linestyle=':', label = 'Критерий оценки "к стали"')
            plt.axhline(critery_2, color ='blue', linestyle=':', label = 'Критерий оценки "в нахлест"')
            plt.axhline(critery_3, color ='black', linestyle=':', label = 'Критерий оценки "в нахлест" - БПИ')
            plt.title(data.index.name + "\nДиаграмма плотности распределения", fontsize=12, y=1.05)
            plt.legend(fontsize=8, shadow=True, framealpha=1,  edgecolor='r', title='', loc='best')
            plt.grid(axis='both', color='black', linestyle='--',linewidth=0.5, alpha=0.3)

    class DistributionHistogramm(Abstract.Graphic):
        """
        Класс построения гистограммы распределения
        ########################################
        Пример запуска:
        ---------------
        _pz = _pz.tail(50)
        #50 значений
        dg = DistributionHistogramm(_pz)
        plt.show()
        """
        def __init__(self, data: pd.DataFrame, name='Название графика'):
            """
            Параметры:
            ----------
            data - нименование переменной (см.таблицу __doc__);
            name - название графика.
            """
            super().__init__(data)
            fig, ax = plt.subplots()
            fig.canvas.set_window_title('Гистограмма распределения')
            sb.distplot(self.data)
            plt.title(data.index.name + "\nГистограмма распределения", fontsize=12, y=1.05)
            plt.xlabel("Значение адгезии, Н/см", fontsize=12)
            plt.grid(axis='both', color='black', linestyle='--',linewidth=0.5, alpha=0.3)

    class ErrorGraphic(Abstract.Graphic):
        """
        Класс построения графика допустимых погрешностей
        ################################################
        Пример запуска:
        ---------------
        _pz = _pz.tail(50)
        50 значений
        dg = ErrorGraphic(_pz)
        plt.show()
        """
        def __init__(self, data: pd.DataFrame, name='Название графика', critery_1 = 20, critery_2 = 15, critery_3 = 7, error = 35):
            """
            Параметры:
            ----------
            data - наименование переменной (см.таблицу выше);
            name - название графика;
            critery_1 - Критерий оценки "к стали";
            critery_2 - Критерий оценки "в нахлест";
            critery_3 - Критерий оценки "в нахлест" - БПИ;
            error - допустимая погрешность в %.
            """
            super().__init__(data)
            self.critery_1 = critery_1
            self.critery_2 = critery_2
            self.critery_3 = critery_3
            self.error = error
            error = error/100
            fig, (ax1, ax2) = plt.subplots(2,1, figsize=(9,6))
            fig.canvas.set_window_title('График погрешностей')
            # Определение x, y и допустимой погрешности y
            x = self.data.index.tolist()
            x = np.array(x)
            y: pd.DataFrame = self.data.transpose().iloc[0]
            y2: pd.DataFrame = self.data.transpose().iloc[2]
            y = np.array(y)
            y2 = np.array(y2)
            err = self.data.apply(lambda x: x*error)
            yerr = err.transpose().iloc[0]
            yerr2 = err.transpose().iloc[2]
            yerr = np.array(yerr)
            yerr2 = np.array(yerr2)
            # Исключение одинаковых значений
            #print(self.data.describe())
            # Построение графика
            ax1.set_title('График при {}%-ой погрешности, {}'.format(error*100, data.index.name), fontsize = 10)
            ax2.set_xlabel('Номер испытания', fontsize = 10)
            ax1.set_ylabel('"' + self.data.columns[0] + '"', fontsize = 10)
            ax1.errorbar(x, y, xerr=0, yerr=yerr, fmt='-', ecolor='red', alpha=1)
            ax2.errorbar(x, y2, xerr=0, yerr=yerr2, fmt='-', ecolor='red', alpha=1)
            ax1.grid(color='black',linewidth=0.5,linestyle=':')
            ax1.axhline(critery_1, color ='red', linestyle=':', label = 'Критерий оценки "к стали"', alpha=0.7)
            ax1.axhline(critery_2, color ='blue', linestyle=':', label = 'Критерий оценки "в нахлест"', alpha=0.7)
            ax1.axhline(critery_3, color ='black', linestyle=':', label = 'Критерий оценки "в нахлест" - БПИ', alpha=0.7)
            ax1.legend(fontsize=6, shadow=True, framealpha=0.5,  edgecolor='r', title='', loc='best')
            ax2.grid(color='black',linewidth=0.5,linestyle=':')
            ax2.set_ylabel('"' + self.data.columns[2] + '"', fontsize = 10)
            ax2.axhline(critery_1, color ='red', linestyle=':', label = 'Критерий оценки "к стали"', alpha=0.7)
            ax2.axhline(critery_2, color ='blue', linestyle=':', label = 'Критерий оценки "в нахлест"', alpha=0.7)
            ax2.axhline(critery_3, color ='black', linestyle=':', label = 'Критерий оценки "в нахлест" - БПИ', alpha=0.7)
            ax2.legend(fontsize=6, shadow=True, framealpha=0.5,  edgecolor='r', title='', loc='best')

    class TableGraphic(Abstract.Graphic):
        """
        Класс визуализации табличных данных для n последних значений
        ОБЯЗАТЕЛЕН ПАРАМЕТР ИСХОДНЫХ ДАННЫХ БЕЗ ФОРМАТИРОВАНИЯ!!!
        Например, pz, а не _pz или __pz
        ############################################################
        Пример запуска:
        ---------------
        #40 значений
        dg = TableGraphic(pz)
        plt.show()
        """
        def __init__(self, data: pd.DataFrame, name='Выборка последних n испытаний'):
            """
            Параметры:
            ----------
            data - нименование переменной (см.таблицу выше);
            name - название графика.
            """
            super().__init__(data)
            self.data = data
            self.name = name
            data = data.tail(40)
            plt.figure(figsize=(10, 8))
            plt.gcf().canvas.set_window_title(name)
            ax = plt.subplot(121)
            plt.title('{}\n{}'.format(data.index.name, name), fontsize=12, y=1.05)
            _data = data.iloc[:, [True, True, False, True]]
            table(ax, _data, loc='upper left')
            plt.axis('off')
            ax = plt.subplot(222)
            table(ax, np.round(_data.describe(), 2), loc='upper right', rowLabels=None, colLabels=None)
            plt.axis('off')
            plt.annotate('count - кол-во значений;\nmean - среднее значение;\nstd - стандартное отклонение;\nmin - минимальное значение\n25% - 25% перцентиль;\n50% - 50% перцентиль;\n75% - 75% перцентиль;\nmax - максимальное значение;\nnan - значение отсутствует.', xy=(0, 0), xytext=(-0.1, -0.05), fontsize=9)
            plt.title('Статистические данные', fontsize=12, y=1.05)
            plt.subplot(224)
            data = data.iloc[:,1:4]
            plt.plot(data, linestyle='solid', linewidth=2, alpha=1)
            plt.xlabel('Номер испытания', fontsize=12)
            plt.ylabel("Значение адгезии", fontsize=12)
            plt.grid(axis='both', color='black', linestyle=':',linewidth=0.5, alpha=0.7)

    class DependenceGraphic(Abstract.Graphic):
        """
        Класс визуализации зависимости данных
        ########################################
        Пример запуска:
        ---------------
        _pz = _pz.tail(50)
        #50 значений
        dg = DependenceGraphic(_pz)
        plt.show()
        """
        def __init__(self, data: pd.DataFrame, name='Диаграмма корреляции'):
            """
            Параметры:
            ----------
            data - нименование переменной (см.таблицу выше);
            name - название графика.
            """
            super().__init__(data)
            self.data = data
            plt.figure(figsize=(12,10), dpi= 80)
            plt.gcf().canvas.set_window_title(name)
            sb.heatmap(data.corr(), xticklabels=data.corr().columns, yticklabels=data.corr().columns, cmap='RdYlGn', center=0, annot=True)
            plt.title('{}\nДиаграмма корреляции значений адгезии'.format(data.index.name), fontsize=16)
            plt.xticks(fontsize=12)
            plt.yticks(fontsize=12)

except Exception:
    print(time.ctime(), 'Graphics_Error: ', sys.exc_info()[:2], file = open('log.txt', 'a'))

try:
    class Data_Table(object):
        """
        Класс отображения исходных данных
        #################################
        ОБЯЗАТЕЛЕН ПАРАМЕТР ИСХОДНЫХ ДАННЫХ БЕЗ ФОРМАТИРОВАНИЯ!!!
        Например, pz, а не _pz или __pz
        Пример запуска:
        ---------------
        #x = Data_Table(bpi_2_0)
        #print(x)
        #x.open_data()
        """
        def __init__(self, data: pd.DataFrame):
            """
            Параметры:
            ----------
            data - нименование переменной (см.таблицу выше);
            """
            self.data = data

        def __str__(self):
            """
            Строковое представление данных
            """
            return tabulate(self.data, headers = 'keys', tablefmt = 'psql')

        def open_data(self):
            """
            Открытие и запись временного файла для отображения всех значений
            """
            print(tabulate(self.data, headers = 'keys', tablefmt = 'psql'), file=open(r'temp_data_graphics.txt', 'w', encoding = 'utf-8'))
            os.system('temp_data_graphics.txt')

except Exception:
    print(time.ctime(), 'Table_Error: ', sys.exc_info()[:2], file = open('log.txt', 'a'))

try:
    class Statistic_Table(Abstract.Statistic):
        """
        Класс отображения статистических данных
        #######################################
        Пример запуска:
        ---------------
        y = Statistic_Table(_lnn_2_0)
        print(y.score())
        print(y.middle())
        print(y.max_min())
        print(y.k_cor())
        print(y.st_d())
        print(y.s_val())
        print(y.data_mode())
        """
        def __init__(self, data: pd.DataFrame):
            """
            Параметры:
            ----------
            data - нименование переменной (см.таблицу выше);
            """
            self.data = data
            self.Ascr = data.count() # количество значений
            self.Asr = data.mean()  # среднее значение df.mean(n), где n - номер оси
            self.Amax = data.max()  # максимальные значения
            self.Amin = data.min()  # минимальные значения
            self.Acor = data.corr() # коэффициент корреляции
            self.Astd = data.std() # стандартные отклонения
            self.Adc = data.iloc[:,0].unique()# np.array массив уникальных значений
            self.Adp = data.iloc[:,1].unique()# np.array массив уникальных значений
            self.Adn = data.iloc[:,2].unique()# np.array массив уникальных значений
            self.Amode = data.iloc[:, [True, False, True]].mode()

        def score(self):
            """
            Метод значений количества проведенных испытаний и номеров партии
            """
            return "Всего результатов испытаний ленты:\n{}".format(self.Ascr)

        def middle(self):
            """
            Метод средних значений
            """
            return "Среднее значение адгезии:\n{}".format(self.Asr)

        def max_min(self):
            """
            Метод максимальных и минимальных значений
            """
            print("Максимальные значения адгезии:\n{}".format(self.Amax))
            print("Минимальные значения адгезии:\n{}".format(self.Amin))

        def k_cor(self):
            """
            Метод для вывода значений коэффициента корреляции
            """
            return "Коэффициенты корреляции:\n{}".format(self.Acor)

        def st_d(self):
            """
            Метод для вывода отклонений результатов испытаний
            """
            return "Отклонение результатов испытаний:\n{}".format(self.Astd)

        def s_val(self):
            """
            Метод для вывода количества уникальных значений
            """
            print ("Количество уникальных значений адгезии 'к стали':\t{} значений".format(self.Adc.size))
            print ("Количество уникальных значений адгезии 'с подплавл':\t{} значений".format(self.Adp.size))
            print ("Количество уникальных значений адгезии 'в нахлест':\t{} значений".format(self.Adn.size))

        def data_mode(self):
            """
            Метод вывода моды значений
            """
            return "Мода значений:\n{}".format(self.Amode)

except Exception:
    print(time.ctime(), 'Statistic_Error: ', sys.exc_info()[:2], file = open('log.txt', 'a'))

try:
    class Save_Data(object):
        """
        Класс сохранения статистических данных и графиков визуализации
        ##############################################################
        Пример запуска:
        ---------------
        # Save_Data(pl)

        """
        def __init__(self, data: pd.DataFrame):
            """
            Параметры:
            ----------
            data - наименование переменной (см.таблицу выше);
            """
            self.data = data
            directory = data.index.name
            parent_dir = r'files/'
            path = os.path.join(parent_dir, directory)
            if not os.path.isdir(path):
                os.mkdir(path)
            else:
                save_data_1 = data
                save_data_2 = Statistic_Table(data).Ascr
                # количество значений
                save_data_3 = Statistic_Table(data).Asr
                # среднее значение df.mean(n), где n - номер оси
                save_data_4 = Statistic_Table(data).Amax
                # максимальные значения
                save_data_5 = Statistic_Table(data).Amin
                # минимальные значения
                save_data_6 = Statistic_Table(data).Acor
                # коэффициент корреляции
                save_data_7 = Statistic_Table(data).Astd
                # стандартные отклонения
                save_data_8 = Statistic_Table(data).Adc.size
                # np.array массив уникальных значений
                save_data_9 = Statistic_Table(data).Adp.size
                # np.array массив уникальных значений
                save_data_10 = Statistic_Table(data).Adn.size
                # np.array массив уникальных значений
                save_data_11 = Statistic_Table(data).Amode
                # мода значений

                with pd.ExcelWriter('{}/results.xlsx'.format(path)) as writer:
                    save_data_1.to_excel(
                                    writer, sheet_name='Исходные данные'
                                        )
                    save_data_2.to_excel(
                                        writer, sheet_name='Кол-во значений'
                                        )
                    save_data_3.to_excel(
                                        writer, sheet_name='Среднее значение'
                                        )
                    save_data_4.to_excel(
                                        writer, sheet_name='Максимальные значения'
                                        )
                    save_data_5.to_excel(
                                        writer, sheet_name='Минимальные значения'
                                        )
                    save_data_6.to_excel(
                                    writer, sheet_name='Коэффициент корреляции'
                                        )
                    save_data_7.to_excel(
                                        writer, sheet_name='Стандартные отклонения'
                                        )
                    save_data_11.to_excel(
                                        writer, sheet_name='Мода значений'
                                        )

                print('Количество уникальных значений адгезии "к стали":\t{} значений\nКоличество уникальных значений адгезии "с подплавл":\t{} значений\nКоличество уникальных значений адгезии "в нахлест":\t{} значений\n'.format(save_data_8, save_data_9, save_data_10), file=open('{}/uniq.txt'.format(path), 'w'))

                print('Сохранение в файл формата *.png ...')
                print('...files/{}/*.png'.format(data.index.name))
                a = LinearGraphic(data) # экземпляр класса линейного графика
                a.middle_value_text() # Aср
                a.save_graphic('{}/Линейный график'.format(path))
                b = LinearGraphic(data)
                b.regres_graphic() # построение графика линейной регресии
                b.save_graphic('{}/График линейной регрессии'.format(path))
                c = DistributionDiagramm(data) # экземпляр класса диаграммы распределения
                c.save_graphic('{}/Диаграмма распределения'.format(path))
                d = DistributionHistogramm(data) # экземпляр класса гистограммы распределения
                d.save_graphic('{}/Гистограмма распределения'.format(path))
                e = ErrorGraphic(data) # экземпляр класса графика погрешностей
                e.save_graphic('{}/График погрешности'.format(path))
                g = DependenceGraphic(data)
                g.save_graphic('{}/Коэффициенты корреляции'.format(path))

    class Save_add_Data(object):
        """
        Класс сохранения статистических данных и графика за квартал
        ##############################################################
        Пример запуска:
        ---------------
        # Save_add_Data(pz)
        """
        def __init__(self, data: pd.DataFrame):
            """
            Параметры:
            ----------
            data - наименование переменной (см.таблицу выше);
            """
            self.data = data
            directory = data.index.name
            parent_dir = r'files/'
            path = os.path.join(parent_dir, directory)
            if not os.path.isdir(path):
                os.mkdir(path, mode=0o777)
            else:
                print('Сохранение в файл формата *.png ...')
                print('...files/{}/*.png'.format(data.index.name))
                e = TableGraphic(data) # экземпляр класса выборки последних значений
                e.save_graphic('{}/Статистика по n последним значениям'.format(path))

except Exception:
    print(time.ctime(), 'Save_Error: ', sys.exc_info()[:2], file = open('log.txt', 'a'))

try:
    class Info(object):
        """
        Класс вывода таблицы на экран для выбора идентификатора
        """
        def __init__(self):
            self.x = PrettyTable()
            field_names = ['Идентификатор', 'Наименование']
            self.x.add_column(field_names[1], LENTA_NAME)
            self.x.add_column(field_names[0], list(NAME_INPUT.keys()))


        def __repr__(self):
            return '{}'.format(self.x)

except Exception:
    print(time.ctime(), 'Table_Error: ', sys.exc_info()[:2], file = open('log.txt', 'a'))

if __name__=='__main__':
    """
        #ПРИМЕР СОЗДАВАЕМЫХ ЭКЗЕМПЛЯРОВ КЛАССОВ
        # Построение графиков
        a = LinearGraphic(df) # экземпляр класса линейного графика
        a.middle_value_text() # Aср
        a.regres_graphic() # построение графика линейной регресии
        b = DistributionDiagramm(df) # экземпляр класса диаграммы распределения
        c = DistributionHistogramm(df) # экземпляр класса гистограммы распределения
        d = ErrorGraphic(df) # экземпляр класса графика погрешностей
        e = TableGraphic(df_1) # экземпляр класса выборки последних значений
        f = DependenceGraphic(df)
        plt.show()
        ############################################################
        # Данные статистических расчетов
        y = Statistic_Table(df)
        print(y.score())
        print(y.middle())
        print(y.max_min())
        print(y.k_cor())
        print(y.st_d())
        print(y.s_val())
        print(y.data_mode())
        ################################################################
        #   Вывод исходных данных в виде файла и таблицы
        x = Data_Table(df_1)
        print(x)
        x.open_data()
        ###############################
        #   СОХРАНЕНИЕ графиков и результатов
        #for i in _lst_adhaesio:
        #Save_Data(i)
        #######################################
        #   СОХРАНЕНИЕ данных за квартал
        #for i in lst_adhaesio:
        #Save_add_Data(i)
        #######################################
    """
    try:
        class New_object(object):  # new_object = New_object()
            """
            Обычно метакласс переопределяет метод __new__ или __init__ класса type, с целью взять на себя управление созданием или инициализацией нового объекта класса. Как и при использовании декораторов классов, суть состоит в том, чтобы определить программный код, который будет вызываться автоматически на этапе создания класса. Оба способа позволяют расширять классы или возвращать произвольные объекты для его замены – протокол с практически неограниченными возможностями.
            """
            obj = None
            items = None

            @classmethod
            def __new__(cls, *args):
                if cls.obj is None:
                    cls.obj = object.__new__(cls)
                    cls.items = []
                return cls.obj

        class BaseCommand(ABC):
            """
            Абстрактным базовым классом (Abstract Base Class, ABC) называется
            класс, который не может использоваться для создания объектов.
            Назначение таких классов состоит в определении интерфейсов, то есть
            в том, чтобы перечислить методы и свойства, которые должны быть
            реализованы в классах, наследующих абстрактный базовый класс. Это
            удобно, так как можно использовать абстрактный базовый класс как
            своего рода договоренность - договоренность о том, что любые
            порожденные классы обеспечат реализацию методов и свойств, объявленных
            в абстрактном базовом.
            """
            @abstractmethod
            def label()->str:
                """
                Наименование комманды
                :return: str
                """
                pass

            def perform(self, object, *args, **kwargs):
                """
                Выполняемые инструкции
                """
                pass

        class Interface_cmd(object):
            """
            Класс запуска интерфейса коммандной строки
            Пример:
            run = Interface()
            run.main()
            """
            def user_input(self):
                """
                Пользовательский ввод input()
                # Наименование комманд из класса 'dict_keys'
                :return: str
                """
                message = '{}: '.format('|'.join(
                    {
                        FirstCommand.label(): FirstCommand,
                        SecondCommand.label(): SecondCommand,
                        ThreeCommand.label(): ThreeCommand,
                        FourCommand.label(): FourCommand,
                        FiveCommand.label(): FiveCommand,
                        SixCommand.label(): SixCommand,
                        #NewCommand.label(): NewCommand,
                        # NEW COMMANDs
                        ExitCommand.label(): ExitCommand,
                    }.keys()
                ))
                return input(message)

            def lst_commands(self):
                """
                Функция определения комманд
                :return: словарь со значением {input_function(message) : class}
                """
                return {
                        '1': FirstCommand,
                        '2': SecondCommand,
                        '3': ThreeCommand,
                        '4': FourCommand,
                        '5': FiveCommand,
                        '6': SixCommand,
                        '0': NewCommand,
                        # NEW COMMANDs
                        'exit': ExitCommand

                }

            def perform_command(self, command):
                """
                Выполнение команды по наименованию.
                Сохраняет результат в 'New_object()'.
                """
                try:
                    command = command.lower()
                    routes = self.lst_commands()
                    command_class = routes[command]
                    command_inst = command_class()
                    new_object = New_object()
                    command_inst.perform(new_object.items)
                except KeyError:
                    print('Неправильная команда, попробуйте снова!!!')

            def main(self):
                """
                Функция запуска
                """
                while True:
                    try:
                        command = self.user_input()
                        assert command != ''
                        self.perform_command(command)
                    except KeyboardInterrupt:
                        print('Выход...')
                        break
                    except UserExitException:
                        print('Выход...')
                        break
                    except AssertionError:
                        pass
                    except Exception:
                        print('Здесь пока ничего')

        class UserExitException(Exception): pass


        ###############################################################
        # NEW_COMMANDs
        ###############################################################

        class FirstCommand(BaseCommand):
            def label():
                return 'Данные-1'

            def perform(self, object, *args, **kwargs):
                info = Info()
                print(info) #вывод в консоль исходных данных
                while True:
                    try:
                        print('--Данные--')
                        a = input("Укажите идентификатор|exit-выход: ")
                        if a =='exit':
                            break
                        reading = NAME_INPUT_ORIGIN[a] # ВЫБОР НАИМЕНОВАНИЯ ЛЕНТЫ
                        df = reading
                        x = Data_Table(df)
                        x.open_data()
                        break
                    except KeyboardInterrupt:
                        print('Выход...')
                        break
                    except:
                        print("Неправильный идентификатор, попробуйте снова!!!")

        class SecondCommand(BaseCommand):
            def label():
                return 'Статистика-2'

            def perform(self, object, *args, **kwargs):
                info = Info()
                print(info) #вывод в консоль исходных данных
                while True:
                    try:
                        print('--Статистика--')
                        a = input("Укажите идентификатор|exit-выход: ")
                        if a =='exit':
                            break
                        reading = NAME_INPUT[a] # ВЫБОР НАИМЕНОВАНИЯ ЛЕНТЫ
                        df = reading
                        y = Statistic_Table(df)
                        print(y.score())
                        print(y.middle())
                        print(y.max_min())
                        print(y.k_cor())
                        print(y.st_d())
                        print(y.s_val())
                        print(y.data_mode())
                        break
                    except KeyboardInterrupt:
                        print('Выход...')
                        break
                    except:
                        print("Неправильный идентификатор, попробуйте снова!!!")
        class ThreeCommand(BaseCommand):
            def label():
                return 'Графики-3'

            def perform(self, object, *args, **kwargs):
                info = Info()
                print(info) #вывод в консоль исходных данных
                while True:
                    try:
                        print('--Графики--')
                        a = input("Укажите идентификатор|exit-выход: ")
                        if a =='exit':
                            break
                        reading = NAME_INPUT[a] # ВЫБОР НАИМЕНОВАНИЯ ЛЕНТЫ
                        df = reading
                        a = LinearGraphic(df) # экземпляр класса линейного графика
                        a.middle_value_text() # Aср
                        a.regres_graphic() # построение графика линейной регресии
                        b = DistributionDiagramm(df) # экземпляр класса диаграммы распределения
                        c = DistributionHistogramm(df) # экземпляр класса гистограммы распределения
                        d = ErrorGraphic(df) # экземпляр класса графика погрешностей
                        f = DependenceGraphic(df)
                        plt.show()
                        break
                    except KeyboardInterrupt:
                        print('Выход...')
                        break
                    except:
                        print("Неправильный идентификатор, попробуйте снова!!!")


        class FourCommand(BaseCommand):
            def label():
                return 'Квартал-4'

            def perform(self, object, *args, **kwargs):
                info = Info()
                print(info) #вывод в консоль исходных данных
                while True:
                    try:
                        print('--Квартал--')
                        a = input("Укажите идентификатор|exit-выход: ")
                        if a =='exit':
                            break
                        reading = NAME_INPUT_ORIGIN[a] # ВЫБОР НАИМЕНОВАНИЯ ЛЕНТЫ
                        df = reading
                        e = TableGraphic(df) # экземпляр класса выборки последних значений
                        plt.show()
                        break
                    except KeyboardInterrupt:
                        print('Выход...')
                        break
                    except:
                        print("Неправильный идентификатор, попробуйте снова!!!")

        class FiveCommand(BaseCommand):
            def label():
                return 'В файл-5'

            def perform(self, object, *args, **kwargs):
                for i in _lst_adhaesio:
                    Save_Data(i)

        class SixCommand(BaseCommand):
            def label():
                return 'В файл за квартал-6'

            def perform(self, object, *args, **kwargs):
                for i in lst_adhaesio:
                    Save_add_Data(i)

        class NewCommand(BaseCommand):
            def label():
                return 'Комманда-0'

            def perform(self, object, *args, **kwargs):
                print("Новая комманда")
                return 'LoL'

        class ExitCommand(BaseCommand):
            def label():
                return 'exit'

            def perform(self, object, *args, **kwargs):
                raise UserExitException

        #############################################################
        # END NEW_COMMANDs
        #############################################################

        if __name__=='__main__':
            run = Interface_cmd()
            run.main()

    except Exception:
        print(time.ctime(), 'Run_Error: ', sys.exc_info()[:2], file = open('log.txt ', 'a'))

