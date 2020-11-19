#-*- coding: utf-8 -*-
import pandas as pd
# Модуль для подготовки данных к определению коэффициентов корреляции

data_complect_year = pd.read_csv(r'data/Уровень укомплектованности кадрами.csv', index_col = 0) # загрузка исходных данных
data_complect_middle_year = pd.read_csv(r'data/Уровень укомплектованности кадрами за полугодие.csv', index_col = 0) # загрузка исходных данных
data_tec_year = pd.read_csv(r'data/Уровень текучести кадров.csv', index_col = 0) # загрузка исходных данных
data_tec_middle_year = pd.read_csv(r'data/Уровень текучести кадров за полугодие.csv', index_col = 0) # загрузка исходных данных
data_propusk_year = pd.read_csv(r'data/Уровень пропуска рабочих дней.csv', index_col = 0) # загрузка исходных данных
data_propusk_middle_year = pd.read_csv(r'data/Уровень пропуска рабочих дней за полугодие.csv', index_col = 0) # загрузка исходных данных


data_complect_year = data_complect_year['показатель(%)'].rename('Компл.кадр.(%)')
data_tec_year = data_tec_year['показатель(%)'].rename('Тек.кадр.(%)')
data_propusk_year = data_propusk_year['показатель(%)'].rename('Пр.дней.(%)')
data_complect_middle_year = data_complect_middle_year['показатель(%)'].rename('Компл.кадр(%)')
data_tec_middle_year = data_tec_middle_year['показатель(%)'].rename('Тек.кадр.(%)')
data_propusk_middle_year = data_propusk_middle_year['показатель(%)'].rename('Пр.дней.(%)')


data_1 = pd.concat([data_complect_year, data_tec_year, data_propusk_year], axis=1)
data_2 = pd.concat([data_complect_middle_year, data_tec_middle_year, data_propusk_middle_year], axis=1)

