# -*- coding: utf-8 -*-
# version 0.1a
# author: andrew.bezzubov - 23/09/2020 year
"""
================================================================
results.py - Модуль аналитики по следующим показателям качества:
- Кол-во реализованной продукции;
- Кол-во выпущенной продукции.
Для сравнительного анализа и определения используемых запасов.
Возможны другие цели.
================================================================
ИСХОДНЫЕ ДАННЫЕ - ФАЙЛ __init__.py в ../Data:
---------------------------------------------
import Data;print(Data.__doc__)
#таблица переменных

info_variable = {
        "data_kol_vip_prod_year":
        "Количество выпущенной продукции по годам",
        "data_kol_vip_prod_middle_year":
        "Количество выпущенной продукции по полугодиям",
        "data_kol_real_prod_year":
        "Количество реализованной продукции по годам",
        "data_kol_real_prod_middle_year":
        "Количество реализованной продукции по полугодиям"
        }

Инструкции при импорте:
-----------------------
import pandas as pd
import matplotlib.pyplot as plt
import results as rs

Построение графиков:
--------------------
f = rs.Visual_all(rs.sum_all)
#график "Столбчатая диаграмма - Итоги"
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
import time
sys.path.append(os.path.realpath('../..'))
# субродительский каталог в sys.path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import Tools.Abstract_Parents as Abstract
# универсальный модуль для выполнения контракта
import Tools.Singleton_Pattern as Pattern_singleton
# универсальный модуль для создания уникального экземпляра класса, реализация паттерна "Одиночка"

from Data import data_kol_vip_prod_year, data_kol_vip_prod_middle_year, data_kol_real_prod_year, data_kol_real_prod_middle_year
# импорт DataFrame объектов с исходными данными

try:
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

    class Visual_all(Abstract.Graphic):
        """
        График общих результатов выпуска и реализации в виде горизонтальной столбчатой диаграммы
        ========================================================================================
        # Пример отображения графика
        va = Visual_all(sum_all)
        plt.show()
        """
        def __init__(self, data: pd.DataFrame):
            super().__init__(data)
            self.data = data
            fig, ax = plt.subplots()
            fig.canvas.set_window_title('График сравнения')
            obj = ('Реализовано', 'Выпущено')
            y_pos = np.arange(len(obj))
            performance = [
                        data.loc['Кол-во реализованной продукции по годам в тоннах'],
                        data.loc['Количество выпущенной продукции по годам в тоннах']]
            plt.barh(y_pos, performance, align='center', alpha = 0.5, label = 'Кол-во в тоннах')
            plt.yticks(y_pos,[])
            plt.ylabel(obj)
            plt.title(r'Реализованная и выпущенная продукции', fontsize=12, y=1.05)
            plt.legend(fontsize=8, shadow=True, framealpha=1, facecolor='w', edgecolor='r', loc='center')
            plt.text(
                    data.loc['Кол-во реализованной продукции по годам в тоннах']/2, 0,
                    round(data.loc['Кол-во реализованной продукции по годам в тоннах'],3),
                    fontsize=14, horizontalalignment='center', verticalalignment='center',
                    bbox=dict(facecolor='pink', alpha=1.0))
            plt.text(
                    data.loc['Количество выпущенной продукции по годам в тоннах']/2, 1,
                    round(data.loc['Количество выпущенной продукции по годам в тоннах'],3),
                    fontsize=14, horizontalalignment='center', verticalalignment='center',
                    bbox=dict(facecolor='pink', alpha=1.0))
            plt.grid()

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

# ИСХОДНЫЕ ДАННЫЕ (ДОПОЛНИТЕЛЬНЫЕ РАСЧЁТЫ):
###########################################
try:
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

except Exception:
    print(time.ctime(), 'Benchmark_Data_Error: ', sys.exc_info()[:2], file = open('log.txt', 'a'))

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
            return 'Запасы-1'

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
                print( time.ctime(), 'FirstCommand_Error: ', sys.exc_info()[:2], file = open('log.txt', 'a'))

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
                f = Visual_all(sum_all)
                g = LinearGraphics(sum_year)
                g.maximum_minimum_text()
                y = LinearGraphics(sum_year.loc[2010:])
                y.maximum_minimum_text()
                y.regres_graphic()
                h = LinearGraphics(sum_middle_year)
                h.maximum_minimum_text()
                h.regres_graphic()
                e = Visual_difference(sum_year)
                k = Visual_difference(sum_middle_year)
                l = Visual_stock(difference_year)
                l = Visual_stock(difference_middle_year)
                plt.show()

            except Exception:
                print( time.ctime(), 'ThreeCommand_Error: ', sys.exc_info()[:2], file = open('log.txt', 'a'))

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
                # ГРАФИКИ
                print('Сохранение в файл формата *.png ...')
                print('...files/*.png')
                f = Visual_all(sum_all)
                f.save_graphic(r'files/Столбчатая диаграмма - Итоги')
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

            except Exception:
                print( time.ctime(), 'FiveCommand_Error: ', sys.exc_info()[:2], file = open('log.txt', 'a'))

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
