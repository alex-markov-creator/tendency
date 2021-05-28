# -*- coding: utf-8 -*-
# version 0.2a
# author: andrew.bezzubov - 13/05/2021
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
|       data_kol_real_prod_year        | Количество реализованной проду... |
|        data_kol_vip_prod_year        | Количество выпущенной продукци... |
|    data_kol_real_prod_middle_year    | Количество реализованной проду... |
|       data_kol_real_komp_year        | Количество реализованных компл... |
|      data_kol_vip_kompl_year         |Количество выпущенных комплектов...|
|    data_kol_real_komp_middle_year    | Количество реализованных компл... |
|       data_ob_vozr_prod_year         | Объем возвращенной продукции ...  |
|       data_ur_vip_zak_year           | Уровень выполнения заказов ...    |
|      data_ur_vip_zak_middle_year     | Уровень выполенния заказов ...    |
|        data_pret_i_rekl_year         | Претензии и рекламации от потр... |
|     data_pret_i_rekl_middle_year     | Претензии и рекламации от потр... |
|         data_ur_postav_year          |   Уровень поставок по годам...   |
|      data_ur_postav_middle_year      | Уровень поставок по полугодиям... |
+--------------------------------------+-----------------------------------+
# ИСХОДНЫЕ ДАННЫЕ (ПЕРЕМЕННЫЕ ШАБЛОНА process_b_7_5): (РЕДАКТИРОВАТЬ!!!)
+-------------------------------------------------------------------------+
|  Переменная    |                  Данные шаблона                        |
+-------------------------------------------------------------------------+
|   prev_year    |# переменные предыдущего и отчетного периода            |
|   next_year    |                                                        |
|                |# нумерация строк                                       |
+--------------------------------------+----------------------------------+
================================================================
ИСХОДНЫЕ ДАННЫЕ - ФАЙЛ __init__.py в ../Data:
---------------------------------------------

СПРАВКА (РЕДАКТИРОВАТЬ!!!)
Инструкции при импорте:
-----------------------
import pandas as pd
import matplotlib.pyplot as plt
import results as rs

Построение графиков:
--------------------
#график "Столбчатая диаграмма - Итоги"
graphic_one = rs.Visual_all(rs.sum_lenta, 'Реализованная и выпущенная продукции (лента) с 2010 года')
graphic_two = rs.Visual_all(rs.sum_kompl, 'Реализованная и выпущенная продукции (комплекты) с 2017 года')

( ДАЛЕЕ РЕДАКТИРОВАТЬ!!!)
g = rs.LinearGraphics(rs.sum_year)
#график "Линейный график по годам"
g.maximum_minimum_text()
#с выводом экстремумов функции
y = rs.LinearGraphics(rs.sum_year.loc[2010:])
y.maximum_minimum_text()
y.regres_graphic()
#график "Линейная регрессия по годам" с 2010 года
h = rs.LinearGraphics(rs.sum_middle_year)
h.maximum_minimum_text()
h.regres_graphic()
#график "Линейная регрессия по полугодиям" с 2010 года
e = rs.Visual_difference(rs.sum_year)
#график "Соотношение по годам"
k = rs.Visual_difference(rs.sum_middle_year)
#график "Соотношение по полугодиям"
l = rs.Visual_stock(rs.difference_year)
#график "Используемые запасы по годам"
l = rs.Visual_stock(rs.difference_middle_year)
#график "Используемые запасы по полугодиям"
plt.show()
#график на экран

Результаты подсчётов:
---------------------
b = rs.Result_Calc()
#вызов экземпляра для расчетов
save_data_1 = b.concat_data(
                            rs.data_kol_vip_prod_year, rs.data_kol_vip_prod_middle_year,
                            rs.data_kol_real_prod_year, rs.data_kol_real_prod_middle_year
                            )#исходные данные
save_data_2 = pd.concat(
                        [rs.difference_year, rs.difference_middle_year],
                        axis = 1
                        )#реализация-выпуск
save_data_3 = pd.concat(
                        [rs.difference_year.describe(), rs.difference_middle_year.describe()], axis = 1
                        )#cтатистика по разнице
save_data_4 = pd.concat(
                        [rs.data_kol_vip_prod_year.describe(), rs.data_kol_vip_prod_middle_year.describe(),
                        rs.data_kol_real_prod_year.describe(), rs.data_kol_real_prod_middle_year.describe()],
                        axis = 1
                        )#cтатистика по исходным данным
save_data_5 = rs.summer.corr()#результаты корреляции

lst = [save_data_1, save_data_2, save_data_3, save_data_4, save_data_5]
for i in lst:
    print(i)#вывод на экран
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
#-------------------------------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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

    logger.info("OK! Load Data") # logging

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
    # ИСХОДНЫЕ ДАННЫЕ (ДОПОЛНИТЕЛЬНОЕ ФОРМАТИРОВАНИЕ ДЛЯ ПОСТРОЕНИЯ ГРАФИКА VISUAL_ALL):
    #########################################################################
    data_kol_real_prod_year_edit = data_kol_real_prod_year.loc[2010:]
    data_kol_real_komp_year_edit = data_kol_real_komp_year.loc[2017:]
    concat_lenta = pd.concat([data_kol_vip_prod_year, data_kol_real_prod_year_edit],axis=1)
    sum_lenta = concat_lenta.sum()
    concat_kompl = pd.concat([data_kol_vip_kompl_year, data_kol_real_komp_year_edit],axis=1)
    sum_kompl = concat_kompl.sum()

    # ИСХОДНЫЕ ДАННЫЕ (ДОПОЛНИТЕЛЬНЫЕ РАСЧЁТЫ):
    ###########################################
    # Переменные: [sum_all,sum_year, sum_middle_year, summer,calc_year, calc_middle_year]
    a = Result_Calc()
    # экземпляр класса для объединения и подсчёта
    sum_all = a.result_all()
    # Общие результаты - итоги
    sum_year = a.result_year().iloc[:,:2]
    # Результаты по годам
    sum_middle_year = a.result_middle_year().iloc[:,:2]
    # Результаты по полугодиям
    summer = a.result_summer()
    # Сконкатенированные результаты для подсчёта коэфициента корреляции
    calc_year = sum_year.iloc[:,:3]
    # Разница по годам для построения столбчатой диаграммы
    calc_middle_year = sum_middle_year.iloc[:,:3]
    # Разница по полугодиям для построения столбчатой диаграммы
    difference_year = a.result_year().loc[2010:].iloc[:,2:3]
    # Результаты по годам
    difference_middle_year = a.result_middle_year().iloc[:,2:3]
    # Результаты по полугодиям

    logger.info("OK! Calculation Data") # logging
    logger.info('OK! end initial assignment ') # logging

except Exception:
    print(time.ctime(), 'Benchmark_Data_Error: ', sys.exc_info()[:2], file = open('log.txt', 'a'))

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


    class Result_Calc(Pattern_singleton.Singleton, Abstract.Calc):
        """
        Класс подсчета и конкатенации исходных данных
        """
        def __init__(self):
            pass

        def result_all(self)->pd.DataFrame:
            """
            Общее количество выпущенной и реализованной продукции
            :return: pd.DataFrame
            """
            data_kol_real_prod_year_edit = data_kol_real_prod_year.loc[2010:]
            sum_all = self.concat_data(data_kol_vip_prod_year, data_kol_real_prod_year_edit).sum()
            return sum_all

        def result_year(self)->pd.DataFrame:
            """
            - Кол-во реализованной продукции по годам;
            - Кол-во выпущенной продукции по годам.
            :return: pd.DataFrame
            """
            sum_year = self.concat_data(data_kol_vip_prod_year, data_kol_real_prod_year)
            sum_year['Разница в тоннах'] = sum_year[
                    'Кол-во реализованной продукции по годам в тоннах'
                                                    ] - sum_year[
                    'Количество выпущенной продукции по годам в тоннах'
                                                                ]
            return sum_year

        def result_middle_year(self)->pd.DataFrame:
            """
            - Кол-во реализованной продукции по полугодиям;
            - Кол-во выпущенной продукции по полугодиям.
            :return: pd.DataFrame
            """
            sum_middle_year = self.concat_data(data_kol_vip_prod_middle_year, data_kol_real_prod_middle_year)
            sum_middle_year['Разница в тоннах'] = sum_middle_year[
                    'Количество реализованной продукции по полугодиям в тоннах'
                                                        ] - sum_middle_year [
                    'Количество выпущенной продукции по полугодиям в тоннах'
                                                                            ]
            return sum_middle_year

        def result_summer(self)->pd.DataFrame:
            """
            Общая конкатенация для подсчёта коэффициента корреляции
            :return: pd.DataFrame
            """
            summer = self.concat_data(sum_year,sum_middle_year)
            return summer
try:
    @time_of_function
    class Visual_all(Abstract.Graphic):
        """
        График общих результатов выпуска и реализации в виде горизонтальной столбчатой диаграммы
        ========================================================================================
        # Пример отображения графика
        va = Visual_all(sum_all)
        plt.show()
        """
        def __init__(self, data: pd.Series, name = 'Реализованная и выпущенная продукции'):
            super().__init__(data)
            self.data = data
            self.logger = logging.getLogger('indicators.results.Visual_all')
            self.logger.info('__Init__ Visual_all')
            fig, ax = plt.subplots()
            fig.canvas.set_window_title('График сравнения')
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

    class LinearGraphics(Abstract.Graphic):
        """
        График общих результатов выпуска и реализации
        в виде линейного графика с визуализацией экстремумов функций графика
        ====================================================================
        Пример запуска:
        ---------------
        gr = LinearGraphics(sum_year)
        gr.maximum_minimum_text()
        plt.show()
        """
        def __init__(self,data):
            super().__init__(data)
            self.data = data
            self.data.plot()
            plt.title(r'Кол-во реализованной и выпущенной продукции', fontsize=16, y=1.05)
            plt.ylabel('Кол-во в тоннах')
            plt.xlabel('Год')
            plt.legend(fontsize=7, shadow=True, framealpha=1, facecolor='w', edgecolor='r', title='', loc = 'best')
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

    class Visual_difference(Abstract.Graphic):
        """
        Класс графического отображения соотношения реализации и выпуска
        ===============================================================
        Пример запуска:
        ---------------
        vd = Visual_difference(calc_year)
        plt.show()
        """
        def __init__(self, data):
            super().__init__(data)
            self.data = data
            self.data.plot(kind='barh')
            plt.title(r'Реализация и выпуск', fontsize=12, y=1.05)
            plt.legend(fontsize=8, shadow=True, framealpha=0.5, facecolor='w', edgecolor='r',loc='best')
            plt.grid()

    class Visual_stock(Abstract.Graphic):
        """
        Класс графического отображения разницы реализации и выпуска
        ===========================================================
        Пример запуска:
        ---------------
        vs = Visual_stock(difference_year)
        plt.show()
        """
        def __init__(self,data):
            super().__init__(data)
            self.data = data
            self.data.plot(kind='bar', stacked=True, alpha = 0.5)
            plt.title(r'Используемые запасы и перевыпуск продукции', fontsize=12, y=1.05)
            plt.legend(fontsize=8, shadow=True, framealpha=1, facecolor='y', edgecolor='r',loc='best')
            plt.grid()

    class AllStatistics(Abstract.Statistic):
        """
        Класс статистических данных
        ===========================
        """
        def __init__(self,data):
            super().__init__(data)
            pass

except Exception:
    print(time.ctime(), 'Tools_Error: ', sys.exc_info()[:2], file = open('log.txt', 'a'))



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
                    SixCommand.label(): SixCommand,
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

    class SecondCommand(BaseCommand):
        def label():
            return 'Статистика-2'

        def perform(self, object, *args, **kwargs):
            """
            СТАТИСТИКА
            """
            try:
                for df in data_kol_vip_prod_year, data_kol_vip_prod_middle_year,data_kol_real_prod_year, data_kol_real_prod_middle_year:
                        print(df)
                b,c,d,e = AllStatistics(data_kol_vip_prod_year), AllStatistics(data_kol_real_prod_year), AllStatistics(data_kol_vip_prod_middle_year), AllStatistics(data_kol_real_prod_middle_year)
                previews  = [b.preview_statistic(), c.preview_statistic(),d.preview_statistic(), e.preview_statistic()] # объекты
                for preview in previews:
                        print(preview) # функция

            except Exception:
                print( time.ctime(), 'SecondCommand_Error: ', sys.exc_info()[:2], file = open('log.txt', 'a'))

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

                #g = LinearGraphics(sum_year)
                #g.maximum_minimum_text()
                #y = LinearGraphics(sum_year.loc[2010:])
                #y.maximum_minimum_text()
                #y.regres_graphic()
                #h = LinearGraphics(sum_middle_year)
                #h.maximum_minimum_text()
                #h.regres_graphic()
                #e = Visual_difference(sum_year)
                #k = Visual_difference(sum_middle_year)
                #l = Visual_stock(difference_year)
                #l = Visual_stock(difference_middle_year)
                plt.show()

            except Exception:
                logger.error("FAILED! ThreeCommand_Error: %s", traceback.format_exc()) # logging

    class FourCommand(BaseCommand):
        def label():
            return 'Корреляция-4'

        def perform(self, object, *args, **kwargs):
            """
            КОРРЕЛЯЦИЯ
            """
            try:
                corr_summer = AllStatistics(summer)
                cr = corr_summer.preview_corr()
                print(cr)

            except Exception:
                print( time.ctime(), 'FourCommand_Error: ', sys.exc_info()[:2], file = open('log.txt', 'a'))


    class FiveCommand(BaseCommand):
        def label():
            return 'Сохранить результаты в файл-5'

        def perform(self, object, *args, **kwargs):
            """
            СОХРАНЕНИЕ В ФАЙЛ
            """
            try:
                ### ИСХОДНЫЕ ДАННЫЕ ##########################################
                """
                b = Result_Calc()
                save_data_1 = b.concat_data(
                                            data_kol_vip_prod_year, data_kol_vip_prod_middle_year,
                                            data_kol_real_prod_year, data_kol_real_prod_middle_year
                                            )
                ### ЗАПАСЫ ###################################################
                save_data_2 = pd.concat(
                                        [difference_year,difference_middle_year], axis = 1
                                        )
                save_data_3 = pd.concat(
                                        [difference_year.describe(),difference_middle_year.describe()], axis = 1
                                        )
                ### СТАТИСТИКА ###############################################
                save_data_4 = pd.concat(
                                        [data_kol_vip_prod_year.describe(), data_kol_vip_prod_middle_year.describe(),
                                        data_kol_real_prod_year.describe(), data_kol_real_prod_middle_year.describe()],
                                        axis = 1
                                        )
                """
                # ГРАФИКИ
                print('Сохранение в файл формата *.png ...')
                print('...files/*.png')
                if data_kol_real_prod_year.isin([0]).all(axis=None) == False and data_kol_vip_prod_year.isin([0]).all(axis=None) == False:
                    graphic_one = Visual_all(sum_lenta, 'Реализованная и выпущенная продукции (лента) с 2010 года')
                    graphic_one.save_graphic(r'files/001')
                else:
                    pass
                if data_kol_real_komp_year.isin([0]).all(axis=None) == False and data_kol_vip_kompl_year.isin([0]).all(axis=None) == False:
                    graphic_two = Visual_all(sum_kompl, 'Реализованная и выпущенная продукции (комплекты) с 2017 года')
                    graphic_two.save_graphic(r'files/002')
                else:
                    pass

                """
                g = LinearGraphics(sum_year)
                g.maximum_minimum_text()
                g.save_graphic(r'files/Линейный график по годам')
                y = LinearGraphics(sum_year.loc[2010:])
                y.maximum_minimum_text()
                y.regres_graphic()
                y.save_graphic(r'files/Линейная регрессия по годам')
                h = LinearGraphics(sum_middle_year)
                h.maximum_minimum_text()
                h.save_graphic(r'files/Линейный график по полугодиям')
                o = LinearGraphics(sum_middle_year)
                o.regres_graphic()
                o.save_graphic(r'files/Линейная регрессия по полугодиям')
                e = Visual_difference(sum_year)
                e.save_graphic(r'files/Соотношение по годам')
                k = Visual_difference(sum_middle_year)
                k.save_graphic(r'files/Соотношение за полугодие')
                l = Visual_stock(difference_year)
                l.save_graphic(r'files/Используемые запасы по годам')
                m = Visual_stock(difference_middle_year)
                m.save_graphic(r'files/Используемые запасы по полугодиям')
                # РЕЗУЛЬТАТЫ КОРРЕЛЯЦИИ
                save_data_5 = summer.corr()
                # ЗАПИСЬ ДАННЫХ В .xlsx файл
                print('Сохранение в файл формата *.xlsx ...')
                print('...files/record.xlsx')
                with pd.ExcelWriter(r'files/record.xlsx') as writer:
                    save_data_1.to_excel(
                                        writer, sheet_name='Исходные данные'
                                        )
                    save_data_2.to_excel(
                                        writer, sheet_name='Реализация-выпуск'
                                        )
                    save_data_3.to_excel(writer, sheet_name='Статистика по разнице')
                    save_data_4.to_excel(writer, sheet_name='Статистика по исходным данным')
                    save_data_5.to_excel(writer, sheet_name='Результаты корреляции')
                """
            except Exception:
                logger.error("FAILED! FiveCommand_Error: %s", traceback.format_exc()) # logging

    class SixCommand(BaseCommand):
        def label():
            """
            Название комманды
            """
            return 'Комманда-6'

        def perform(self, object, *args, **kwargs):
            """
            ЗАПАСЫ
            """
            try:
                st_year = AllStatistics(difference_year)
                st_middle_year = AllStatistics(difference_middle_year)
                previews  = [st_year.preview_data(), st_middle_year.preview_data()] # объекты
                stats  = [st_year.preview_statistic(), st_middle_year.preview_statistic()] # объекты
                for preview,stat in previews,stats:
                    print(preview) # функция
                    print(stat)

            except Exception:
                print( time.ctime(), 'SixCommand_Error: ', sys.exc_info()[:2], file = open('log.txt', 'a'))

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

    except:
        print(time.ctime(), 'Run_Error: ', sys.exc_info()[:2], file = open('log.txt', 'a'))
