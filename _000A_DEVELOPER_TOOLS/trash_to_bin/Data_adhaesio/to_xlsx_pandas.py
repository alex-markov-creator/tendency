#-*- coding: utf-8 -*-
"""
to_xlsx_pandas.py - pandas converter to *.xlsx
"""
import os
import glob
import pandas as pd

df_lst=[]
name_lst = []
for csvfile in glob.glob(os.path.join('.', '*.csv')):
    save_data = pd.read_csv(csvfile)
    df_lst.append(save_data)
    name_lst.append(csvfile[2:][:-4])

class Converter:
    """
    Class for convert to *.xlsx
    """
    def __init__(self, df_lst, name_lst, name = r'file.xlsx'):
        self.df_lst = df_lst
        self.name_lst = name_lst
        self.name = name

    def to_xlsx(self):
        """
        Method for convert to *xlsx
        """
        with pd.ExcelWriter(self.name) as writer:
            for df, sheet in zip(df_lst, name_lst):
                df.to_excel(writer, sheet_name=sheet, index=False)

a = Converter(df_lst, name_lst, name = r'adhaesio.xlsx')
a.to_xlsx()