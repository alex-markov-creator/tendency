#-*- coding: utf-8 -*-
# version 0.2a
# author: andrew.bezzubov - 07/03/2021
# email: ruizcontrol@yandex.ru, agb2019@list.ru
# https://github.com/alex-markov-creator/tendency.git
# GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""
===============================================================
help.py - здесь должна быть справка
"""
from PyQt5 import QtWidgets, QtGui

WIDTH = 640  # Ширина
HEIGHT = 480  # Высота
ICON_HELP = 'gui_icon/help.png'  # Глобальная переменная

##########################################################################
# Окно справки
##########################################################################

class HelpWhat(QtWidgets.QDialog):
    """Класс диалогового окна справки
    """
    def __init__(self, *args, **kwargs):
        super(HelpWhat, self).__init__(*args, **kwargs)
        self.setWindowTitle('Cправка')
        self.setFixedWidth(WIDTH)  # Глобальная переменная
        self.setFixedHeight(HEIGHT)  # Глобальная переменная
        self.setWindowIcon(QtGui.QIcon(ICON_HELP))  # Глобальная переменная

# Тестирование
if __name__ == "__main__":
    import sys

    ICON_HELP = '../gui_icon/help.png'  # Глобальная переменная
    app = QtWidgets.QApplication(sys.argv)
    run_about = HelpWhat()
    run_about.show()
    sys.exit(app.exec_())
