#-*- coding: utf-8 -*-
"""
Файл __init__ используется как модуль для подготовки данных к определению коэффициентов корреляции
"""
__all__ = ['data_1', 'data_2'] # присвоение списка строк с именами доступными для импортирования
import pandas as pd # импортирование библиотеки для обработки данных
# Присвоение именам переменных объектов DataFrame()
#
_data_new_develop_year = pd.read_csv('data/Коэфициент новизны при разработке лент.csv', index_col = 0) # загрузка исходных данных
_data_new_develop_middle_year = pd.read_csv('data/Коэфициент новизны при разработке лент за полугодие.csv', index_col = 0)
_data_koef_inc_year = pd.read_csv('data/Коэффициент внедрения конструкторской документации.csv', index_col = 0)
_data_koef_inc_middle_year = pd.read_csv('data/Коэффициент внедрения конструкторской документации за полугодие.csv', index_col = 0)
_data_dev_td_year = pd.read_csv('data/Показатель качества разработанной технической документации.csv', index_col = 0)
_data_dev_td_middle_year = pd.read_csv('data/Показатель качества разработанной технической документации.csv', index_col = 0)
# Переформатированние данных для обработки
#
_data_new_develop_year = _data_new_develop_year['показатель(%)'].rename('Нов.при разраб.(%)')
_data_new_develop_middle_year = _data_new_develop_middle_year['показатель(%)'].rename('Нов.при разраб п.г.(%)')
_data_koef_inc_year = _data_koef_inc_year['показатель(%)'].rename('Коэф.вн.(%)')
_data_koef_inc_middle_year = _data_koef_inc_middle_year['показатель(%)'].rename('Коэф.вн.(%)')
_data_dev_td_year = _data_dev_td_year['показатель(%)'].rename('Пок.кач.ТД(%)')
_data_dev_td_middle_year = _data_dev_td_middle_year['показатель(%)'].rename('Пок.кач.ТД(%)')
# Подготовка данных к импорту
#
data_1 = pd.concat([_data_new_develop_year, _data_koef_inc_year, _data_dev_td_year], axis=1)
data_2 = pd.concat([_data_new_develop_middle_year, _data_koef_inc_middle_year, _data_dev_td_middle_year], axis=1)




