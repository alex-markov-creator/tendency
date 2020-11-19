# -*-coding: utf-8 -*-
from prettytable import PrettyTable
import settings as st


x = PrettyTable()
x.field_names = ['Разрешение экрана', 'Цвет']
x.add_row([st.screen,st.color])

if __name__ == '__main__':
    print(x)
    print(list(st.__dict__.keys()))