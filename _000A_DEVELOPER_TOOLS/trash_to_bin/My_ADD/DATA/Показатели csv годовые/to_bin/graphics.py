import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('Уровень привлечения новых потребителей 2008-2019.csv', index_col=0)
print(data.info())
print(data)
data.plot()
plt.show()


