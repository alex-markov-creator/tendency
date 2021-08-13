# -*- coding: utf-8 -*-
# version 0.2a
# author: andrew.bezzubov - 02/07/2021 year
# email: ruizcontrol@yandex.ru, agb2019@list.ru
# https://github.com/alex-markov-creator/tendency.git
# GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""
===============================================================
consumer.py - модуль для статистических подсчетов, расчетов сводных данных и построения графиков  по показателям качества:
- Уровень удовлетворённости потребителей (Критерий>=75%) - методика расчёта в Р СМК (8.2) 001 , %;
- Уровень привлечения новых потребителей (Критерий>=5%) – соотношение кол-ва «новых» потребителей к общему числу потребителей предшествующего периода, %;
- Уровень повторных закупок, совершаемых новыми (закупившими продукцию в предшествующем отчётном периоде) потребителями (Критерий>=5%) – соотношение кол-ва «новых» потребителей, повторно закупивших продукцию в отчётном периоде, к общему количеству новых потребителей в соответствующем периоде прошлого года, %;
- Уровень выполнения заказов (Критерий = 100%) – отношение количества заказов, выполненных в срок, к общему количеству заказов, %;
- Уровень претензий и рекламаций, Кпр (Критерий-<3) в количественном выражении;
- Объем возвращённой продукции, Квоз (Критерий-<5% от общего объёма реализованной продукции за год) – отношение количества возвращённой продукции от потребителя к общему количеству реализованной продукции, (в %).

===============================================================
Процесс Б (7.2) "Связь с потребителем"
===============================================================

ИСХОДНЫЕ ДАННЫЕ - ФАЙЛ __init__.py в ../Data:
+--------------------------------------+-----------------------------------+
|              Переменная              |             Показатель            |
+--------------------------------------+-----------------------------------+
|          data_ur_udovl_year          |      Ур. удовлетв. потреб.        |
|      data_ur_priv_new_cons_year      | Ур. привлеч. новых потр. по годам |
|  data_ur_priv_new_cons_middle_year   | Ур. привлеч. новых потр. по полуг |
|         data_ur_pov_zak_year         |    Ур. повтор. закупок по годам   |
|     data_ur_pov_zak_middle_year      | Ур. повтор. закупок по полугодиям |
|         data_ur_vip_zak_year         |    Ур. выполн.заказов по годам    |
|     data_ur_vip_zak_middle_year      | Ур. выполн. заказов по полугодиям |
|        data_ob_vozr_prod_year        | Объем возвр. продукции по годам   |
|     data_ob_vozr_prod_middle_year    | Объем возвр. продукции по полугод.|
|        data_pret_i_rekl_year         | Уровень прет. и рекл. по годам    |
|     data_pret_i_rekl_middle_year     | Уровень прет. и рекл. по полгод.  |
+--------------------------------------+-----------------------------------+

# ИСХОДНЫЕ ДАННЫЕ (ПЕРЕМЕННЫЕ ШАБЛОНА process_b_7_2):
+-------------------------------------------------------------------------+
|  Переменная    |                  Данные шаблона                        |
+-------------------------------------------------------------------------+
|   prev_year    |# переменные предыдущего и отчетного периода            |
|   next_year    |                                                        |
|next_middle_year|                                                        |
|prev_middle_year|                                                        |
|    i_1_1_1     |# Переменные уровня удовлетворенности потребителей      |
|    i_1_2_1     |                                                        |
|    i_1_1_m_1   |                                                        |
|    i_1_2_m_1   |                                                        |
|    i_2_1_1     |# Переменные уровня привлечения новых потребителей      |
|    i_2_2_1     |                                                        |
|    i_2_1_m_1   |                                                        |
|    i_2_2_m_1   |                                                        |
|    i_3_1_1     |# Переменные уровня повторных закупок                   |
|    i_3_2_1     |                                                        |
|    i_3_1_m_1   |                                                        |
|    i_3_2_m_1   |                                                        |
|    e_1_1       |# перем. изм. ур. удовлетворенности потребителей        |
|    e_1_m_1     |                                                        |
|    e_2_1       |# перем. изм. ур. привлечения новых потребителей        |
|    e_2_m_1     |                                                        |
|    e_3_1       |# перем. изм. ур. повторных закупок                     |
|    e_3_m_1     |                                                        |
+--------------------------------------+----------------------------------+

Инструкции при импорте:
-----------------------
import consumer as cm

СПРАВКА
-------
print(cm.__doc__)

Вывод исходных данных в виде таблицы
---------------------------------------------
x = cm.Data_Table(cm.data_ur_priv_new_cons_year)
print(x)
x.open_data()

Данные статистических расчетов
--------------------------------
x = cm.Statistic_Table(cm.data_ur_priv_new_cons_year)
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
a = cm.Graphics_Histogram_Consumer(cm.data_ur_udovl_year, name= 'Гистограмма распределения')
b = cm.Graphics_Indicators_Consumer(cm.data_ur_udovl_year, name= 'Уровень удовлетворенности потребителей', critery=75)
c = cm.Graphics_Indicators_Consumer_Full(cm.data_ur_priv_new_cons_year, name= 'Уровень привлечения новых потребителей по годам', critery=5)
d = cm.Graphics_Indicators_Consumer_Full(cm.data_ur_priv_new_cons_middle_year, name= 'Уровень привлечения новых потребителей по полугодиям', critery=5)
e = cm.Graphics_Indicators_Consumer_Full(cm.data_ur_pov_zak_year, name= 'Уровень повторных закупок по годам', critery=5)
f = cm.Graphics_Indicators_Consumer_Full(cm.data_ur_pov_zak_middle_year, name= 'Уровень повторных закупок по полугодиям', critery=5)
g = cm.Graphics_Indicators_Consumer_Full(cm.data_ur_vip_zak_year, name= 'Уровень выполнения заказов по годам', critery=100)
h = cm.Graphics_Indicators_Consumer_Full(cm.data_ur_vip_zak_middle_year, name= 'Уровень выполнения заказов по полугодиям', critery=100)
i = cm.Graphics_Indicators_Consumer_Full(cm.data_ob_vozr_prod_year, name= 'Объем возвращенной продукции по годам', critery=5)
j = cm.Graphics_Indicators_Consumer_Full(cm.data_ob_vozr_prod_middle_year, name= 'Объем возвращенной продукции по полугодиям', critery=5)
k = cm.Graphics_Indicators_Consumer_Full(cm.data_pret_i_rekl_year, name= 'Кол-во претензий и рекламаций по годам', critery=3)
l = cm.Graphics_Indicators_Consumer_Full(cm.data_pret_i_rekl_middle_year, name= 'Кол-во претензий и рекламаций по полугодиям', critery=3)
cm.plt.show()

СРАВНЕНИЕ значений с предыдущими результатами
---------------------------------------------
x = cm.Comparise(cm.data_ur_priv_new_cons_year)
print(x)
print(x.score())

СОХРАНЕНИЕ графиков и результатов
---------------------------------
cm.Save_Data()
"""
import sys
import os
import platform # информация о версии оси
#-------------------------------------------------------
# модуль для логирования(журналирования)
import logging
import logging.config # файл конфигурации
import logging.handlers # ротация логов
import traceback # трасировка сообщений об исключениях
#-------------------------------------------------------
# модуль для тестирования
import pytest
import time
import pdb
#-------------------------------------------------------
sys.path.append(os.path.realpath('../..'))
# субродительский каталог в sys.path
#-------------------------------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from tabulate import tabulate
# модуль для вывода табличных данных
#-------------------------------------------------------
import Tools.Abstract_Parents as Abstract
# универсальный модуль для выполнения контракта
#-------------------------------------------------------
from scipy.stats import linregress
# модуль для построения линейной регрессии
#-------------------------------------------------------
from prettytable import PrettyTable
# импорт библиотеки для вывода табличных данных в консоли(терминале)
#-------------------------------------------------------
from abc import ABC, abstractmethod
# импорт модуля для абстрактных классов
#-------------------------------------------------------

#ЛОГИРОВАНИЕ
logging.config.fileConfig('logging.conf') # файл конфигурации
logger = logging.getLogger('indicators.consumer') # возвращает объект логгера
logger.info(f'Started on platform {platform.platform()}') # logging

#ДЕКОРАТОР ХРОНОМЕТРАЖА
def time_of_function(function):
    """
    #ДЕКОРАТОР  ВРЕМЕНИ ВЫПОЛНЕНИЯ
    (не применим к классам построения графиков)
    """
    def wrapped(*args):
        start_time = time.perf_counter()
        start_time_ns = time.perf_counter_ns()
        res = function(*args)
        print(f'Время выполнения в секундах: {time.perf_counter() - start_time}')
        print(f'Время выполнения в наносекундах: {time.perf_counter_ns() - start_time_ns}')
        return res
    return wrapped

#ДЕКОРАТОР ВЫВОДА СООБЩЕНИЙ
def message_save(function):
    """
    #ДЕКОРАТОР СООБЩЕНИЙ О СОХРАНЕНИИ файлов
    """
    def wrapped(*args):
        start_time = time.perf_counter()
        res = function(*args)
        print('Сохранение...')
        print(f'Время сохранения файлов в секундах: {time.perf_counter() - start_time}')
        return res
    return wrapped

# ИСХОДНЫЕ ДАННЫЕ (ДОПОЛНИТЕЛЬНОЕ ФОРМАТИРОВАНИЕ):
##################################################
try:
# импорт DataFrame объектов с исходными данными
    from Data import data_ur_vip_zak_year, data_ur_pov_zak_year,data_ur_priv_new_cons_year, data_ur_udovl_year, data_ur_vip_zak_middle_year, data_ur_pov_zak_middle_year, data_ur_priv_new_cons_middle_year, data_ob_vozr_prod_year, data_ob_vozr_prod_middle_year, data_pret_i_rekl_year, data_pret_i_rekl_middle_year
    logger.info("start initial assignment") # logging

    INDICATOR_NAME = [
                "Уровень выполнения заказов по годам",
                "Уровень повторных закупок по годам",
                "Уровень привлечения новых потребителей по годам",
                "Уровень удовлетворенности по годам",
                "Уровень выполнения заказов по полугодиям",
                "Уровень повторных закупок по полугодиям",
                "Уровень привлечения новых потребителей по полугодиям",
                "Объем возвращенной продукции по годам",
                "Объем возвращенной продукции по полугодиям",
                "Уровень претензий и рекламаций по годам",
                "Уровень претензий и рекламаций по полугодиям",
                 ] #запись наименований

    NAME_INPUT = {
                    '001':data_ur_vip_zak_year,
                    '002':data_ur_pov_zak_year,
                    '003':data_ur_priv_new_cons_year,
                    '004':data_ur_udovl_year,
                    '005':data_ur_vip_zak_middle_year,
                    '006':data_ur_pov_zak_middle_year,
                    '007':data_ur_priv_new_cons_middle_year,
                    '008':data_ob_vozr_prod_year,
                    '009':data_ob_vozr_prod_middle_year,
                    '010':data_pret_i_rekl_year,
                    '011':data_pret_i_rekl_middle_year,
                    } #идентификатор
    logger.info("OK! Load Data") #logging

    lst_name = [data_ur_vip_zak_year, data_ur_pov_zak_year,data_ur_priv_new_cons_year, data_ur_udovl_year, data_ur_vip_zak_middle_year, data_ur_pov_zak_middle_year, data_ur_priv_new_cons_middle_year]
    logger.info("OK! Load Data") # logging

    # ИСХОДНЫЕ ДАННЫЕ (ДОПОЛНИТЕЛЬНОЕ ФОРМАТИРОВАНИЕ ДЛЯ СОХРАНЕНИЯ):
    #################################################################
    data_add = pd.concat([data_ur_vip_zak_year, data_ur_pov_zak_year,data_ur_priv_new_cons_year, data_ur_udovl_year, data_ur_vip_zak_middle_year, data_ur_pov_zak_middle_year, data_ur_priv_new_cons_middle_year], axis=1)
    # Конкатенация
    logger.info("OK! Calculation Data") # logging

    # ИСХОДНЫЕ ДАННЫЕ (ПЕРЕМЕННЫЕ ШАБЛОНА process_b_7_2):
    #################################################################
    prev_year = data_ur_priv_new_cons_year.index[-2]
    next_year = data_ur_priv_new_cons_year.index[-1]
    prev_middle_year = data_ur_priv_new_cons_middle_year.index[-2]
    next_middle_year = data_ur_priv_new_cons_middle_year.index[-1]

    n_1 = '1'# нумерация строк
    n_2 = '2'# нумерация строк
    n_3 = '3'# нумерация строк

    # Переменные уровня удовлетворенности потребителей
    i_1_1_1 = data_ur_udovl_year.tail(2).iloc[0,0]
    i_1_2_1 = data_ur_udovl_year.tail(2).iloc[1,0]
    i_1_1_m_1 = None
    i_1_2_m_1 = None

    # Переменные уровня привлечения новых потребителей
    i_2_1_1 = data_ur_priv_new_cons_year.tail(2).iloc[0,0]
    i_2_2_1 = data_ur_priv_new_cons_year.tail(2).iloc[1,0]
    i_2_1_m_1 = data_ur_priv_new_cons_middle_year.tail(2).iloc[0,0]
    i_2_2_m_1 = data_ur_priv_new_cons_middle_year.tail(2).iloc[1,0]

    # Переменные уровня повторных закупок
    i_3_1_1 = data_ur_pov_zak_year.tail(2).iloc[0,0]
    i_3_2_1 = data_ur_pov_zak_year.tail(2).iloc[1,0]
    i_3_1_m_1 = data_ur_pov_zak_middle_year.tail(2).iloc[0,0]
    i_3_2_m_1 = data_ur_pov_zak_middle_year.tail(2).iloc[1,0]

    # переменные изменений уровня удовлетворенности потребителей
    e_1_1 = round(i_1_2_1-i_1_1_1, 2)
    e_1_m_1 = None

    # переменные изменений уровня привлечения новых потребителей
    e_2_1 = round(i_2_2_1-i_2_1_1, 2)
    e_2_m_1 = round(i_2_2_m_1-i_2_1_m_1,2)

    # переменные изменений уровня повторных закупок
    e_3_1 = round(i_3_2_1-i_3_1_1, 2)
    e_3_m_1 = round(i_3_2_m_1-i_3_1_m_1,2)

except ImportError:
    logger.error(f'FAILED! Data_Launch_Error: {sys.exc_info()[:2]}', exc_info=True) # logging

except TypeError:
    def test_add_raises():
        """Все, что находиться в следующем блоке кода, должно
        вызвать исключение
        """
        with pytest.raises(TypeError):
            raise TypeError

    logger.error(f'FAILED! Data_Launch_Error: {sys.exc_info()[:2]}', exc_info=True) # logging

try:
    #@time_of_function
    class Info(object):
        """
        Класс вывода таблицы на экран для выбора идентификатора
        """
        def __init__(self):
            self.logger = logging.getLogger('indicators.consumer.Info')
            self.logger.info('__Init__ Info')
            self.x = PrettyTable()
            field_names = ['Идентификатор', 'Наименование']
            self.x.add_column(field_names[1], INDICATOR_NAME)
            self.x.add_column(field_names[0], list(NAME_INPUT.keys()))

        def __str__(self):
            return '{}'.format(self.x)

        def __repr__(self):
            return f'Class: {self.__class__.__qualname__}\n {self.__class__.__doc__}'

    logger.info("OK! Load object class") # logging

except Exception:
    logger.error(f'FAILED! Info_Error: {sys.exc_info()[:2]}') # logging

try:
    #@time_of_function
    class Data_Table(object):
        """
        Класс отображения данных
        #################################
        Пример запуска:
        ---------------
        #x = Data_Table(data_ur_udovl_year)
        #print(x)
        #x.open_data()
        """
        def __init__(self, data: pd.DataFrame):
            """
            Параметры:
            ----------
            data - наименование переменной (см.таблицу выше);
            """
            self.logger = logging.getLogger('indicators.consumer.Data_Table')
            self.logger.info('__Init__ Data_Table')
            self.data = data

        def __str__(self):
            """
            Строковое представление данных
            """
            return tabulate(self.data, headers = 'keys', tablefmt = 'psql')

        def __repr__(self):
            return f'Class: {self.__class__.__qualname__}\n {self.__class__.__doc__}'

        def open_data(self):
            """
            Открытие и запись временного файла для отображения всех значений
            """
            if sys.platform == "linux" or sys.platform == "linux2":
                print(tabulate(self.data, headers = 'keys', tablefmt = 'psql')) # Linux
            elif sys.platform == "darwin":
                pass
            elif sys.platform == "win32":
                print(tabulate(self.data, headers = 'keys', tablefmt = 'psql'))

    logger.info("OK! Load object class") # logging

except Exception:
    logger.error(f'FAILED! Data_Table_Error: {sys.exc_info()[:2]}') # logging

try:
    #@time_of_function
    class Statistic_Table(Abstract.Statistic):
        """
        Класс отображения статистических данных
        #######################################
        Пример запуска:
        ---------------
        x = Statistic_Table(data_ur_udovl_year)
        print(x.score())
        print(x.middle())
        print(x.max())
        print(x.min())
        print(x.st_d())
        print(x.quantile_25())
        print(x.quantile_50())
        print(x.quantile_75())
        """
        def __init__(self, data: pd.DataFrame):
            """
            Параметры:
            ----------
            data - нименование переменной (см.таблицу выше);
            """
            self.logger = logging.getLogger('indicators.consumer.Statistic_Table')
            self.logger.info('__Init__ Statistic_Table')
            self.data = data
            self.Ascr = data.count() # количество значений
            self.Asr = data.mean()  # среднее значение df.mean(n), где n - номер оси
            self.Amax = data.max()  # максимальные значения
            self.Amin = data.min()  # минимальные значения
            self.Astd = data.std() # стандартные отклонения
            self.A25 = data.quantile(0.25) # 25% процентиль
            self.A50 = data.quantile(0.50) # 50% процентиль
            self.A75 = data.quantile(0.75) # 75% процентиль

        def name(self):
            """
            Метод значений количества проведенных испытаний и номеров партии
            """
            return "{}".format(self.data.columns.to_list()[0])

        def score(self):
            """
            Метод значений количества проведенных испытаний и номеров партии
            """
            return "Всего результатов: {}".format(self.Ascr.iloc[0])

        def middle(self):
            """
            Метод средних значений
            """
            return "Среднее значение: {}".format(self.Asr.iloc[0])

        def max_min(self):
            """
            Метод максимальных и минимальных значений
            """
            print("Максимальные значения: {}".format(self.Amax.iloc[0]))
            print("Минимальные значения: {}".format(self.Amin.iloc[0]))

        def max(self):
            """
            Метод максимальных значений
            """
            return "Максимальные значения: {}".format(self.Amax.iloc[0])

        def min(self):
            """
            Метод максимальных значений
            """
            return "Минимальные значения: {}".format(self.Amin.iloc[0])

        def st_d(self):
            """
            Метод для вывода отклонений результатов
            """
            return "Отклонение результатов: {}".format(self.Astd.iloc[0])

        def quantile_25(self):
            """
            Метод для вывода 25% процентиля
            """
            return "25% процентиль: {}".format(self.A25.iloc[0])

        def quantile_50(self):
            """
            Метод для вывода 50% процентиля
            """
            return "50% процентиль: {}".format(self.A50.iloc[0])

        def quantile_75(self):
            """
            Метод для вывода 75% процентиля
            """
            return "75% процентиль: {}".format(self.A75.iloc[0])

        logger.info("OK! Load object class") # logging

except Exception:
    logger.error(f'FAILED! Statistic_Table_Error: {sys.exc_info()[:2]}') # logging

try:
    #@time_of_function
    class Graphics_Indicators_Consumer(Abstract.Graphic):
        """
        Класс запуска графического отображения линейного графика показателя качества уровня удовлетворенности потребителя Процесса Б(7.2) "Связь с потребителем". Линейный график показателя уровня удовлетворенности.
        """
        def __init__(self, data, name='Наименование графика', critery = 0):
            super().__init__(data)
            self.logger = logging.getLogger('indicators.consumer.Graphics_Indicators_Consumer')
            self.logger.info('__Init__ Graphics_Indicators_Consumer')
            x = self.data.index.tolist()
            x = np.array(x)
            y = self.data.transpose().iloc[0]
            y = np.array(y)
            stats = linregress(x, y)
            m = stats.slope
            b = stats.intercept
            self.data.plot(color='blue', marker='o', linestyle='dashed', linewidth=2, alpha=0.5)
            plt.plot(x, b + m * x ,linestyle='dashed', color="blue", label='Линейная регрессия')
            plt.axhline(critery, color ='red', linestyle='dashed', label='Критерий оценки')
            plt.title(name, fontsize=16, y=1.05)
            plt.xlabel('Год')
            plt.legend(fontsize=8, shadow=True, framealpha=1, facecolor='y', edgecolor='r', title='', loc='center')
            plt.gcf().canvas.set_window_title('Процесс Б(7.2) "Связь с потребителем"')
            plt.grid(axis='both', color='black', linestyle='dotted',linewidth=2, alpha=0.5)

    logger.info("OK! Load object class") # logging

except Exception:
    logger.error(f'FAILED! Graphics_Indicators_Consumer: {sys.exc_info()[:2]}') # logging

try:
    #@time_of_function
    class Graphics_Histogram_Consumer(Abstract.Graphic):
        """
        Класс запуска графического отображения гистограммы распределения показателя качества уровня удовлетворенности потребителя Процесса Б(7.2) "Связь с потребителем". Гистограмма распределения показателя уровня удовлетворенности.
        """
        def __init__(self, data, name='Наименование графика'):
            super().__init__(data)
            self.logger = logging.getLogger('indicators.consumer.Graphics_Histogram_Consumer')
            self.logger.info('__Init__ Graphics_Histogram_Consumer')
            fig, ax = plt.subplots()
            sns_plot = sb.distplot(self.data.transpose().iloc[0], label='Показатели')
            fig.canvas.set_window_title('Процесс Б (7.2) "Связь с потребителем"')
            fig = sns_plot.get_figure()
            plt.title(name, fontsize=16, y=1.05)
            plt.xlabel('Уровень удовлетворенности потребителей')
            plt.legend(fontsize=8, shadow=True, framealpha=1, facecolor='y', edgecolor='r', title='Частота распределения')
            plt.grid()

    logger.info("OK! Load object class") # logging

except Exception:
    logger.error(f'FAILED! Graphics_Histogram_Consumer: {sys.exc_info()[:2]}') # logging

try:
    #@time_of_function
    class Graphics_Indicators_Consumer_Full(Abstract.Graphic):
        """
        Класс запуска графического отображения линейного графика показателей  Процесса Б(7.2) "Связь с потребителем".
        Линейный график, другой визуальный ряд (с заполнением).
        """
        def __init__(self, data, name='Наименование графика', critery = 0):
            super().__init__(data)
            self.logger = logging.getLogger('indicators.consumer.Graphics_Indicators_Consumer_Full')
            self.logger.info('__Init__ Graphics_Indicators_Consumer_Full')
            x = self.data.index.tolist()
            x = np.array(x)
            y = self.data.transpose().iloc[0]
            y = np.array(y)
            stats = linregress(x, y)
            m = stats.slope
            b = stats.intercept
            self.data.plot.area(color='blue', linestyle='dashed', linewidth=2, alpha=0.3)
            plt.plot(x, b + m * x ,linestyle='dashed', color="blue", label='Линейная регрессия')
            plt.axhline(critery, color ='red', linestyle='dashed', label='Критерий оценки')
            plt.gcf().canvas.set_window_title('Процесс Б(7.2) "Связь с потребителем')
            plt.title(name, fontsize=16, y=1.05)
            plt.xlabel('Год')
            plt.legend(fontsize=8, shadow=True, framealpha=1, facecolor='y', edgecolor='r', title='', loc='upper left')
            plt.grid(axis='both', color='black', linestyle='dotted',linewidth=2, alpha=0.5)

    logger.info("OK! Load object class") # logging

except Exception:
    logger.error(f'FAILED! Graphics_Indicators_Consumer_Full: {sys.exc_info()[:2]}') # logging

try:
    @time_of_function
    class Comparise(object):
        """
        Класс сравнительного анализа с результатами предыдущего отчётного периода
        #################################################################
        """
        def __init__(self, data: pd.DataFrame):
            self.logger = logging.getLogger('indicators.consumer.Comparise')
            self.logger.info('__Init__ Comparise')
            self.data = data.tail(2)

        def __str__(self):
            """
            Строковое представление данных
            """
            return tabulate(self.data, headers = 'keys', tablefmt = 'psql')

        def __repr__(self):
            return f'Class: {self.__class__.__qualname__}\n {self.__class__.__doc__}'

        def score(self):
            """
            Изменение послених двух значений
            """
            sc = round(self.data.iloc[1, 0] - self.data.iloc[0, 0], 2)
            return "Изменение значений c {} года по {} год:\n{}".format(prev_year, next_year, sc)

    logger.info("OK! Load object class") # logging

except Exception:
    logger.error(f'FAILED! Comparise(): {sys.exc_info()[:2]}') # logging

try:
    @time_of_function
    @message_save
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
            self.logger = logging.getLogger('indicators.consumer.Save_Data')
            self.logger.info('__Init__ Save_Data')

            # ЗАПИСЬ ДАННЫХ В .xlsx файл
            try:
                print('Сохранение в файл формата *.xlsx ...')
                save_data_1 = data_add
                print('...files/record.xlsx')
                with pd.ExcelWriter(r'files/record.xlsx') as writer:
                    save_data_1.to_excel(
                                        writer, sheet_name='Исходные данные'
                                        )
                logger.info("OK! Save_TO_XLSX") # logging
            except:
                logger.error(f'Error {traceback.print_exc(file=sys.stdout)}') # logging

            # ЗАПИСЬ СТАТИСТИЧЕСКОЙ ИНФОРМАЦИИ в *.txt файл
            try:
                print('Сохранение в файл формата *.txt ...')
                print('...files/*.txt')
                i = 0
                for i_name in lst_name:
                    x = Statistic_Table(i_name)
                    i +=1
                    print(f'{x.name()}\n{x.score()}\n{x.middle()}\n{x.max()}\n{x.min()}\n{x.st_d()}\n{x.quantile_25()}\n{x.quantile_50()}\n{x.quantile_75()}\n', file=open('files/{}.txt'.format(i), 'w'))
            except:
                logger.error(f'Error {traceback.print_exc(file=sys.stdout)}') # logging

            # СОХРАНЕНИЕ ГРАФИКОВ
            try:
                print('Сохранение в файл формата *.png ...')
                print('...files/*.png')

                if data_ur_udovl_year.isin([0]).all(axis=None) == False:
                    graphic_year_one = Graphics_Histogram_Consumer(data_ur_udovl_year, name= 'Гистограмма распределения')
                    graphic_year_one.save_graphic('files/001')
                    logger.debug("OK! GRAPHICS_1") # logging
                else:
                    pass

                if data_ur_udovl_year.isin([0]).all(axis=None) == False:
                    graphic_year_two = Graphics_Indicators_Consumer(data_ur_udovl_year, name= 'Уровень удовлетворенности потребителей', critery=75)
                    graphic_year_two.save_graphic('files/002')
                    logger.debug("OK! GRAPHICS_2") # logging
                else:
                    pass

                if data_ur_priv_new_cons_year.isin([0]).all(axis=None) == False:
                    graphic_year_three = Graphics_Indicators_Consumer_Full(data_ur_priv_new_cons_year, name= 'Уровень привлечения новых потребителей по годам', critery=5)
                    graphic_year_one.save_graphic('files/003')
                    logger.debug("OK! GRAPHICS_3") # logging
                else:
                    pass

                if data_ur_priv_new_cons_middle_year.isin([0]).all(axis=None) == False:
                    graphic_year_four = Graphics_Indicators_Consumer_Full(data_ur_priv_new_cons_middle_year, name= 'Уровень привлечения новых потребителей по полугодиям', critery=5)
                    graphic_year_four.save_graphic('files/004')
                    logger.debug("OK! GRAPHICS_4") # logging
                else:
                    pass

                if data_ur_pov_zak_year.isin([0]).all(axis=None) == False:
                    graphic_year_five = Graphics_Indicators_Consumer_Full(data_ur_pov_zak_year, name= 'Уровень повторных закупок по годам', critery=5)
                    graphic_year_five.save_graphic('files/005')
                    logger.debug("OK! GRAPHICS_5") # logging
                else:
                    pass

                if data_ur_pov_zak_middle_year.isin([0]).all(axis=None) == False:
                    graphic_year_six = Graphics_Indicators_Consumer_Full(data_ur_pov_zak_middle_year, name= 'Уровень повторных закупок по полугодиям', critery=5)
                    graphic_year_six.save_graphic('files/006')
                    logger.debug("OK! GRAPHICS_6") # logging
                else:
                    pass

                if data_ur_vip_zak_year.isin([0]).all(axis=None) == False:
                    graphic_year_seven = Graphics_Indicators_Consumer_Full(data_ur_vip_zak_year, name= 'Уровень выполнения заказов по годам', critery=100)
                    graphic_year_seven.save_graphic('files/007')
                    logger.debug("OK! GRAPHICS_7") # logging
                else:
                    pass


                if data_ur_vip_zak_middle_year.isin([0]).all(axis=None) == False:
                    graphic_year_eight = Graphics_Indicators_Consumer_Full(data_ur_vip_zak_middle_year, name= 'Уровень выполнения заказов по полугодиям', critery=100)
                    graphic_year_eight.save_graphic('files/008')
                    logger.debug("OK! GRAPHICS_8") # logging
                else:
                    pass

                if data_ob_vozr_prod_year.isin([0]).all(axis=None) == False:
                    graphic_year_nine = Graphics_Indicators_Consumer_Full(data_ob_vozr_prod_year, name= 'Объем возвращенной продукции по годам', critery=5)
                    graphic_year_nine.save_graphic('files/009')
                    logger.debug("OK! GRAPHICS_9") # logging
                else:
                    pass


                if data_ob_vozr_prod_middle_year.isin([0]).all(axis=None) == False:
                    graphic_year_ten = Graphics_Indicators_Consumer_Full(data_ob_vozr_prod_middle_year, name= 'Объем возвращенной продукции по полугодиям', critery=5)
                    graphic_year_ten.save_graphic('files/010')
                    logger.debug("OK! GRAPHICS_10") # logging
                else:
                    pass

                if data_pret_i_rekl_year.isin([0]).all(axis=None) == False:
                    graphic_year_eleven = Graphics_Indicators_Consumer_Full(data_pret_i_rekl_year, name= 'Кол-во претензий и рекламаций по годам', critery=3)
                    graphic_year_eleven.save_graphic('files/011')
                    logger.debug("OK! GRAPHICS_11") # logging
                else:
                    pass

                if data_pret_i_rekl_middle_year.isin([0]).all(axis=None) == False:
                    graphic_year_twelve = Graphics_Indicators_Consumer_Full(data_pret_i_rekl_middle_year, name= 'Кол-во претензий и рекламаций по полугодиям', critery=3)
                    graphic_year_twelve.save_graphic('files/012')
                    logger.debug("OK! GRAPHICS_12") # logging
                else:
                    pass

                logger.info("OK! SAVE_GRAPHICS") # logging
            except:
                logger.error(f'Error {traceback.print_exc(file=sys.stdout)}') # logging
            logger.info("OK! Load object class") # logging

except Exception:
    logger.error(f'FAILED! Save_Error: {sys.exc_info()[:2]}') # logging

logger.info(f"OK! Module on {platform.platform()}") # logging

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
                    print(x.quantile_25())
                    print(x.quantile_50())
                    print(x.quantile_75())
                except KeyboardInterrupt:
                    print('Выход...')
                    break
                except:
                    print("Неправильный идентификатор, попробуйте снова!!!")

    class ThreeCommand(BaseCommand):
        def label():
            return 'Графики-3'

        def perform(self, object, *args, **kwargs):
            # Графики Процесса Б(7.2) "Связь с потребителем"
            # Годовые показатели
            if data_ur_udovl_year.isin([0]).all(axis=None) == False:
                graphic_year_one = Graphics_Histogram_Consumer(data_ur_udovl_year, name= 'Гистограмма распределения')
            else:
                pass

            if data_ur_udovl_year.isin([0]).all(axis=None) == False:
                graphic_year_two = Graphics_Indicators_Consumer(data_ur_udovl_year, name= 'Уровень удовлетворенности потребителей', critery=75)
            else:
                pass

            if data_ur_priv_new_cons_year.isin([0]).all(axis=None) == False:
                graphic_year_three = Graphics_Indicators_Consumer_Full(data_ur_priv_new_cons_year, name= 'Уровень привлечения новых потребителей по годам', critery=5)
            else:
                pass

            if data_ur_priv_new_cons_middle_year.isin([0]).all(axis=None) == False:
                graphic_year_four = Graphics_Indicators_Consumer_Full(data_ur_priv_new_cons_middle_year, name= 'Уровень привлечения новых потребителей по полугодиям', critery=5)
            else:
                pass

            if data_ur_pov_zak_year.isin([0]).all(axis=None) == False:
                graphic_year_five = Graphics_Indicators_Consumer_Full(data_ur_pov_zak_year, name= 'Уровень повторных закупок по годам', critery=5)
            else:
                pass

            if data_ur_pov_zak_middle_year.isin([0]).all(axis=None) == False:
                graphic_year_six = Graphics_Indicators_Consumer_Full(data_ur_pov_zak_middle_year, name= 'Уровень повторных закупок по полугодиям', critery=5)
            else:
                pass

            if data_ur_vip_zak_year.isin([0]).all(axis=None) == False:
                graphic_year_seven = Graphics_Indicators_Consumer_Full(data_ur_vip_zak_year, name= 'Уровень выполнения заказов по годам', critery=100)
            else:
                pass


            if data_ur_vip_zak_middle_year.isin([0]).all(axis=None) == False:
                graphic_year_eight = Graphics_Indicators_Consumer_Full(data_ur_vip_zak_middle_year, name= 'Уровень выполнения заказов по полугодиям', critery=100)
            else:
                pass

            if data_ob_vozr_prod_year.isin([0]).all(axis=None) == False:
                graphic_year_nine = Graphics_Indicators_Consumer_Full(data_ob_vozr_prod_year, name= 'Объем возвращенной продукции по годам', critery=5)
            else:
                pass


            if data_ob_vozr_prod_middle_year.isin([0]).all(axis=None) == False:
                graphic_year_ten = Graphics_Indicators_Consumer_Full(data_ob_vozr_prod_middle_year, name= 'Объем возвращенной продукции по полугодиям', critery=5)
            else:
                pass

            if data_pret_i_rekl_year.isin([0]).all(axis=None) == False:
                graphic_year_eleven = Graphics_Indicators_Consumer_Full(data_pret_i_rekl_year, name= 'Кол-во претензий и рекламаций по годам', critery=3)
            else:
                pass

            if data_pret_i_rekl_middle_year.isin([0]).all(axis=None) == False:
                graphic_year_twelve = Graphics_Indicators_Consumer_Full(data_pret_i_rekl_middle_year, name= 'Кол-во претензий и рекламаций по полугодиям', critery=3)
            else:
                pass
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
                    reading = NAME_INPUT[a] # ВЫБОР НАИМЕНОВАНИЯ
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
