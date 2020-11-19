#-*- coding: utf-8 -*-
# Модуль построения графиков по показателям качества: - Уровень укомплектованности кадрами; - Уровень текучести кадров; - Уровнеь пропуска рабочих дней.
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
from scipy.stats import linregress # модуль для построения линейной регрессии
import numpy as np
#from mpl_toolkits.mplot3d import Axes3D # модуль для построения 3D графиков
from abc import ABC, abstractmethod # модуль для определения базового абстрактного класса

# ИСХОДНЫЕ ДАННЫЕ - DataFrame библиотека pandas
data_year_graphics = pd.read_csv('Уровень укомплектованности кадрами 2007-2019.csv', index_col = 0) # загрузка исходных данных
data_middle_year_graphics = pd.read_csv('Уровень укомплектованности кадрами за полугодие 2007-2019.csv', index_col = 0) # загрузка исходных данных
#print(data_First_Graphics)
data_year = pd.read_csv('Уровень текучести кадров 2007-2019.csv', index_col=0)
data_middle_year = pd.read_csv('Уровень текучести кадров за полугодие 2007-2020.csv', index_col=0)
df_year = pd.read_csv('Уровень пропуска рабочих дней 2007-2019.csv', index_col=0)
df_middle_year = pd.read_csv('Уровень пропуска рабочих дней за полугодие 2007-2020.csv', index_col=0)

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
    def __init__(self,data, name='Название графика', critery = 0):
        """
        Оформление графика
        """
        super().__init__(data)
        self.data.plot.bar(color='blue', linestyle='dashed', linewidth=2, alpha=0.5)
        plt.axhline(critery, color ='red', linestyle='dashed', label='Критерий оценки')
        plt.title(name, fontsize=16, y=1.05)
        plt.xlabel('Год')
        plt.legend(fontsize=8, shadow=True, framealpha=1, facecolor='y', edgecolor='r', title='', loc='lower left')
        plt.grid(axis='both', color='orange', linestyle='dotted',linewidth=2)

if __name__ == '__main__':
    fg = First_Graphics(data_year_graphics, name= 'Уровень укомплектованности кадрами по годам', critery=90)
    fg.regres_graphics()
    #fg.save_Graphics('Уровень укомплектованности кадрами по годам')
    #fg.save_Graphics('Линия регрессии уровня укомплектованности по годам')
    fg = First_Graphics(data_middle_year_graphics, name= 'Уровень укомплектованности кадрами по полугодиям')
    fg.regres_graphics()
    #fg.save_Graphics('Уровень укомплектованности кадрами по полугодиям')
    #fg.save_Graphics('Линия регрессии уровня укомплектованности по полугодиям')
    fg = First_Graphics(data_year, name = 'Уровень текучести кадров по годам')
    fg.regres_graphics()
    #fg.save_Graphics('Уровень текучести кадров по годам')
    #fg.save_Graphics('Линия регрессии уровня текучести кадров по годам')
    fg = First_Graphics(data_middle_year, name = 'Уровень текучести кадров по полугодиям')
    fg.regres_graphics()
    #fg.save_Graphics('Уровень текучести кадров по полугодиям')
    #fg.save_Graphics('Линия регрессии уровня текучести кадров по полугодиям')
    fg = First_Graphics(df_year, name = 'Уровень пропуска рабочих дней по годам')
    fg.regres_graphics()
    #fg.save_Graphics('Уровень пропуска рабочих дней по годам')
    #fg.save_Graphics('Линия регрессии уровня пропуска рабочих дней по годам')
    fg = First_Graphics(df_middle_year, name = 'Уровень пропуска рабочих дней по полугодиям')
    fg.regres_graphics()
    #fg.save_Graphics('Уровень пропуска рабочих дней по полугодиям')
    #fg.save_Graphics('Линия регрессии уровня пропуска рабочих дней по полугодиям')
    plt.show()