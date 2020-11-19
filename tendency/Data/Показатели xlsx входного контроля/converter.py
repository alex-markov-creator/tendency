#-*- coding: utf-8 -*-
"""
converter.py - name file
"""
import pandas as pd

file = 'control.xlsx'
file_creating = '2019_year.xlsm'
file_adding = '2020_middle_year.xlsm'

control = pd.read_excel(file_creating, 'Журнал входного контроля', index_col=0, header=1, usecols='A:I')
add = pd.read_excel(file_adding, 'Журнал входного контроля', index_col=0, header=2, usecols='A:I')

reader = pd.read_excel(file, sheet_name = 'Лаборатория')
length = len(reader)
print(length)

with pd.ExcelWriter(file, engine='xlsxwriter') as writer:
    #control.to_excel(writer, sheet_name='Лаборатория', startrow=0)
    add.to_excel(writer, sheet_name='Лаборатория', startrow=length)

