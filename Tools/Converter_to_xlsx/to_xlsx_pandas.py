# -*- coding: utf-8 -*-
"""
to_xlsx_pandas.py - pandas converter to *.xlsx

df_lst=[] # list db, type->pandas.DataFrame
name_lst = [] # list name, type->list

The Example importing:

import to_xlsx_pandas as txp
txp.name_df()
a = txp.Converter(txp.df_lst, txp.name_lst)
a.to_xlsx()
"""
import os
import glob
import pandas as pd

df_lst=[] # list db
name_lst = [] # list name

def name_df():
    """
    Function create df_list and name_list
    """
    for csvfile in glob.glob(os.path.join('.', '*.csv')):
        save_data = pd.read_csv(csvfile)
        df_lst.append(save_data)
        name_lst.append(csvfile[2:][:-4])

class Converter:
    """
    Class for convert to *.xlsx
    """
    def __init__(self, df_lst = [], name_lst=[], name = r'file.xlsx'):
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

if __name__ == '__main__':
    name_df()
    a = Converter(df_lst, name_lst)
    a.to_xlsx()
