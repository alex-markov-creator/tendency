#-*- coding: utf-8 -*-
"""
Файл __init__ используется как модуль для подготовки данных
+---------------+---------------------------+-----------------------------+
| Идентификатор |     Наименования лент     |      Наименование листов    |
+---------------+---------------------------+-----------------------------+
|      001      |          ПИРМА-З          |            П_З              |
|      002      |          ПИРМА-Л          |            П_Л              |
|      003      |        ЛИТКОР-З_газ       |         ЛИТ_З_газ           |
|      004      |     ЛИТКОР-З_тр_нефть     |       ЛИТ_З_тр_нефть        |
|      005      |        ЛИТКОР-Л_газ       |         ЛИТ_Л_газ           |
|      006      |     ЛИТКОР-Л_тр_нефть     |       ЛИТ_Л_тр_нефть        |
|      007      | ЛИТКОР-НН толщина 1.9 мм. |         ЛИТ_НН_1_9          |
|      008      | ЛИТКОР-НН толщина 2.0 мм. |         ЛИТ_НН_2_0          |
|      009      | ЛИТКОР-НН толщина 1.7 мм. |         ЛИТ_НН_1_7          |
|      010      |    БПИ толщина 1.7 мм.    |           БПИ_1_7           |
|      011      |     БПИ толщина 2.0 мм    |           БПИ_2_0           |
+---------------+---------------------------+-----------------------------+
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_excel('adhaesio.xlsx', sheet_name='П_З')
print(df)
df = df.iloc[:, 1:4]
print(df)

import sys
import os
sys.path.append(os.path.realpath('../..')) # субродительский каталог в sys.path

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import Tools.Abstract_Parents as Abstract # варианты импорта Abstract.Graphic - вызов абстрактного класса

class FirstGraphic(Abstract.Graphic):
    def __init__(self, data):
        super().__init__(data)
        pass

class SecondGraphic(Abstract.Graphic):
    def __init__(self, data):
        super().__init__(data)
        pass

if __name__=='__main__':
    data = pd.DataFrame({'Показатель,%': np.array([x**2 for x in range(10)])})
    a = FirstGraphic(df) # экземпляр класса первого графика
    a.regres_graphic() # построение графика линейной регресии
    b = SecondGraphic(df) # экземпляр класса второго графика
    b.test_graphic() # Построение "Тест-графика""
    #b.save_graphic('Название файла изображения')
    b.regres_graphic()
    plt.show()

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
#print(df.dropna())# удаление строк с NaN
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

#-*- coding: utf-8 -*-
"""
Файл __init__ используется как модуль для подготовки данных
+---------------+---------------------------+--------------------------------+
| Идентификатор |     Наименования лент     | Наименование листов/переменных |
+---------------+---------------------------+--------------------------------+
|      001      |          ПИРМА-З          |            П_З / pz            |
|      002      |          ПИРМА-Л          |            П_Л / pl            |
|      003      |        ЛИТКОР-З_газ       |      ЛИТ_З_газ / lz_gaz        |
|      004      |     ЛИТКОР-З_тр_нефть     | ЛИТ_З_тр_нефть / lz_tr_neft    |
|      005      |        ЛИТКОР-Л_газ       |      ЛИТ_Л_газ / ll_gaz        |
|      006      |     ЛИТКОР-Л_тр_нефть     | ЛИТ_Л_тр_нефть / ll_tr_neft    |
|      007      | ЛИТКОР-НН толщина 1.9 мм. |     ЛИТ_НН_1_9 / lnn_1_9       |
|      008      | ЛИТКОР-НН толщина 2.0 мм. |     ЛИТ_НН_2_0 / lnn_2_0       |
|      009      | ЛИТКОР-НН толщина 1.7 мм. |     ЛИТ_НН_1_7 / lnn_1_7       |
|      010      |    БПИ толщина 1.7 мм.    |     БПИ_1_7 / bpi_1_7          |
|      011      |     БПИ толщина 2.0 мм    |     БПИ_2_0 / bpi_2_0          |
+---------------+---------------------------+--------------------------------+
"""
__all__ = ['pz','pl','lz_gaz','lz_tr_neft','ll_gaz','ll_tr_neft','lnn_1_9','lnn_2_0','lnn_1_7','bpi_1_7', 'bpi_2_0'] # присвоение списка строк с именами доступными для импортирования

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

pz = pd.read_excel(
        r'../../../Data/Показатели xlsx адгезии/adhaesio.xlsx',
    sheet_name='П_З'
    )
pl = pd.read_excel(
        r'../../../Data/Показатели xlsx адгезии/adhaesio.xlsx',
    sheet_name='П_Л'
    )
lz_gaz = pd.read_excel(
        r'../../../Data/Показатели xlsx адгезии/adhaesio.xlsx',
    sheet_name='ЛИТ_З_газ'
    )
lz_tr_neft = pd.read_excel(
        r'../../../Data/Показатели xlsx адгезии/adhaesio.xlsx',
    sheet_name='ЛИТ_З_тр_нефть'
    )
ll_gaz = pd.read_excel(
        r'../../../Data/Показатели xlsx адгезии/adhaesio.xlsx',
    sheet_name='ЛИТ_Л_газ'
    )
ll_tr_neft = pd.read_excel(
        r'../../../Data/Показатели xlsx адгезии/adhaesio.xlsx',
    sheet_name='ЛИТ_Л_тр_нефть'
    )
lnn_1_9 = pd.read_excel(
        r'../../../Data/Показатели xlsx адгезии/adhaesio.xlsx',
    sheet_name='ЛИТ_НН_1_9'
    )
lnn_2_0 = pd.read_excel(
        r'../../../Data/Показатели xlsx адгезии/adhaesio.xlsx',
    sheet_name='ЛИТ_НН_2_0'
    )
lnn_1_7 = pd.read_excel(
        r'../../../Data/Показатели xlsx адгезии/adhaesio.xlsx',
    sheet_name='ЛИТ_НН_1_7'
    )
bpi_1_7 = pd.read_excel(
        r'../../../Data/Показатели xlsx адгезии/adhaesio.xlsx',
    sheet_name='БПИ_1_7'
    )
bpi_2_0 = pd.read_excel(
        r'../../../Data/Показатели xlsx адгезии/adhaesio.xlsx',
    sheet_name='БПИ_2_0'
    )

lst_name = [pz,
            pl,
            lz_gaz,
            lz_tr_neft,
            ll_gaz,
            ll_tr_neft,
            lnn_1_9,
            lnn_2_0,
            lnn_1_7,
            bpi_1_7,
            bpi_2_0
            ]