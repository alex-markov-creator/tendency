#-*- coding: utf-8 -*-
# version 0.1a
# author: andrew.bezzubov - 10/11/2020 year
"""
===============================================================
people.py - модуль для статистических расчетов и построения графиков по показателям качества:
- Уровень укомплектованности кадрами (Критерий >= 90) - отношение фактической численности на конец отчётного периода к численности согласно штатному расписанию, %;
- Уровень текучести кадров (Критерий <= 20) - отношение числа работников, уволившихся по причинам, относимым к текучести (по собственному желанию, за нарушение трудовой дисциплины) к списочной численности в %;
- Уровень пропуска рабочих дней (Критерий <= 7) - отношение количества пропущенных человеко-дней к количеству планируемых человеко-дней.
ИСХОДНЫЕ ДАННЫЕ - ФАЙЛ __init__.py в ../Data:
+--------------------------------------+-----------------------------------+
|              Переменная              |             Показатель            |
+--------------------------------------+-----------------------------------+
|       data_ur_prop_rab_dn_year       | Уровень пропуска рабочих дней ... |
|         data_ur_tek_kad_year         | Уровень текучести кадров по го... |
|        data_ur_ukomp_kad_year        | Уровень укомплектованности кад... |
|   data_ur_prop_rab_dnmiddle__year    | Уровень пропуска рабочих дней ... |
|     data_ur_tek_kad_middle_year      | Уровень текучести кадров за по... |
|    data_ur_ukomp_kad_middle_year     | Уровень укомплектованности кад... |
+--------------------------------------+-----------------------------------+
Инструкции при импорте:
-----------------------
import pandas as pd
import matplotlib.pyplot as plt
import people as ppl

СПРАВКА
-------
print(ppl.__doc__)

Вывод исходных данных в виде файла и таблицы
---------------------------------------------
x = ppl.Data_Table(ppl.data_ur_prop_rab_dn_year)
print(x)
x.open_data()

Данные статистических расчетов
--------------------------------
x = ppl.Statistic_Table(ppl.data_ur_prop_rab_dn_year)
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
a = ppl.First_Graphics(ppl.data_ur_ukomp_kad_year, name= 'Уровень укомплектованности кадрами по годам', critery=90)
b = ppl.First_Graphics(ppl.data_ur_ukomp_kad_middle_year, name= 'Уровень укомплектованности кадрами по полугодиям', critery=90)
c = ppl.First_Graphics(ppl.data_ur_tek_kad_year, name= 'Уровень текучести кадров по годам', critery=20)
d = ppl.First_Graphics(ppl.data_ur_tek_kad_middle_year, name= 'Уровень текучести кадров по полугодиям', critery=20)
e = ppl.First_Graphics(ppl.data_ur_prop_rab_dn_year, name= 'Уровень пропуска рабочих дней по годам', critery=7)
f = ppl.First_Graphics(ppl.data_ur_prop_rab_dnmiddle__year, name= 'Уровень пропуска рабочих дней по полугодиям', critery=7)
plt.show()

СОХРАНЕНИЕ графиков и результатов
---------------------------------
ppl.Save_Data()
"""
import sys
import os
import time
sys.path.append(os.path.realpath('../..'))
# субродительский каталог в sys.path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from tabulate import tabulate
# модуль для вывода табличных данных
import Tools.Abstract_Parents as Abstract
# универсальный модуль для выполнения контракта
from scipy.stats import linregress
# модуль для построения линейной регрессии
from Data import data_ur_prop_rab_dn_year, data_ur_tek_kad_year, data_ur_ukomp_kad_year, data_ur_prop_rab_dnmiddle__year,data_ur_tek_kad_middle_year, data_ur_ukomp_kad_middle_year
# импорт DataFrame объектов с исходными данными
from prettytable import PrettyTable
# импорт библиотеки для вывода табличных данных в консоли(терминале)
from abc import ABC, abstractmethod
# импорт модуля для абстрактных классов

# ИСХОДНЫЕ ДАННЫЕ (ДОПОЛНИТЕЛЬНОЕ ФОРМАТИРОВАНИЕ):
##################################################
try:
    INDICATOR_NAME = [
                "Уровень пропуска рабочих дней по годам",
                "Уровень текучести кадров по годам",
                "Уровень укомплектованности кадров по годам",
                "Уровень пропуска рабочих дней за полугодия",
                "Уровень текучести кадров за полугодия",
                "Уровень укомплектованности кадров за полугодия"
                 ]#запись наименований

    NAME_INPUT = {
                    '001':data_ur_prop_rab_dn_year,
                    '002':data_ur_tek_kad_year,
                    '003':data_ur_ukomp_kad_year,
                    '004':data_ur_prop_rab_dnmiddle__year,
                    '005':data_ur_tek_kad_middle_year,
                    '006':data_ur_ukomp_kad_middle_year,
                    } #идентификатор

    lst_name = [data_ur_prop_rab_dn_year, data_ur_tek_kad_year, data_ur_ukomp_kad_year, data_ur_prop_rab_dnmiddle__year,data_ur_tek_kad_middle_year, data_ur_ukomp_kad_middle_year]

    # ИСХОДНЫЕ ДАННЫЕ (ДОПОЛНИТЕЛЬНОЕ ФОРМАТИРОВАНИЕ ДЛЯ КОРРЕЛЯЦИИ):
    #################################################################
    data_corr = pd.concat([data_ur_prop_rab_dn_year, data_ur_tek_kad_year, data_ur_ukomp_kad_year, data_ur_prop_rab_dnmiddle__year,data_ur_tek_kad_middle_year, data_ur_ukomp_kad_middle_year], axis=1)
    # Конкатенация Км по мастике за год

except Exception:
    print(time.ctime(), 'Benchmark_Data_Error: ', sys.exc_info()[:2], file = open('log.txt', 'a'))

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
    print(time.ctime(), 'Info_Error: ', sys.exc_info()[:2], file = open('log.txt', 'a'))

try:
    class Data_Table(object):
        """
        Класс отображения данных
        #################################
        Пример запуска:
        ---------------
        #x = Data_Table(data_ur_ukomp_kad_year)
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
            print(tabulate(self.data, headers = 'keys', tablefmt = 'psql'), file=open(r'temp_data_people.txt', 'w', encoding = 'utf-8'))
            os.system('temp_data_people.txt')

except Exception:
    print(time.ctime(), 'Data_Table_Error: ', sys.exc_info()[:2], file = open('log.txt', 'a'))

try:
    class Statistic_Table(Abstract.Statistic):
        """
        Класс отображения статистических данных
        #######################################
        Пример запуска:
        ---------------
        x = Statistic_Table(data_ur_ukomp_kad_year)
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
    class First_Graphics(Abstract.Graphic):
        """
        Класс построения столбчатой диаграммы с критерием и линией регресии
        Процесс О (6.2)
        ---------
        """
        def __init__(self, data, name='Название графика', critery = 0):
            """
            Оформление графика
            """
            super().__init__(data)
            fig, ax = plt.subplots()
            fig.canvas.set_window_title('Человеческие ресурсы')
            x = self.data.index.tolist()
            x = np.array(x)
            y = self.data.transpose().iloc[0]
            y = np.array(y)
            stats = linregress(x, y)
            m = stats.slope
            b = stats.intercept
            ax = plt.plot(x, b + m * x , color="blue", label='Линейная регрессия')  # I've added a color argument here
            ax = plt.bar(x,y,color='blue', linestyle='dashed', linewidth=2, alpha=0.5, label = 'Значение показателя')
            ax = plt.axhline(critery, color ='red', linestyle='dashed', label='Критерий оценки')
            plt.title(name, fontsize=16, y=1.05)
            plt.xlabel('Год')
            plt.legend(fontsize=8, shadow=True, framealpha=1, facecolor='y', edgecolor='r', title='', loc='lower left')
            plt.grid(axis='both', color='orange', linestyle='dotted',linewidth=1.5)

except Exception:
    print(time.ctime(), 'Graphics_Error: ', sys.exc_info()[:2], file = open('log.txt', 'a'))

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
            save_data_1 = data_corr
            save_data_2 = data_corr.corr()
            print('...files/record.xlsx')
            with pd.ExcelWriter(r'files/record.xlsx') as writer:
                save_data_1.to_excel(
                                    writer, sheet_name='Исходные данные'
                                    )
                save_data_2.to_excel(
                                    writer, sheet_name="Результаты корреляции"
                                    )
            # ЗАПИСЬ СТАТИСТИЧЕСКОЙ ИНФОРМАЦИИ в *.txt файл
            print('Сохранение в файл формата *.txt ...')
            print('...files/*.txt')
            for i_name in lst_name:
                x = Statistic_Table(i_name)
                print('{}\n{}\n{}\n{}\n{}'.format(x.score(),x.middle(),x.max(), x.min(),x.st_d()), file=open('files/{}.txt'.format(i_name.columns[0]), 'w'))
            # СОХРАНЕНИЕ ГРАФИКОВ
            print('Сохранение в файл формата *.png ...')
            print('...files/*.png')
            a = First_Graphics(data_ur_ukomp_kad_year, name= 'Уровень укомплектованности кадрами по годам', critery=90)
            a.save_graphic('files/{}'.format(data_ur_ukomp_kad_year.columns[0]))
            b = First_Graphics(data_ur_ukomp_kad_middle_year, name= 'Уровень укомплектованности кадрами по полугодиям', critery=90)
            b.save_graphic('files/{}'.format(data_ur_ukomp_kad_middle_year.columns[0]))
            c = First_Graphics(data_ur_tek_kad_year, name= 'Уровень текучести кадров по годам', critery=20)
            c.save_graphic('files/{}'.format(data_ur_tek_kad_year.columns[0]))
            d = First_Graphics(data_ur_tek_kad_middle_year, name= 'Уровень текучести кадров по полугодиям', critery=20)
            d.save_graphic('files/{}'.format(data_ur_tek_kad_middle_year.columns[0]))
            e = First_Graphics(data_ur_prop_rab_dn_year, name= 'Уровень пропуска рабочих дней по годам', critery=7)
            e.save_graphic('files/{}'.format(data_ur_prop_rab_dn_year.columns[0]))
            f = First_Graphics(data_ur_prop_rab_dnmiddle__year, name= 'Уровень пропуска рабочих дней по полугодиям', critery=7)
            f.save_graphic('files/{}'.format(data_ur_prop_rab_dnmiddle__year.columns[0]))

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
            #ГРАФИКИ
            a = First_Graphics(data_ur_ukomp_kad_year, name= 'Уровень укомплектованности кадрами по годам', critery=90)
            b = First_Graphics(data_ur_ukomp_kad_middle_year, name= 'Уровень укомплектованности кадрами по полугодиям', critery=90)
            c = First_Graphics(data_ur_tek_kad_year, name= 'Уровень текучести кадров по годам', critery=20)
            d = First_Graphics(data_ur_tek_kad_middle_year, name= 'Уровень текучести кадров по полугодиям', critery=20)
            e = First_Graphics(data_ur_prop_rab_dn_year, name= 'Уровень пропуска рабочих дней по годам', critery=7)
            f = First_Graphics(data_ur_prop_rab_dnmiddle__year, name= 'Уровень пропуска рабочих дней по полугодиям', critery=7)
            plt.show()


    class FourCommand(BaseCommand):
        def label():
            return 'В файл-4'

        def perform(self, object, *args, **kwargs):
            #СОХРАНЕНИЕ
            Save_Data()


    class FiveCommand(BaseCommand):
        def label():
            return 'Корреляция-5'

        def perform(self, object, *args, **kwargs):
            # КОРРЕЛЯЦИЯ
            x = Data_Table(data_corr.corr())
            x.open_data()


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