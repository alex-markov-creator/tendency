import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="darkgrid")

df = pd.read_csv('Уровень пропуска рабочих дней 2007-2019.csv', index_col=0)
#print(data.info())
#g = sns.relplot(x="год", y="показатель(%)", kind="line", data=df)
#g.fig.autofmt_xdate()
sns.set()
df.plot()
plt.show()