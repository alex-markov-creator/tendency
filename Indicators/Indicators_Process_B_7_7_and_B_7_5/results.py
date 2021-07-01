# -*- coding: utf-8 -*-
# version 0.2a
# author: andrew.bezzubov - 02/07/2021 year
# email: ruizcontrol@yandex.ru, agb2019@list.ru
# https://github.com/alex-markov-creator/tendency.git
# GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""
================================================================
results.py - Модуль аналитики по следующим показателям качества:
- Кол-во реализованной продукции (Кр);
- Кол-во выпущенной продукции (Процесс Б(7.5) "Производство продукции");
- Уровень поставок продукции (Кпп);
- Уровень претензий и рекламаций (Кпр);
- Уровень выполнения заказов (Квз);
- Объем возвращенной продукции (Квоз).
===============================================================
Процесс Б (7.7) "Сбыт"
===============================================================
ИСХОДНЫЕ ДАННЫЕ - ФАЙЛ database.py в ../Data:
+--------------------------------------+-----------------------------------+
|              Переменная              |             Показатель            |
+--------------------------------------+-----------------------------------+
|       data_kol_real_prod_year        |     Кол. реализов. прод. год      |
|        data_kol_vip_prod_year        |     Кол. вып. продукци год        |
|    data_kol_real_prod_middle_year    |  Кол. реализов. прод. полугодие   |
|     data_kol_vip_prod_middle_year    |    Кол. выпущ. прод. полугодие    |
|       data_kol_real_komp_year        |   Кол. реализов. компл. год       |
|      data_kol_vip_kompl_year         |   Кол. выпущ. комплектов год      |
|    data_kol_real_komp_middle_year    |  Кол. реализов. компл. полугодие  |
|    data_kol_vip_kompl_middle_year    |  Кол. выпущ. компл. полугодие     |
|       data_ob_vozr_prod_year         |    Объем возвращ. прод. год       |
|       data_ur_vip_zak_year           |   Уров. выпол. заказов год        |
|      data_ur_vip_zak_middle_year     |   Уров. выпол. заказов полугодие  |
|        data_pret_i_rekl_year         |      Претен. и реклам. год        |
|     data_pret_i_rekl_middle_year     |    Претен. и реклам. полугодие    |
|         data_ur_postav_year          |         Уров. постав. год         |
|      data_ur_postav_middle_year      |      Уров. постав. полугодие      |
+--------------------------------------+-----------------------------------+
# ИСХОДНЫЕ ДАННЫЕ (ПЕРЕМЕННЫЕ ШАБЛОНА process_b_7_5): (РЕДАКТИРОВАТЬ!!!)
+-------------------------------------------------------------------------+
|  Переменная    |                  Данные шаблона                        |
+-------------------------------------------------------------------------+
|   prev_year    |# переменные предыдущего и отчетного периода            |
|   next_year    |                                                        |
|    n_4         |# нумерация строк                                       |
|    n_5         |                                                        |
|    n_6         |                                                        |
|    n_7         |                                                        |
|    n_8         |                                                        |
|    i_4_1_1     |# переменные уровня выполнения заказов                  |
|    i_4_2_1     |                                                        |
|    i_4_1_m_1   |                                                        |
|    i_4_2_m_1   |                                                        |
|    i_5_1_1     |# переменные уровня претензий и рекламаций              |
|    i_5_2_1     |                                                        |
|    i_5_1_m_1   |                                                        |
|    i_5_2_m_1   |                                                        |
|    i_6_1_1     |# переменные объема возвращенной продукции              |
|    i_6_2_1     |                                                        |
|    i_6_1_m_1   |                                                        |
|    i_6_2_m_1   |                                                        |
|    i_7_1_1     |# переменные количества реализованной продукции         |
|    i_7_2_1     |                                                        |
|    i_7_1_m_1   |                                                        |
|    i_7_2_m_1   |                                                        |
|    i_7_1_2     |                                                        |
|    i_7_2_2     |                                                        |
|    i_7_1_m_2   |                                                        |
|    i_7_2_m_2   |                                                        |
|    i_7_1_3     |                                                        |
|    i_7_1_4     |                                                        |
|    i_7_1_5     |                                                        |
|    i_7_2_3     |                                                        |
|    i_7_2_4     |                                                        |
|    i_7_2_5     |                                                        |
|    i_7_1_m_3   |                                                        |
|    i_7_1_m_4   |                                                        |
|    i_7_1_m_5   |                                                        |
|    i_7_2_m_3   |                                                        |
|    i_7_2_m_4   |                                                        |
|    i_7_2_m_5   |                                                        |
|    i_8_1       |# переменные уровня поставок продукции Кпп              |
|    i_8_m_1     |                                                        |
|    i_8_2       |                                                        |
|    i_8_m_2     |                                                        |
|    e_4_1       |# переменные изменений уровня выполнения заказов        |
|    e_4_m_1     |                                                        |
|    e_5_1       |# переменные изменений уровня претензий и рекламаций    |
|    e_5_m_1     |                                                        |
|    e_6_1       |# переменные изменений объема возвращенной продукции    |
|    e_6_m_1     |                                                        |
|    e_7_1       |# переменные изменений кол-ва реализованной продукции   |
|    e_7_2       |                                                        |
|    e_7_3       |                                                        |
|    e_7_4       |                                                        |
|    e_7_5       |                                                        |
|    e_7_m_1     |                                                        |
|    e_7_m_2     |                                                        |
|    e_7_m_3     |                                                        |
|    e_7_m_4     |                                                        |
|    e_7_m_5     |                                                        |
|    e_8_1       |# переменные уровня поставок продукции                  |
|    e_8_m_1     |                                                        |
+--------------------------------------+----------------------------------+
================================================================
ИСХОДНЫЕ ДАННЫЕ - ФАЙЛ __init__.py в ../Data:
---------------------------------------------
Инструкции при импорте:
-----------------------
import pandas as pd
import matplotlib.pyplot as plt
import results as rs

СПРАВКА
print(pr.__doc__)

Вывод исходных данных в виде файла и таблицы
---------------------------------------------
x = rs.Data_Table(rs.data_kol_real_prod_year)
print(x)
x.open_data()

ДАННЫЕ статистических расчетов
--------------------------------
x = rs.Statistic_Table(rs.data_kol_real_prod_year)
print(x.score())
#Экземпляр значений количества проведенных испытаний и номеров партии
print(x.middle())
# Экземпляр средних значений
print(x.max_min())
# Экземпляр максимальных и минимальных значений
print(x.st_d())
# Экземпляр для вывода отклонений результатов испытаний

ПОСТРОЕНИЕ графиков:
--------------------
#график "Столбчатая диаграмма - Итоги"
graphic_one = rs.Visual_all(rs.sum_lenta, 'Реализованная и выпущенная продукции (лента) с 2010 года')

graphic_two = rs.Visual_all(rs.sum_kompl, 'Реализованная и выпущенная продукции (комплекты) с 2017 года')

graphic_three = rs.LinearGraphics(sum_lenta_year, name = 'Выпуск и реализация п/б ленты по годам')
graphic_three.maximum_minimum_text()

graphic_four = rs.LinearGraphics(sum_lenta_middle_year, name = 'Выпуск и реализация п/б ленты по полугодиям')
graphic_four.maximum_minimum_text()

graphic_five = rs.LinearGraphics(sum_kompl_year, name = 'Выпуск и реализация комплектов по годам')
graphic_five.maximum_minimum_text()

graphic_six = rs.LinearGraphics(sum_kompl_middle_year, name = 'Выпуск и реализация комплектов по полугодиям')
graphic_six.maximum_minimum_text()

graphic_seven = rs.Visual_difference(sum_lenta_year, name = 'Реализация и выпуск п/б ленты по годам')

graphic_eight = rs.Visual_difference(sum_lenta_middle_year,name = 'Реализация и выпуск п/б ленты по полугодиям')

graphic_nine = rs.Visual_difference(sum_kompl_year, name = 'Реализация и выпуск комплектов по годам')

graphic_ten = rs.Visual_difference(sum_kompl_middle_year, name = 'Реализация и выпуск комплектов по полугодиям')

graphic_eleven = rs.Visual_stock(diff_lenta_year, name='Используемые запасы и перевыпуск п/б лент(тонн) по годам')

graphic_twelve = rs.Visual_stock(diff_lenta_middle_year, name='Используемые запасы и перевыпуск п/б лент(тонн) по полугодиям')

graphic_thirteen = rs.Visual_stock(diff_kompl_year, name='Используемые запасы и перевыпуск комплектов (шт.) по годам')

graphic_fourteen = rs.Visual_stock(diff_kompl_middle_year, name='Используемые запасы и перевыпуск комплектов(шт.) по полугодиям')
plt.show()#график на экран

СРАВНЕНИЕ значений с предыдущими результатами
---------------------------------------------
x = rs.Comparise(rs.data_kol_real_prod_year)
print(x)
print(x.score())

СОХРАНЕНИЕ графиков и результатов
---------------------------------
rs.Save_Data()
"""
import sys
import os
sys.path.append(os.path.realpath('../..'))
# субродительский каталог в sys.path
#-------------------------------------------------------
# импорт библиотеки для вывода табличных данных в консоли(терминале)
from prettytable import PrettyTable
# модуль для вывода табличных данных
from tabulate import tabulate
# модуль для построения линейной регрессии
from scipy.stats import linregress
#-------------------------------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib._pylab_helpers as pylhelp
# очистка памяти
#-------------------------------------------------------
import Tools.Abstract_Parents as Abstract
# универсальный модуль для выполнения контракта
import Tools.Singleton_Pattern as Pattern_singleton
# универсальный модуль для создания уникального экземпляра класса, реализация паттерна "Одиночка"
#-------------------------------------------------------
# информация о версии оси
import platform
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
#-------------------------------------------------------
#ЛОГИРОВАНИЕ
logging.config.fileConfig('logging.conf') # файл конфигурации
logger = logging.getLogger('indicators.results') # возвращает объект логгера
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

#-------------------------------------------------------
try:
    # импорт DataFrame объектов с исходными данными
    from Data import data_kol_vip_prod_year, data_kol_vip_prod_middle_year, data_kol_real_prod_year, data_kol_real_prod_middle_year,data_kol_real_komp_year, data_kol_real_komp_middle_year,data_ob_vozr_prod_year, data_ur_vip_zak_year, data_ur_vip_zak_middle_year,data_kol_vip_kompl_year,data_kol_vip_kompl_middle_year,data_pret_i_rekl_year,data_pret_i_rekl_middle_year, data_ur_postav_year,data_ur_postav_middle_year
    # ИСХОДНЫЕ ДАННЫЕ (ДОПОЛНИТЕЛЬНОЕ ФОРМАТИРОВАНИЕ):
    ##################################################
    logger.info("start initial assignment") # logging

    INDICATOR_NAME = [
                        "Количество выпущенной продукции (ленты) Квып",
                        "Количество выпущенной продукции Квып по полугодиям",
                        "Количество выпущенных комплектов",
                        "Количество выпущенных комплектов по полугодиям",
                        "Количество реализованной продукции, Кр",
                        "Количество реализованной продукции, Кр по полугодиям",
                        "Количество реализованных комплектов",
                        "Количество реализованных комплектов по полугодиям",
                        "Объем возвращенной продукции, Квз",
                        "Уровень выполнения заказов, Квз",
                        "Уровень выполнения заказов, Квз по полугодиям",
                        "Уровень претензий и рекламаций, Кпр",
                        "Уровень претензий и рекламаций, Кпр по полугодиям",
                        "Уровень поставок продукции, Кпп",
                        "Уровень поставок продукции, Кпп по полугодиям",
                     ]#запись наименований

    NAME_INPUT = {
                    '001': data_kol_vip_prod_year,
                    '002': data_kol_vip_prod_middle_year,
                    '003': data_kol_vip_kompl_year,
                    '004': data_kol_vip_kompl_middle_year,
                    '005': data_kol_real_prod_year,
                    '006': data_kol_real_prod_middle_year,
                    '007': data_kol_real_komp_year,
                    '008': data_kol_real_komp_middle_year,
                    '009': data_ob_vozr_prod_year,
                    '010': data_ur_vip_zak_year,
                    '011': data_ur_vip_zak_middle_year,
                    '012': data_pret_i_rekl_year,
                    '013': data_pret_i_rekl_middle_year,
                    '014': data_ur_postav_year,
                    '015': data_ur_postav_middle_year,
                    } #идентификатор

    lst_name = [data_kol_vip_prod_year, data_kol_vip_prod_middle_year, data_kol_real_prod_year, data_kol_real_prod_middle_year,data_kol_real_komp_year, data_kol_real_komp_middle_year,data_ob_vozr_prod_year, data_ur_vip_zak_year, data_ur_vip_zak_middle_year,data_kol_vip_kompl_year,data_kol_vip_kompl_middle_year,data_pret_i_rekl_year,data_pret_i_rekl_middle_year, data_ur_postav_year,data_ur_postav_middle_year] #список для сохранения стаистических расчетов
    logger.info("OK! Load Data") # logging

    # ИСХОДНЫЕ ДАННЫЕ (ДОПОЛНИТЕЛЬНОЕ ФОРМАТИРОВАНИЕ ДЛЯ ПОСТРОЕНИЯ ГРАФИКА VISUAL_ALL):
    #########################################################################
    sum_lenta = pd.concat([data_kol_real_prod_year, data_kol_vip_prod_year], axis=1).dropna().sum()
    sum_kompl = pd.concat([data_kol_real_komp_year, data_kol_vip_kompl_year], axis=1).dropna().sum()

    # ИСХОДНЫЕ ДАННЫЕ (ДОПОЛНИТЕЛЬНОЕ ФОРМАТИРОВАНИЕ ДЛЯ ПОСТРОЕНИЯ ГРАФИКА LINEAR_GRAPHICS, VISUAL_DIFFERENCE, VISUAL_STACK):
    #########################################################################
    sum_lenta_year = pd.concat([data_kol_vip_prod_year, data_kol_real_prod_year],axis=1)
    sum_lenta_middle_year = pd.concat([data_kol_vip_prod_middle_year, data_kol_real_prod_middle_year],axis=1)
    sum_kompl_year = pd.concat([data_kol_vip_kompl_year, data_kol_real_komp_year],axis=1)
    sum_kompl_middle_year = pd.concat([data_kol_real_komp_middle_year, data_kol_vip_kompl_middle_year],axis=1)
    diff_lenta_year = pd.concat([data_kol_real_prod_year, data_kol_vip_prod_year], axis=1).dropna().transpose().iloc[0]-pd.concat([data_kol_real_prod_year, data_kol_vip_prod_year], axis=1).dropna().transpose().iloc[1]
    diff_lenta_middle_year = pd.concat([data_kol_real_prod_middle_year, data_kol_vip_prod_middle_year], axis=1).dropna().transpose().iloc[0]-pd.concat([data_kol_real_prod_middle_year, data_kol_vip_prod_middle_year], axis=1).dropna().transpose().iloc[1]
    diff_kompl_year = pd.concat([data_kol_real_komp_year, data_kol_vip_kompl_year], axis=1).dropna().transpose().iloc[0]-pd.concat([data_kol_real_komp_year, data_kol_vip_kompl_year], axis=1).dropna().transpose().iloc[1]
    diff_kompl_middle_year = pd.concat([data_kol_real_komp_middle_year, data_kol_vip_kompl_middle_year], axis=1).dropna().transpose().iloc[0]-pd.concat([data_kol_real_komp_middle_year, data_kol_vip_kompl_middle_year], axis=1).dropna().transpose().iloc[1]

    logger.info("OK! Calculation Data") # logging
    logger.info('OK! end initial assignment ') # logging

    # ИСХОДНЫЕ ДАННЫЕ (ПЕРЕМЕННЫЕ ШАБЛОНА process_b_7_7):
    #################################################################
    prev_year = data_kol_real_prod_year.index[-2]
    next_year = data_kol_real_prod_year.index[-1]

    n_4 = '4'# нумерация строк
    n_5 = '5'# нумерация строк
    n_6 = '6'# нумерация строк
    n_7 = '7'# нумерация строк
    n_8 = '8'# нумерация строк

    # Переменные уровня выполнения заказов
    i_4_1_1 = data_ur_vip_zak_year.tail(2).iloc[0,0]
    i_4_2_1 = data_ur_vip_zak_year.tail(2).iloc[1,0]
    i_4_1_m_1 = data_ur_vip_zak_middle_year.tail(2).iloc[0,0]
    i_4_2_m_1 = data_ur_vip_zak_middle_year.tail(2).iloc[1,0]

    # Переменные уровня претензий и рекламаций
    i_5_1_1 = data_pret_i_rekl_year.tail(2).iloc[0,0]
    i_5_2_1 = data_pret_i_rekl_year.tail(2).iloc[1,0]
    i_5_1_m_1 = data_pret_i_rekl_middle_year.tail(2).iloc[0,0]
    i_5_2_m_1 = data_pret_i_rekl_middle_year.tail(2).iloc[1,0]

    # Переменные объема возвращенной продукции
    i_6_1_1 = data_ob_vozr_prod_year.tail(2).iloc[0,0]
    i_6_2_1 = data_ob_vozr_prod_year.tail(2).iloc[1,0]
    i_6_1_m_1 = None
    i_6_2_m_1 = None

    # Переменные количества реализованной продукции
    i_7_1_1 = data_kol_real_prod_year.tail(2).iloc[0,0]
    i_7_2_1 = data_kol_real_prod_year.tail(2).iloc[1,0]
    i_7_1_m_1 = data_kol_real_prod_middle_year.tail(2).iloc[0,0]
    i_7_2_m_1 = data_kol_real_prod_middle_year.tail(2).iloc[1,0]
    i_7_1_2 = data_kol_real_komp_year.tail(2).iloc[0,0]
    i_7_2_2 = data_kol_real_komp_year.tail(2).iloc[1,0]
    i_7_1_m_2 = data_kol_real_komp_middle_year.tail(2).iloc[0,0]
    i_7_2_m_2 = data_kol_real_komp_middle_year.tail(2).iloc[1,0]
    i_7_1_3 = None
    i_7_1_4 = None
    i_7_1_5 = None
    i_7_2_3 = None
    i_7_2_4 = None
    i_7_2_5 = None
    i_7_1_m_3 = None
    i_7_1_m_4 = None
    i_7_1_m_5 = None
    i_7_2_m_3 = None
    i_7_2_m_4 = None
    i_7_2_m_5 = None

    # Переменные уровня поставок продукции Кпп
    i_8_1 = data_ur_postav_year.tail(2).iloc[0,0]
    i_8_2 = data_ur_postav_year.tail(2).iloc[1,0]
    i_8_m_1 = data_ur_postav_middle_year.tail(2).iloc[0,0]
    i_8_m_2 = data_ur_postav_middle_year.tail(2).iloc[1,0]

    # переменные изменений уровня выполнения заказов
    e_4_1 = round(i_4_2_1-i_4_1_1, 2)
    e_4_m_1 = round(i_4_2_m_1-i_4_1_m_1, 2)

    # переменные изменений уровня претензий и рекламаций
    e_5_1 = round(i_5_2_1-i_5_1_1, 2)
    e_5_m_1 = round(i_5_2_m_1-i_5_1_m_1,2)

    # переменные изменений объема возвращенной продукции
    e_6_1 = round(i_6_2_1-i_6_1_1, 2)
    e_6_m_1 = None

    # переменные изменений кол-ва реализованной продукции
    e_7_1 = round(i_7_2_1-i_7_1_1 , 2)
    e_7_2 = round(i_7_2_2-i_7_1_2 , 2)
    e_7_3 = None
    e_7_4 = None
    e_7_5 = None
    e_7_m_1 = round(i_7_2_m_1-i_7_1_m_1 , 2)
    e_7_m_2 = round(i_7_2_m_2-i_7_1_m_2 , 2)
    e_7_m_3 = None
    e_7_m_4 = None
    e_7_m_5 = None

    # переменные уровня поставок продукции
    e_8_1 = round(i_8_2-i_8_1, 2)
    e_8_m_1 = round(i_8_m_2-i_8_m_1, 2)


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

except:
    logger.error("FAILED! Data_Launch_Error: %s", traceback.format_exc()) # logging

try:
    @time_of_function
    class Info(object):
        """
        Класс вывода таблицы на экран для выбора идентификатора
        """
        def __init__(self):
            self.logger = logging.getLogger('indicators.results.Info')
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
    @time_of_function
    class Data_Table(object):
        """
        Класс отображения данных
        #################################
        Пример запуска:
        ---------------
        #x = Data_Table(data_kol_real_prod_year)
        #print(x)
        #x.open_data()
        """
        def __init__(self, data: pd.DataFrame):
            """
            Параметры:
            ----------
            data - нименование переменной (см.таблицу выше);
            """
            self.logger = logging.getLogger('indicators.results.Data_Table')
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
                print(tabulate(self.data, headers = 'keys', tablefmt = 'psql'), file=open(r'data_results.temp', 'w', encoding = 'utf-8'))
                os.system('data_results.temp')

    logger.info("OK! Load object class") # logging

except Exception:
    logger.error(f'FAILED! Data_Table_Error: {sys.exc_info()[:2]}') # logging

try:
    @time_of_function
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
            self.logger = logging.getLogger('indicators.production.Statistic_Table')
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
    logger.error(f'FAILED! Statistic_Error: {sys.exc_info()[:2]}') # logging

try:
    #@time_of_function
    class Visual_all(Abstract.Graphic):
        """
        График общих результатов выпуска и реализации в виде горизонтальной столбчатой диаграммы
        ========================================================================================
        # Пример отображения графика
        graphic_one = Visual_all(sum_lenta, 'Реализованная и выпущенная продукции (лента) с 2010 года')
        graphic_two = Visual_all(sum_kompl, 'Реализованная и выпущенная продукции (комплекты) с 2017 года')
        plt.show()
        """
        def __init__(self, data: pd.Series, name = 'Реализованная и выпущенная продукции'):
            super().__init__(data)
            self.logger = logging.getLogger('indicators.results.Visual_all')
            self.logger.info('__Init__ Visual_all')
            self.data = data
            fig, ax = plt.subplots()
            fig.canvas.set_window_title('Процесс Б(7.7) "Сбыт"')
            obj = ('Реализовано', 'Выпущено')
            y_pos = np.arange(len(obj))
            logger.info("OK!") # logging
            performance = [
                        data.iloc[1],
                        data.iloc[0]]
            plt.barh(y_pos, performance, align='center', alpha = 0.5, label = 'Кол-во в тоннах')
            plt.yticks(y_pos,[])
            plt.ylabel(obj)
            plt.title(name, fontsize=12, y=1.05)
            plt.legend(fontsize=8, shadow=True, framealpha=1, facecolor='w', edgecolor='r', loc='center')
            plt.text(data.iloc[1]/2, 0,round(data.iloc[1],3),
                    fontsize=14, horizontalalignment='center', verticalalignment='center',
                    bbox=dict(facecolor='pink', alpha=1.0))
            plt.text(
                    data.iloc[0]/2, 1,
                    round(data.iloc[0],3),
                    fontsize=14, horizontalalignment='center', verticalalignment='center',
                    bbox=dict(facecolor='pink', alpha=1.0))
            plt.grid()

    logger.info("OK! Load object class") # logging

except Exception:
    logger.error(f'FAILED! Visual_all_Error: {sys.exc_info()[:2]}') # logging

try:
    class LinearGraphics(Abstract.Graphic):
        """
        График общих результатов выпуска и реализации
        в виде линейного графика с визуализацией экстремумов функций графика
        и графиком линейной регрессии
        ====================================================================
        Пример запуска:
        ---------------
        gr = LinearGraphics(sum_lenta_year, name = 'Выпуск и реализация п/б ленты по годам')
        gr.maximum_minimum_text()
        """
        def __init__(self, data: pd.DataFrame, name = 'Реализованная и выпущенная продукции'):
            super().__init__(data)
            self.logger = logging.getLogger('indicators.results.LinearGraphics')
            self.logger.info('__Init__ LinearGraphics')
            self.data = self.data.dropna()
            x = self.data.index.tolist()
            x = np.array(x)
            y = self.data.transpose().iloc[0]
            y = np.array(y)
            stats = linregress(x, y)
            m = stats.slope
            b = stats.intercept
            self.data.plot()
            plt.plot(x, b + m * x ,linestyle='dashed', color="blue", label='Линейная регрессия')
            plt.title(name, fontsize=16, y=1.05)
            plt.ylabel('Кол-во')
            plt.xlabel('Год')
            plt.legend(fontsize=7, shadow=True, framealpha=1, facecolor='w', edgecolor='r', title='', loc = 'best')
            plt.gcf().canvas.set_window_title('Процесс Б(7.5) "Сбыт"')
            plt.grid()

        def maximum_minimum_text(self):
            """
            Экстремумы функций
            """
            max_value_realized = self.data.iloc[:,1:2].max() # максимальное
            max_index = self.data.iloc[:,1:2].idxmax() # индекс максимального
            min_value_realized = self.data.iloc[:,1:2].min() # минимальное
            min_index = self.data.iloc[:,1:2].idxmin()# индекс  минимального

            plt.annotate(
                        "Максимум", xy=(max_index, max_value_realized),
                        xytext=(max_index , max_value_realized+10), fontsize=9,
                        arrowprops = dict(arrowstyle = '->',color = 'red'),
                        bbox=dict(facecolor='pink', alpha=0.1)) # надпись "Максимум"

            plt.annotate(
                        "Минимум", xy=(min_index, min_value_realized),
                        xytext=(min_index, min_value_realized+10), fontsize=9,
                        arrowprops = dict(arrowstyle = '->', color = 'red'),
                        bbox=dict(facecolor='pink', alpha=0.1)) # надпись "Минимум"

    logger.info("OK! Load object class") # logging

except Exception:
    logger.error(f'FAILED!LinearGraphics_Error: {sys.exc_info()[:2]}') # logging

try:
    class Visual_difference(Abstract.Graphic):
        """
        Класс графического отображения соотношения реализации и выпуска
        ===============================================================
        Пример запуска:
        ---------------
        gr = Visual_difference(sum_kompl_year, name = 'Реализация и выпуск комплектов по годам')
        plt.show()
        """
        def __init__(self, data:pd.DataFrame, name = 'Реализация и выпуск'):
            super().__init__(data)
            self.logger = logging.getLogger('indicators.results.Visual_difference')
            self.logger.info('__Init__ Visual_difference')
            self.data = data
            self.data.plot(kind='barh')
            plt.title(name, fontsize=12, y=1.05)
            plt.legend(fontsize=8, shadow=True, framealpha=0.5, facecolor='w', edgecolor='r',loc='best')
            plt.gcf().canvas.set_window_title('Процесс Б(7.5) "Сбыт"')
            plt.grid()

    logger.info("OK! Load object class") # logging

except Exception:
    logger.error(f'FAILED!Visual_difference_Error: {sys.exc_info()[:2]}') # logging

try:
    class Visual_stock(Abstract.Graphic):
        """
        Класс графического отображения разницы реализации и выпуска
        ===========================================================
        Пример запуска:
        ---------------
        vs = Visual_stock(diff_lenta_year, name='Используемые запасы и перевыпуск п/б лент(тонн) по годам')
        plt.show()
        """
        def __init__(self,data: pd.DataFrame, name='Используемые запасы и перевыпуск продукции'):
            super().__init__(data)
            self.logger = logging.getLogger('indicators.results.Visual_stock')
            self.logger.info('__Init__ Visual_stock')
            self.data = data
            fig = plt.subplots()
            self.data.plot(kind='bar', stacked=True, alpha = 0.5)
            plt.title(name, fontsize=12, y=1.05)
            plt.legend(['Отклонение от выпуска'], fontsize=8, shadow=True, framealpha=0.5, facecolor='w', edgecolor='r',loc='best')
            plt.gcf().canvas.set_window_title('Процесс Б(7.5) "Сбыт"')
            plt.grid()

    logger.info("OK! Load object class") # logging

except Exception:
    logger.error(f'FAILED!Visual_stock_Error: {sys.exc_info()[:2]}') # logging

try:
    @time_of_function
    class Comparise(object):
        """
        Класс сравнительного анализа с результатами предыдущего отчётного периода
        #################################################################
        """
        def __init__(self, data: pd.DataFrame):
            self.logger = logging.getLogger('indicators.results.Comparise')
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
            self.logger = logging.getLogger('indicators.results.Save_Data')
            self.logger.info('__Init__ Save_Data')

            # ЗАПИСЬ ДАННЫХ В .xlsx файл
            try:
                print('Сохранение в файл формата *.xlsx ...')
                save_data_1 = pd.concat([data_kol_vip_prod_year, data_kol_vip_prod_middle_year, data_kol_real_prod_year, data_kol_real_prod_middle_year,data_kol_real_komp_year, data_kol_real_komp_middle_year,data_ob_vozr_prod_year, data_ur_vip_zak_year, data_ur_vip_zak_middle_year,data_kol_vip_kompl_year,data_kol_vip_kompl_middle_year,data_pret_i_rekl_year,data_pret_i_rekl_middle_year, data_ur_postav_year,data_ur_postav_middle_year], axis=1)

                save_data_2 = pd.concat([data_kol_real_prod_year, data_kol_vip_prod_year], axis=1).dropna()
                save_data_2['Отклонение от выпуска'] = save_data_2.transpose().iloc[0] - save_data_2.transpose().iloc[1]

                save_data_3 = pd.concat([data_kol_real_komp_year, data_kol_vip_kompl_year], axis=1).dropna()
                save_data_3['Отклонение от выпуска'] = save_data_3.transpose().iloc[0] - save_data_3.transpose().iloc[1]

                save_data_4 = pd.concat([data_kol_vip_prod_year, data_kol_vip_prod_middle_year, data_kol_real_prod_year, data_kol_real_prod_middle_year,], axis=1).dropna().corr()

                print('...files/record.xlsx')
                with pd.ExcelWriter(r'files/record.xlsx') as writer:
                    save_data_1.to_excel(
                                        writer, sheet_name='Исходные данные'
                                        )
                    save_data_2.to_excel(
                                        writer, sheet_name='Реализация-выпуск лента'
                                        )
                    save_data_3.to_excel(
                                        writer, sheet_name='Реализация-выпуск комплекты'
                                        )
                    save_data_4.to_excel(writer, sheet_name='Результаты корреляции')

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

                print('Сохранение в файл формата *.png ...')
                print('...files/*.png')
                if data_kol_real_prod_year.isin([0]).all(axis=None) == False and data_kol_vip_prod_year.isin([0]).all(axis=None) == False:
                    graphic_1 = Visual_all(sum_lenta, 'Реализованная и выпущенная продукции (лента) с 2010 года')
                    graphic_1.save_graphic(r'files/001')
                else:
                    pass
                if data_kol_real_komp_year.isin([0]).all(axis=None) == False and data_kol_vip_kompl_year.isin([0]).all(axis=None) == False:
                    graphic_2 = Visual_all(sum_kompl, 'Реализованная и выпущенная продукции (комплекты) с 2017 года')
                    graphic_2.save_graphic(r'files/002')
                else:
                    pass

                if data_kol_real_prod_year.isin([0]).all(axis=None) == False and data_kol_vip_prod_year.isin([0]).all(axis=None) == False:
                    graphic_3 = LinearGraphics(sum_lenta_year, name = 'Выпуск и реализация п/б ленты по годам')
                    graphic_3.maximum_minimum_text()
                    graphic_3.save_graphic(r'files/003')
                else:
                    pass
                if data_kol_real_prod_middle_year.isin([0]).all(axis=None) == False and data_kol_vip_prod_middle_year.isin([0]).all(axis=None) == False:
                    graphic_4 = LinearGraphics(sum_lenta_middle_year, name = 'Выпуск и реализация п/б ленты по полугодиям')
                    graphic_4.maximum_minimum_text()
                    graphic_4.save_graphic(r'files/004')
                else:
                    pass
                if data_kol_real_komp_year.isin([0]).all(axis=None) == False and data_kol_vip_kompl_year.isin([0]).all(axis=None) == False:
                    graphic_5 = LinearGraphics(sum_kompl_year, name = 'Выпуск и реализация комплектов по годам')
                    graphic_5.maximum_minimum_text()
                    graphic_5.save_graphic(r'files/005')
                else:
                    pass
                if data_kol_real_komp_middle_year.isin([0]).all(axis=None) == False and data_kol_vip_kompl_middle_year.isin([0]).all(axis=None) == False:
                    #graphic_6 = LinearGraphics(sum_kompl_middle_year, name = 'Выпуск и реализация комплектов по полугодиям')
                    #graphic_6.maximum_minimum_text()
                    #graphic_6.save_graphic(r'files/006')
                    pass # недостаточно значений
                else:
                    pass

                if data_kol_real_prod_year.isin([0]).all(axis=None) == False and data_kol_vip_prod_year.isin([0]).all(axis=None) == False:
                    graphic_7 = Visual_difference(sum_lenta_year, name = 'Реализация и выпуск п/б ленты по годам')
                    graphic_7.save_graphic(r'files/007')
                else:
                    pass

                if data_kol_real_prod_middle_year.isin([0]).all(axis=None) == False and data_kol_vip_prod_middle_year.isin([0]).all(axis=None) == False:
                    graphic_8 = Visual_difference(sum_lenta_middle_year,name = 'Реализация и выпуск п/б ленты по полугодиям')
                    graphic_8.save_graphic(r'files/008')
                else:
                    pass

                if data_kol_real_komp_year.isin([0]).all(axis=None) == False and data_kol_vip_kompl_year.isin([0]).all(axis=None) == False:
                    graphic_9 = Visual_difference(sum_kompl_year, name = 'Реализация и выпуск комплектов по годам')
                    graphic_9.save_graphic(r'files/009')
                else:
                    pass

                if data_kol_real_komp_middle_year.isin([0]).all(axis=None) == False and data_kol_vip_kompl_middle_year.isin([0]).all(axis=None) == False:
                    graphic_10 = Visual_difference(sum_kompl_middle_year, name = 'Реализация и выпуск комплектов по полугодиям')
                    graphic_10.save_graphic(r'files/010')
                else:
                    pass

                if data_kol_real_prod_year.isin([0]).all(axis=None) == False and data_kol_vip_prod_year.isin([0]).all(axis=None) == False:
                    graphic_11 = Visual_stock(diff_lenta_year, name='Используемые запасы и перевыпуск п/б лент(тонн) по годам')
                    graphic_11.save_graphic(r'files/011')
                else:
                    pass

                if data_kol_real_prod_middle_year.isin([0]).all(axis=None) == False and data_kol_vip_prod_middle_year.isin([0]).all(axis=None) == False:
                    graphic_12 = Visual_stock(diff_lenta_middle_year, name='Используемые запасы и перевыпуск п/б лент(тонн) по полугодиям')
                    graphic_12.save_graphic(r'files/012')
                else:
                    pass

                if data_kol_real_komp_year.isin([0]).all(axis=None) == False and data_kol_vip_kompl_year.isin([0]).all(axis=None) == False:
                    graphic_13 = Visual_stock(diff_kompl_year, name='Используемые запасы и перевыпуск комплектов (шт.) по годам')
                    graphic_13.save_graphic(r'files/013')
                else:
                    pass

                if data_kol_real_komp_middle_year.isin([0]).all(axis=None) == False and data_kol_vip_kompl_middle_year.isin([0]).all(axis=None) == False:
                    graphic_14 = Visual_stock(diff_kompl_middle_year, name='Используемые запасы и перевыпуск комплектов(шт.) по полугодиям')
                    graphic_14.save_graphic(r'files/014')
                else:
                    pass

                pylhelp.Gcf().destroy_all() # очистка памяти
                logger.info("OK! SAVE_GRAPHICS") # logging

            except:
                logger.error(f'Error {traceback.print_exc(file=sys.stdout)}') # logging

        logger.info("OK! Load object class") # logging

except Exception:
    logger.error(f'FAILED! Save_Error: {sys.exc_info()[:2]}') # logging

logger.info(f"OK! Module on {platform.platform()}") # logging
try:
    class AllStatistics(Abstract.Statistic):
        """
        Класс статистических данных
        ===========================
        """
        def __init__(self,data):
            super().__init__(data)
            pass

    logger.info("OK! Load object class") # logging

except Exception:
    logger.error(f'FAILED! AllStatistics_Error: {sys.exc_info()[:2]}') # logging

if __name__ == '__main__':
###########################################################################
# КЛАССЫ ИНТЕРФЕЙСА КОММАНДНОЙ СТРОКИ
###########################################################################
    from abc import ABC, abstractmethod

    class New_object(object):  # new_object = New_object()
        """
        Обычно метакласс переопределяет метод __new__ или
        __init__ класса type, с целью взять на себя управление созданием
        или инициализацией нового объекта класса. Как и при использовании
        декораторов классов, суть состоит в том, чтобы определить программный код,
        который будет вызываться автоматически на этапе создания класса.
        Оба способа позволяют расширять классы или возвращать произвольные
        объекты для его замены – протокол с практически неограниченными возможностями.
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
                    '0': NewCommand,
                    '1': FirstCommand,
                    '2': SecondCommand,
                    '3': ThreeCommand,
                    '4': FourCommand,
                    '5': FiveCommand,
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
                    print("Здесь пока ничего...")

    class UserExitException(Exception): pass
###############################################################################
# КЛАССЫ НОВЫХ КОММАНД
###############################################################################

    class FirstCommand(BaseCommand):
        def label():
            return 'Данные-1'

        def perform(self, object, *args, **kwargs):
            try:
                #ТАБЛИЦА ИСХОДНЫХ ФАЙЛОВ
                info = Info()
                print(info)
                while True:
                    try:
                        a = input("Укажите идентификатор|exit-выход: ")
                        if a =='exit':
                            break
                        reading = NAME_INPUT[a] # ВЫБОР НАИМЕНОВАНИЯ ЛЕНТЫ
                        logger.info("OK! NAME_INPUT") # logging
                        df = reading
                        x = Data_Table(df)
                        x.open_data()
                    except KeyboardInterrupt:
                        print('Выход...')
                        break
                    except:
                        print("Неправильный идентификатор, попробуйте снова!!!")

            except Exception:
                logger.error(f'FAILED! FirstCommand_Error: {sys.exc_info()[:2]}') # logging

    class SecondCommand(BaseCommand):
        def label():
            return 'Статистика-2'

        def perform(self, object, *args, **kwargs):
            """
            СТАТИСТИКА
            """
            try:
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
                        print(x.name())
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
                logger.info("OK! SecondCommand") # logging

            except Exception:
                logger.error(f'FAILED! SecondCommand_Error: {sys.exc_info()[:2]}') # logging

    class ThreeCommand(BaseCommand):
        def label():
            return 'Графики-3'

        def perform(self, object, *args, **kwargs):
            """
            ГРАФИКИ
            """
            try:
                if data_kol_real_prod_year.isin([0]).all(axis=None) == False and data_kol_vip_prod_year.isin([0]).all(axis=None) == False:
                    graphic_one = Visual_all(sum_lenta, 'Реализованная и выпущенная продукции (лента) с 2010 года')
                else:
                    pass

                if data_kol_real_komp_year.isin([0]).all(axis=None) == False and data_kol_vip_kompl_year.isin([0]).all(axis=None) == False:
                    graphic_two = Visual_all(sum_kompl, 'Реализованная и выпущенная продукции (комплекты) с 2017 года')
                else:
                    pass

                if data_kol_real_prod_year.isin([0]).all(axis=None) == False and data_kol_vip_prod_year.isin([0]).all(axis=None) == False:
                    graphic_three = LinearGraphics(sum_lenta_year, name = 'Выпуск и реализация п/б ленты по годам')
                    graphic_three.maximum_minimum_text()
                else:
                    pass

                if data_kol_real_prod_middle_year.isin([0]).all(axis=None) == False and data_kol_vip_prod_middle_year.isin([0]).all(axis=None) == False:
                    graphic_four = LinearGraphics(sum_lenta_middle_year, name = 'Выпуск и реализация п/б ленты по полугодиям')
                    graphic_four.maximum_minimum_text()
                else:
                    pass

                if data_kol_real_komp_year.isin([0]).all(axis=None) == False and data_kol_vip_kompl_year.isin([0]).all(axis=None) == False:
                    graphic_five = LinearGraphics(sum_kompl_year, name = 'Выпуск и реализация комплектов по годам')
                    graphic_five.maximum_minimum_text()
                else:
                    pass

                if data_kol_real_komp_middle_year.isin([0]).all(axis=None) == False and data_kol_vip_kompl_middle_year.isin([0]).all(axis=None) == False:
                    #graphic_six = LinearGraphics(sum_kompl_middle_year, name = 'Выпуск и реализация комплектов по полугодиям')
                    #graphic_six.maximum_minimum_text()
                    pass # недостаточно значений
                else:
                    pass

                if data_kol_real_prod_year.isin([0]).all(axis=None) == False and data_kol_vip_prod_year.isin([0]).all(axis=None) == False:
                    graphic_seven = Visual_difference(sum_lenta_year, name = 'Реализация и выпуск п/б ленты по годам')
                else:
                    pass

                if data_kol_real_prod_middle_year.isin([0]).all(axis=None) == False and data_kol_vip_prod_middle_year.isin([0]).all(axis=None) == False:
                    graphic_eight = Visual_difference(sum_lenta_middle_year,name = 'Реализация и выпуск п/б ленты по полугодиям')
                else:
                    pass

                if data_kol_real_komp_year.isin([0]).all(axis=None) == False and data_kol_vip_kompl_year.isin([0]).all(axis=None) == False:
                    graphic_nine = Visual_difference(sum_kompl_year, name = 'Реализация и выпуск комплектов по годам')
                else:
                    pass

                if data_kol_real_komp_middle_year.isin([0]).all(axis=None) == False and data_kol_vip_kompl_middle_year.isin([0]).all(axis=None) == False:
                    graphic_ten = Visual_difference(sum_kompl_middle_year, name = 'Реализация и выпуск комплектов по полугодиям')
                else:
                    pass
                if data_kol_real_prod_year.isin([0]).all(axis=None) == False and data_kol_vip_prod_year.isin([0]).all(axis=None) == False:
                    graphic_eleven = Visual_stock(diff_lenta_year, name='Используемые запасы и перевыпуск п/б лент(тонн) по годам')
                else:
                    pass
                if data_kol_real_prod_middle_year.isin([0]).all(axis=None) == False and data_kol_vip_prod_middle_year.isin([0]).all(axis=None) == False:
                    graphic_twelve = Visual_stock(diff_lenta_middle_year, name='Используемые запасы и перевыпуск п/б лент(тонн) по полугодиям')
                else:
                    pass
                if data_kol_real_komp_year.isin([0]).all(axis=None) == False and data_kol_vip_kompl_year.isin([0]).all(axis=None) == False:
                    graphic_thirteen = Visual_stock(diff_kompl_year, name='Используемые запасы и перевыпуск комплектов (шт.) по годам')
                else:
                    pass
                if data_kol_real_komp_middle_year.isin([0]).all(axis=None) == False and data_kol_vip_kompl_middle_year.isin([0]).all(axis=None) == False:
                    graphic_fourteen = Visual_stock(diff_kompl_middle_year, name='Используемые запасы и перевыпуск комплектов(шт.) по полугодиям')
                else:
                    pass
                plt.show()
                logger.info("OK! ThreeCommand") # logging

            except Exception:
                logger.error("FAILED! ThreeCommand_Error: %s", traceback.format_exc()) # logging

    class FourCommand(BaseCommand):
        def label():
            return 'Сравнение-4'

        def perform(self, object, *args, **kwargs):
            # СРАВНЕНИЕ
            try:
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
                logger.info("OK! FourCommand") # logging
            except Exception:
                logger.error(f'FAILED! FourCommand_Error: {sys.exc_info()[:2]}') # logging

    class FiveCommand(BaseCommand):
        def label():
            return 'В файл-5'

        def perform(self, object, *args, **kwargs):
            """
            СОХРАНЕНИЕ В ФАЙЛ
            """
            try:
                Save_Data()
                logger.info("OK! FourCommand") # logging
            except Exception:
                logger.error("FAILED! FiveCommand_Error: %s", traceback.format_exc()) # logging

    class ExitCommand(BaseCommand):
        def label():
            return 'exit'

        def perform(self, object, *args, **kwargs):
            """
            Выход из приложения
            """
            raise UserExitException

    class NewCommand(BaseCommand):
        def label():
            """
            Название комманды
            """
            return 'Комманда-0'

        def perform(self, object, *args, **kwargs):
            """
            Выполняемые инструкции
            """
            raise # NEW OBJECTs

###############################################################################
# END NEW_COMMANDs
###############################################################################
    try:
        run = Interface_cmd()
        run.main()

    except Exception:
        logger.error(f'FAILED! Run_Error: {sys.exc_info()[:2]}') # logging
