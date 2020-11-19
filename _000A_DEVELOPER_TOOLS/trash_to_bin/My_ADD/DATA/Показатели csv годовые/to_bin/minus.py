import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
"""
data_realised = pd.read_csv('Количество реализованной продукции 2007-2019.csv', index_col = 0)
data_production = pd.read_csv(r'../Процесс Б(7.5) Производство продукции/Количество выпущенной продукции.csv', index_col = 0)
#print(data_realised[3:])
#print(data_production)

frames = [data_realised[3:], data_production]
data = pd.concat(frames, axis=1, sort=False)

#print(data)
a = data['кол-во(тонн)'].sum()
b = data['показатель(%)'].sum()

print(a)
print(b)
print(a-b)
"""
#data.to_csv('Разница выпущенной и реализованной.csv')


data_graphics = pd.read_csv('Разница выпущенной и реализованной.csv', index_col = 0)
print(data_graphics)
data_graphics.plot()
plt.grid()
plt.show()
input()
