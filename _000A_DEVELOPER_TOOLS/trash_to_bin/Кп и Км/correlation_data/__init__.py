#-*- coding: utf-8 -*-
"""
Файл __init__ используется как модуль для подготовки данных к определению коэффициентов корреляции
# Обработка файлов с данными из единого каталога
# Переименование наименований столбцов реализовать в данном модуле
#
#
#
"""
__all__ = ['data_1', 'data_2', 'data_3', 'data_4', 'data_5', 'data_6', 'data_7, data_8'] # присвоение списка строк с именами доступными для импортирования
import pandas as pd # импортирование библиотеки для обработки данных
# Присвоение именам переменных объектов DataFrame()
#

# Присвоение именам переменных объектов DataFrame()
#

_data_km_bitkor_year = pd.read_csv(r'correlation_data/Км_Биткор_Р.csv', index_col = 0) # загрузка исходных данных
_data_kp_bitkor_year = pd.read_csv(r'correlation_data/Кп_Биткор_Р.csv', index_col = 0) # загрузка исходных данных

_data_km_transkor_year = pd.read_csv(r'correlation_data/Км_Транскор.csv', index_col = 0) # загрузка исходных данных
_data_kp_transkor_year = pd.read_csv(r'correlation_data/Кп_Транскор.csv', index_col = 0) # загрузка исходных данных

_data_km_mbpr_year = pd.read_csv(r'correlation_data/Км_МБПР.csv', index_col = 0) # загрузка исходных данных
_data_kp_mbpr_year = pd.read_csv(r'correlation_data/Кп_МБПР.csv', index_col = 0) # загрузка исходных данных

_data_km_bitkor_u_year = pd.read_csv(r'correlation_data/Км_Биткор_Р(У).csv', index_col = 0) # загрузка исходных данных
_data_kp_bitkor_u_year = pd.read_csv(r'correlation_data/Кп_Биткор_Р(У).csv', index_col = 0) # загрузка исходных данных

_data_km_pvh_selaron_year = pd.read_csv(r'correlation_data/Км_ООО_Сэларон_ПВХ .csv', index_col = 0) # загрузка исходных данных
_data_kp_pvh_selaron_year = pd.read_csv(r'correlation_data/Кп_ООО_Сэларон_ПВХ.csv', index_col = 0) # загрузка исходных данных

_data_km_pvh_bsk_year = pd.read_csv(r'correlation_data/Км_ПВХ_ОАО_БСК.csv', index_col = 0) # загрузка исходных данных
_data_kp_pvh_bsk_year = pd.read_csv(r'correlation_data/Кп_ПВХ_ОАО_БСК.csv', index_col = 0) # загрузка исходных данных

_data_km_mastic_year = pd.read_csv(r'data/Км_Мастика.csv', index_col = 0) # загрузка исходных данных
_data_kp_mastic_year = pd.read_csv(r'data/Кп_Мастика.csv', index_col = 0) # загрузка исходных данных
_data_km_pvh_year = pd.read_csv(r'data/Км_ПВХ.csv', index_col = 0) # загрузка исходных данных
_data_kp_pvh_year = pd.read_csv(r'data/Кп_ПВХ.csv', index_col = 0) # загрузка исходных данных

_data_km_mastic_middle_year = pd.read_csv(r'data/Км_Мастика за полугодие.csv', index_col = 0) # загрузка исходных данных
_data_kp_mastic_middle_year = pd.read_csv(r'data/Кп_Мастика за полугодие.csv', index_col = 0) # загрузка исходных данных
_data_km_pvh_middle_year = pd.read_csv(r'data/Км_ПВХ за полугодие.csv', index_col = 0) # загрузка исходных данных
_data_kp_pvh_middle_year = pd.read_csv(r'data/Кп_ПВХ за полугодие.csv', index_col = 0) # загрузка исходных данных

# Переформатированние данных для обработки
#
_data_km_mastic_year = _data_km_mastic_year['показатель(%)'].rename('Км(общий)- мастика(%)')
_data_kp_mastic_year = _data_kp_mastic_year['показатель(%)'].rename('Кп(общий)- мастика(%)')
_data_km_pvh_year = _data_km_pvh_year['показатель(%)'].rename('Км(общий)- ПВХ(%)')
_data_kp_pvh_year = _data_kp_pvh_year['показатель(%)'].rename('Кп(общий)- ПВХ(%)')

_data_km_mastic_middle_year = _data_km_mastic_middle_year['показатель(%)'].rename('Км(общий)- мастика(%)')
_data_kp_mastic_middle_year = _data_kp_mastic_middle_year['показатель(%)'].rename('Кп(общий)- мастика(%)')
_data_km_pvh_middle_year = _data_km_pvh_middle_year['показатель(%)'].rename('Км(общий)- ПВХ(%)')
_data_kp_pvh_middle_year = _data_kp_pvh_middle_year['показатель(%)'].rename('Кп(общий)- ПВХ(%)')


# Подготовка данных к импорту
#
data_1 = pd.concat([_data_km_mastic_year,_data_km_bitkor_year, _data_km_transkor_year, _data_km_bitkor_u_year, _data_km_mbpr_year], axis=1)
data_2 = pd.concat([_data_kp_mastic_year,_data_kp_bitkor_year, _data_kp_transkor_year, _data_kp_bitkor_u_year, _data_kp_mbpr_year], axis=1)

data_3 = pd.concat([_data_km_pvh_year, _data_km_pvh_selaron_year, _data_km_pvh_bsk_year], axis=1)
data_4 = pd.concat([_data_kp_pvh_year, _data_kp_pvh_selaron_year, _data_kp_pvh_bsk_year], axis=1)

data_5 = pd.concat([_data_km_mastic_year, _data_kp_mastic_year], axis=1)
data_6 = pd.concat([_data_km_pvh_year, _data_kp_pvh_year], axis=1)

data_7 = pd.concat([_data_km_mastic_middle_year, _data_kp_mastic_middle_year], axis=1)
data_8 = pd.concat([_data_km_pvh_middle_year, _data_kp_pvh_middle_year], axis=1)

