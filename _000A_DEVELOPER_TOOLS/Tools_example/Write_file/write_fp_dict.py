#-*- coding: utf-8 -*-
"""
write_fp_dict.py - write dict in file and read csv
"""
import shelve
from prettytable import from_csv

note_1 = {'one': 'First a note', 'two': 'Second a note'}
note_2 = {'one': 'First a note', 'two': 'Second a note'}
note_3 = {'one': 'New a note', 'two': 'new_note'}
note_4 = {'one': 'New new a note', 'two': 'new_note'}
note_5 = {'one': 'New new a note', 'two': 'new_note'}
note_6 = dict(zip('absdefghi', range(7,10)))
d = {}

d = shelve.open("d_shelve")
d['note_1'] = note_1
d['note_2'] = note_2
d['note_3'] = note_3
d['note_4'] = note_4
d['note_5'] = note_5
d['note_6'] = note_6
d.close()

file = 'temp.csv'
field_names = ['title_001,', 'title_002\n']
db = shelve.open('d_shelve')
fp = open(file,'w+' )
fp.writelines(field_names)
for key in db:
    fp.writelines(str(list(db[key].values())[0]) + ',' + str(list(db[key].values())[1]) + '\n')

fp.close()
db.close()

with open(file, 'r') as f:
    x = from_csv(f)
    print(x)
