#-*- coding: utf-8 -*-
"""
to_xlsx.py - custom converter to *.xlsx
"""
import os
import glob
import csv
from xlsxwriter.workbook import Workbook # pip install xlsxwriter

def convert():
    for csvfile in glob.glob(os.path.join('.', '*.csv')):
        workbook = Workbook(csvfile[:-4] + '.xlsx')
        worksheet = workbook.add_worksheet('test')
        with open(csvfile, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    worksheet.write(r,c,col)
        workbook.close()

if __name__ == '__main__':
    convert()

