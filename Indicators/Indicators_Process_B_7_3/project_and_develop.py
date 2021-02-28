#-*- coding: utf-8 -*-
# version 0.1a
# author: andrew.bezzubov - 12/11/2020 year
"""
===============================================================
project_and_develop.py - модуль для статистических подсчетов и построения графиков  по показателям качества:
- Коэфициент новизы при разработке изоляционных материалов, Кн (Критерий>=1) -
Изменяемые элементы при изготовлении лент:
    - лента-основа - 0,5;
    - антиадгезив - 0,5;
    - мастика - 1;
    - добавленный новый элемент - 1;
    - разработка нового ТУ -1.
- Коэффициент внедрения КД (чертежи), Квн (Критерий>=70) - отношение количества изделий, внедренных в производство, к общему числу разработанных изделий, %;
- Показатель качества разработанной ТД (ТУ, ПМИ), Ктд (Критерий<=20) - отношение количества листов документации с внесенными по замечаниям в результате экспертизы (внутренней и внешней) изменениями к общему числу листов, %.

ИСХОДНЫЕ ДАННЫЕ - ФАЙЛ __init__.py в ../Data::
+--------------------------------------+-----------------------------------+
|              Переменная              |             Показатель            |
+--------------------------------------+-----------------------------------+
|     data_koef_nov_pri_razr_year      |           Кн по годам...          |
|    data_koef_vned_konst_dok_year     | Квн конструкторской документац... |
|      data_pok_kach_razr_td_year      |          Ктд по годам...          |
|  data_koef_nov_pri_razr_middle_year  |        Кн по полугодиям...        |
| data_koef_vned_konst_dok_middle_year | Квн конструкторской документац... |
|  data_pok_kach_razr_td_middle_year   |        Ктд по полугодиям...       |
+--------------------------------------+-----------------------------------+
Инструкции при импорте:
-----------------------
import pandas as pd
import matplotlib.pyplot as plt
import project_and_develop as pad

СПРАВКА
-------
print(pad.__doc__)

Вывод исходных данных в виде файла и таблицы
---------------------------------------------
x = pad.Data_Table(pad.data_koef_nov_pri_razr_year)
print(x)
x.open_data()

Данные статистических расчетов
--------------------------------
x = pad.Statistic_Table(pad.data_koef_nov_pri_razr_year)
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
a = pad.First_Graphics(pad.data_koef_nov_pri_razr_year, name= 'Коэфициент новизы при разработке изоляционных материалов по годам', critery=1)
b = pad.First_Graphics(pad.data_koef_nov_pri_razr_middle_year, name= 'Коэфициент новизы при разработке изоляционных материалов по полугодиям', critery=1)
c = pad.First_Graphics(pad.data_koef_vned_konst_dok_year, name= 'Коэффициент внедрения КД (чертежи) по годам', critery=70)
d = pad.First_Graphics(pad.data_koef_vned_konst_dok_middle_year, name= 'Коэффициент внедрения КД (чертежи) по полугодиям', critery=70)
e = pad.First_Graphics(pad.data_pok_kach_razr_td_year, name= 'Показатель качества разработанной ТД (ТУ, ПМИ) по годам', critery=20)
f = pad.First_Graphics(pad.data_pok_kach_razr_td_middle_year, name= 'Показатель качества разработанной ТД (ТУ, ПМИ) по полугодиям', critery=20)
plt.show()

СОХРАНЕНИЕ графиков и результатов
---------------------------------
pad.Save_Data()
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
# модуль для логирования(журналирования)
import logging
# модуль для вывода табличных данных
import Tools.Abstract_Parents as Abstract
# универсальный модуль для выполнения контракта
from scipy.stats import linregress
# модуль для построения линейной регрессии
from Data import data_koef_nov_pri_razr_year, data_koef_vned_konst_dok_year,data_pok_kach_razr_td_year, data_koef_nov_pri_razr_middle_year,data_koef_vned_konst_dok_middle_year, data_pok_kach_razr_td_middle_year
# импорт DataFrame объектов с исходными данными
from prettytable import PrettyTable
# импорт библиотеки для вывода табличных данных в консоли(терминале)
from abc import ABC, abstractmethod
# импорт модуля для абстрактных классов
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('indicators.project_and_develop') # возвращает объект логгера
# ИСХОДНЫЕ ДАННЫЕ (ДОПОЛНИТЕЛЬНОЕ ФОРМАТИРОВАНИЕ):
##################################################
try:
    logger.debug("start initial assignment") # logging
    INDICATOR_NAME = [
                'Кн по годам',
                'Квн конструкторской документации',
                'Ктд по годам',
                'Кн по полугодиям',
                'Квн конструкторской документации по полугодиям',
                'Ктд по полугодиям'
                 ]#запись наименований

    NAME_INPUT = {
                    '001':data_koef_nov_pri_razr_year,
                    '002':data_koef_vned_konst_dok_year,
                    '003':data_pok_kach_razr_td_year,
                    '004':data_koef_nov_pri_razr_middle_year,
                    '005':data_koef_vned_konst_dok_middle_year,
                    '006':data_pok_kach_razr_td_middle_year,
                    } #идентификатор

    lst_name = [data_koef_nov_pri_razr_year, data_koef_vned_konst_dok_year,data_pok_kach_razr_td_year, data_koef_nov_pri_razr_middle_year,data_koef_vned_konst_dok_middle_year, data_pok_kach_razr_td_middle_year]

    # ИСХОДНЫЕ ДАННЫЕ (ДОПОЛНИТЕЛЬНОЕ ФОРМАТИРОВАНИЕ ДЛЯ СОХРАНЕНИЯ):
    #################################################################
    data_add = pd.concat([data_koef_nov_pri_razr_year, data_koef_vned_konst_dok_year,data_pok_kach_razr_td_year, data_koef_nov_pri_razr_middle_year,data_koef_vned_konst_dok_middle_year, data_pok_kach_razr_td_middle_year], axis=1)
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
            print(tabulate(self.data, headers = 'keys', tablefmt = 'psql'), file=open(r'temp_data_project_and_develop.txt', 'w', encoding = 'utf-8'))
            os.system('temp_data_p_a_d.txt')

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
        # Процесс Б(7.3)
        # Показатели "Проектирование и разработка"
        def __init__(self, data, name='Название графика', critery = 0):
            super().__init__(data)
            plt.style.use('Solarize_Light2')
            fig, ax = plt.subplots()
            fig.canvas.set_window_title('Проектирование и разработка')
            x = self.data.index.tolist()
            x = np.array(x)
            y = self.data.transpose().iloc[0]
            y = np.array(y)
            stats = linregress(x, y)
            m = stats.slope
            b = stats.intercept
            ax = plt.bar(x,y,label='Значение показателя', color='green', alpha=0.5)
            ax = plt.plot(x, b + m * x , color="blue", label='Регрессия')
            # I've added a color argument here
            plt.axhline(critery, color ='red', linestyle='dashed', label='Критерий оценки')
            plt.title(name, fontsize=16, y=1.05)
            plt.legend(fontsize=8, shadow=True, framealpha=1, edgecolor='r', title='', loc='best')
            plt.grid(axis='both', color='black', linestyle='dotted', linewidth=1)

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
            a = First_Graphics(data_koef_nov_pri_razr_year, name= 'Коэфициент новизы при разработке изоляционных материалов по годам', critery=1)
            a.save_graphic('files/{}'.format(data_koef_nov_pri_razr_year.columns[0]))
            b = First_Graphics(data_koef_nov_pri_razr_middle_year, name= 'Коэфициент новизы при разработке изоляционных материалов по полугодиям', critery=1)
            b.save_graphic('files/{}'.format(data_koef_nov_pri_razr_middle_year.columns[0]))
            c = First_Graphics(data_koef_vned_konst_dok_year, name= 'Коэффициент внедрения КД (чертежи) по годам', critery=70)
            c.save_graphic('files/{}'.format(data_koef_vned_konst_dok_year.columns[0]))
            d = First_Graphics(data_koef_vned_konst_dok_middle_year, name= 'Коэффициент внедрения КД (чертежи) по полугодиям', critery=70)
            d.save_graphic('files/{}'.format(data_koef_vned_konst_dok_middle_year.columns[0]))
            e = First_Graphics(data_pok_kach_razr_td_year, name= 'Показатель качества разработанной ТД (ТУ, ПМИ) по годам', critery=20)
            e.save_graphic('files/{}'.format(data_pok_kach_razr_td_year.columns[0]))
            f = First_Graphics(data_pok_kach_razr_td_middle_year, name= 'Показатель качества разработанной ТД (ТУ, ПМИ) по полугодиям', critery=20)
            f.save_graphic('files/{}'.format(data_pok_kach_razr_td_middle_year.columns[0]))

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
            a = First_Graphics(data_koef_nov_pri_razr_year, name= 'Коэфициент новизы при разработке изоляционных материалов по годам', critery=1)
            b = First_Graphics(data_koef_nov_pri_razr_middle_year, name= 'Коэфициент новизы при разработке изоляционных материалов по полугодиям', critery=1)
            c = First_Graphics(data_koef_vned_konst_dok_year, name= 'Коэффициент внедрения КД (чертежи) по годам', critery=70)
            d = First_Graphics(data_koef_vned_konst_dok_middle_year, name= 'Коэффициент внедрения КД (чертежи) по полугодиям', critery=70)
            e = First_Graphics(data_pok_kach_razr_td_year, name= 'Показатель качества разработанной ТД (ТУ, ПМИ) по годам', critery=20)
            f = First_Graphics(data_pok_kach_razr_td_middle_year, name= 'Показатель качества разработанной ТД (ТУ, ПМИ) по полугодиям', critery=20)
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