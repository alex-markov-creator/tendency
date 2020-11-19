#-*- coding: utf-8 -*-
#
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

data_graphics = pd.read_csv('Уровень удовлетворенности 2007-2019.csv', index_col = 0) # загрузка исходных данных
#print(data_graphics)
data_year = pd.read_csv('Уровень привлечения новых потребителей 2008-2019.csv', index_col=0)
data_middle_year = pd.read_csv('Уровень привлечения новых потребителей полугодие 2012-2019.csv', index_col=0)
df_year = pd.read_csv('Уровень повторных закупок 2014-2019.csv', index_col=0)
df_middle_year = pd.read_csv('Уровень повторных закупок полугодие 2014-2019.csv', index_col=0)
#data_graphics = pd.read_csv('Разница выпущенной и реализованной за полугодие.csv', index_col = 0) # загрузка исходных данных

#data_graphics = data_graphics.loc[2012:] # урезанные данные
#print(data_graphics)

class HistGraphics(object):
    """
    Класс запуска графического отображения

    #Пример запуска:
    # vs = HistGraphics(data_graphics)
    #vs.save_graphics('Тестовый график')
    #vs.file_preferences()
    #plt.show()
    """
    def __init__(self, data_graphics):
        """
        Оформление графика
        """
        self.data_graphics = data_graphics
        sns_plot = sns.distplot(self.data_graphics['показатель(%)'])
        fig = sns_plot.get_figure()
        plt.title(r'Гистограмма распределения', fontsize=16, y=1.05)
        plt.xlabel('Уровень удовлетворенности потребителей до 2019 года')
        plt.legend(fontsize=8, shadow=True, framealpha=1, facecolor='y', edgecolor='r', title='Частота распределения')
        plt.grid()

    def linear_graphics(self):
        #fig, ax = plt.subplots()
        x = data_graphics.index.tolist()
        x = np.array(x)
        y = data_graphics['показатель(%)']
        y = np.array(y)
        stats = linregress(x, y)
        m = stats.slope
        b = stats.intercept
        ax = self.data_graphics.plot(color='blue', marker='o', linestyle='dashdot', linewidth=2, markersize=8,alpha=0.5)
        plt.axhline(75, color ='red', linestyle='dashed', alpha=0.5)
        plt.title(r'Уровень удовлетвореннности потребителей', fontsize=16, y=1.05)
        plt.xlabel('Год')
        plt.legend(fontsize=8, shadow=True, framealpha=1, facecolor='y', edgecolor='r', title='')
        ax = plt.plot(x, b + m * x , color="red")   # I've added a color argument here
        plt.grid()

    def regres_graphics(self):
        fig, ax = plt.subplots()
        x = data_graphics.index.tolist()
        x = np.array(x)
        y = data_graphics['показатель(%)']
        y = np.array(y)
        stats = linregress(x, y)
        m = stats.slope
        b = stats.intercept
        ax = plt.scatter(x,y)
        ax = plt.plot(x, b + m * x , color="red")   # I've added a color argument here

    def three_graphics(self):
        x = data_graphics.index.tolist()
        x = np.array(x)
        z = x
        y = data_graphics['показатель(%)']
        y = np.array(y)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x,y,z, label = 'parametric curve')

    def save_graphics(self, name):
        """
        Функция сохранения файла изображения графика
        """
        self.name = name
        fmt = 'png'
        plt.savefig('{}.{}'.format(name, fmt))

    def file_preferences(self):
        """
        Путь файла настроек и текущие настройки
        """
        import matplotlib as plt
        print(plt.matplotlib_fname())
        #print(plt.rcParams)

class MarkerGraphics(object):
    """
    Класс запуска графического отображения

    #Пример запуска:
    # vs = MarkerGraphics(data_graphics)
    #vs.save_graphics('Тестовый график')
    #plt.show()
    """
    def __init__(self, data):
        """
        Оформление графика
        """
        self.data = data
        self.data.plot(color='blue', marker='o', linestyle='dashed', linewidth=2, markersize=8)
        plt.axhline(5, color ='red', linestyle='dashed')
        plt.title(r'Уровень привлечения новых потребителей', fontsize=16, y=1.05)
        plt.xlabel('Год')
        plt.legend(fontsize=8, shadow=True, framealpha=1, facecolor='y', edgecolor='r', title='', loc='upper left')
        plt.grid()

    def save_graphics(self, name):
        """
        Функция сохранения файла изображения графика
        """
        self.name = name
        fmt = 'png'
        plt.savefig('{}.{}'.format(name, fmt))

class MarkerGraphics(object):
    """
    Класс запуска графического отображения

    #Пример запуска:
    # vs = MarkerGraphics(data_graphics)
    # vs.save_graphics('Тестовый график')
    # plt.show()
    """
    def __init__(self, data):
        """
        Оформление графика
        """
        self.data = data
        self.data.plot(color='blue', marker='o', linestyle='dashed', linewidth=2, markersize=8)
        plt.axhline(5, color ='red', linestyle='dashed')
        plt.title(r'Уровень привлечения новых потребителей', fontsize=16, y=1.05)
        plt.xlabel('Год')
        plt.legend(fontsize=8, shadow=True, framealpha=1, facecolor='y', edgecolor='r', title='', loc='upper left')
        plt.grid()

    def save_graphics(self, name):
        """
        Функция сохранения файла изображения графика
        """
        self.name = name
        fmt = 'png'
        plt.savefig('{}.{}'.format(name, fmt))

class ScatterGraphics(object):
    """
    Класс запуска графического отображения

    #Пример запуска:
    #vs = ScatterGraphics(data_graphics)
    #vs.maximum_minimum_text()
    #vs.save_graphics('Тестовый график')
    #vs.file_preferences()
    #plt.show()
    """
    def __init__(self, data):
        """
        Оформление графика
        """
        self.data = data
        self.data.plot(color='green', marker='o', linestyle='dotted', linewidth=2, markersize=8)
        plt.axhline(5, color ='red', linestyle='dashed')
        plt.title(r'Уровень повторных закупок', fontsize=16, y=1.05)
        plt.xlabel('Год')
        plt.legend(fontsize=8, shadow=True, framealpha=1, facecolor='y', edgecolor='r', title='', loc='upper left')
        plt.grid()

    def save_graphics(self, name):
        """
        Функция сохранения файла изображения графика
        """
        self.name = name
        fmt = 'png'
        plt.savefig('{}.{}'.format(name, fmt))

if __name__ == '__main__':
    vs = HistGraphics(data_graphics)
    vs.three_graphics()
    #vs.linear_graphics()
    #vs.regres_graphics()
    #vs.save_graphics('Диаграмма распределения в год')
    #vs.file_preferences()
    #mg = MarkerGraphics(data_middle_year)
    #mg.save_graphics('Уровень привлечения новых потребителей в полугодие')
    #sg = ScatterGraphics(df_year)
    plt.show()

input()