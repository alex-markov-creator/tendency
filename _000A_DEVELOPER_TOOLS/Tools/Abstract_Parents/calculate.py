#-*- coding: utf-8 -*-
"""
Универсальный модуль для определения применяемых классов при выполнении инструкций редактирования объектов типа pandas.DataFrame, а также различных подсчётов и т. д., необходимых для вывода статистической информации и построения графиков.
from abc import ABC, abstractmethod # модуль для определения базового абстрактного класса

# Пример использования:

from Tools.Abstract_Parents import Calc # универсальный модуль для выполнения контракта
#import Tools.Abstract_Parents as Abstract # варианты импорта Abstract.Calc - вызов абстрактного класса
#import Tools # варианты импорта Tools.Graphic - вызов абстрактного класса
import pandas as pd
import numpy as np
data = pd.DataFrame(
    {'X**2': np.array([x**2 for x in range(100)]),
    'X**3': np.array([y**3 for y in range(100)])}
    )

data_1 = pd.DataFrame(
    {'X*2': np.array([x*2 for x in range(100)]),
    'X*3': np.array([y*3 for y in range(100)])}
    )

class Example_Calc(Calc):
    def __init__(self, data):
        super().__init__(data)
        pass

class NotImp_Calc(Calc):
    pass

a = Example_Calc(data)
new_data = a.concat_data(data,data_1)
new_data['(X**2)-(X*2)'] = new_data['X**2']-new_data['X*2']
print(new_data)

try:
    b = NotImp_Calc()
except:
    print("В данном классе не реализованы предусмотренные абстрактным классом методы")

"""
from abc import ABC, abstractmethod
import numpy as np
import pandas as pd

class Calc(ABC):
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
    def __init__(self):
        pass

    def concat_data(self, *args: pd.DataFrame):
        return pd.concat(list(args), axis=1)

if __name__ == '__main__':

    data = pd.DataFrame(
        {'X**2': np.array([x**2 for x in range(100)]),
        'X**3': np.array([y**3 for y in range(100)])}
        )

    data_1 = pd.DataFrame(
        {'X*2': np.array([x*2 for x in range(100)]),
        'X*3': np.array([y*3 for y in range(100)])}
        )

    class Example_Calc(Calc):
        def __init__(self):
            super().__init__()
            pass

    class NotImp_Calc(Calc):
        pass

    a = Example_Calc()
    new_data = a.concat_data(data,data_1)
    new_data['(X**2)-(X*2)'] = new_data['X**2']-new_data['X*2']
    print(new_data)

    try:
        b = NotImp_Calc()
    except:
        print("В данном классе не реализованы предусмотренные абстрактным классом методы")