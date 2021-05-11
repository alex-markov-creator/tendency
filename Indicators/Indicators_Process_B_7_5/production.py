#-*- coding: utf-8 -*-
# version 0.2a
# author: andrew.bezzubov - 11/05/2021
# email: ruizcontrol@yandex.ru, agb2019@list.ru
# https://github.com/alex-markov-creator/tendency.git
# GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""
===============================================================
production.py - модуль для статистических подсчетов, расчетов сводных данных и построения графиков  по показателям качества:
- Количество выпущенной продукции Квып (Критерия нет) - фактическое количество
выпущенной продукции, т:
    - п/б ленты;
    - резка п/б ленты;
    - муфты;
    - комплекты ЛИТКОР КМ;
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
# ИСХОДНЫЕ ДАННЫЕ (ПЕРЕМЕННЫЕ ШАБЛОНА process_b_7_5):
+-------------------------------------------------------------------------+
|  Переменная    |                  Данные шаблона                        |
+-------------------------------------------------------------------------+
|   prev_year    |# переменные предыдущего и отчетного периода            |
|   next_year    |                                                        |
|    n_13        |# нумерация строк                                       |
|    n_14        |                                                        |
|    n_15        |                                                        |
|    n_16        |                                                        |
|    n_17        |                                                        |
|    n_18        |                                                        |
|    n_19        |                                                        |
|    n_20        |                                                        |
|    i_13_1_1    |# переменные уровня несоответствующей продукции         |
|    i_13_1_2    |                                                        |
|    i_13_1_3    |                                                        |
|    i_13_1_4    |                                                        |
|    i_13_1_5    |                                                        |
|    i_13_2_1    |                                                        |
|    i_13_2_2    |                                                        |
|    i_13_2_3    |                                                        |
|    i_13_2_4    |                                                        |
|    i_13_2_5    |                                                        |
|    i_13_1_m_1  |                                                        |
|    i_13_1_m_2  |                                                        |
|    i_13_1_m_3  |                                                        |
|    i_13_1_m_4  |                                                        |
|    i_13_1_m_5  |                                                        |
|    i_13_2_m_1  |                                                        |
|    i_13_2_m_2  |                                                        |
|    i_13_2_m_3  |                                                        |
|    i_13_2_m_4  |                                                        |
|    i_13_2_m_5  |                                                        |
|    i_14_1_1    |# переменные количества выпускаемой продукции           |
|    i_14_1_2    |                                                        |
|    i_14_1_3    |                                                        |
|    i_14_1_4    |                                                        |
|    i_14_1_5    |                                                        |
|    i_14_2_1    |                                                        |
|    i_14_2_2    |                                                        |
|    i_14_2_3    |                                                        |
|    i_14_2_4    |                                                        |
|    i_14_2_5    |                                                        |
|    i_14_1_m_1  |                                                        |
|    i_14_1_m_2  |                                                        |
|    i_14_1_m_3  |                                                        |
|    i_14_1_m_4  |                                                        |
|    i_14_1_m_5  |                                                        |
|    i_14_2_m_1  |                                                        |
|    i_14_2_m_2  |                                                        |
|    i_14_2_m_3  |                                                        |
|    i_14_2_m_4  |                                                        |
|    i_14_2_m_5  |                                                        |
|    i_15_1      |# переменные уровня расхода материала                   |
|    i_15_m_1    |                                                        |
|    i_15_2      |                                                        |
|    i_15_m_2    |                                                        |
|    i_16_1      |# переменные уровня технических отходов                 |
|    i_16_m_1    |                                                        |
|    i_16_2      |                                                        |
|    i_16_m_2    |                                                        |
|    i_17_1      |# переменные уровня неисправности оборудования          |
|    i_17_m_1    |                                                        |
|    i_17_2      |                                                        |
|    i_17_m_2    |                                                        |
|    i_18_1      |# переменные уровня простоя оборудования из-за качества |
|    i_18_m_1    |                                                        |
|    i_18_2      |                                                        |
|    i_18_m_2    |                                                        |
|    i_19_1      |# переменные уровня простоя обор. из-за непоставок      |
|    i_19_m_1    |                                                        |
|    i_19_2      |                                                        |
|    i_19_m_2    |                                                        |
|    i_20_1      |# переменные уровня отклонений продукции                |
|    i_20_m_1    |                                                        |
|    i_20_2      |                                                        |
|    i_20_m_2    |                                                        |
|    e_13_1      |# переменные изменений уровня несоответ продукции       |
|    e_13_m_1    |                                                        |
|    e_14_1_1    |# переменные изменений количества выпускаемой продукции |
|    e_14_1_2    |                                                        |
|    e_14_1_3    |                                                        |
|    e_14_1_4    |                                                        |
|    e_14_1_5    |                                                        |
|    e_14_1_m_1  |                                                        |
|    e_14_1_m_2  |                                                        |
|    e_14_1_m_3  |                                                        |
|    e_14_1_m_4  |                                                        |
|    e_14_1_m_5  |                                                        |
|    e_15_1      |# переменные изменений уровня расхода материала         |
|    e_15_m_1    |                                                        |
|    e_16_1      |# переменные изменений уровня технических отходов       |
|    e_16_m_1    |                                                        |
|    e_17_1      |# переменные изменений уровня неисправности оборудования|
|    e_17_m_1    |                                                        |
|    e_18_1      |# переменные изменений уровня пр. оборудования из-за кач|
|    e_18_m_1    |                                                        |
|    e_19_1      |# перем. изм. ур. простоя оборудования из-за непоставок |
|    e_19_m_1    |                                                        |
|    e_20_1      |# переменные изменений уровня отклонений продукции      |
|    e_20_m_1    |                                                        |
+--------------------------------------+----------------------------------+

Инструкции при импорте:
-----------------------
import pandas as pd
import matplotlib.pyplot as plt
import production as pr

СПРАВКА
-------
print(pr.__doc__)

Вывод исходных данных в виде файла и таблицы
---------------------------------------------
x = pr.Data_Table(pr.data_ur_neispr_obor_middle_year)
print(x)
x.open_data()

ДАННЫЕ статистических расчетов
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

ПОСТРОЕНИЕ графиков:
--------------------
a = pr.Graphics_Indicators_Production(pr.data_ur_neispr_obor_year, name= 'Уровень неисправности оборудования по годам')
b = pr.Graphics_Indicators_Production(pr.data_ur_nesoot_prod_year, name= 'Уровень несоответствующей продукции по годам')
c = pr.Graphics_Indicators_Production(pr.data_ur_teh_oth_year, name= 'Уровень техотходов по годам', critery=2)
d = pr.Graphics_Indicators_Production(pr.data_ur_otkl_prod_year, name= 'Уровень отклонений продукции Котк по годам')
e = pr.Graphics_Indicators_Production(pr.data_ur_prost_kach_year, name= 'Уровень простоя оборудования из-за несоответствующего качества расходных материалов Кпр кач')
f = pr.Graphics_Indicators_Production(pr.data_ur_prost_nepost_year, name= 'Уровень простоя оборудования из-за непоставки расходных материалов Кпр кол')
g = pr.Graphics_Number_Production(pr.data_number_year, name= 'Количество выпущенной п/б ленты  по годам')

# Полугодовые показатели
h = pr.Graphics_Indicators_Production(pr.data_ur_neispr_obor_middle_year, name= 'Уровень неисправности оборудования по полугодиям')
i = pr.Graphics_Indicators_Production(pr.data_ur_nesoot_prod_middle_year, name= 'Уровень несоответствующей продукции по полугодиям')
j = pr.Graphics_Indicators_Production(pr.data_ur_teh_oth_middle_year, name= 'Уровень техотходов по полугодиям', critery=2)
k = pr.Graphics_Indicators_Production(pr.data_ur_otkl_prod_middle_year, name= 'Уровень отклонений продукции Котк по полугодиям')
l = pr.Graphics_Indicators_Production(pr.data_ur_prost_kach_middle_year, name= 'Уровень простоя оборудования из-за несоответствующего качества расходных материалов Кпр кач по полугодиям')
m = pr.Graphics_Indicators_Production(pr.data_ur_prost_nepost_middle_year, name= 'Уровень простоя оборудования из-за непоставки расходных материалов Кпр кол по полугодиям')
n = pr.Graphics_Number_Production(pr.data_number_middle_year, name= 'Количество выпущенной п/б ленты  по полугодиям')
plt.show()

СРАВНЕНИЕ значений с предыдущими результатами
---------------------------------------------
x = pr.Comparise(pr.data_kol_vip_prod_year)
print(x)
print(x.score())

РАСХОД материалов
------------------
x = pr.MaterialConsumption(pr.data_ur_rash_mater_year)
print(x)
print(x.excess())

СОХРАНЕНИЕ графиков и результатов
---------------------------------
pr.Save_Data()
"""
import os
import sys
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
#-------------------------------------------------------
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
# импорт библиотеки для вывода табличных данных в консоли(терминале)
from prettytable import PrettyTable
# импорт модуля для абстрактных классов
from abc import ABC, abstractmethod

#ЛОГИРОВАНИЕ
logging.config.fileConfig('logging.conf') # файл конфигурации
logger = logging.getLogger('indicators.production') # возвращает объект логгера
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

try:
# импорт DataFrame объектов с исходными данными
    from Data import data_kol_vip_prod_year, data_ur_neispr_obor_year,data_ur_nesoot_prod_year, data_ur_teh_oth_year, data_kol_vip_mufty_year, data_kol_vip_kompl_year, data_kol_narezki_year, data_kol_rezki_pvh_lip_year, data_ur_rash_mater_year, data_ur_otkl_prod_year, data_ur_prost_kach_year,data_ur_prost_nepost_year, data_ur_neispr_obor_middle_year, data_ur_nesoot_prod_middle_year, data_ur_teh_oth_middle_year,data_kol_vip_prod_middle_year, data_kol_vip_mufty_middle_year,data_kol_vip_kompl_middle_year, data_kol_narezki_middle_year,data_kol_rezki_pvh_lip_middle_year, data_ur_rash_mater_middle_year,data_ur_otkl_prod_middle_year, data_ur_prost_kach_middle_year,data_ur_prost_nepost_middle_year

# ИСХОДНЫЕ ДАННЫЕ (ДОПОЛНИТЕЛЬНОЕ ФОРМАТИРОВАНИЕ):
##################################################
    logger.info("start initial assignment") # logging

    INDICATOR_NAME = [
                    "Количество выпущенной продукции (ленты) Квып",
                    "Уровень неисправности оборудования Кно",
                    "Уровень несоответствующей прод. в проц. произв. Кн",
                    "Уровень техотходов по годам",
                    "Количество выпущенных муфт",
                    "Количество выпущенных комплектов",
                    "Количество нарезки пб ленты",
                    "Количество резки ПВХ липкой",
                    # другой подсчёт статистики
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
                    # другой подсчёт статистики
                    # "Уровень расхода материалов Крм по полугодиям",
                    "Уровень отклонений продукции Котк по полугодиям",
                    "Уровень простоя обор. Кпр кач по полугодиям",
                    "Уровень простоя обор. Кпр кол по полугодиям"
                 ]#запись наименований

    INDICATOR_NAME_ADD = [
                    "Уровень расхода материалов Крм",
                    "Уровень расхода материалов Крм по полугодиям",
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
    logger.info("OK! Load Data") # logging
    NAME_INPUT_ADD = {
                    # другой подсчёт статистики
                    '009': data_ur_rash_mater_year,
                    '021': data_ur_rash_mater_middle_year,
                    } #идентификатор
    logger.info("OK! Load Data") # logging
    lst_name = [data_kol_vip_prod_year, data_ur_neispr_obor_year,data_ur_nesoot_prod_year, data_ur_teh_oth_year,data_kol_vip_mufty_year, data_kol_vip_kompl_year, data_kol_narezki_year, data_kol_rezki_pvh_lip_year, data_ur_otkl_prod_year,data_ur_prost_kach_year, data_ur_prost_nepost_year,data_ur_neispr_obor_middle_year, data_ur_nesoot_prod_middle_year,data_ur_teh_oth_middle_year, data_kol_vip_prod_middle_year,data_kol_vip_mufty_middle_year, data_kol_vip_kompl_middle_year,data_kol_narezki_middle_year, data_kol_rezki_pvh_lip_middle_year,data_ur_otkl_prod_middle_year, data_ur_prost_kach_middle_year,data_ur_prost_nepost_middle_year] #список для сохранения стаистических расчетов
    logger.info("OK! Load Data") # logging
    # ИСХОДНЫЕ ДАННЫЕ (ДОПОЛНИТЕЛЬНОЕ ФОРМАТИРОВАНИЕ ДЛЯ ПОСТРОЕНИЯ ГРАФИКА):
    #########################################################################
    data_number_year = pd.concat([data_kol_vip_prod_year, data_kol_vip_mufty_year,data_kol_vip_kompl_year, data_kol_narezki_year,data_kol_rezki_pvh_lip_year], axis=1)# Конкатенация pd.DataFrame объектов
    data_number_middle_year = pd.concat([data_kol_vip_prod_middle_year,data_kol_vip_mufty_middle_year, data_kol_vip_kompl_middle_year,data_kol_narezki_middle_year, data_kol_rezki_pvh_lip_middle_year], axis=1)# Конкатенация pd.DataFrame объектов
    logger.info("OK! Calculation Data") # logging
    # ИСХОДНЫЕ ДАННЫЕ (ДОПОЛНИТЕЛЬНОЕ ФОРМАТИРОВАНИЕ ДЛЯ СОХРАНЕНИЯ):
    #################################################################
    data_add = pd.concat([data_kol_vip_prod_year,data_ur_neispr_obor_year,data_ur_nesoot_prod_year,data_ur_teh_oth_year,data_kol_vip_mufty_year, data_kol_vip_kompl_year, data_kol_narezki_year, data_kol_rezki_pvh_lip_year, data_ur_otkl_prod_year,data_ur_prost_kach_year,data_ur_prost_nepost_year,data_ur_neispr_obor_middle_year,data_ur_nesoot_prod_middle_year,data_ur_teh_oth_middle_year,data_kol_vip_prod_middle_year,data_kol_vip_mufty_middle_year,data_kol_vip_kompl_middle_year,data_kol_narezki_middle_year,data_kol_rezki_pvh_lip_middle_year,data_ur_otkl_prod_middle_year,data_ur_prost_kach_middle_year,data_ur_prost_nepost_middle_year], axis=1)# Конкатенация pd.DataFrame объектов
    logger.info("OK! Calculation Data") # logging
    logger.info('OK! end initial assignment ') # logging

    # ИСХОДНЫЕ ДАННЫЕ (ПЕРЕМЕННЫЕ ШАБЛОНА process_b_7_5):
    #################################################################
    prev_year = data_kol_vip_prod_year.index[-2]
    next_year = data_kol_vip_prod_year.index[-1]

    n_13 = '13'# нумерация строк
    n_14 = '14'# нумерация строк
    n_15 = '15'# нумерация строк
    n_16 = '16'# нумерация строк
    n_17 = '17'# нумерация строк
    n_18 = '18'# нумерация строк
    n_19 = '19'# нумерация строк
    n_20 = '20'# нумерация строк

    # переменные уровня несоответствующей продукции
    i_13_1_1 = data_ur_nesoot_prod_year.tail(2).iloc[0,0]
    i_13_1_2 = None
    i_13_1_3 = None
    i_13_1_4 = None
    i_13_1_5 = None

    i_13_2_1 = data_ur_nesoot_prod_year.tail(2).iloc[1,0]
    i_13_2_2 = None
    i_13_2_3 = None
    i_13_2_4 = None
    i_13_2_5 = None

    i_13_1_m_1 = data_ur_nesoot_prod_middle_year.tail(2).iloc[0,0]
    i_13_1_m_2 = None
    i_13_1_m_3 = None
    i_13_1_m_4 = None
    i_13_1_m_5 = None

    i_13_2_m_1 = data_ur_nesoot_prod_middle_year.tail(2).iloc[1,0]
    i_13_2_m_2 = None
    i_13_2_m_3 = None
    i_13_2_m_4 = None
    i_13_2_m_5 = None

    # переменные количества выпускаемой продукции
    i_14_1_1 = data_kol_vip_prod_year.tail(2).iloc[0,0]
    i_14_1_2 = data_kol_narezki_year.tail(2).iloc[0,0]
    i_14_1_3 = data_kol_vip_mufty_year.tail(2).iloc[0,0]
    i_14_1_4 = data_kol_vip_kompl_year.tail(2).iloc[0,0]
    i_14_1_5 = data_kol_rezki_pvh_lip_year.tail(2).iloc[0,0]

    i_14_2_1 = data_kol_vip_prod_year.tail(2).iloc[1,0]
    i_14_2_2 = data_kol_narezki_year.tail(2).iloc[1,0]
    i_14_2_3 = data_kol_vip_mufty_year.tail(2).iloc[1,0]
    i_14_2_4 = data_kol_vip_kompl_year.tail(2).iloc[1,0]
    i_14_2_5 = data_kol_rezki_pvh_lip_year.tail(2).iloc[1,0]

    i_14_1_m_1 = data_kol_vip_prod_middle_year.tail(2).iloc[0,0]
    i_14_1_m_2 = data_kol_narezki_middle_year.tail(2).iloc[0,0]
    i_14_1_m_3 = data_kol_vip_mufty_middle_year.tail(2).iloc[0,0]
    i_14_1_m_4 = data_kol_vip_kompl_middle_year.tail(2).iloc[0,0]
    i_14_1_m_5 = data_kol_rezki_pvh_lip_middle_year.tail(2).iloc[0,0]

    i_14_2_m_1 = data_kol_vip_prod_middle_year.tail(2).iloc[1,0]
    i_14_2_m_2 = data_kol_narezki_middle_year.tail(2).iloc[1,0]
    i_14_2_m_3 = data_kol_vip_mufty_middle_year.tail(2).iloc[1,0]
    i_14_2_m_4 = data_kol_vip_kompl_middle_year.tail(2).iloc[1,0]
    i_14_2_m_5 = data_kol_rezki_pvh_lip_middle_year.tail(2).iloc[1,0]

    # переменные уровня расхода материала
    i_15_1 = data_ur_rash_mater_year.loc[prev_year].astype(str).apply(lambda x: x + '<br>').to_string(header=False, index=False)
    i_15_m_1 = data_ur_rash_mater_middle_year.loc[prev_year].astype(str).apply(lambda x: x + '<br>').to_string(header=False, index=False)
    i_15_2 = data_ur_rash_mater_year.loc[next_year].astype(str).apply(lambda x: x + '<br>').to_string(header=False, index=False)
    i_15_m_2 = data_ur_rash_mater_middle_year.loc[next_year].astype(str).apply(lambda x: x + '<br>').to_string(header=False, index=False)

    # переменные уровня технических отходов
    i_16_1 = data_ur_teh_oth_year.tail(2).iloc[0,0]
    i_16_m_1 = data_ur_teh_oth_middle_year.tail(2).iloc[0,0]
    i_16_2 = data_ur_teh_oth_year.tail(2).iloc[1,0]
    i_16_m_2 = data_ur_teh_oth_middle_year.tail(2).iloc[1,0]

    # переменные уровня неисправности оборудования
    i_17_1 = data_ur_neispr_obor_year.tail(2).iloc[0,0]
    i_17_m_1 = data_ur_neispr_obor_middle_year.tail(2).iloc[0,0]
    i_17_2 = data_ur_neispr_obor_year.tail(2).iloc[1,0]
    i_17_m_2 = data_ur_neispr_obor_middle_year.tail(2).iloc[1,0]

    # переменные уровня простоя оборудования из-за качества
    i_18_1 = data_ur_prost_kach_year.tail(2).iloc[0,0]
    i_18_m_1 = data_ur_prost_kach_middle_year.tail(2).iloc[0,0]
    i_18_2 = data_ur_prost_kach_year.tail(2).iloc[1,0]
    i_18_m_2 = data_ur_prost_kach_middle_year.tail(2).iloc[1,0]

    # переменные уровня простоя оборудования из-за непоставок
    i_19_1 = data_ur_prost_nepost_year.tail(2).iloc[0,0]
    i_19_m_1 = data_ur_prost_nepost_middle_year.tail(2).iloc[0,0]
    i_19_2 = data_ur_prost_nepost_year.tail(2).iloc[1,0]
    i_19_m_2 = data_ur_prost_nepost_middle_year.tail(2).iloc[1,0]

    # переменные уровня отклонений продукции
    i_20_1 = data_ur_otkl_prod_year.tail(2).iloc[0,0]
    i_20_m_1 = data_ur_otkl_prod_middle_year.tail(2).iloc[0,0]
    i_20_2 = data_ur_otkl_prod_year.tail(2).iloc[1,0]
    i_20_m_2 = data_ur_otkl_prod_middle_year.tail(2).iloc[1,0]

    # переменные изменений уровня несоответствующей продукции
    e_13_1 = round(i_13_2_1-i_13_1_1, 2)
    e_13_m_1 = round(i_13_2_m_1-i_13_1_m_1, 2)

    # переменные изменений количества выпускаемой продукции
    e_14_1_1 =round(i_14_2_1-i_14_1_1, 2)
    e_14_1_2 =round(i_14_2_2-i_14_1_2, 2)
    e_14_1_3 =round(i_14_2_3-i_14_1_3, 2)
    e_14_1_4 =round(i_14_2_4-i_14_1_4, 2)
    e_14_1_5 =round(i_14_2_5-i_14_1_5, 2)

    e_14_1_m_1 = round(i_14_2_m_1-i_14_1_m_1, 2)
    e_14_1_m_2 = round(i_14_2_m_2-i_14_1_m_2, 2)
    e_14_1_m_3 = round(i_14_2_m_3-i_14_1_m_3, 2)
    e_14_1_m_4 = round(i_14_2_m_4-i_14_1_m_4, 2)
    e_14_1_m_5 = round(i_14_2_m_5-i_14_1_m_5, 2)

    # переменные изменений уровня расхода материала
    e_15_1 = data_ur_rash_mater_year[data_ur_rash_mater_year[data_ur_rash_mater_year.columns[1]]>100].astype(str).apply(lambda x: x + '<br>').to_string(header=False, index=False)
    e_15_m_1 = data_ur_rash_mater_middle_year[data_ur_rash_mater_middle_year[data_ur_rash_mater_middle_year.columns[1]]>100].astype(str).apply(lambda x: x + '<br>').to_string(header=False, index=False)

    # переменные изменений уровня технических отходов
    e_16_1 = round(i_16_2 - i_16_1, 2)
    e_16_m_1 = round(i_16_m_2-i_16_m_1, 2)
    # переменные изменений уровня неисправности оборудования
    e_17_1 = round(i_17_2-i_17_1, 2)
    e_17_m_1 = round(i_17_m_2-i_17_m_1, 2)
    # переменные изменений уровня простоя оборудования из-за качества
    e_18_1 = round(i_18_2-i_18_1, 2)
    e_18_m_1 = round(i_18_m_2-i_18_m_1, 2)
    # переменные изменений уровня простоя оборудования из-за непоставок
    e_19_1 = round(i_19_2-i_19_1, 2)
    e_19_m_1 = round(i_19_m_2 - i_19_m_1, 2)
    # переменные изменений уровня отклонений продукции
    e_20_1 = round(i_20_2 - i_20_1, 2)
    e_20_m_1 = round(i_20_m_2 - i_20_m_1, 2)

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
            self.logger = logging.getLogger('indicators.production.Info')
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

    @time_of_function
    class Info_add(object):
        """
        Класс вывода дополнительной таблицы на экран для выбора идентификатора
        """
        def __init__(self):
            self.logger = logging.getLogger('indicators.production.Info_add')
            self.logger.info('__Init__ Info_add')
            self.x = PrettyTable()
            field_names = ['Идентификатор', 'Наименование']
            self.x.add_column(field_names[1], INDICATOR_NAME_ADD)
            self.x.add_column(field_names[0], list(NAME_INPUT_ADD.keys()))

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
            self.logger = logging.getLogger('indicators.production.Data_Table')
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
                print(tabulate(self.data, headers = 'keys', tablefmt = 'psql'), file=open(r'data_production.temp', 'w', encoding = 'utf-8'))
                os.system('data_production.temp')

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
    class Graphics_Indicators_Production(Abstract.Graphic):
        """
        Класс запуска графического отображения показателей качества
        Процесса Б(7.5) "Производство продукции", за исключением показателей
        количества выпущенной продукции
        """
        num_instances = 0 # переменная счётчика экземпляров класса

        def __init__(self, data, name='Название графика', critery = 0):
            super().__init__(data)
            self.logger = logging.getLogger('indicators.production.Graphics_Indicators_Production')
            self.logger.info('__Init__ Graphics_Indicators_Production')
            self.__class__.num_instances += 1 # счётчик экземпляров класса
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
    logger.info("OK! Load object class") # logging

except Exception:
    logger.error(f'FAILED! Graphics_Indicators_Production_Error: {sys.exc_info()[:2]}') # logging

try:
    class Graphics_Number_Production(Abstract.Graphic):
        """
        Класс запуска графического отображения показателя количества выпущенной продукции Процесса Б(7.5) "Производство продукции".
        """
        def __init__(self, data, name='Название графика', critery = 0):
            super().__init__(data)
            self.logger = logging.getLogger('indicators.production.Graphics_Number_Production')
            self.logger.info('__Init__ Graphics_Number_Production')
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
            ax2 = plt.bar(x_ax2,y_ax2,label='Значение показателя', color='red', alpha=0.5)
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
            ax3 = plt.bar(x_ax3,y_ax3,label='Значение показателя', color='red', alpha=0.5)
            ax3 = plt.plot(x_ax3,y_ax3,label='Значение показателя',marker = 'D', color='black', alpha=0.5)
            ax3 = plt.title(data_ax3.name, fontsize=10, y=1.05)
            ax3 = plt.grid(axis='both', color='black', linestyle='dotted',linewidth=1)
            ax3 = plt.legend(fontsize=4, shadow=True, framealpha=1, edgecolor='r', title='', loc='best')
            # График слоя ax4
            ax4 = fig.add_subplot(gs[-1, 0])
            data_ax4 = self.data.iloc[:, 3]
            x_ax4 = data_ax4.index.tolist()
            x_ax4 = np.array(x_ax4)
            y_ax4 = data_ax4.transpose()
            y_ax4 = np.array(y_ax4)
            ax4 = plt.bar(x_ax4,y_ax4,label='Значение показателя', color='red', alpha=0.5)
            ax4 = plt.plot(x_ax4,y_ax4,label='Значение показателя',marker = 'D', color='black', alpha=0.5)
            ax4 = plt.title(data_ax4.name, fontsize=10, y=1.05)
            ax4 = plt.grid(axis='both', color='black', linestyle='dotted',linewidth=1)
            ax4 = plt.legend(fontsize=4, shadow=True, framealpha=1, edgecolor='r', title='', loc='best')
            # График слоя ax5
            ax5 = fig.add_subplot(gs[-1, -2])
            data_ax5 = self.data.iloc[:, 4]
            x_ax5 = data_ax5.index.tolist()
            x_ax5 = np.array(x_ax5)
            y_ax5 = data_ax5.transpose()
            y_ax5 = np.array(y_ax5)
            ax5 = plt.bar(x_ax5, y_ax5,label='Значение показателя', color='red', alpha=0.5)
            ax5 = plt.plot(x_ax5,y_ax5,label='Значение показателя',marker = 'D', color='black', alpha=0.5)
            ax5 = plt.title(data_ax5.name, fontsize=10, y=1.05)
            ax5 = plt.grid(axis='both', color='black', linestyle='dotted',linewidth=1)
            ax5 = plt.legend(fontsize=4, shadow=True, framealpha=1, edgecolor='r', title='', loc='best')

    logger.info("OK! Load object class") # logging

except Exception:
    logger.error(f'FAILED! Graphics_Number_Production(): {sys.exc_info()[:2]}') # logging

try:
    @time_of_function
    class Comparise(object):
        """
        Класс сравнительного анализа с результатами предыдущего отчётного периода
        #################################################################
        """
        def __init__(self, data: pd.DataFrame):
            self.logger = logging.getLogger('indicators.production.Comparise')
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
    class MaterialConsumption(object):
        """
        Класс просмотра превышения критерия уровня расхода материалов Крм (Критерий <=100%) и просмотра данных показателя.
        #################################################################
        """
        def __init__(self, data: pd.DataFrame):
            self.logger = logging.getLogger('indicators.production.MaterialConsumption')
            self.logger.info('__Init__ MaterialConsumption')
            self.data = data

        def __str__(self):
            """
            Строковое представление данных
            """
            return tabulate(self.data, headers = 'keys', tablefmt = 'psql')

        def __repr__(self):
            return f'Class: {self.__class__.__qualname__}\n {self.__class__.__doc__}'

        def excess(self):
            """
            Превышение критерия показателя ВЫВОД ПО КРИТЕРИЮ???????
            """
            return tabulate(self.data[self.data[self.data.columns[1]]>100], headers = 'keys', tablefmt = 'psql')


    logger.info("OK! Load object class") # logging

except Exception:
    logger.error(f'FAILED! MaterialConsumption(): {sys.exc_info()[:2]}') # logging

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
            self.logger = logging.getLogger('indicators.production.Save_Data')
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

                if data_ur_neispr_obor_year.isin([0]).all(axis=None) == False:
                    graphic_year_one = Graphics_Indicators_Production(data_ur_neispr_obor_year, name= 'Уровень неисправности оборудования по годам')
                    graphic_year_one.save_graphic('files/001')
                    logger.debug("OK! GRAPHICS_1") # logging
                else:
                    pass

                if data_ur_nesoot_prod_year.isin([0]).all(axis=None) == False:
                    graphic_year_two = Graphics_Indicators_Production(data_ur_nesoot_prod_year, name= 'Уровень несоответствующей продукции по годам')
                    graphic_year_two.save_graphic('files/002')
                    logger.debug("OK! GRAPHICS_2") # logging
                else:
                    pass

                if data_ur_teh_oth_year.isin([0]).all(axis=None) == False:
                    graphic_year_three = Graphics_Indicators_Production(data_ur_teh_oth_year, name= 'Уровень техотходов по годам', critery=2)
                    graphic_year_three.save_graphic('files/003')
                    logger.debug("OK! GRAPHICS_3") # logging
                else:
                    pass

                if data_ur_otkl_prod_year.isin([0]).all(axis=None) == False:
                    graphic_year_four = Graphics_Indicators_Production(data_ur_otkl_prod_year, name= 'Уровень отклонений продукции Котк по годам')
                    graphic_year_four.save_graphic('files/004')
                    logger.debug("OK! GRAPHICS_4") # logging
                else:
                    pass

                if data_ur_prost_kach_year.isin([0]).all(axis=None) == False:
                    graphic_year_five = Graphics_Indicators_Production(data_ur_prost_kach_year, name= 'Уровень простоя оборудования из-за несоответствующего качества расходных материалов Кпр кач')
                    graphic_year_five.save_graphic('files/005')
                    logger.debug("OK! GRAPHICS_5") # logging
                else:
                    pass

                if data_ur_prost_nepost_year.isin([0]).all(axis=None) == False:
                    graphic_year_six = Graphics_Indicators_Production(data_ur_prost_nepost_year, name= 'Уровень простоя оборудования из-за непоставки расходных материалов Кпр кол')
                    graphic_year_six.save_graphic('files/006')
                    logger.debug("OK! GRAPHICS_6") # logging
                else:
                    pass

                if data_number_year.isin([0]).all(axis=None) == False:
                    graphic_year_seven = Graphics_Number_Production(data_number_year, name= 'Количество выпущенной п/б ленты по годам')
                    graphic_year_seven.save_graphic('files/007')
                    logger.debug("OK! GRAPHICS_7") # logging
                else:
                    pass

                # Полугодовые показатели
                if data_ur_neispr_obor_middle_year.isin([0]).all(axis=None) == False:
                    graphic_middle_one = Graphics_Indicators_Production(data_ur_neispr_obor_middle_year, name= 'Уровень неисправности оборудования по полугодиям')
                    graphic_middle_one.save_graphic('files/008')
                    logger.debug("OK! GRAPHICS_8") # logging
                else:
                    pass

                if data_ur_nesoot_prod_middle_year.isin([0]).all(axis=None) == False:
                    graphic_middle_two = Graphics_Indicators_Production(data_ur_nesoot_prod_middle_year, name= 'Уровень несоответствующей продукции по полугодиям')
                    graphic_middle_two.save_graphic('files/009')
                    logger.debug("OK! GRAPHICS_9") # logging
                else:
                    pass

                if data_ur_teh_oth_middle_year.isin([0]).all(axis=None) == False:
                    graphic_middle_three = Graphics_Indicators_Production(data_ur_teh_oth_middle_year, name= 'Уровень техотходов по полугодиям', critery=2)
                    graphic_middle_three.save_graphic('files/010')
                    logger.debug("OK! GRAPHICS_10") # logging
                else:
                    pass

                if data_ur_otkl_prod_middle_year.isin([0]).all(axis=None) == False:
                    graphic_middle_four = Graphics_Indicators_Production(data_ur_otkl_prod_middle_year, name= 'Уровень отклонений продукции Котк по полугодиям')
                    graphic_middle_four.save_graphic('files/011')
                    logger.debug("OK! GRAPHICS_11") # logging
                else:
                    pass

                if data_ur_prost_kach_middle_year.isin([0]).all(axis=None) == False:
                    graphic_middle_five = Graphics_Indicators_Production(data_ur_prost_kach_middle_year, name= 'Уровень простоя оборудования в Кпр кач по полугодиям')
                    graphic_middle_five.save_graphic('files/012')
                    logger.debug("OK! GRAPHICS_12") # logging
                else:
                    pass

                if data_ur_prost_nepost_middle_year.isin([0]).all(axis=None) == False:
                    graphic_middle_six = Graphics_Indicators_Production(data_ur_prost_nepost_middle_year, name= 'Уровень простоя оборудования из-за непоставки расходных материалов Кпр кол по полугодиям')
                    graphic_middle_six.save_graphic('files/013')
                    logger.debug("OK! GRAPHICS_13") # logging
                else:
                    pass

                if data_number_middle_year.isin([0]).all(axis=None) == False:
                    graphic_middle_seven = Graphics_Number_Production(data_number_middle_year, name= 'Количество выпущенной п/б ленты  по полугодиям')
                    graphic_middle_seven.save_graphic('files/014')
                    logger.debug("OK! GRAPHICS_14") # logging
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
        Обычно метакласс переопределяет метод __new__ или __init__ класса type, с целью взять на себя управление созданием или инициализацией нового объекта класса. Как и при использовании декораторов классов, суть состоит в том, чтобы определить программный код, который будет вызываться автоматически на этапе создания класса. Оба способа позволяют расширять классы или возвращать произвольные объекты для его замены – протокол с практически неограниченными возaiможностями.
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


    ###########################################################################
    # NEW_COMMANDs
    ###########################################################################

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

    class ThreeCommand(BaseCommand):
        def label():
            return 'Графики-3'

        def perform(self, object, *args, **kwargs):
            # Графики Процесса Б(7.5) "Производство продукции"
            # Годовые показатели
            if data_ur_neispr_obor_year.isin([0]).all(axis=None) == False:
                graphic_year_one = Graphics_Indicators_Production(data_ur_neispr_obor_year, name= 'Уровень неисправности оборудования по годам')
            else:
                pass
            if data_ur_nesoot_prod_year.isin([0]).all(axis=None) == False:
                graphic_year_two = Graphics_Indicators_Production(data_ur_nesoot_prod_year, name= 'Уровень несоответствующей продукции по годам')
            else:
                pass
            if data_ur_teh_oth_year.isin([0]).all(axis=None) == False:
                graphic_year_three = Graphics_Indicators_Production(data_ur_teh_oth_year, name= 'Уровень техотходов по годам', critery=2)
            else:
                pass
            if data_ur_otkl_prod_year.isin([0]).all(axis=None) == False:
                graphic_year_four = Graphics_Indicators_Production(data_ur_otkl_prod_year, name= 'Уровень отклонений продукции Котк по годам')
            else:
                pass
            if data_ur_prost_kach_year.isin([0]).all(axis=None) == False:
                graphic_year_five = Graphics_Indicators_Production(data_ur_prost_kach_year, name= 'Уровень простоя оборудования из-за несоответствующего качества расходных материалов Кпр кач')
            else:
                pass
            if data_ur_prost_nepost_year.isin([0]).all(axis=None) == False:
                graphic_year_six = Graphics_Indicators_Production(data_ur_prost_nepost_year, name= 'Уровень простоя оборудования из-за непоставки расходных материалов Кпр кол')
            else:
                pass
            if data_number_year.isin([0]).all(axis=None) == False:
                graphic_year_seven = Graphics_Number_Production(data_number_year, name= 'Количество выпущенной п/б ленты  по годам')
            else:
                pass
            # Полугодовые показатели
            if data_ur_neispr_obor_middle_year.isin([0]).all(axis=None) == False:
                graphic_middle_one = Graphics_Indicators_Production(data_ur_neispr_obor_middle_year, name= 'Уровень неисправности оборудования по полугодиям')
            else:
                pass
            if data_ur_nesoot_prod_middle_year.isin([0]).all(axis=None) == False:
                graphic_middle_two = Graphics_Indicators_Production(data_ur_nesoot_prod_middle_year, name= 'Уровень несоответствующей продукции по полугодиям')
            else:
                pass
            if data_ur_teh_oth_middle_year.isin([0]).all(axis=None) == False:
                graphic_middle_three = Graphics_Indicators_Production(data_ur_teh_oth_middle_year, name= 'Уровень техотходов по полугодиям', critery=2)
            else:
                pass
            if data_ur_otkl_prod_middle_year.isin([0]).all(axis=None) == False:
                graphic_middle_four = Graphics_Indicators_Production(data_ur_otkl_prod_middle_year, name= 'Уровень отклонений продукции Котк по полугодиям')
            else:
                pass
            if data_ur_prost_kach_middle_year.isin([0]).all(axis=None) == False:
                graphic_middle_five = Graphics_Indicators_Production(data_ur_prost_kach_middle_year, name= 'Уровень простоя оборудования из-за несоответствующего качества расходных материалов Кпр кач по полугодиям')
            else:
                pass
            if data_ur_prost_nepost_middle_year.isin([0]).all(axis=None) == False:
                graphic_middle_six = Graphics_Indicators_Production(data_ur_prost_nepost_middle_year, name= 'Уровень простоя оборудования из-за непоставки расходных материалов Кпр кол по полугодиям')
            else:
                pass
            if data_number_middle_year.isin([0]).all(axis=None) == False:
                graphic_middle_seven = Graphics_Number_Production(data_number_middle_year, name= 'Количество выпущенной п/б ленты  по полугодиям')
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
            return 'Расход-5'

        def perform(self, object, *args, **kwargs):
            #СРАВНЕНИЕ
            info = Info_add()
            print(info)
            while True:
                try:
                    a = input("Укажите идентификатор|exit-выход: ")
                    if a =='exit':
                        break
                    reading = NAME_INPUT_ADD[a] # ВЫБОР НАИМЕНОВАНИЯ
                    df = reading
                    x = MaterialConsumption(df)
                    print(x)
                    print(f'КРИТЕРИЙ ПРЕВЫШЕН ПО СЛЕДУЮЩИМ МАТЕРИАЛАМ:\n{x.excess()}')
                except KeyboardInterrupt:
                    print('Выход...')
                    break
                except:
                    print("Неправильный идентификатор, попробуйте снова!!!")

    class SixCommand(BaseCommand):
        def label():
            return 'В файл-6'

        def perform(self, object, *args, **kwargs):
            #СОХРАНЕНИЕ
            Save_Data()

    class NewCommand(BaseCommand):
        def label():
            return 'Комманда-0'

        def perform(self, object, *args, **kwargs):
            print(f'Кол-во экземпляров класса {Graphics_Indicators_Production.__name__} = {Graphics_Indicators_Production.num_instances}')
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

