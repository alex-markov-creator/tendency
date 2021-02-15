#-*- coding: utf-8 -*-
# version 0.2a
# author: andrew.bezzubov - 02/02/2020
# email: ruizcontrol@yandex.ru
# https://github.com/alex-markov-creator/tendency.git
# GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""
===============================================================
production.py - модуль для статистических подсчетов и построения графиков  по показателям качества:
- Количество выпущенной продукции Квып (Критерия нет) - фактическое количество
выпущенной продукции, т:
    - п/б ленты;
    - муфты;
    - комплекты ЛИТКОР КМ;
    - резка п/б ленты;
    - резка ПВХ липкой.
- Уровень несоответствующей продукции в процессе производства Кн (Критерий <=5%) - отношение количества забракованной продукции к количеству выпущенной, %;
- Уровень отклонений продукции Котк (Критерий <10%) - отношение количества продукции с отклонением от ТУ к общему количеству выпущенной продукции, %;
- Уровень расхода материалов Крм (Критерий <=100%) - отношение коэффициента фактического расхода материалов (отношение количества затраченного материала к количеству выпущенной продукции) к коэффициенту нормативного расхода, %;
- Уровень тех. отходов Кто (Критерий <=2.0%) - отношение количества тех. отходов к общему количеству выпущенной продукции, %;
- Уровень простоя оборудования из-за несоответствующего качества расходных материалов Кпр кач (Критерий <5%) - отношение времени простоя оборудования к общему времени работы, %;
- Уровень простоя оборудования из-за непоставки расходных материалов Кпр кол (Критерий <5%)- отношение времени простоя оборудования к общему времени работы, %;
- Уровень неисправности оборудования Кно (Критерий <=5%) - отношение количества времени простоя по причине поломки оборудования к общему времени работы, %.
===============================================================
Процесс Б (7.5) "Производство продукции"
===============================================================

ИСХОДНЫЕ ДАННЫЕ - ФАЙЛ database.py в ../Data:
+--------------------------------------+-----------------------------------+
|              Переменная              |             Показатель            |
+--------------------------------------+-----------------------------------+
|        data_kol_vip_prod_year        | Количество выпущенной продукци... |
|       data_ur_neispr_obor_year       | Уровень неисправности оборудов... |
|       data_ur_nesoot_prod_year       | Уровень несоответствующей прод... |
|         data_ur_teh_oth_year         |   Уровень техотходов по годам...  |
|      data_kol_vip_mufty_year         |   Количество выпущенных муфт...   |
|      data_kol_vip_kompl_year         |Количество выпущенных комплектов...|
|      data_kol_narezki_year           |   Количество нарезки пб ленты...  |
|      data_kol_rezki_pvh_lip_year     |   Количество резки ПВХ липкой...  |
|       data_ur_rash_mater_year        | Уровень расхода материалов Крм... |
|        data_ur_otkl_prod_year        |Уровень отклонений продукции Котк..|
|      data_ur_prost_kach_year         | Уровень простоя обор. Кпр кач...  |
|      data_ur_prost_nepost_year       | Уровень простоя обор. Кпр кол...  |
|   data_ur_neispr_obor_middle_year    | Уровень неисправности оборудов... |
|   data_ur_nesoot_prod_middle_year    | Уровень несоответствующей прод... |
|     data_ur_teh_oth_middle_year      | Уровень техотходов по полугоди... |
|    data_kol_vip_prod_middle_year     | Количество выпущеной продукции... |
|  data_kol_vip_mufty_middle_year      |   Количество выпущенных муфт...   |
|  data_kol_vip_kompl_middle_year      |Количество выпущенных комплектов...|
|  data_kol_narezki_middle_year        |   Количество нарезки пб ленты...  |
|  data_kol_rezki_pvh_lip_middle_year  |   Количество резки ПВХ липкой...  |
|  data_ur_rash_mater_middle_year      | Уровень расхода материалов Крм... |
|  data_ur_otkl_prod_middle_year       |Уровень отклонений продукции Котк..|
|  data_ur_prost_kach_middle_year      | Уровень простоя обор. Кпр кач...  |
|  data_ur_prost_nepost_middle_year    | Уровень простоя обор. Кпр кол...  |
+--------------------------------------+-----------------------------------+

Инструкции при импорте:
-----------------------
import pandas as pd
import matplotlib.pyplot as plt
import production as pr

СПРАВКА (ОБНОВИТЬ!!!!!)
-------
print(pr.__doc__)

Вывод исходных данных в виде файла и таблицы
---------------------------------------------
x = pr.Data_Table(pr.data_ur_neispr_obor_middle_year)
print(x)
x.open_data()

Данные статистических расчетов
--------------------------------
x = pr.Statistic_Table(pr.data_ur_neispr_obor_middle_year)
print(x.score())
#Экземпляр значений количества проведенных испытаний и номеров партии
print(x.middle())
# Экземпляр средних значений
print(x.max_min())
# Экземпляр максимальных и минимальных значений
print(x.st_d())
# Экземпляр для вывода отклонений результатов испытаний

Построение графиков:
--------------------
a = pr.Graphics_Indicators_Production(pr.data_ur_neispr_obor_year, name= 'Уровень неисправности оборудования по годам')
b = pr.Graphics_Indicators_Production(pr.data_ur_neispr_obor_middle_year, name= 'Уровень неисправности оборудования по полугодиям')
c = pr.Graphics_Indicators_Production(pr.data_ur_nesoot_prod_year, name= 'Уровень несоответствующей продукции по годам')
d = pr.Graphics_Indicators_Production(pr.data_ur_nesoot_prod_middle_year, name= 'Уровень несоответствующей продукции по полугодиям')
e = pr.Graphics_Indicators_Production(pr.data_ur_teh_oth_year, name= 'Уровень техотходов по годам', critery=2)
f = pr.Graphics_Indicators_Production(pr.data_ur_teh_oth_middle_year, name= 'Уровень техотходов по полугодиям', critery=2)
plt.show()

СОХРАНЕНИЕ графиков и результатов
---------------------------------
pr.Save_Data()
"""
import sys
import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# импорт для построения нескольких графиков на одном уровне слоя
from matplotlib.gridspec import GridSpec
# дополнительная библиотека визуализации графиков
import seaborn as sb
# модуль для вывода табличных данных
from tabulate import tabulate
# субродительский каталог в sys.path
sys.path.append(os.path.realpath('../..'))
# универсальный модуль для выполнения контракта(контрактов)
import Tools.Abstract_Parents as Abstract
#import Tools.Singleton_Pattern as Singleton
# модуль для построения линейной регрессии
from scipy.stats import linregress
# импорт DataFrame объектов с исходными данными
from Data import data_kol_vip_prod_year, data_ur_neispr_obor_year,data_ur_nesoot_prod_year, data_ur_teh_oth_year, data_kol_vip_mufty_year, data_kol_vip_kompl_year, data_kol_narezki_year, data_kol_rezki_pvh_lip_year, data_ur_rash_mater_year, data_ur_otkl_prod_year, data_ur_prost_kach_year,data_ur_prost_nepost_year, data_ur_neispr_obor_middle_year, data_ur_nesoot_prod_middle_year, data_ur_teh_oth_middle_year,data_kol_vip_prod_middle_year, data_kol_vip_mufty_middle_year,data_kol_vip_kompl_middle_year, data_kol_narezki_middle_year,data_kol_rezki_pvh_lip_middle_year, data_ur_rash_mater_middle_year,data_ur_otkl_prod_middle_year, data_ur_prost_kach_middle_year,data_ur_prost_nepost_middle_year
# импорт библиотеки для вывода табличных данных в консоли(терминале)
from prettytable import PrettyTable
# импорт модуля для абстрактных классов
from abc import ABC, abstractmethod

# ИСХОДНЫЕ ДАННЫЕ (ДОПОЛНИТЕЛЬНОЕ ФОРМАТИРОВАНИЕ):
##################################################
try:
    INDICATOR_NAME = [
                    "Количество выпущенной продукции (ленты) Квып",#???график
                    "Уровень неисправности оборудования Кно",
                    "Уровень несоответствующей прод. в проц. произв. Кн",
                    "Уровень техотходов по годам",
                    "Количество выпущенных муфт",
                    "Количество выпущенных комплектов",
                    "Количество нарезки пб ленты",
                    "Количество резки ПВХ липкой",
                    #"Уровень расхода материалов Крм",
                    "Уровень отклонений продукции Котк",
                    "Уровень простоя обор. Кпр кач",
                    "Уровень простоя обор. Кпр кол",
                    "Уровень неисправности оборудов по полугодиям",
                    "Уровень несоответствующей прод. по полугодиям",
                    "Уровень техотходов по полугодиям",
                    "Количество выпущенной продукции Квып по полугодиям",
                    "Количество выпущенных муфт по полугодиям",
                    "Количество выпущенных комплектов по полугодиям",
                    "Количество нарезки пб ленты по полугодиям",
                    "Количество резки ПВХ липкой по полугодиям",
                    # "Уровень расхода материалов Крм по полугодиям",
                    "Уровень отклонений продукции Котк по полугодиям",
                    "Уровень простоя обор. Кпр кач по полугодиям",
                    "Уровень простоя обор. Кпр кол по полугодиям"
                 ]#запись наименований

    NAME_INPUT = {
                    '001': data_kol_vip_prod_year,
                    '002': data_ur_neispr_obor_year,
                    '003': data_ur_nesoot_prod_year,
                    '004': data_ur_teh_oth_year,
                    '005': data_kol_vip_mufty_year,
                    '006': data_kol_vip_kompl_year,
                    '007': data_kol_narezki_year,
                    '008': data_kol_rezki_pvh_lip_year,
                    # другой подсчёт статистики
                    #'009': data_ur_rash_mater_year,
                    '010': data_ur_otkl_prod_year,
                    '011': data_ur_prost_kach_year,
                    '012': data_ur_prost_nepost_year,
                    '013': data_ur_neispr_obor_middle_year,
                    '014': data_ur_nesoot_prod_middle_year,
                    '015': data_ur_teh_oth_middle_year,
                    '016': data_kol_vip_prod_middle_year,
                    '017': data_kol_vip_mufty_middle_year,
                    '018':data_kol_vip_kompl_middle_year,
                    '019': data_kol_narezki_middle_year,
                    '020': data_kol_rezki_pvh_lip_middle_year,
                    # другой подсчёт статистики
                    #'021': data_ur_rash_mater_middle_year,
                    '022': data_ur_otkl_prod_middle_year,
                    '023': data_ur_prost_kach_middle_year,
                    '024': data_ur_prost_nepost_middle_year,
                    } #идентификатор

    lst_name = [data_kol_vip_prod_year,data_ur_neispr_obor_year,data_ur_nesoot_prod_year,data_ur_teh_oth_year,data_kol_vip_mufty_year, data_kol_vip_kompl_year, data_kol_narezki_year, data_kol_rezki_pvh_lip_year, data_ur_otkl_prod_year,data_ur_prost_kach_year,data_ur_prost_nepost_year,data_ur_neispr_obor_middle_year,data_ur_nesoot_prod_middle_year,data_ur_teh_oth_middle_year,data_kol_vip_prod_middle_year,data_kol_vip_mufty_middle_year,data_kol_vip_kompl_middle_year,data_kol_narezki_middle_year,data_kol_rezki_pvh_lip_middle_year,data_ur_otkl_prod_middle_year,data_ur_prost_kach_middle_year,data_ur_prost_nepost_middle_year]

    # ИСХОДНЫЕ ДАННЫЕ (ДОПОЛНИТЕЛЬНОЕ ФОРМАТИРОВАНИЕ ДЛЯ ПОСТРОЕНИЯ ГРАФИКА):
    #########################################################################
    data_number_year = pd.concat([data_kol_vip_prod_year, data_kol_vip_mufty_year,data_kol_vip_kompl_year, data_kol_narezki_year,data_kol_rezki_pvh_lip_year], axis=1)
    data_number_middle_year = pd.concat([data_kol_vip_prod_middle_year,data_kol_vip_mufty_middle_year, data_kol_vip_kompl_middle_year,data_kol_narezki_middle_year, data_kol_rezki_pvh_lip_middle_year], axis=1)

    # ИСХОДНЫЕ ДАННЫЕ (ДОПОЛНИТЕЛЬНОЕ ФОРМАТИРОВАНИЕ ДЛЯ СОХРАНЕНИЯ):
    #################################################################
    data_add = pd.concat([data_kol_vip_prod_year,data_ur_neispr_obor_year,data_ur_nesoot_prod_year,data_ur_teh_oth_year,data_kol_vip_mufty_year, data_kol_vip_kompl_year, data_kol_narezki_year, data_kol_rezki_pvh_lip_year, data_ur_otkl_prod_year,data_ur_prost_kach_year,data_ur_prost_nepost_year,data_ur_neispr_obor_middle_year,data_ur_nesoot_prod_middle_year,data_ur_teh_oth_middle_year,data_kol_vip_prod_middle_year,data_kol_vip_mufty_middle_year,data_kol_vip_kompl_middle_year,data_kol_narezki_middle_year,data_kol_rezki_pvh_lip_middle_year,data_ur_otkl_prod_middle_year,data_ur_prost_kach_middle_year,data_ur_prost_nepost_middle_year], axis=1)
    # Конкатенация

except Exception:
    print(time.ctime(), 'Benchmark_Data_Error: ', sys.exc_info()[:2], file = open('warning.log', 'a'))

try:
    class Info(object):
        """
        Класс вывода таблицы на экран для выбора идентификатора
        """
        def __init__(self):
            self.x = PrettyTable()
            field_names = ['Идентификатор', 'Наименование']
            self.x.add_column(field_names[1], INDICATOR_NAME)
            self.x.add_column(field_names[0], list(NAME_INPUT.keys()))

        def __str__(self):
            return '{}'.format(self.x)

except Exception:
    print(time.ctime(), 'Info_Error: ', sys.exc_info()[:2], file = open('warning.log', 'a'))

try:
    class Data_Table(object):
        """
        Класс отображения данных
        #################################
        Пример запуска:
        ---------------
        #x = Data_Table(data_ur_teh_oth_year)
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
            print(tabulate(self.data, headers = 'keys', tablefmt = 'psql'), file=open(r'data_production.temp', 'w', encoding = 'utf-8'))
            os.system('data_production.temp')

except Exception:
    print(time.ctime(), 'Data_Table_Error: ', sys.exc_info()[:2], file = open('warning.log', 'a'))

try:
    class Statistic_Table(Abstract.Statistic):
        """
        Класс отображения статистических данных
        #######################################
        Пример запуска:
        ---------------
        x = Statistic_Table(data_ur_teh_oth_year)
        print(x.score())
        print(x.middle())
        print(x.max_min())
        print(x.max())
        print(x.min())
        print(x.st_d())
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
            self.Astd = data.std() # стандартные отклонения

        def score(self):
            """
            Метод значений количества проведенных испытаний и номеров партии
            """
            return "Всего результатов:\n{}".format(self.Ascr)

        def middle(self):
            """
            Метод средних значений
            """
            return "Среднее значение:\n{}".format(self.Asr)

        def max_min(self):
            """
            Метод максимальных и минимальных значений
            """
            print("Максимальные значения:\n{}".format(self.Amax))
            print("Минимальные значения:\n{}".format(self.Amin))

        def max(self):
            """
            Метод максимальных значений
            """
            return "Максимальные значения:\n{}".format(self.Amax)

        def min(self):
            """
            Метод максимальных значений
            """
            return "Минимальные значения:\n{}".format(self.Amin)

        def st_d(self):
            """
            Метод для вывода отклонений результатов испытаний
            """
            return "Отклонение результатов:\n{}".format(self.Astd)

except Exception:
    print(time.ctime(), 'Statistic_Error: ', sys.exc_info()[:2], file = open('warning.log', 'a'))

try:
    class Graphics_Indicators_Production(Abstract.Graphic):
        """
        Класс запуска графического отображения показателей качества
        Процесса Б(7.5) "Производство продукции", за исключением показателей
        количества выпущенной продукции
        """
        def __init__(self, data, name='Название графика', critery = 0):
            super().__init__(data)
            plt.style.use('bmh')
            fig, ax = plt.subplots(figsize=(12,10), dpi= 80)
            fig.canvas.set_window_title('Процесс Б (7.5) "Производство продукции"')
            x = self.data.index.tolist()
            x = np.array(x)
            y = self.data.transpose().iloc[0]
            y = np.array(y)
            stats = linregress(x, y)
            m = stats.slope
            b = stats.intercept
            ax = plt.bar(x,y,label='Значение показателя', color='red', alpha=0.5)
            ax = plt.plot(x,y,label='Значение показателя',marker = 'D', color='black', alpha=0.5)
            ax = plt.plot(x, b + m * x ,linestyle='dashed', color="blue", label='Регрессия')   # I've added a color argument here
            plt.axhline(critery, color ='red', linestyle='dashed', label='Критерий оценки')
            plt.title(name, fontsize=16, y=1.05)
            plt.legend(fontsize=8, shadow=True, framealpha=1, edgecolor='r', title='', loc='best')
            plt.grid(axis='both', color='black', linestyle='dotted',linewidth=1)

except Exception:
    print(time.ctime(), 'Graphics_Indicators_Production_Error: ', sys.exc_info()[:2], file = open('warning.log', 'a'))

try:
    class Graphics_Number_Production(Abstract.Graphic):
        """
        Класс запуска графического отображения показателя количества выпущенной продукции Процесса Б(7.5) "Производство продукции".
        """
        def __init__(self, data, name='Название графика', critery = 0):
            super().__init__(data)
            plt.style.use('bmh')
            fig = plt.figure(constrained_layout=True, figsize=(12,10), dpi= 80)
            fig.canvas.set_window_title('Процесс Б (7.5) "Производство продукции"')
            gs = GridSpec(3,3, figure=fig) # выбор сетки слоя
            # График слоя ax1
            ax1 = fig.add_subplot(gs[0, :])
            data_ax1 = self.data.iloc[:, 0]
            x_ax1 = data_ax1.index.tolist()
            x_ax1 = np.array(x_ax1)
            y_ax1 = data_ax1.transpose()
            y_ax1 = np.array(y_ax1)
            stats = linregress(x_ax1, y_ax1)
            m_ax1 = stats.slope
            b_ax1 = stats.intercept
            ax1 = plt.bar(x_ax1,y_ax1,label='Значение показателя', color='red', alpha=0.5)
            ax1 = plt.plot(x_ax1,y_ax1,label='Значение показателя',marker = 'D', color='black', alpha=0.5)
            ax1 = plt.plot(x_ax1, b_ax1 + m_ax1 * x_ax1 ,linestyle='dashed', color="blue", label='Регрессия')   # I've added a color argument here
            ax1 = plt.title(data_ax1.name, fontsize=12, y=1.05)
            ax1 = plt.grid(axis='both', color='black', linestyle='dotted',linewidth=1)
            ax1 = plt.legend(fontsize=6, shadow=True, framealpha=1, edgecolor='r', title='', loc='best')
            # График слоя ax2
            ax2 = fig.add_subplot(gs[1, :-1])
            data_ax2 = self.data.iloc[:, 1]
            x_ax2 = data_ax2.index.tolist()
            x_ax2 = np.array(x_ax2)
            y_ax2 = data_ax2.transpose()
            y_ax2 = np.array(y_ax2)
            ax2 = plt.bar(x_ax2,y_ax2,label='Значение показателя', color='yellow', alpha=0.5)
            ax2 = plt.plot(x_ax2,y_ax2,label='Значение показателя',marker = 'D', color='black', alpha=0.5)
            ax2 = plt.title(data_ax2.name, fontsize=10, y=1.05)
            ax2 = plt.grid(axis='both', color='black', linestyle='dotted',linewidth=1)
            ax2 = plt.legend(fontsize=4, shadow=True, framealpha=1, edgecolor='r', title='', loc='best')
            # График слоя ax3
            ax3 = fig.add_subplot(gs[1:, -1])
            data_ax3 = self.data.iloc[:, 2]
            x_ax3 = data_ax3.index.tolist()
            x_ax3 = np.array(x_ax3)
            y_ax3 = data_ax3.transpose()
            y_ax3 = np.array(y_ax3)
            ax3 = plt.bar(x_ax3,y_ax3,label='Значение показателя', color='blue', alpha=0.5)
            ax3 = plt.plot(x_ax3,y_ax3,label='Значение показателя',marker = 'D', color='black', alpha=0.5)
            ax3 = plt.title(data_ax3.name, fontsize=4, y=1.05)
            ax3 = plt.grid(axis='both', color='black', linestyle='dotted',linewidth=1)
            ax3 = plt.legend(fontsize=4, shadow=True, framealpha=1, edgecolor='r', title='', loc='best')
            # График слоя ax4
            ax4 = fig.add_subplot(gs[-1, 0])
            data_ax4 = self.data.iloc[:, 3]
            x_ax4 = data_ax4.index.tolist()
            x_ax4 = np.array(x_ax4)
            y_ax4 = data_ax4.transpose()
            y_ax4 = np.array(y_ax4)
            ax4 = plt.bar(x_ax4,y_ax4,label='Значение показателя', color='orange', alpha=0.5)
            ax4 = plt.plot(x_ax4,y_ax4,label='Значение показателя',marker = 'D', color='black', alpha=0.5)
            ax4 = plt.title(data_ax4.name, fontsize=5, y=1.05)
            ax4 = plt.grid(axis='both', color='black', linestyle='dotted',linewidth=1)
            ax4 = plt.legend(fontsize=4, shadow=True, framealpha=1, edgecolor='r', title='', loc='best')
            # График слоя ax5
            ax5 = fig.add_subplot(gs[-1, -2])
            data_ax5 = self.data.iloc[:, 4]
            x_ax5 = data_ax5.index.tolist()
            x_ax5 = np.array(x_ax5)
            y_ax5 = data_ax5.transpose()
            y_ax5 = np.array(y_ax5)
            ax5 = plt.bar(x_ax5,y_ax5,label='Значение показателя', color='green', alpha=0.5)
            ax5 = plt.plot(x_ax5,y_ax5,label='Значение показателя',marker = 'D', color='black', alpha=0.5)
            ax5 = plt.title(data_ax5.name, fontsize=5, y=1.05)
            ax5 = plt.grid(axis='both', color='black', linestyle='dotted',linewidth=1)
            ax5 = plt.legend(fontsize=4, shadow=True, framealpha=1, edgecolor='r', title='', loc='best')

except Exception:
    print(time.ctime(), 'Исключение в классе Graphics_Number_Production() модуля production.py: ', sys.exc_info()[:2], file = open('warning.log', 'a'))

try:
    class Comparise(object):# В РАЗРАБОТКЕ!!!!!!!!!!!!!!!!!!!!!!
        """
        Класс сравнительного анализа с результатами предыдущего отчётного периода
        #################################################################
        НЕОБХОДИМЫ ГОДА ПО ФАКТУ ИЗМЕНЕНИЙ И ОКРУГЛЕНИЕ объекта numpy.float64 до 2 знаков!!!! возможно отдельной функцией
        """
        def __init__(self, data: pd.DataFrame):
            self.data = data.tail(2)

        def __str__(self):
            """
            Строковое представление данных
            """
            return tabulate(self.data, headers = 'keys', tablefmt = 'psql')

        def score(self):
            """
            Изменение послених двух значений
            """
            sc = self.data.iloc[1, 0] - self.data.iloc[0, 0]
            return "Изменение двух последних значений:\n{}".format(sc)

except Exception:
    print(time.ctime(), 'Исключение в классе Comparise() модуля production.py: ', sys.exc_info()[:2], file = open('warning.log', 'a'))

try:
    class Save_Data(object):
        """
        Класс сохранения статистических данных и графиков визуализации
        ##############################################################
        Пример запуска:
        ---------------
        # Save_Data()
        """
        def __init__(self):
            """
            Параметры:
            ----------
            data - наименование переменной (см.таблицу выше);
            """

            # ЗАПИСЬ ДАННЫХ В .xlsx файл
            print('Сохранение в файл формата *.xlsx ...')
            save_data_1 = data_add
            print('...files/record.xlsx')
            with pd.ExcelWriter(r'files/record.xlsx') as writer:
                save_data_1.to_excel(
                                    writer, sheet_name='Исходные данные'
                                    )

            # ЗАПИСЬ СТАТИСТИЧЕСКОЙ ИНФОРМАЦИИ в *.txt файл
            #print('Сохранение в файл формата *.txt ...')
            #print('...files/*.txt')
            #for i_name in lst_name:
                #x = Statistic_Table(i_name)
                #print('{}\n{}\n{}\n{}\n{}'.format(x.score(),x.middle(),x.max(), x.min(),x.st_d()), file=open('files/{}.txt'.format(i_name.columns[0]), 'w'))

            # СОХРАНЕНИЕ ГРАФИКОВ
            print('Сохранение в файл формата *.png ...')
            print('...files/*.png')
            graphic_year_one = Graphics_Indicators_Production(data_ur_neispr_obor_year, name= 'Уровень неисправности оборудования по годам')
            graphic_year_one.save_graphic('files/{}'.format(data_ur_neispr_obor_year.columns[0]))

            graphic_year_two = Graphics_Indicators_Production(data_ur_nesoot_prod_year, name= 'Уровень несоответствующей продукции по годам')
            graphic_year_two.save_graphic('files/{}'.format(data_ur_nesoot_prod_year.columns[0]))

            graphic_year_three = Graphics_Indicators_Production(data_ur_teh_oth_year, name= 'Уровень техотходов по годам', critery=2)
            graphic_year_three.save_graphic('files/{}'.format(data_ur_teh_oth_year.columns[0]))

            graphic_year_four = Graphics_Indicators_Production(data_ur_otkl_prod_year, name= 'Уровень отклонений продукции Котк по годам')
            graphic_year_four.save_graphic('files/{}'.format(data_ur_otkl_prod_year.columns[0]))

            graphic_year_five = Graphics_Indicators_Production(data_ur_prost_kach_year, name= 'Уровень простоя оборудования из-за несоответствующего качества расходных материалов Кпр кач')
            graphic_year_five.save_graphic('files/{}'.format(data_ur_prost_kach_year.columns[0]))

            graphic_year_six = Graphics_Indicators_Production(data_ur_prost_nepost_year, name= 'Уровень простоя оборудования из-за непоставки расходных материалов Кпр кол')
            graphic_year_six.save_graphic('files/{}'.format(data_ur_prost_nepost_year.columns[0]))

            graphic_year_seven = Graphics_Number_Production(data_number_year, name= 'Количество выпущенной п/б ленты по годам')
            graphic_year_seven.save_graphic('files/{}'.format(data_number_year.columns[0]))

            # Полугодовые показатели
            graphic_middle_one = Graphics_Indicators_Production(data_ur_neispr_obor_middle_year, name= 'Уровень неисправности оборудования по полугодиям')
            graphic_middle_one.save_graphic('files/{}'.format(data_ur_neispr_obor_middle_year.columns[0]))

            graphic_middle_two = Graphics_Indicators_Production(data_ur_nesoot_prod_middle_year, name= 'Уровень несоответствующей продукции по полугодиям')
            graphic_middle_two.save_graphic('files/{}'.format(data_ur_nesoot_prod_middle_year.columns[0]))

            graphic_middle_three = Graphics_Indicators_Production(data_ur_teh_oth_middle_year, name= 'Уровень техотходов по полугодиям', critery=2)
            graphic_middle_three.save_graphic('files/{}'.format(data_ur_teh_oth_middle_year.columns[0]))

            graphic_middle_four = Graphics_Indicators_Production(data_ur_otkl_prod_middle_year, name= 'Уровень отклонений продукции Котк по полугодиям')
            graphic_middle_four.save_graphic('files/{}'.format(data_ur_otkl_prod_middle_year.columns[0]))

            graphic_middle_five = Graphics_Indicators_Production(data_ur_prost_kach_middle_year, name= 'Уровень простоя оборудования в Кпр кач по полугодиям')
            graphic_middle_five.save_graphic('files/{}'.format(data_ur_prost_kach_middle_year.columns[0]))

            graphic_middle_six = Graphics_Indicators_Production(data_ur_prost_nepost_middle_year, name= 'Уровень простоя оборудования из-за непоставки расходных материалов Кпр кол по полугодиям')
            graphic_middle_six.save_graphic('files/{}'.format(data_ur_prost_nepost_middle_year.columns[0]))

            graphic_middle_seven = Graphics_Number_Production(data_number_middle_year, name= 'Количество выпущенной п/б ленты  по полугодиям')
            graphic_middle_seven.save_graphic('files/{}'.format(data_number_middle_year.columns[0]))


except Exception:
    print(time.ctime(), 'Save_Error: ', sys.exc_info()[:2], file = open('warning.log', 'a'))

if __name__ == '__main__':
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


    ###############################################################################
    # NEW_COMMANDs
    ###############################################################################

    class FirstCommand(BaseCommand):
        def label():
            return 'Данные-1'

        def perform(self, object, *args, **kwargs):
            #ТАБЛИЦА ИСХОДНЫХ ФАЙЛОВ
            info = Info()
            print(info)
            while True:
                try:
                    a = input("Укажите идентификатор|exit-выход: ")
                    if a =='exit':
                        break
                    reading = NAME_INPUT[a] # ВЫБОР НАИМЕНОВАНИЯ ЛЕНТЫ
                    df = reading
                    x = Data_Table(df)
                    x.open_data()
                except KeyboardInterrupt:
                    print('Выход...')
                    break
                except:
                    print("Неправильный идентификатор, попробуйте снова!!!")

    class SecondCommand(BaseCommand):
        def label():
            return 'Статистика-2'

        def perform(self, object, *args, **kwargs):
            #СТАТИСТИКА
            info = Info()
            print(info)
            while True:
                try:
                    a = input("Укажите идентификатор|exit-выход: ")
                    if a =='exit':
                        break
                    reading = NAME_INPUT[a] # ВЫБОР НАИМЕНОВАНИЯ ЛЕНТЫ
                    df = reading
                    x = Statistic_Table(df)
                    print(x.score())
                    print(x.middle())
                    print(x.max())
                    print(x.min())
                    print(x.st_d())
                except KeyboardInterrupt:
                    print('Выход...')
                    break
                except:
                    print("Неправильный идентификатор, попробуйте снова!!!")

    class ThreeCommand(BaseCommand):
        def label():
            return 'Графики-3'

        def perform(self, object, *args, **kwargs):
            # Графики Процесса Б(7.5) "Производство продукции"
            # Годовые показатели
            graphic_year_one = Graphics_Indicators_Production(data_ur_neispr_obor_year, name= 'Уровень неисправности оборудования по годам')
            graphic_year_two = Graphics_Indicators_Production(data_ur_nesoot_prod_year, name= 'Уровень несоответствующей продукции по годам')
            graphic_year_three = Graphics_Indicators_Production(data_ur_teh_oth_year, name= 'Уровень техотходов по годам', critery=2)
            graphic_year_four = Graphics_Indicators_Production(data_ur_otkl_prod_year, name= 'Уровень отклонений продукции Котк по годам')
            # НУЛЕВЫЕ ЗНАЧЕНИЯ
            #graphic_year_five = Graphics_Indicators_Production(data_ur_prost_kach_year, name= 'Уровень простоя оборудования из-за несоответствующего качества расходных материалов Кпр кач')
            # НУЛЕВЫЕ ЗНАЧЕНИЯ
            #graphic_year_six = Graphics_Indicators_Production(data_ur_prost_nepost_year, name= 'Уровень простоя оборудования из-за непоставки расходных материалов Кпр кол')
            graphic_year_seven = Graphics_Number_Production(data_number_year, name= 'Количество выпущенной п/б ленты  по годам')

            # Полугодовые показатели
            graphic_middle_one = Graphics_Indicators_Production(data_ur_neispr_obor_middle_year, name= 'Уровень неисправности оборудования по полугодиям')
            graphic_middle_two = Graphics_Indicators_Production(data_ur_nesoot_prod_middle_year, name= 'Уровень несоответствующей продукции по полугодиям')
            graphic_middle_three = Graphics_Indicators_Production(data_ur_teh_oth_middle_year, name= 'Уровень техотходов по полугодиям', critery=2)
            # НУЛЕВЫЕ ЗНАЧЕНИЯ
            #graphic_middle_four = Graphics_Indicators_Production(data_ur_otkl_prod_middle_year, name= 'Уровень отклонений продукции Котк по полугодиям')
            # НУЛЕВЫЕ ЗНАЧЕНИЯ
            #graphic_middle_five = Graphics_Indicators_Production(data_ur_prost_kach_middle_year, name= 'Уровень простоя оборудования из-за несоответствующего качества расходных материалов Кпр кач по полугодиям')
            # НУЛЕВЫЕ ЗНАЧЕНИЯ
            #graphic_middle_six = Graphics_Indicators_Production(data_ur_prost_nepost_middle_year, name= 'Уровень простоя оборудования из-за непоставки расходных материалов Кпр кол по полугодиям')
            graphic_middle_seven = Graphics_Number_Production(data_number_middle_year, name= 'Количество выпущенной п/б ленты  по полугодиям')
            plt.show()

    class FourCommand(BaseCommand):
        def label():
            return 'Сравнение-4'

        def perform(self, object, *args, **kwargs):
            #СРАВНЕНИЕ
            info = Info()
            print(info)
            while True:
                try:
                    a = input("Укажите идентификатор|exit-выход: ")
                    if a =='exit':
                        break
                    reading = NAME_INPUT[a] # ВЫБОР НАИМЕНОВАНИЯ ЛЕНТЫ
                    df = reading
                    x = Comparise(df)
                    print(x)
                    print(x.score())
                except KeyboardInterrupt:
                    print('Выход...')
                    break
                except:
                    print("Неправильный идентификатор, попробуйте снова!!!")

    class FiveCommand(BaseCommand):
        def label():
            return 'В файл-5'

        def perform(self, object, *args, **kwargs):
            #СОХРАНЕНИЕ
            Save_Data()

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

    ###########################################################################
    # END NEW_COMMANDs
    ###########################################################################
    run = Interface_cmd()
    run.main()

