#-*- coding: utf-8 -*-
# Модуль построения графиков по показателям качества: - Общий Км и Кп по мастике; - Общий Км и Кп по ПВХ.
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
from scipy.stats import linregress # модуль для построения линейной регрессии
import numpy as np
#from mpl_toolkits.mplot3d import Axes3D # модуль для построения 3D графиков
from abc import ABC, abstractmethod # модуль для определения базового абстрактного класса

import correlation_data as cr # коэффициенты корреляции из __init__ файла


# ИСХОДНЫЕ ДАННЫЕ - DataFrame библиотека pandas
data_km_mastic_year = pd.read_csv('data/Км_Мастика.csv', index_col = 0) # загрузка исходных данных
data_kp_mastic_year = pd.read_csv('data/Кп_Мастика.csv', index_col = 0) # загрузка исходных данных
data_km_mastic_middle_year = pd.read_csv('data/Км_Мастика за полугодие.csv', index_col = 0) # загрузка исходных данных
data_kp_mastic_middle_year = pd.read_csv('data/Кп_Мастика за полугодие.csv', index_col = 0) # загрузка исходных данных

data_km_pvh_year = pd.read_csv('data/Км_ПВХ.csv', index_col = 0) # загрузка исходных данных
data_kp_pvh_year = pd.read_csv('data/Кп_ПВХ.csv', index_col = 0) # загрузка исходных данных
data_km_pvh_middle_year = pd.read_csv('data/Км_ПВХ за полугодие.csv', index_col = 0) # загрузка исходных данных
data_kp_pvh_middle_year = pd.read_csv('data/Кп_ПВХ за полугодие.csv', index_col = 0) # загрузка исходных данных

class Static(ABC):
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
    def __init__(self,data, name='Название графика'):
        self.data = data

    def save_Graphics(self, name='Нет названия'):
        """
        Функция сохранения файла изображения графика
        """
        self.name = name
        fmt = 'png'
        plt.savefig('{}.{}'.format(name, fmt))

    def regres_graphics(self):
        """
        Точечный график с линейной регрессией
        """
        fig, ax = plt.subplots()
        x = self.data.index.tolist()
        x = np.array(x)
        y = self.data['показатель(%)']
        y = np.array(y)
        stats = linregress(x, y)
        m = stats.slope
        b = stats.intercept
        ax = plt.scatter(x,y,marker='+',label='Значение показателя')
        ax = plt.plot(x, b + m * x , color="red", label='Регрессия')   # I've added a color argument here
        plt.title(r'Линейная регрессия', fontsize=16, y=1.05)
        plt.legend(fontsize=8, shadow=True, framealpha=1, facecolor='y', edgecolor='r', title='', loc='upper right')
        plt.grid(axis='both', color='black', linestyle='dotted',linewidth=1)

class First_Graphics(Graphics):
    """
    Класс запуска графического отображения
    """
    # Процесс Б(7.4)
    # Диаграмма качества входящей продукции
    def __init__(self, data, name='Название графика', critery = 0):
        super().__init__(data)
        plt.style.use('seaborn-bright')
        self.data.plot.barh(color='black', linestyle='dashed', linewidth=2, alpha=0.7)
        plt.axvline(critery, color ='red', linestyle='dashed', label='Критерий оценки')
        plt.title(name, fontsize=16, y=1.05)
        plt.legend(fontsize=8, shadow=True, framealpha=1, facecolor=None, edgecolor='r', title='', loc='lower right')
        plt.grid(axis='both', color='black', linestyle='dotted',linewidth=1, alpha=0.5)


if __name__ == '__main__':
    a = First_Graphics(data_km_mastic_year,name = "Км по мастике (общий)", critery = 3)
    #a.regres_graphics()
    b = First_Graphics(data_km_mastic_middle_year,name = "Км по мастике (общий) по полугодиям", critery = 3)
    c = First_Graphics(data_kp_mastic_year,name = "Кп по мастике (общий)", critery = 50)
    d = First_Graphics(data_kp_mastic_middle_year, name = "Кп по мастике (общий) по полугодиям", critery = 50)
    e = First_Graphics(data_km_pvh_year,name = "Км по ПВХ (общий)", critery = 3)
    f = First_Graphics(data_km_pvh_middle_year,name = "Км по ПВХ (общий) по полугодиям", critery = 3)
    g = First_Graphics(data_kp_pvh_year,name = "Кп по ПВХ (общий)", critery = 50)
    h = First_Graphics(data_kp_pvh_middle_year,name = "Кп по ПВХ (общий) по полугодиям", critery = 50)

    print('Таблица данных показателей Км по мастике:\n{}'.format(cr.data_1))
    print('Таблица данных показателей Кп по мастике:\n{}'.format(cr.data_2))
    print('Коэффициенты корреляции Км по мастике:\n{}'.format(cr.data_1.corr()))
    print('Коэффициенты корреляции Кп по мастике:\n{}'.format(cr.data_2.corr()))

    print('Таблица данных показателей Км по ПВХ:\n{}'.format(cr.data_3))
    print('Таблица данных показателей Кп по ПВХ:\n{}'.format(cr.data_4))
    print('Коэффициенты корреляции Км по ПВХ:\n{}'.format(cr.data_3.corr()))
    print('Коэффициенты корреляции Кп по ПВХ:\n{}'.format(cr.data_4.corr()))

    print('Таблица данных Км и Кп по мастике - годовые:\n{}'.format(cr.data_5))
    print('Таблица данных Км и Кп по ПВХ - годовые:\n{}'.format(cr.data_6))

    print('Коэффициенты корреляции Кп к Км - мастика - годовые:\n{}'.format(cr.data_5.corr()))
    print('Коэффициенты корреляции Кп к Км - ПВХ - годовые:\n{}'.format(cr.data_6.corr()))

    print('Таблица данных Км и Кп по мастике - полугодовые:\n{}'.format(cr.data_7))
    print('Таблица данных Км и Кп по ПВХ - полугодовые:\n{}'.format(cr.data_8))

    print('Коэффициенты корреляции Кп к Км - мастика - полугодовые:\n{}'.format(cr.data_7.corr()))
    print('Коэффициенты корреляции Кп к Км - ПВХ - полугодовые:\n{}'.format(cr.data_8.corr()))

    plt.show()