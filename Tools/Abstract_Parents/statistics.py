#-*- coding: utf-8 -*-
"""
Универсальный модуль для определения применяемых классов при выводе статистических данных с использованием библотеки pandas.
from abc import ABC, abstractmethod # модуль для определения базового абстрактного класса

# Пример использования:

from Tools.Abstract_Parents import Statistic # универсальный модуль для выполнения контракта
#import Tools.Abstract_Parents as Abstract # варианты импорта Abstract.Statistic - вызов абстрактного класса
#import Tools # варианты импорта Tools.Statistic - вызов абстрактного класса
import pandas as pd
import numpy as np

class FirstStatistic(Statistic):
    def __init__(self, data):
        super().__init__(data)
        pass

class SecondStatistic(Statistic):
        pass

if __name__ == '__main__':
    data = pd.DataFrame(
            {'X**2': np.array([x**2 for x in range(100)]),
            'X**3': np.array([y**3 for y in range(100)])}
                    )
    a = FirstStatistic(data)
    print(a.preview_data(25))
    print(a.preview_statistic())
    print(a.preview_corr())

    try:
        b = SecondStatistic(data)
    except:
        print("В данном классе не реализованы предусмотренные абстрактным классом методы")

"""
from abc import ABC, abstractmethod
import numpy as np
import pandas as pd

class Statistic(ABC):
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
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def preview_data(self, n:int = 25)->str:
        """
        Исходные данные object.preview_data(n), где n количество последних значений
        :return: str
        """
        self.n = n
        return 'Последние {} значений исходных данных:\n{}'.format(self.n, self.data.tail(n))

    def preview_statistic(self)->str:
        """
        Статистические данные
        :return: str
        """
        return 'Стандартные статистические данные:\n{}'.format(self.data.describe())

    def preview_corr(self)->str:
        """
        Стандартный коэффициент корреляции
        :return: str
        """
        return 'Стандартный коэффициент корреляции:\n{}'.format(self.data.corr())


if __name__ == '__main__':

    data = pd.DataFrame(
        {'X**2': np.array([x**2 for x in range(100)]),
        'X**3': np.array([y**3 for y in range(100)])}
        )

    class FirstStatistic(Statistic):
        def __init__(self, data):
            super().__init__(data)
            pass

    class SecondStatistic(Statistic):
        pass

    a = FirstStatistic(data)
    print(a.preview_data(25))
    print(a.preview_statistic())
    print(a.preview_corr())

    try:
        b = SecondStatistic(data)
    except:
        print("В данном классе не реализованы предусмотренные абстрактным классом методы")
