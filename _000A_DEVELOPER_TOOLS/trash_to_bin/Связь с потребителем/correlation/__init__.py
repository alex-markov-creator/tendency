#-*- coding: utf-8 -*-
import pandas as pd
# Модуль для подготовки данных к определению коэффициентов корреляции

data_graphics = pd.read_csv('data/Уровень удовлетворенности.csv', index_col = 0) # загрузка исходных данных
df_year = pd.read_csv('data/Уровень повторных закупок.csv', index_col=0)
data_run = pd.read_csv('data/Уровень выполнения заказов.csv', index_col=0)
data_pr = pd.read_csv('correlation/Претензии и рекламации от потребителей.csv', index_col=0)
data_real = pd.read_csv(r'correlation/Количество реализованной продукции.csv', index_col=0)
data_post = pd.read_csv(r'correlation/Уровень поставок.csv', index_col=0)
data_mast = pd.read_csv(r'correlation/Км_Мастика.csv', index_col=0)
data_pvh = pd.read_csv(r'correlation/Км_ПВХ.csv', index_col=0)

df_year = df_year['показатель(%)'].rename('Пов.закупки(%)')
data_graphics = data_graphics['показатель(%)'].rename('Ур.удов.(%)')
data_run = data_run['показатель(%)'].rename('Вып.заказов(%)')
data_pr = data_pr['показатель(%)'].rename('Пр.и.рек.(%)')
data_real = data_real['кол-во(тонн)'].rename('Кол.реал(т)')
data_post = data_post['показатель(%)'].rename('Ур.пост.(%)')
data_mast = data_mast['показатель(%)'].rename('Км.маст(%)')
data_pvh = data_pvh['показатель(%)'].rename('Км.пвх(%)')


df = pd.concat([data_graphics,data_pr,data_real,df_year], axis=1)
#print(df.corr())