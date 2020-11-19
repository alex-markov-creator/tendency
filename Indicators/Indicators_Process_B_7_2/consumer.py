#-*- coding: utf-8 -*-
# version 0.1a
# author: andrew.bezzubov - 16/11/2020 year
"""
===============================================================
consumer.py - модуль для статистических подсчетов и построения графиков  по показателям качества:
- Уровень удовлетворенности потребителей (Критерий>=75);
- Уровень привлечения новых потребителей (Критерий>=5) - соотношение кол-ва "новых" потребителей к общему числу потребителей предшествующего периода, %;
- Уровень повторных закупок, совершаемых новыми (закупившими продукцию в предшествующем отчётном периоде) потребителями в % (Критерий>=5) - соотношение кол-ва "новых" потребителей, повторно закупивших продукцию в отчётном периоде, к общему количеству новых потребителей в соответствующем периоде прошлого года в %.

ИСХОДНЫЕ ДАННЫЕ - ФАЙЛ __init__.py в ../Data::
+--------------------------------------+-----------------------------------+
|              Переменная              |             Показатель            |
+--------------------------------------+-----------------------------------+
|         data_ur_vip_zak_year         | Уровень выполнения заказов по ... |
|         data_ur_pov_zak_year         | Уровень повторных закупок по г... |
|      data_ur_priv_new_cons_year      | Уровень привлечения новых потр... |
|          data_ur_udovl_year          | Уровень удовлетворенности по г... |
|     data_ur_vip_zak_middle_year      | Уровень выполнения заказов по ... |
|     data_ur_pov_zak_middle_year      | Уровень повторных закупок по п... |
|  data_ur_priv_new_cons_middle_year   | Уровень привлечения новых потр... |
+--------------------------------------+-----------------------------------+
Инструкции при импорте:
-----------------------
import pandas as pd
import matplotlib.pyplot as plt
import consumer as cm

СПРАВКА
-------
print(cm.__doc__)

Вывод исходных данных в виде файла и таблицы
---------------------------------------------
x = cm.Data_Table(cm.data_koef_nov_pri_razr_year)
print(x)
x.open_data()

Данные статистических расчетов
--------------------------------
x = cm.Statistic_Table(cm.data_koef_nov_pri_razr_year)
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
b = cm.First_Graphics(cm.data_ur_udovl_year, name='Уровень удовлетворенности потребителей', critery = 75)
b.regres_graphic(name='Уровень удовлетворенности потребителей')
c = cm.Second_Graphics(cm.data_ur_udovl_year, name = 'Гистограмма распределения')
e = cm.Three_Graphics(cm.data_ur_priv_new_cons_year, name = 'Уровень привлечений новых потребителей по годам', critery=5)
e.regres_graphic(name='Уровень привлечений новых потребителей по годам')
g = cm.Three_Graphics(cm.data_ur_priv_new_cons_middle_year, name = 'Уровень привлечения новых потребителей по полугодиям', critery=5)
g.regres_graphic(name='Уровень привлечения новых потребителей по полугодиям')
i = cm.Three_Graphics(cm.data_ur_pov_zak_year, name = 'Уровень повторных закупок по годам', critery=5)
i.regres_graphic(name = 'Уровень повторных закупок по годам')
k = cm.Three_Graphics(cm.data_ur_pov_zak_middle_year, name = 'Уровень повторных закупок по полугодиям', critery=5)
k.regres_graphic(name = 'Уровень повторных закупок по полугодиям')
plt.show()

СОХРАНЕНИЕ графиков и результатов
---------------------------------
cm.Save_Data()
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
from Data import data_ur_vip_zak_year, data_ur_pov_zak_year,data_ur_priv_new_cons_year, data_ur_udovl_year, data_ur_vip_zak_middle_year, data_ur_pov_zak_middle_year, data_ur_priv_new_cons_middle_year
# импорт DataFrame объектов с исходными данными
from prettytable import PrettyTable
# импорт библиотеки для вывода табличных данных в консоли(терминале)
from abc import ABC, abstractmethod
# импорт модуля для абстрактных классов

# ИСХОДНЫЕ ДАННЫЕ (ДОПОЛНИТЕЛЬНОЕ ФОРМАТИРОВАНИЕ):
##################################################
try:
    INDICATOR_NAME = [
                "Уровень выполнения заказов по годам",
                "Уровень повторных закупок по годам",
                "Уровень привлечения новых потребителей по годам",
                "Уровень удовлетворенности по годам",
                "Уровень выполнения заказов по полугодиям",
                "Уровень повторных закупок по полугодиям",
                "Уровень привлечения новых потребителей по полугодиям",
                 ]#запись наименований

    NAME_INPUT = {
                    '001':data_ur_vip_zak_year,
                    '002':data_ur_pov_zak_year,
                    '003':data_ur_priv_new_cons_year,
                    '004':data_ur_udovl_year,
                    '005':data_ur_vip_zak_middle_year,
                    '006':data_ur_pov_zak_middle_year,
                    '007':data_ur_priv_new_cons_middle_year,
                    } #идентификатор

    lst_name = [data_ur_vip_zak_year, data_ur_pov_zak_year,data_ur_priv_new_cons_year, data_ur_udovl_year, data_ur_vip_zak_middle_year, data_ur_pov_zak_middle_year, data_ur_priv_new_cons_middle_year]

    # ИСХОДНЫЕ ДАННЫЕ (ДОПОЛНИТЕЛЬНОЕ ФОРМАТИРОВАНИЕ ДЛЯ СОХРАНЕНИЯ):
    #################################################################
    data_add = pd.concat([data_ur_vip_zak_year, data_ur_pov_zak_year,data_ur_priv_new_cons_year, data_ur_udovl_year, data_ur_vip_zak_middle_year, data_ur_pov_zak_middle_year, data_ur_priv_new_cons_middle_year], axis=1)
    # Конкатенация

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
        #x = Data_Table(data_ur_neispr_obor_year)
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
            print(tabulate(self.data, headers = 'keys', tablefmt = 'psql'), file=open(r'temp_data_consumer.txt', 'w', encoding = 'utf-8'))
            os.system('temp_data_consumer.txt')

except Exception:
    print(time.ctime(), 'Data_Table_Error: ', sys.exc_info()[:2], file = open('log.txt', 'a'))

try:
    class Statistic_Table(Abstract.Statistic):
        """
        Класс отображения статистических данных
        #######################################
        Пример запуска:
        ---------------
        x = Statistic_Table(data_ur_neispr_obor_year)
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
        Класс запуска графического отображения
        """
        # Процесс О(6.2)
        # Линейный график уровня удовлетворенности
        def __init__(self, data, name='Связь с потребителем', critery = 0):
            super().__init__(data)
            self.data.plot(color='blue', marker='o', linestyle='dashed', linewidth=2, alpha=0.5)
            plt.gcf().canvas.set_window_title('Связь с потребителем')
            plt.axhline(critery, color ='red', linestyle='dashed', label='Критерий оценки')
            plt.title(name, fontsize=16, y=1.05)
            plt.xlabel('Год')
            plt.legend(fontsize=8, shadow=True, framealpha=1, facecolor='y', edgecolor='r', title='', loc='center')
            plt.grid(axis='both', color='black', linestyle='dotted',linewidth=2, alpha=0.5)

    class Second_Graphics(Abstract.Graphic):
        """
        Класс запуска графического отображения
        """
        # Процесс О(6.2)
        # Гистограмма распределения показателя уровня удовлетворенности
        def __init__(self, data, name='Связь с потребителем'):
            super().__init__(data)
            fig, ax = plt.subplots()
            sns_plot = sb.distplot(self.data.transpose().iloc[0], label='Показатели')
            fig.canvas.set_window_title('Гистограмма распределения')
            fig = sns_plot.get_figure()
            plt.title(name, fontsize=16, y=1.05)
            plt.xlabel('Уровень удовлетворенности потребителей')
            plt.legend(fontsize=8, shadow=True, framealpha=1, facecolor='y', edgecolor='r', title='Частота распределения')
            plt.grid()

    class Three_Graphics(Abstract.Graphic):
        """
        Класс графического отображения
        """
        # Процесс О(6.2)
        # Линейный, заполненный график показателей:
        # - уровень привлечения новых потребителей;
        # - уровень повторных закупок.
        def __init__(self, data, name='Связь с потребителем', critery = 0):
            super().__init__(data)
            self.data.plot.area(color='blue', linestyle='dashed', linewidth=2, alpha=0.3)
            plt.gcf().canvas.set_window_title('Связь с потребителем')
            plt.axhline(critery, color ='red', linestyle='dashed', label='Критерий оценки')
            plt.title(name, fontsize=16, y=1.05)
            plt.xlabel('Год')
            plt.legend(fontsize=8, shadow=True, framealpha=1, facecolor='y', edgecolor='r', title='', loc='upper left')
            plt.grid(axis='both', color='black', linestyle='dotted',linewidth=2, alpha=0.5)

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
            save_data_1 = data_add
            print('...files/record.xlsx')
            with pd.ExcelWriter(r'files/record.xlsx') as writer:
                save_data_1.to_excel(
                                    writer, sheet_name='Исходные данные'
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
            a = First_Graphics(data_ur_udovl_year, name='Уровень удовлетворенности потребителей', critery = 75)
            a.save_graphic('files/Уровень удовлетворенности потребителей')
            b = First_Graphics(data_ur_udovl_year, name='Уровень удовлетворенности потребителей', critery = 75)
            b.regres_graphic(name='Уровень удовлетворенности потребителей')
            b.save_graphic('files/Линия регрессии уровня удовлетворенности')
            c = Second_Graphics(data_ur_udovl_year, name = 'Гистограмма распределения')
            c.save_graphic('files/Диаграмма распределения уровня удовлетворенности')
            d = Three_Graphics(data_ur_priv_new_cons_year, name = 'Уровень привлечений новых потребителей по годам', critery=5)
            d.save_graphic('files/Уровень привлечений новых потребителей по годам')
            e = Three_Graphics(data_ur_priv_new_cons_year, name = 'Уровень привлечений новых потребителей по годам', critery=5)
            e.regres_graphic(name = 'Уровень привлечений новых потребителей по годам')
            e.save_graphic('files/Линия регрессии уровня привлечений новых потребителей по годам')
            f = Three_Graphics(data_ur_priv_new_cons_middle_year, name = 'Уровень привлечения новых потребителей по полугодиям', critery=5)
            f.save_graphic('files/Уровень привлечений новых потребителей по полугодиям')
            g = Three_Graphics(data_ur_priv_new_cons_middle_year, name = 'Уровень привлечения новых потребителей по полугодиям', critery=5)
            g.regres_graphic(name = 'Уровень привлечения новых потребителей по полугодиям')
            g.save_graphic('files/Линия регресии уровня привлечений новых потребителей по полугодиям')
            h = Three_Graphics(data_ur_pov_zak_year, name = 'Уровень повторных закупок по годам', critery=5)
            h.save_graphic('files/Уровень повторных закупок по годам')
            i = Three_Graphics(data_ur_pov_zak_year, name = 'Уровень повторных закупок по годам', critery=5)
            i.regres_graphic(name = 'Уровень повторных закупок по годам')
            i.save_graphic('files/Линия регрессии уровня повторных закупок по годам')
            j = Three_Graphics(data_ur_pov_zak_middle_year, name = 'Уровень повторных закупок по полугодиям', critery=5)
            j.save_graphic('files/Уровень повторных закупок по полугодиям')
            k = Three_Graphics(data_ur_pov_zak_middle_year, name = 'Уровень повторных закупок по полугодиям', critery=5)
            k.regres_graphic(name = 'Уровень повторных закупок по полугодиям')
            k.save_graphic('files/Линия регрессии уровня повторных закупок по полугодиям')

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
            b = First_Graphics(data_ur_udovl_year, name='Уровень удовлетворенности потребителей', critery = 75)
            b.regres_graphic(name='Уровень удовлетворенности потребителей')
            c = Second_Graphics(data_ur_udovl_year, name = 'Гистограмма распределения')
            e = Three_Graphics(data_ur_priv_new_cons_year, name = 'Уровень привлечений новых потребителей по годам', critery=5)
            e.regres_graphic(name='Уровень привлечений новых потребителей по годам')
            g = Three_Graphics(data_ur_priv_new_cons_middle_year, name = 'Уровень привлечения новых потребителей по полугодиям', critery=5)
            g.regres_graphic(name='Уровень привлечения новых потребителей по полугодиям')
            i = Three_Graphics(data_ur_pov_zak_year, name = 'Уровень повторных закупок по годам', critery=5)
            i.regres_graphic(name = 'Уровень повторных закупок по годам')
            k = Three_Graphics(data_ur_pov_zak_middle_year, name = 'Уровень повторных закупок по полугодиям', critery=5)
            k.regres_graphic(name = 'Уровень повторных закупок по полугодиям')
            plt.show()

    class FourCommand(BaseCommand):
        def label():
            return 'В файл-4'

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