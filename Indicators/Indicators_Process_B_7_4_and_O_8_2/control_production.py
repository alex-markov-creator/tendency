#-*- coding: utf-8 -*-
# version 0.1a
# author: andrew.bezzubov - 09/11/2020 year
"""
=============================================================================
control_production.py - Модуль обработки данных по следующим показателям качества закупаемой(входящей) продукции:
- Кп – отношение количества случаев выявления несоответствий закупаемой продукции при входном контроле и в процессе производства к количеству партий материала, %;
- Км – отношение массы выявленной несоответствующей закупаемой продукции при входном контроле и в процессе производства к массе поступивших материалов, %.
Для сравнительного анализа, построения графиков и подсчета статистических данных, а также сохранения результатов в файл.

Поставляемые материалы по состоянию до 2020 года:
- Материал антиадгезионный на основе ПЭТ;
- Материал антиадгезионный на основе пленки;
- Материал антиадгезионный на основе бумаги;
- ПВХ липкая ООО "НПО Промхимтехнология";
- ПВХ липкая АО "БСК";
- ПВХ липкая ООО "СибТрубизол";
- Лента ПВХ марка "Б" ООО "Сэларон";
- Лента ПВХ марка "Б" ОАО "БСК";
- Лента ПВХ ООО "Сибтрубизол";
- Пакеты;
- Коробки;
- Коробки "Гофралюкс";
- ПЭКОМ;
- Полилен 40-ОБ-63;
- Полилен 40-ЛИ-63;
- Полилен 40-ЛИ-45;
- Политерм;
- Грунтовка "Транскор" №1;
- Праймер ПЛ-М;
- Праймер ПЛ-Л;
- Праймер НК-50;
- Грунтовка "Транскор" №2;
- Мастика Транскор - Л;
- Мастика Транскор - З;
- Мастика Биткор - Р;
- Мастика МБПР - З;
- Мастика МБПР - Л;
- Мастика Биткор - Р(У);
- Шпули;
- Муфта термоусаживающаяся ИЗТМ.

============================================================================
ИСХОДНЫЕ ДАННЫЕ - ФАЙЛ __init__.py в ../Data:
+---+-----------------------------------+-----------------------------------+
| № |  Переменная(общие показатели)     |    Наименование(общие показатели) |
+---+-----------------------------------+-----------------------------------+
|001|      data_km_mastic_year          |       Км_Мастика по годам...      |
|002|        data_km_pvh_year           |         Км_ПВХ по годам...        |
|003|      data_kp_mastic_year          |       Кп_Мастика по годам...      |
|004|        data_kp_pvh_year           |         Кп_ПВХ по годам...        |
|005|   data_km_mastic_middle_year      |    Км_Мастика по полугодиям...    |
|006|    data_km_pvh_middle_year        |      Км_ПВХ по полугодиям...      |
|007|   data_kp_mastic_middle_year      |    Кп_Мастика по полугодиям...    |
|008|    data_kp_pvh_middle_year        |      Кп_ПВХ по полугодиям...      |
+---------------------------------------------------------------------------+
| № |          Переменная               |           Наименование            |
+---+-----------------------------------------------------------------------+
|009|    data_km_antiadgeziv_year       |     Км_Антиадгезив по годам...    |
|010|    data_kp_antiadgeziv_year       |     Кп_Антиадгезив по годам...    |
|011|     data_km_bitkor_r_year         |      Км_Биткор_Р по годам...      |
|012|     data_kp_bitkor_r_year         |      Кп_Биткор_Р по годам...      |
|013|     data_km_bitkor_u_year         |     Км_Биткор_Р(У) по годам...    |
|014|     data_kp_bitkor_u_year         |     Кп_Биткор_Р(У) по годам...    |
|015|      data_km_korobki_year         |       Км_Коробки по годам...      |
|016|      data_kp_korobki_year         |       Кп_Коробки по годам...      |
|017|       data_km_mbpr_year           |        Км_МБПР по годам...        |
|018|       data_kp_mbpr_year           |        Кп_МБПР по годам...        |
|019|       data_km_mufty_year          |        Км_Муфты по годам...       |
|020|       data_kp_mufty_year          |        Кп_Муфты по годам...       |
|021|    data_km_bsk_pvh_lip_year       | Км_ОАО_БСК_липкая_ПВХ по годам... |
|022|    data_kp_bsk_pvh_lip_year       | Кп_ОАО_БСК_липкая_ПВХ по годам... |
|023|    data_km_selaron_pvh_year       |   Км_ООО_Сэларон_ПВХ по годам...  |
|024|    data_kp_selaron_pvh_year       |   Кп_ООО_Сэларон_ПВХ по годам...  |
|025|      data_km_bsk_pvh_year         |     Км_ПВХ_ОАО_БСК по годам...    |
|026|      data_kp_bsk_pvh_year         |     Кп_ПВХ_ОАО_БСК по годам...    |
|027|       data_km_pekom_year          |        Км_ПЭКОМ по годам...       |
|028|       data_kp_pekom_year          |        Кп_ПЭКОМ по годам...       |
|029|      data_km_pakety_year          | Км_Пакеты полиэтиленовые по го... |
|030|      data_kp_pakety_year          | Кп_Пакеты полиэтиленовые по го... |
|031|      data_km_polilen_year         |       Км_Полилен по годам...      |
|032|      data_kp_polilen_year         |       Кп_Полилен по годам...      |
|033|     data_km_politerm_year         |      Км_Политерм по годам...      |
|034|     data_kp_politerm_year         |      Кп_Политерм по годам...      |
|035| data_km_sibtrubizol_pvh_lip_year  | Км_Сибтрубизол_липкая_ПВХ по г... |
|036| data_kp_sibtrubizol_pvh_lip_year  | Кп_Сибтрубизол_липкая_ПВХ по г... |
|037|     data_km_transkor_year         |      Км_Транскор по годам...      |
|038|     data_kp_transkor_year         |      Кп_Транскор по годам...      |
|039|      data_km_shpuly_year          |        Км_Шпули по годам...       |
|040|      data_kp_shpuly_year          |        Кп_Шпули по годам...       |
|041| data_km_antiadgeziv_middle_year   |  Км_Антиадгезив по полугодиям...  |
|042| data_kp_antiadgeziv_middle_year   |  Кп_Антиадгезив по полугодиям...  |
|043|  data_km_bitkor_r_middle_year     |    Км_Биткор_Р по полугодиям...   |
|044|  data_kp_bitkor_r_middle_year     |    Кп_Биткор_Р по полугодиям...   |
|045|  data_km_bitkor_u_middle_year     |  Км_Биткор_Р(У) по полугодиям...  |
|046|  data_kp_bitkor_u_middle_year     |  Кп_Биткор_Р(У) по полугодиям...  |
|047|  data_km_korobki_middle_year      |    Км_Коробки по полугодиям...    |
|048|  data_kp_korobki_middle_year      |    Кп_Коробки по полугодиям...    |
|049|    data_km_mbpr_middle_year       |      Км_МБПР по полугодиям...     |
|050|    data_kp_mbpr_middle_year       |      Кп_МБПР по полугодиям...     |
|051|   data_km_mufty_middle_year       |     Км_Муфты по полугодиям...     |
|052|   data_kp_mufty_middle_year       |     Кп_Муфты по полугодиям...     |
|053| data_km_bsk_pvh_lip_middle_year   | Км_ОАО_БСК_липкая_ПВХ по полуг... |
|054| data_kp_bsk_pvh_lip_middle_year   | Кп_ОАО_БСК_липкая_ПВХ по полуг... |
|055| data_km_selaron_pvh_middle_year   | Км_ООО_Сэларон_ПВХ по полугоди... |
|056| data_kp_selaron_pvh_middle_year   | Кп_ООО_Сэларон_ПВХ по полугоди... |
|057|  data_km_bsk_pvh_middle_year      |  Км_ПВХ_ОАО_БСК по полугодиям...  |
|058|  data_kp_bsk_pvh_middle_year      |  Кп_ПВХ_ОАО_БСК по полугодиям...  |
|059|   data_km_pekom_middle_year       |     Км_ПЭКОМ по полугодиям...     |
|060|   data_kp_pekom_middle_year       |     Кп_ПЭКОМ по полугодиям...     |
|061|   data_km_pakety_middle_year      | Км_Пакеты полиэтиленовые по по... |
|062|   data_kp_pakety_middle_year      | Кп_Пакеты полиэтиленовые по по... |
|063|  data_km_polilen_middle_year      |    Км_Полилен по полугодиям...    |
|064|  data_kp_polilen_middle_year      |    Кп_Полилен по полугодиям...    |
|065|  data_km_transkor_middle_year     |    Км_Транскор по полугодиям...   |
|066|  data_kp_transkor_middle_year     |    Кп_Транскор по полугодиям...   |
|067|   data_km_shpuly_middle_year      |     Км_Шпули по полугодиям...     |
|068|   data_kp_shpuly_middle_year      |     Кп_Шпули по полугодиям...     |
+---+-----------------------------------+-----------------------------------+

Выполняет следующие задачи:
---------------------------
- Структурирование pandas.DataFrame объектов для дальнейшей обработки;
- Построение графиков;
- Расчёт и вывод статистических и исходных данных;
- Сохранение результатов в файл.

Дополнительные исходные данные для подсчетов корреляции:
-------------------------------------------------------
+---+-----------------------------------+-----------------------------------+
| № |  Переменная(общие показатели)     |    Наименование(общие показатели) |
+---+-----------------------------------+-----------------------------------+
|069|            data_1                 |       Км_Мастика по годам...      |
|070|            data_2                 |         Км_ПВХ по годам...        |
|071|            data_3                 |       Кп_Мастика по годам...      |
|072|            data_4                 |         Кп_ПВХ по годам...        |
|073|            data_5                 |    Км_Мастика по полугодиям...    |
|074|            data_6                 |      Км_ПВХ по полугодиям...      |
|075|            data_7                 |    Кп_Мастика по полугодиям...    |
|076|            data_8                 |      Кп_ПВХ по полугодиям...      |
+---------------------------------------------------------------------------+
Инструкции при импорте:
-----------------------
import pandas as pd
import matplotlib.pyplot as plt
import control_production as cp

СПРАВКА
-------
print(cp.__doc__)

Вывод исходных данных в виде файла и таблицы
---------------------------------------------
x = cp.Data_Table(cp.data_km_mastic_year)
print(x)
x.open_data()

Данные статистических расчетов
--------------------------------
x = cp.Statistic_Table(cp.data_km_mastic_year)
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
for i_name in cp.lst_kp:
    a = cp.Kp_Graphics(i_name)
    a.regres_graphic()
for i_name in cp.lst_km:
    a = cp.Km_Graphics(i_name)
    a.regres_graphic()
plt.show()

СОХРАНЕНИЕ графиков и результатов
---------------------------------
cp.Save_Data()
"""
import sys
import os
import time
sys.path.append(os.path.realpath('../..'))
# субродительский каталог в sys.path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
# модуль для вывода табличных данных
import Tools.Abstract_Parents as Abstract
# универсальный модуль для выполнения контракта
from scipy.stats import linregress
# модуль для построения линейной регрессии
from Data import *
# импорт DataFrame объектов с исходными данными
from prettytable import PrettyTable
# импорт библиотеки для вывода табличных данных в консоли(терминале)
from abc import ABC, abstractmethod
# импорт модуля для абстрактных классов

# ИСХОДНЫЕ ДАННЫЕ (ДОПОЛНИТЕЛЬНОЕ ФОРМАТИРОВАНИЕ):
##################################################
try:
    MATTER_NAME = [
                "Км_Мастика по годам",
                "Км_ПВХ по годам",
                "Кп_Мастика по годам",
                "Кп_ПВХ по годам",
                "Км_Мастика по полугодиям",
                "Км_ПВХ по полугодиям",
                "Кп_Мастика по полугодиям",
                "Кп_ПВХ по полугодиям"
                 ]#запись наименований (общие показатели)

    NAME_INPUT = {
                    '001':data_km_mastic_year,
                    '002':data_km_pvh_year,
                    '003':data_kp_mastic_year,
                    '004':data_kp_pvh_year,
                    '005':data_km_mastic_middle_year,
                    '006':data_km_pvh_middle_year,
                    '007':data_kp_mastic_middle_year,
                    '008':data_kp_pvh_middle_year
                    } #идентификатор (общие показатели)

    lst_name = [
                data_km_mastic_year,
                data_km_pvh_year,
                data_kp_mastic_year,
                data_kp_pvh_year,
                data_km_mastic_middle_year,
                data_km_pvh_middle_year,
                data_kp_mastic_middle_year,
                data_kp_pvh_middle_year
                ] # общий список объектов (общие показатели)

    lst_kp = [
            data_kp_mastic_year,
            data_kp_pvh_year,
            data_kp_mastic_middle_year,
            data_kp_pvh_middle_year
            ] # список объектов для Кп (общие показатели)

    lst_km = [
            data_km_mastic_year,
            data_km_pvh_year,
            data_km_mastic_middle_year,
            data_km_pvh_middle_year
            ] # список объектов для Км (общие показатели)

    MATTER_ADD_NAME = [
                        "Км_Антиадгезив по годам",
                        "Кп_Антиадгезив по годам",
                        "Км_Биткор_Р по годам",
                        "Кп_Биткор_Р по годам",
                        "Км_Биткор_Р(У) по годам",
                        "Кп_Биткор_Р(У) по годам",
                        "Км_Коробки по годам",
                        "Кп_Коробки по годам",
                        "Км_МБПР по годам",
                        "Кп_МБПР по годам",
                        "Км_Муфты по годам",
                        "Кп_Муфты по годам",
                        "Км_ОАО_БСК_липкая_ПВХ по годам",
                        "Кп_ОАО_БСК_липкая_ПВХ по годам",
                        "Км_ООО_Сэларон_ПВХ по годам",
                        "Кп_ООО_Сэларон_ПВХ по годам",
                        "Км_ПВХ_ОАО_БСК по годам",
                        "Кп_ПВХ_ОАО_БСК по годам",
                        "Км_ПЭКОМ по годам",
                        "Кп_ПЭКОМ по годам",
                        "Км_Пакеты полиэтиленовые по го",
                        "Кп_Пакеты полиэтиленовые по го",
                        "Км_Полилен по годам",
                        "Кп_Полилен по годам",
                        "Км_Политерм по годам",
                        "Кп_Политерм по годам",
                        "Км_Сибтрубизол_липкая_ПВХ по г",
                        "Кп_Сибтрубизол_липкая_ПВХ по г",
                        "Км_Транскор по годам",
                        "Кп_Транскор по годам",
                        "Км_Шпули по годам",
                        "Кп_Шпули по годам",
                        "Км_Антиадгезив по полугодиям",
                        "Кп_Антиадгезив по полугодиям",
                        "Км_Биткор_Р по полугодиям",
                        "Кп_Биткор_Р по полугодиям",
                        "Км_Биткор_Р(У) по полугодиям",
                        "Кп_Биткор_Р(У) по полугодиям",
                        "Км_Коробки по полугодиям",
                        "Кп_Коробки по полугодиям",
                        "Км_МБПР по полугодиям",
                        "Кп_МБПР по полугодиям",
                        "Км_Муфты по полугодиям",
                        "Кп_Муфты по полугодиям",
                        "Км_ОАО_БСК_липкая_ПВХ по полуг",
                        "Кп_ОАО_БСК_липкая_ПВХ по полуг",
                        "Км_ООО_Сэларон_ПВХ по полугоди",
                        "Кп_ООО_Сэларон_ПВХ по полугоди",
                        "Км_ПВХ_ОАО_БСК по полугодиям",
                        "Кп_ПВХ_ОАО_БСК по полугодиям",
                        "Км_ПЭКОМ по полугодиям",
                        "Кп_ПЭКОМ по полугодиям",
                        "Км_Пакеты полиэтиленовые по по",
                        "Кп_Пакеты полиэтиленовые по по",
                        "Км_Полилен по полугодиям",
                        "Кп_Полилен по полугодиям",
                        "Км_Транскор по полугодиям",
                        "Кп_Транскор по полугодиям",
                        "Км_Шпули по полугодиям",
                        "Кп_Шпули по полугодиям"
                     ]#запись наименований по материалам

    NAME_ADD_INPUT = {
                    '009':data_km_antiadgeziv_year,
                    '010':data_kp_antiadgeziv_year,
                    '011':data_km_bitkor_r_year,
                    '012':data_kp_bitkor_r_year,
                    '013':data_km_bitkor_u_year,
                    '014':data_kp_bitkor_u_year,
                    '015':data_km_korobki_year,
                    '016':data_kp_korobki_year,
                    '017':data_km_mbpr_year,
                    '018':data_kp_mbpr_year,
                    '019':data_km_mufty_year,
                    '020':data_kp_mufty_year,
                    '021':data_km_bsk_pvh_lip_year,
                    '022':data_kp_bsk_pvh_lip_year,
                    '023':data_km_selaron_pvh_year,
                    '024':data_kp_selaron_pvh_year,
                    '025':data_km_bsk_pvh_year,
                    '026':data_kp_bsk_pvh_year,
                    '027':data_km_pekom_year,
                    '028':data_kp_pekom_year,
                    '029':data_km_pakety_year,
                    '030':data_kp_pakety_year,
                    '031':data_km_polilen_year,
                    '032': data_kp_polilen_year,
                    '033':data_km_politerm_year,
                    '034':data_kp_politerm_year,
                    '035':data_km_sibtrubizol_pvh_lip_year,
                    '036':data_kp_sibtrubizol_pvh_lip_year,
                    '037':data_km_transkor_year,
                    '038':data_kp_transkor_year,
                    '039':data_km_shpuly_year,
                    '040':data_kp_shpuly_year,
                    '041':data_km_antiadgeziv_middle_year,
                    '042':data_kp_antiadgeziv_middle_year,
                    '043':data_km_bitkor_r_middle_year,
                    '044':data_kp_bitkor_r_middle_year,
                    '045':data_km_bitkor_u_middle_year,
                    '046':data_kp_bitkor_u_middle_year,
                    '047':data_km_korobki_middle_year,
                    '048':data_kp_korobki_middle_year,
                    '049':data_km_mbpr_middle_year,
                    '050': data_kp_mbpr_middle_year,
                    '051':data_km_mufty_middle_year,
                    '052':data_kp_mufty_middle_year,
                    '053':data_km_bsk_pvh_lip_middle_year,
                    '054':data_kp_bsk_pvh_lip_middle_year,
                    '055':data_km_selaron_pvh_middle_year,
                    '056':data_kp_selaron_pvh_middle_year,
                    '057':data_km_bsk_pvh_middle_year,
                    '058':data_kp_bsk_pvh_middle_year,
                    '059':data_km_pekom_middle_year,
                    '060':data_kp_pekom_middle_year,
                    '061':data_km_pakety_middle_year,
                    '062':data_kp_pakety_middle_year,
                    '063':data_km_polilen_middle_year,
                    '064':data_kp_polilen_middle_year,
                    '065':data_km_transkor_middle_year,
                    '066':data_kp_transkor_middle_year,
                    '067':data_km_shpuly_middle_year,
                    '068':data_kp_shpuly_middle_year
                    } #идентификатор по материалам

    # ИСХОДНЫЕ ДАННЫЕ (ДОПОЛНИТЕЛЬНОЕ ФОРМАТИРОВАНИЕ ДЛЯ КОРРЕЛЯЦИИ):
    #################################################################
    data_1 = pd.concat([data_km_mastic_year,data_km_bitkor_r_year, data_km_transkor_year, data_km_bitkor_u_year, data_km_mbpr_year], axis=1)
    # Конкатенация Км по мастике за год
    data_2 = pd.concat([data_kp_mastic_year,data_kp_bitkor_r_year, data_kp_transkor_year, data_kp_bitkor_u_year, data_kp_mbpr_year], axis=1)
    # Конкатенация Кп по мастике за год
    data_3 = pd.concat([data_km_pvh_year, data_km_selaron_pvh_year, data_km_bsk_pvh_year], axis=1)
    # Конкатенация Км по ПВХ за год
    data_4 = pd.concat([data_kp_pvh_year, data_kp_selaron_pvh_year, data_kp_bsk_pvh_year], axis=1)
    # Конкатенация Кп по ПВХ за год
    data_5 = pd.concat([data_km_mastic_middle_year, data_km_bitkor_r_middle_year, data_km_bitkor_u_middle_year,data_km_mbpr_middle_year, data_km_transkor_middle_year], axis=1)
    # Конкатенация Км по мастике за полугодие
    data_6 = pd.concat([data_kp_mastic_middle_year, data_kp_bitkor_r_middle_year, data_kp_bitkor_u_middle_year,data_kp_mbpr_middle_year, data_kp_transkor_middle_year], axis=1)
    # Конкатенация Кп по мастике за полугодие
    data_7 = pd.concat([data_km_pvh_middle_year, data_km_selaron_pvh_middle_year, data_km_bsk_pvh_middle_year], axis=1)
    # Конкатенация Кп по ПВХ за полугодие
    data_8 = pd.concat([data_kp_pvh_middle_year, data_kp_selaron_pvh_middle_year, data_kp_bsk_pvh_middle_year], axis=1)
    # Конкатенация Кп по ПВХ за полугодие

    NAME_CORR_INPUT = {
                '069':data_1,
                '070':data_2,
                '071':data_3,
                '072':data_4,
                '073':data_5,
                '074':data_6,
                '075':data_7,
                '076':data_8
                } # идентификатор данных для корреляции

except Exception:
    print(time.ctime(), 'Benchmark_Data_Error: ', sys.exc_info()[:2], file = open('log.txt', 'a'))

try:
    class Kp_Graphics(Abstract.Graphic):
        """
        Класс запуска графического отображения
        """
        # Процесс Б(7.4)
        # Диаграмма качества входящей продукции
        def __init__(self, data, name='Коэффициент Кп', critery = 50):
            super().__init__(data)
            plt.style.use('seaborn-bright')
            self.data.plot.barh(color='black', linestyle='dashed', linewidth=2, alpha=0.7)
            plt.gcf().canvas.set_window_title('Уровень качества закупаемой продукции')
            plt.axvline(critery, color ='red', linestyle='dashed', label='Критерий оценки')
            plt.title(name, fontsize=16, y=1.05)
            plt.legend(fontsize=8, shadow=True, framealpha=1, facecolor=None, edgecolor='r', title='', loc='lower right')
            plt.grid(axis='both', color='black', linestyle='dotted',linewidth=1, alpha=0.5)

        def regres_graphic(self, name = r'Линейная регрессия значений Кп'):
            """
            Точечный график с линейной регрессией.
            object.regres_graphic(name), где name - название графика
            :name: str
            """
            fig, ax = plt.subplots()
            fig.canvas.set_window_title('График линейной регресии')
            x = self.data.index.tolist()
            x = np.array(x)
            y: pd.DataFrame = self.data.transpose().iloc[0]
            y = np.array(y)
            stats = linregress(x, y)
            m = stats.slope
            b = stats.intercept
            ax = plt.scatter(x,y,marker='D', label = self.data.columns[0])
            ax = plt.plot(x, b + m * x , color="red", label='Линия регрессии')
            plt.xlabel('Ось - X')
            plt.ylabel('Значение показателя')
            plt.title(name, fontsize=16, y=1.05)
            plt.legend(fontsize=8, shadow=True, framealpha=1, facecolor='w',    edgecolor='r', title='', loc='upper right')
            plt.grid(axis='both', color='black', linestyle='dotted',linewidth=1)

    class Km_Graphics(Abstract.Graphic):
        """
        Класс запуска графического отображения
        """
        # Процесс Б(7.4)
        # Диаграмма качества входящей продукции
        def __init__(self, data, name='Коэффициент Км', critery = 3):
            super().__init__(data)
            plt.style.use('seaborn-bright')
            self.data.plot.barh(color='black', linestyle='dashed', linewidth=2, alpha=0.7)
            plt.gcf().canvas.set_window_title('Уровень качества закупаемой продукции')
            plt.axvline(critery, color ='red', linestyle='dashed', label='Критерий оценки')
            plt.title(name, fontsize=16, y=1.05)
            plt.legend(fontsize=8, shadow=True, framealpha=1, facecolor=None, edgecolor='r', title='', loc='lower right')
            plt.grid(axis='both', color='black', linestyle='dotted',linewidth=1, alpha=0.5)

        def regres_graphic(self, name = r'Линейная регрессия значений Км'):
            """
            Точечный график с линейной регрессией.
            object.regres_graphic(name), где name - название графика
            :name: str
            """
            fig, ax = plt.subplots()
            fig.canvas.set_window_title('График линейной регресии')
            x = self.data.index.tolist()
            x = np.array(x)
            y: pd.DataFrame = self.data.transpose().iloc[0]
            y = np.array(y)
            stats = linregress(x, y)
            m = stats.slope
            b = stats.intercept
            ax = plt.scatter(x,y,marker='D',label=self.data.columns[0])
            ax = plt.plot(x, b + m * x , color="red", label='Линия регрессии')
            plt.xlabel('Ось - X')
            plt.ylabel('Значение показателя')
            plt.title(name, fontsize=16, y=1.05)
            plt.legend(fontsize=8, shadow=True, framealpha=1, facecolor='w',    edgecolor='r', title='', loc='upper right')
            plt.grid(axis='both', color='black', linestyle='dotted',linewidth=1)

except Exception:
    print(time.ctime(), 'Graphics_Error: ', sys.exc_info()[:2], file = open('log.txt', 'a'))

try:
    class Info_table(object):
        """
        Класс вывода таблицы на экран для выбора идентификатора
        (общие показатели)
        """
        def __init__(self):
            self.x = PrettyTable()
            field_names = ['Идентификатор', 'Наименование']
            self.x.add_column(field_names[1], MATTER_NAME)
            self.x.add_column(field_names[0], list(NAME_INPUT.keys()))

        def __repr__(self):
            return '{}'.format(self.x)

    class Info_add_table(object):
        """
        Класс вывода таблицы на экран для выбора идентификатора
        (отдельно по материалам)
        """
        def __init__(self):
            self.x = PrettyTable()
            field_names = ['Идентификатор', 'Наименование']
            self.x.add_column(field_names[1], MATTER_ADD_NAME)
            self.x.add_column(field_names[0], list(NAME_ADD_INPUT.keys()))

        def __repr__(self):
            return '{}'.format(self.x)

    class Info_corr_table(object):
        """
        Класс вывода таблицы на экран для выбора идентификатора
        (корреляция)
        """
        def __init__(self):
            self.x = PrettyTable()
            field_names = ['Идентификатор', 'Наименование']
            self.x.add_column(field_names[1], MATTER_NAME)
            self.x.add_column(field_names[0], list(NAME_CORR_INPUT.keys()))

        def __repr__(self):
            return '{}'.format(self.x)

except Exception:
    print(time.ctime(), 'Info_table_Error: ', sys.exc_info()[:2], file = open('log.txt', 'a'))

try:
    class Data_Table(object):
        """
        Класс отображения данных
        #################################
        Пример запуска:
        ---------------
        #x = Data_Table(data_km_mastic_year)
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
            print(tabulate(self.data, headers = 'keys', tablefmt = 'psql'), file=open(r'temp_data_control_production.txt', 'w', encoding = 'utf-8'))
            os.system('temp_data_control_production.txt')

except Exception:
    print(time.ctime(), 'Data_Table_Error: ', sys.exc_info()[:2], file = open('log.txt', 'a'))

try:
    class Statistic_Table(Abstract.Statistic):
        """
        Класс отображения статистических данных
        #######################################
        Пример запуска:
        ---------------
        x = Statistic_Table(data_km_mastic_year)
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
    print(time.ctime(), 'Statistic_Error: ', sys.exc_info()[:2], file = open('log.txt', 'a'))

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
            # ЗАПИСЬ ДАННЫХ В .xlsx файл
            print('Сохранение в файл формата *.xlsx ...')
            save_data_1 = data_1.corr()
            save_data_2 = data_2.corr()
            save_data_3 = data_3.corr()
            save_data_4 = data_4.corr()
            save_data_5 = data_5.corr()
            save_data_6 = data_6.corr()
            save_data_7 = data_7.corr()
            save_data_8 = data_8.corr()
            print('...files/record.xlsx')
            with pd.ExcelWriter(r'files/record.xlsx') as writer:
                save_data_1.to_excel(
                                    writer, sheet_name=save_data_1.columns[0]
                                    )
                save_data_2.to_excel(
                                    writer, sheet_name=save_data_2.columns[0]
                                    )
                save_data_3.to_excel(writer, sheet_name=save_data_3.columns[0])
                save_data_4.to_excel(writer, sheet_name=save_data_4.columns[0])
                save_data_5.to_excel(writer, sheet_name=save_data_5.columns[0])
                save_data_6.to_excel(writer, sheet_name=save_data_6.columns[0])
                save_data_7.to_excel(writer, sheet_name=save_data_7.columns[0])
                save_data_8.to_excel(writer, sheet_name=save_data_8.columns[0])
            # ЗАПИСЬ СТАТИСТИЧЕСКОЙ ИНФОРМАЦИИ в *.txt файл
            print('Сохранение в файл формата *.txt ...')
            print('...files/*.txt')
            for i_name in lst_name:
                x = Statistic_Table(i_name)
                print('{}\n{}\n{}\n{}\n{}'.format(x.score(),x.middle(),x.max(), x.min(),x.st_d()), file=open('files/{}.txt'.format(i_name.columns[0][0:16]), 'w'))

            # ЗАПИСЬ ИСХОДНЫХ ДАННЫХ в .xlsx файл
            print('Сохранение в файл формата *.xlsx ...')
            print('...files/origin.xlsx')
            with pd.ExcelWriter(r'files/origin.xlsx') as writer:
                lst_name[0].to_excel(
                                    writer, sheet_name=lst_name[0].columns[0]
                                    )
                lst_name[1].to_excel(
                                    writer, sheet_name=lst_name[1].columns[0]
                                    )
                lst_name[2].to_excel(writer, sheet_name=lst_name[2].columns[0])
                lst_name[3].to_excel(writer, sheet_name=lst_name[3].columns[0])
                lst_name[4].to_excel(writer, sheet_name=lst_name[4].columns[0])
                lst_name[5].to_excel(writer, sheet_name=lst_name[5].columns[0])
                lst_name[6].to_excel(writer, sheet_name=lst_name[6].columns[0])
                lst_name[7].to_excel(writer, sheet_name=lst_name[7].columns[0])
            # СОХРАНЕНИЕ ГРАФИКОВ
            print('Сохранение в файл формата *.png ...')
            print('...files/*.png')
            for i_name in lst_kp:
                name = i_name.columns[0]
                a = Kp_Graphics(i_name)
                a.save_graphic('files/Столбчатая диаграмма {}'.format(name))
                b = Kp_Graphics(i_name)
                b.regres_graphic()
                b.save_graphic('files/Линейная регрессия {}'.format(name))

            for i_name in lst_km:
                name = i_name.columns[0]
                a = Km_Graphics(i_name)
                a.save_graphic('files/Столбчатая диаграмма {}'.format(name))
                b = Km_Graphics(i_name)
                b.regres_graphic()
                b.save_graphic('files/Линейная регрессия {}'.format(name))

except Exception:
    print(time.ctime(), 'Save_Error: ', sys.exc_info()[:2], file = open('log.txt', 'a'))

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
            # ТАБЛИЦА ВЫБОРА ИСХОДНЫХ ДАННЫХ
            info = Info_table()
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
            # ТАБЛИЦА ВЫБОРА ИСХОДНЫХ ДАННЫХ
            info = Info_table()
            print(info)
            while True:
                try:
                    a = input("Укажите идентификатор|exit-выход: ")
                    if a =='exit':
                        break
                    reading = NAME_INPUT[a] # ВЫБОР НАИМЕНОВАНИЯ ЛЕНТЫ
                    df = reading
                    # СТАТИСТИКА
                    x = Statistic_Table(df)
                    print(x.score())
                    #Экземпляр значений количества проведенных испытаний и номеров партии
                    print(x.middle())
                    # Экземпляр средних значений
                    print(x.max_min())
                    # Экземпляр максимальных и минимальных значений
                    print(x.st_d())
                    # Экземпляр для вывода отклонений результатов испытаний
                except KeyboardInterrupt:
                    print('Выход...')
                    break
                except:
                    print("Неправильный идентификатор, попробуйте снова!!!")

    class ThreeCommand(BaseCommand):
        def label():
            return 'Графики-3'

        def perform(self, object, *args, **kwargs):
                for i_name in lst_kp:
                    a = Kp_Graphics(i_name)
                    a.regres_graphic()
                for i_name in lst_km:
                    a = Km_Graphics(i_name)
                    a.regres_graphic()
                plt.show()

    class FourCommand(BaseCommand):
        def label():
            return 'В файл-4'

        def perform(self, object, *args, **kwargs):
            # СОХРАНЕНИЕ РЕЗУЛЬТАТОВ
            Save_Data()

    class FiveCommand(BaseCommand):
        def label():
            return 'По материалам-5'

        def perform(self, object, *args, **kwargs):
            # ТАБЛИЦА ВЫБОРА ИСХОДНЫХ ДАННЫХ
            info_add = Info_add_table()
            print(info_add) #вывод в консоль исходных данных
            while True:
                try:
                    a = input("Укажите идентификатор|exit-выход: ")
                    if a =='exit':
                        break
                    reading = NAME_ADD_INPUT[a] # ВЫБОР НАИМЕНОВАНИЯ ЛЕНТЫ
                    df = reading
                    x = Data_Table(df)
                    x.open_data()

                except KeyboardInterrupt:
                    print('Выход...')
                    break
                except:
                    print("Неправильный идентификатор, попробуйте снова!!!")

    class SixCommand(BaseCommand):
        def label():
            return 'Корреляция-6'

        def perform(self, object, *args, **kwargs):
            # ТАБЛИЦА ВЫБОРА ИСХОДНЫХ ДАННЫХ
            info_corr = Info_corr_table()
            print(info_corr) #вывод в консоль исходных данных
            while True:
                try:
                    a = input("Укажите идентификатор|exit-выход: ")
                    if a =='exit':
                        break
                    reading = NAME_CORR_INPUT[a] # ВЫБОР НАИМЕНОВАНИЯ ЛЕНТЫ
                    df = reading
                    x = Data_Table(df.corr())
                    x.open_data()

                except KeyboardInterrupt:
                    print('Выход...')
                    break
                except:
                    print("Неправильный идентификатор, попробуйте снова!!!")

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
