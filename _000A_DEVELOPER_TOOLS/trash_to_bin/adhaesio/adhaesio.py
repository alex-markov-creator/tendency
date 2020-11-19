# -*- coding: utf-8 -*-
"""
adhaesio.py - модуль обработки данных по показателям качества характеризующих адгезию.

Показатели:
1 Адгезия ленты к праймированной стальной поверхности при температуре
(20 "плюс минус 3" градусов по Цельсию), Н/см, не менее 15-20 Н/см,
обозначение в таблице - "к стали";
2 Адгезия ленты к праймированной стальной поверхности с подплавлением мастичного слоя при температуре (20 "плюс минус 3" градусов по Цельсию), Н/см, не менее 15-20 Н/см,;
обозначение в таблице - "с подплавл"
3 Адгезия ленты к ленте в нахлесте при температуре
(20 "плюс минус 3" градусов по Цельсию), Н/см, не менее 7-15 Н/см,
обозначение в таблице - "в нахлест".

Критерии значений по наименования соответственно:
ПИРМА-З - 20 Н/см, 20 Н/см, 15 Н/см;
ПИРМА-Л - 20 Н/см, 20 Н/см, 15 Н/см;
ЛИТКОР-З_газ - 20 Н/см, 20 Н/см, 15 Н/см;
ЛИТКОР-З_тр_нефть - 20 Н/см, 20 Н/см, 15 Н/см;
ЛИТКОР-Л_газ - 20 Н/см, 20 Н/см, 15 Н/см;
ЛИТКОР-Л_тр_нефть - 20 Н/см, 20 Н/см, 15 Н/см;
ЛИТКОР-НН толщина 1.9 мм. - 20 Н/см, 20 Н/см, 15 Н/см;
ЛИТКОР-НН толщина 2.0 мм. - 20 Н/см, 20 Н/см, 15 Н/см;
ЛИТКОР-НН толщина 1.7 мм. - 20 Н/см, 20 Н/см, 15 Н/см;
БПИ толщина 1.7 мм. - 20 Н/см, 20 Н/см, 7 Н/см;
БПИ толщина 2.0 мм - 20 Н/см, 20 Н/см, 7 Н/см;

Выполняет следующие задачи:
- Чтение файлов формата .csv;
- Построение графиков;
- Расчёт и вывод статистических данных.
"""
import DATA_CSV as data # импорт данных в формате .csv

from prettytable import PrettyTable # импорт библиотеки для вывода табличных данных в консоли(терминале)
import pandas as pd # импорт библиотеки для работы с типом данных DataFrame
import numpy as np # импорт библиотеки для работы с массивами и матрицами
import matplotlib.pyplot as plt # графическая библиотека для построения графиков
import seaborn as sns # графическая библиотека - переоформленная matplotlib
from scipy.stats import linregress # модуль для построения линейной регрессии
#from mpl_toolkits.mplot3d import Axes3D # модуль для построения 3D графиков
from abc import ABC, abstractmethod, abstractproperty # модуль для определения базового абстрактного класса

class Info(object):
    """
    Класс c информацией в виде таблицы по исходным данным
    """
    def __init__(self):
        self.x = PrettyTable()
        field_names = ['Идентификатор','Наименования лент', 'Файлы с данными']
        self.x.add_column(field_names[0],list(data.NAME_INPUT.keys()))
        self.x.add_column(field_names[1],data.LENTA_NAME)
        self.x.add_column(field_names[2],data.PATH)


    def __repr__(self):
        return 'Исходные данные:\n{}'.format(self.x)

class Read(object):
    """
    Класс чтения файла формата .csv
    """
    def __init__(self, lenta):
        """
        Метод перегрузки, инициализации экземпляров класса
        """
        self.lenta = lenta
        self.data = pd.read_csv(lenta, header = 0)

class Statistic(ABC):
    """
    Абстрактный класс для статистических данных.
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
    def __init__(self, data):
        self.data = data

class Graphics(ABC):
    """
    Абстрактный класс для определения визуализируемых данных, сохранения файла с изображением графика и построения графика линейной регресии  с помощью библиотеки matplolib.
    """
    @abstractmethod
    def __init__(self,data, name='Название графика'):
        self.data = data

    def save_Graphics(self, name='Нет названия'):
        """
        Функция сохранения файла изображения графика
        """
        self.name = name
        fmt = 'png'
        plt.savefig('{}.{}'.format(name, fmt))

    def regres_graphics(self, pk = 'к стали'):
        """
        Точечный график с линейной регрессией
        """
        fig, ax = plt.subplots()
        x = self.data.index.tolist()
        x = np.array(x)
        y = self.data[pk]
        y = np.array(y)
        stats = linregress(x, y)
        m = stats.slope
        b = stats.intercept
        ax = plt.scatter(x,y,marker='o',label = pk, color = 'black', alpha=0.3)
        ax = plt.plot(x, b + m * x , color="red", label='Регрессия')   # I've added a color argument here
        plt.title(r'Линейная регрессия значений показателя адгезии', fontsize=16, y=1.05)
        plt.legend(fontsize=8, shadow=True, framealpha=1,  edgecolor='r', title='', loc='best')
        plt.grid(axis='both', color='black', linestyle='dotted',linewidth=1)

class Visual(Graphics):
    """
    Класс визуализации данных используя библиотеку matplotlib
    """
    def __init__(self, data, name='Название графика', critery_1 = 20, critery_2 = 15, critery_3 = 7):
        super().__init__(data)
        self.data.plot(linestyle='solid', linewidth=2, alpha=1)
        plt.axhline(critery_1, color ='red', linestyle=':', label='Критерий оценки "к стали"')
        plt.axhline(critery_2, color ='blue', linestyle=':', label='Критерий оценки "в нахлест"')
        plt.axhline(critery_3, color ='black', linestyle=':', label='Критерий оценки "в нахлест" - БПИ')
        plt.xlabel('Номер испытания', fontsize=12)
        plt.ylabel("Значение адгезии, Н/см", fontsize=12)
        plt.legend(fontsize=8, shadow=True, framealpha=1,  edgecolor='r', title='', loc='best')
        plt.grid(axis='both', color='black', linestyle=':',linewidth=0.5, alpha=0.7)
        plt.title(LENTA_NAME[PATH.index(reading.lenta)],fontsize=16, y=1.05)

class Visual_box(Graphics):
    def __init__(self, data):
        super().__init__(data)
        sns.boxplot(data=self.data)
        #g = sns.PairGrid(self.data)
        #g.map_diag(plt.hist)
        #g.map_offdiag(plt.scatter)
        plt.ylabel("Значение адгезии, Н/см", fontsize=12)
        plt.grid(axis='both', color='red', linestyle=':',linewidth=0.5, alpha=0.7)
        plt.title('Диаграмма плотности - ' + LENTA_NAME[PATH.index(reading.lenta)],fontsize=16, y=1.05)

class Visual_grid(Graphics):
    def __init__(self, data):
        super().__init__(data)
        g = sns.PairGrid(self.data)
        g.map_diag(plt.hist)
        g.map_offdiag(plt.scatter)


class Visual_scatter(object):
    """
    Класс визуализации зависимости данных
    """
    def __init__(self):
        df.plot.scatter(x = 'к стали',
                        y = 'с подплавл',
                        alpha=0.5)
        df.plot.scatter(x = 'к стали',
                        y = 'в нахлест',
                        alpha=0.5)
        df.plot.scatter(x = 'с подплавл',
                        y = 'в нахлест',
                        alpha=0.5)
        plt.grid()
        plt.show()

class Visual_ex(object):
    """
    Класс визуализации плотности данных используя библиотеку matplotlib
    """
    def __init__(self):
        df.plot.box()
        plt.grid()
        plt.show()

class Visual_alternative(object):
    """
    Альтернативный класс визуализации данных используя библиотеку matplotlib
    """
    def __init__(self):
        df.plot.area(figsize=(12, 4), subplots=True)
        plt.grid()
        plt.show()

#C 43 DOCUMENTATION FOR PANDAS

class Statistic_adhaesio(Statistic):
    """
    Класс вывода статистических данных
    """
    def __init__(self, *args, **kwargs):
        self.Ascr = df.count() # количество значений
        self.Aall = df.describe() # статистические данные
        self.Asr = df.mean()# среднее значение df.mean(n), где n - номер оси
        self.Amax = df.loc[:,['к стали','с подплавл','в нахлест']].max()# применение функции к данным
        self.Amin = df.loc[:,['к стали','с подплавл','в нахлест']].min()# применение функции к данным
        self.Acor = df.corr()# коэффициент корреляции
        self.Astd = df.std() # стандартные отклонения
        self.Adc = df['к стали'].unique()# np.array массив уникальных значений
        self.Adp = df['с подплавл'].unique()# np.array массив уникальных значений
        self.Adn = df['в нахлест'].unique()# np.array массив уникальных значений

    def __str__(self):
        """
        Функция автоматических статистических данных
        """
        return "Статистические данные:\n{}".format(self.Aall)

    def score(self):
        """
        Функция значения количества проведенных испытаний и номеров партии
        """
        return "Всего результатов испытаний ленты:\n{}".format(self.Ascr)

    def middle(self, c):
        """
        Функция средних значений
        """
        return "Среднее значение адгезии:\n{}".format(self.Asr)

    def max_min(self, d):
        print("Максимальные значения адгезии:\n{}".format(self.Amax))
        print("Минимальные значения адгезии:\n{}".format(self.Amin))

    def k_cor(self, e):
        return "Коэффициенты корреляции:\n{}".format(self.Acor)

    def st_d(self, f):
        return "Отклонение результатов испытаний:\n{}".format(self.Astd)

    def s_val(self,g):
        print ("Количество уникальных значений адгезии 'к стали':\t{} значений".format(self.Adc.size))
        print ("Количество уникальных значений адгезии 'с подплавл':\t{} значений".format(self.Adp.size))
        print ("Количество уникальных значений адгезии 'в нахлест':\t{} значений".format(self.Adn.size))
#TESTING
if __name__ == '__main__':
    try:
        info = Info()
        print(info) #вывод в консоль исходных данных

        a = input("Укажите идентификатор: ") # временное решение (необходимо упростить ввод данных до наименования переменной)

        reading = Read(data.NAME_INPUT[a]) # ВЫБОР НАИМЕНОВАНИЯ ЛЕНТЫ
        df = reading.data


        #vs = Visual(df) # график + КРИТЕРИЙ ОЦЕНКИ
        #vs.regres_graphics(pk = 'к стали')
        #vs.regres_graphics(pk = 'в нахлест')
        #Visual_box(df)
        #Visual_grid(df)
        #vsc = Visual_scatter(df)
        #vsb = Visual_box(df)
        #vsa = Visual_alternative(df)



        St = Statistic_adhaesio()
        print(St.score())
        St.middle(df)
        St.max_min(df)
        print(St.k_cor(df))
        print(St.st_d(df))
        St.s_val(df)
        # МЕТОДЫ БИБЛИОТЕКИ PANDAS
        print(df.tail(50)) # ДАННЫЕ

        #print("Статистические данные:\n", df.describe())
        #print (df.corr()) # коэффициент корреляции
        #print(df.mean()) # средние значения
        #print(df.melt()) # данные перечнем
        #print(df.dtypes) # тип данных
        #print(df.head())# первые 5 строк данных
        #print(df.index) # список индексов
        #print(df.tail(3)) # последние 3 строки
        #print(df.columns) # индексы заголовков
        #print(df.to_numpy()) # тип данных np.array
        #print(df.T)# транспонирование таблицы DataFrame
        #df_sort = df.sort_index(axis=0, ascending=False)# обратная сортировка по   индексу
        #df_sort = df.sort_values(by='к стали')# сортировка по значению
        #print(df['к стали']) # обращение по заголовку
        #print(df.loc[1:4])# обращение по индексу строки
        #print(df[4:30]) # срез данных по индексу
        #print(df.loc[:,['к стали','в нахлест']])# вывод двух столбцов
        #print(df[df['с подплавл'] < 20])# с условием
        #print(df.copy()) # копия
        #print(df.reindex(index = ['a','b','c','d'])#переиндексация
        #print(df.dropna()) удаление строк с NaN
        #print(df.fillna(value='Нет значения')) # заполнение недостающих данных
        #print(pd.isna(df)) # булевое значение если значение NaN
        #print("Среднее значение адгезии:\n", df.mean()) # среднее значение df.mean(n), где n - номер оси
        #print(df.apply(lambda x: x.max())) # примененее функции к данным
        #print(df.count()) # количество значений не NaN

        # МЕТОДЫ merge() и concat() C.25-26 ПЕРЕСЕЧЕНИЕ ТАБЛИЦЫ И КОНКАТЕНАЦИЯ
        # МЕТОДЫ groupby()  C.27 ГРУППИРОВКА ОДИНАКОВЫХ ЗНАЧЕНИЙ

        #print(df.info()) # техническая информация о DataFrame
        #print(df.std()) # стандартное отклонение
        #dc = df['к стали'].unique()# np.array массив уникальных значений
        #print(df['к стали'].value_counts()) # статистика уникальных значений
        #print(dc.size) # количество значений в массиве (длина)

        #print(df.loc[df['к стали']>30, 'в нахлест']) # выбрать специфические строки и колонки из DataFrame

        #df['новый столбец'] = df['к стали'] - df['в нахлест'] #новый столик с подсчитанными значениями
        #df_name = df.rename(columns={"к стали": "К стали"}) # переименовать колонки
        #df.median() - медиана, 50% превышает это значение 50% ниже данного значения
        #print(df["к стали"].value_counts()) # кол-во одинаковых значений
    except:
        print("Error!!!")

    # c61
#input("Press Enter: ")



plt.show()








