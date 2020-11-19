# -*- coding: utf-8 -*-
import pandas as pd # импорт библиотеки для работы с типом данных DataFrame
import numpy as np # импорт библиотеки для работы с массивами и матрицами
import matplotlib.pyplot as plt # графическая библиотека для построения графиков

NAME = ['DATA_CSV/П_З.csv','DATA_CSV/П_Л.csv','DATA_CSV/ЛИТ_З_газ.csv','DATA_CSV/ЛИТ_З_тр_нефть.csv','DATA_CSV/ЛИТ_Л_газ.csv','DATA_CSV/ЛИТ_Л_тр_нефть.csv', 'DATA_CSV/ЛИТ_НН_1_9.csv', 'DATA_CSV/ЛИТ_НН_2_0.csv', 'DATA_CSV/ЛИТ_НН_1_7.csv', 'DATA_CSV/БПИ_1_7.csv', 'DATA_CSV/БПИ_2_0.csv']
PZ,PL,LZ_gaz,LZ_tr_neft,LL_gaz,LL_tr_neft,LNN_1_9,LNN_2_0,LNN_1_7,BPI_1_7, BPI_2_0, *_ = NAME # распределение последовательности по переменным
LENTA_NAME = ['ПИРМА-З','ПИРМА-Л','ЛИТКОР-З_газ','ЛИТКОР-З_тр_нефть','ЛИТКОР-Л_газ', 'ЛИТКОР-Л_тр_нефть', 'ЛИТКОР-НН толщина 1.9 мм.',  'ЛИТКОР-НН толщина 2.0 мм.', 'ЛИТКОР-НН толщина 1.7 мм.','БПИ толщина 1.7 мм.','БПИ толщина 2.0 мм',*_]

"""
Модуль обработки данных по показателям качества:
1 Адгезия ленты к праймированной стальной поверхности при температуре
(20 "плюс минус 3" градусов по Цельсию), Н/см, не менее 20 Н/см,
обозначение в таблице - "к стали".
2 Адгезия ленты к ленте в нахлесте при температуре
(20 "плюс минус 3" градусов по Цельсию), Н/см, не менее 15 Н/см,
обозначение в таблице - "внахлест".

Предполагаемые действия:
# возможен вариант замены библиотеки matplotlib на plotly или другую бибилиотеку
"""

# СОЗДАНИЕ ООП КЛАССОВ ДЛЯ ИЗВЛЕЧЕНИЯ И ЗАПИСИ ДАННЫХ
class Read(object):
    """
    Класс чтения файла формата .csv
    """
    def __init__(self):
        """
        Инициализация
        """
        self.df = pd.read_csv(PZ, header = 0)
        #self.df = pd.read_csv(PL, header = 0)

class Statistic(object):
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


class Visual(object):
    """
    Класс визуализации данных используя библиотеку matplotlib
    """
    def __init__(self):
        df.to_excel('Данные адгезии для за период 2012 - 2019гг.xls')
        df.plot()

        plt.title(LENTA_NAME[0]) # реализовать вызов метода по индексу значения в коллекции

        plt.xlabel('Номер испытания', fontsize=12)
        plt.ylabel("Значение адгезии, Н/см", fontsize=12)
        plt.legend()
        plt.show()


#C 43 DOCUMENTATION FOR PANDAS


#TESTING
if __name__ == '__main__':
    df = Read().df
    St = Statistic()
    #print(St)
    print(St.score())
    St.middle(df)
    St.max_min(df)
    print(St.k_cor(df))
    print(St.st_d(df))
    St.s_val(df)
    #vs = Visual() # график
    # МЕТОДЫ БИБЛИОТЕКИ PANDAS
    #print(df) # ДАННЫЕ
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



input("Press Enter: ")






















