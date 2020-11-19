import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


data_graphics = pd.read_csv('Разница выпущенной и реализованной за год.csv', index_col = 0)
print(data_graphics)

data_graphics.plot()
plt.grid()
plt.show()
input()