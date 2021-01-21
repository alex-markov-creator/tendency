#-*- coding: utf-8 -*-
"""
Модуль обработки и сохранения результатов расчётов коэффициентов корреляции.
Результаты сохраняются в файл формата .xlsx

ИСХОДНЫЕ ДАННЫЕ - ФАЙЛ __init__.py в ../Data:

import Data;print(Data.__doc__) # таблица переменных
"""
import sys
import os
sys.path.append(os.path.realpath('../..')) # субродительский каталог в sys.path

import numpy as np
import pandas as pd

from Data import * # импорт DataFrame объектов

import Tools.Abstract_Parents as Abstract # универсальный модуль для выполнения контракта

class Concat(Abstract.Statistic):
    def __init__(self, data):
        super().__init__(data)
        pass

lst_corr = []
for i in lst_name:
    if int(i.count())>10:
        lst_corr.append(i)
corr_data = pd.concat(lst_corr, axis = 1)
corr_data = corr_data.dropna()
record_data = corr_data.corr()
# УДАЛИТЬ ЗНАЧЕНИЯ С NAN и пустые строки, а также значения коэффициентов в интервале -0.5...0.5...!!!!!!!!!!!!!!!!!!!!!!!!!!
record_data.to_excel('corr.xlsx')
