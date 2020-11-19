import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['font.fantasy'] = 'Arial', 'Times New Roman', 'Tahoma', 'Comic Sans MS', 'Courier'
mpl.rcParams['font.family'] = 'fantasy'
# Текущий стиль-семейство шрифтов
cfam = mpl.rcParams.get('font.family')[0]
print('cfam %s' % cfam)
cfont = mpl.rcParams.get('font.fantasy')[0]
# Первый шрифт в текущем семействе
print(mpl.rcParams.get('font.%s' % cfam))
N = 100
x = np.arange(N)
# Задаём выборку из Гамма-распредления с параметрами формы=1. и масштаба=3.0
y = np.random.gamma(1.0, 3.0, N)
fig = plt.figure()
cc = plt.hist(y)
text_style = ['italic', 'oblique', 'normal']
font_weights = ['bold', 'light', 'normal']
for i, ts in enumerate(text_style):
    plt.text(6, 20-5*i, '%s text style' % ts, {'fontname':'Courier'}, style=ts, fontsize=14)
    plt.text(6, 35-4*i, '%s & %s text style' % (ts, font_weights[i]), {'fontname':'Courier'}, style=ts, fontweight=font_weights[i], fontsize=12)
plt.title('Title has %s font' % cfont, fontweight='normal', color='k', fontsize=16)
plt.xlabel('Bold weight', {'fontname':'Times New Roman'}, fontweight='bold', fontsize=16)
plt.ylabel('Light weight', {'fontname':'Times New Roman'}, fontweight='light', fontsize=14)
plt.grid(True)
plt.show()