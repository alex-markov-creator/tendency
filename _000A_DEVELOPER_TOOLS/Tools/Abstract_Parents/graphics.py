#-*- coding: utf-8 -*-
"""
Универсальный модуль для определения применяемых классов при построении графиков, сохранения изображения графика, построения линейной регресии
from abc import ABC, abstractmethod # модуль для определения базового абстрактного класса

# Пример использования:

from Tools.Abstract_Parents import Graphic # универсальный модуль для выполнения контракта
#import Tools.Abstract_Parents as Abstract # варианты импорта Abstract.Graphic - вызов абстрактного класса
#import Tools # варианты импорта Tools.Graphic - вызов абстрактного класса
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class FirstGraphic(Graphic):
    def __init__(self, data):
        super().__init__(data)
        pass

class SecondGraphic(Graphic):
    def __init__(self, data):
        super().__init__(data)
        pass

if __name__=='__main__':
    data = pd.DataFrame({'Показатель,%': np.array([x**2 for x in range(10)])})
    a = FirstGraphic(data) # экземпляр класса первого графика
    a.regres_graphic() # построение графика линейной регресии
    b = SecondGraphic(data) # экземпляр класса второго графика
    b.test_graphic() # Построение "Тест-графика""
    b.save_graphic('Название файла изображения')
    b.regres_graphic()
    plt.show()
"""
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
from scipy.stats import linregress # модуль для построения линейной регрессии
import numpy as np
import pandas as pd

class Graphic(ABC):
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
    def __init__(self, data: pd.DataFrame, name: str='Название графика'):
        self.data = data

    def test_graphic(self):
        """
        Простой линейный график для тестового просмотра
        """
        fig, ax = plt.subplots()
        fig.canvas.set_window_title('Тест - график')
        plt.plot(self.data)
        plt.title('Название графика')
        plt.grid()

    def save_graphic(self, name: str = 'Нет названия'):
        """
        Функция сохранения файла изображения графика.
        object.save_graphic(name), где name - название графика
        :name: str
        """
        self.name = name
        fmt = 'png' # type: str
        plt.savefig('{}.{}'.format(name, fmt))

    def regres_graphic(self, name = r'Линейная регрессия'):
        """
        Точечный график с линейной регрессией.
        object.regres_graphic(name), где name - название графика
        :name: str
        """
        fig, ax = plt.subplots()
        fig.canvas.set_window_title('График линейной регресии')
        x = self.data.index.tolist()
        x = np.array(x)
        y: pd.DataFrame = self.data.transpose().iloc[0]
        y = np.array(y)
        stats = linregress(x, y)
        m = stats.slope
        b = stats.intercept
        ax = plt.scatter(x,y,marker='D',label='Значение показателя')
        ax = plt.plot(x, b + m * x , color="red", label='Линия регрессии')
        plt.xlabel('Ось - X')
        plt.ylabel('Значение показателя')
        plt.title(name, fontsize=16, y=1.05)
        plt.legend(fontsize=8, shadow=True, framealpha=1, facecolor='w', edgecolor='r', title='', loc='upper right')
        plt.grid(axis='both', color='black', linestyle='dotted',linewidth=1)

if __name__=='__main__':
    data = pd.DataFrame({'Значение': np.array([x**2 for x in range(10)])})

    class FirstGraphics(Graphic):
        def __init__(self, data):
            super().__init__(data)
            pass

    class SecondGraphics(Graphic):
            pass

    a = FirstGraphics(data)
    a.test_graphic()
    a.save_graphic('Название файла изображения Тест-графика')
    a.regres_graphic()

    try:
        b = SecondGraphics(data)
    except:
        print("В данном классе не реализованы предусмотренные абстрактным классом методы")

    plt.show()