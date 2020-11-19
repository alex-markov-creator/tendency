#-*- coding: utf-8 -*-
"""
write_fp_str.py - write str in file and read csv
"""
import shelve
from prettytable import from_csv


one = 'First a note'
two = 'Second a note'
tree = 'New a note'
four = 'New new a note'


d = shelve.open("d_shelve")
d['one'] = one
d['two'] = two
d['three'] = tree
d['four'] = four
d.close()

file = 'temp.csv'
field_names = ['title_001,', 'title_002\n']
db = shelve.open('d_shelve')
fp = open(file,'w+' )
fp.writelines(field_names)
for key in db:
    fp.writelines(key + ',' + db[key] + '\n')
    print(key + '-->', db[key])

fp.close()
db.close()

with open(file, 'r') as f:
    x = from_csv(f)
    print(x)
