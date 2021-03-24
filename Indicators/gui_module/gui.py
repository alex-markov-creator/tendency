#-*- coding: utf-8 -*-
# version 0.2a
# author: andrew.bezzubov - 07/03/2021
# email: ruizcontrol@yandex.ru, agb2019@list.ru
# https://github.com/alex-markov-creator/tendency.git
# GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""
===============================================================
gui.py -???.
# ПРЕДПОЛАГАЕМЫЕ ИЗМЕНЕНИЯ
# - отображение часов и даты в правой нижней позиции главного окна (QTimer и модуль time);
# - смена указателя при наведении только на область с данными - enterEvent, leaveEvent.
# ПОСЛЕДУЮЩИЕ ВЕРСИИ(варианты):
# - возможность отключения отображения времени в настройках приложения (QObject.killTimer()).
"""
import sys
import os
sys.path.append(os.path.realpath('..'))
import logging

import pandas as pd
import matplotlib.pyplot as plt
import Indicators.Indicators_Process_B_7_5.production as pr
import Indicators.Indicators_Process_B_7_2.consumer as cm
import Indicators.Indicators_Process_B_7_3.project_and_develop as pad
import Indicators.Indicators_Process_B_7_4_and_O_8_2.control_production as cp
import Indicators.Indicators_Process_B_7_4_and_O_8_2.adhaesio as ad
import Indicators.Indicators_Process_B_7_7_and_B_7_5.results as rs
import Indicators.Indicators_Process_O_6_2.people as ppl

from PyQt5 import QtCore, QtWidgets, QtGui, QtSql

from gui_module.about import AboutDialog
from gui_module.help import HelpWhat

WIDTH = 1200  # Ширина главного окна
HEIGHT = 768  # Высота главного окна

ICON_TITLE = 'gui_icon/title_icon.png'  # Иконка заголовка главного окна
ICON_ADD = "gui_icon/add.png"  # Иконка "Добавить"
ICON_EDIT = "gui_icon/edit.png"  # Иконка "Редактировать"
ICON_SEARCH = "gui_icon/search.png"  # Иконка "Поиск"
ICON_REFRESH = "gui_icon/refresh.png"  # Иконка "Обновить"
ICON_SCORE_M = "gui_icon/score_m.png"  # Иконка "Ежмесячные начисления"
ICON_SUM = "gui_icon/sum.png"  # Иконка "Ежегодные начисления"
ICON_TRASH = "gui_icon/trash.png"  # Иконка "Удалить"
ICON_CALC = "gui_icon/calc.png"  # Иконка "Общий подсчёт"
ICON_HELP = "gui_icon/help.png"  # Иконка "Справка"
ICON_ABOUT = "gui_icon/about.png"  # Иконка "О программме"
ICON_QT = "gui_icon/qt.png"  # Иконка "О Qt"

ICON_FREE = "gui_icon/free_icon.png"  # Иконка временная


##########################################################################
# ОСНОВНОЕ ОКНО
##########################################################################
class MainWindow(QtWidgets.QMainWindow):
    """Класс главного окна
    """

    def __init__(self, *args, **kwargs):
        """
        Инициализация
        """
        super(MainWindow, self).__init__(*args, **kwargs)
        #########################################################
        # ГЛАВНОЕ МЕНЮ И ТИТУЛЬНЫЙ ЗАГОЛОВОК
        #########################################################
        # file_menu = self.menuBar().addMenu("&Файл") # МЕНЮ ФАЙЛ -- ВРЕМЕННО ОТКЛЮЧЕНО ДО ПОСЛЕДУЮЩИХ ВЕРСИЙ
        process_menu = self.menuBar().addMenu("&Процессы")
        preferences_menu = self.menuBar().addMenu("&Настройки")
        help_menu = self.menuBar().addMenu("&Справка")
        self.setWindowTitle("tendency v.0.2a")
        self.setMinimumSize(WIDTH, HEIGHT)
        self.ico = QtGui.QIcon(ICON_TITLE)

        #######################################################################
        # ГЛАВНОЕ МЕНЮ
        #######################################################################
        indicators_process_1 = QtWidgets.QAction("Процесс_1", self,
                                              shortcut=QtGui.QKeySequence(QtCore.Qt.SHIFT + QtCore.Qt.Key_1))
        indicators_process_1.triggered.connect(self.loaddata)
        process_menu.addAction(indicators_process_1)


        fullscreen_action = QtWidgets.QAction(QtGui.QIcon(ICON_FREE), "Полноэкранный режим", self,
                                              shortcut=QtGui.QKeySequence(QtCore.Qt.SHIFT + QtCore.Qt.Key_F))
        fullscreen_action.triggered.connect(self.fullscreen_run)
        preferences_menu.addAction(fullscreen_action)

        normalscreen_action = QtWidgets.QAction(QtGui.QIcon(ICON_FREE), "Нормальный режим", self,
                                                shortcut=QtGui.QKeySequence(QtCore.Qt.SHIFT + QtCore.Qt.Key_N))
        normalscreen_action.triggered.connect(self.normalscreen_run)
        preferences_menu.addAction(normalscreen_action)

        help_action = QtWidgets.QAction(QtGui.QIcon(ICON_HELP), "Что делать?", self,
                                        shortcut=QtGui.QKeySequence(QtCore.Qt.Key_F1))
        help_action.triggered.connect(self.help)
        help_menu.addAction(help_action)

        about_action = QtWidgets.QAction(QtGui.QIcon(ICON_ABOUT), "О программе", self)
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)
        help_menu.addSeparator()

        qt_action = QtWidgets.QAction(QtGui.QIcon(ICON_QT), "О Qt...", self)
        qt_action.triggered.connect(self.qt)
        help_menu.addAction(qt_action)
        #######################################################################
        # ПОЗИЦИОНИРОВАНИЕ
        #######################################################################
        self.centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralWidget)
        self.vbox = QtWidgets.QVBoxLayout()
        vbox = QtWidgets.QVBoxLayout(self.centralWidget)
        self.label_1 = QtWidgets.QPushButton("Кнопка")
        self.label_1.clicked.connect(self.on_clicked_button1)
        x = pr.data_ur_neispr_obor_middle_year
        textEdit = QtWidgets.QTextEdit(f'<b>{str(x)}</b>')
        #self.label_2.setAlignment(QtCore.Qt.AlignHCenter)
        vbox.addWidget(self.label_1)
        vbox.addWidget(textEdit)
        #######################################################################
        # ФУНКЦИИ ВЫПОЛНЕНИЯ КОМАНД
        #######################################################################

    def loaddata(self):
        pass

    def fullscreen_run(self):
        self.showFullScreen()  # полноэкранный режим

    def normalscreen_run(self):
        self.showNormal()  # полноэкранный режим

    def help(self):  # Функция окна справки - временное решение
        dlg = HelpWhat()
        dlg.exec_()

    def about(self):  # Функция - ссылка на класс окна "О программе" - меню
        dlg = AboutDialog()
        dlg.exec_()

    def qt(self):  # Функция - ссылка на класс окна "О Qt" - меню
        QtWidgets.QMessageBox.aboutQt(self, title="О библиотеке Qt")

    def closeEvent(self, e):
        result = QtWidgets.QMessageBox.question(self,
                                                "Подтверждение выхода из приложения",
                                                "Вы действительно хотите выйти из приложения?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            e.accept()
            QtWidgets.QWidget.closeEvent(self, e)
        else:
            e.ignore()

    def on_clicked_button1(self):
        a = pr.Graphics_Indicators_Production(pr.data_ur_neispr_obor_year, name= 'Уровень неисправности оборудования по годам')
        b = pr.Graphics_Indicators_Production(pr.data_ur_neispr_obor_middle_year, name= 'Уровень неисправности оборудования по полугодиям')
        c = pr.Graphics_Indicators_Production(pr.data_ur_nesoot_prod_year, name= 'Уровень несоответствующей продукции по годам')
        d = pr.Graphics_Indicators_Production(pr.data_ur_nesoot_prod_middle_year, name= 'Уровень несоответствующей продукции по полугодиям')
        e = pr.Graphics_Indicators_Production(pr.data_ur_teh_oth_year, name= 'Уровень техотходов по годам', critery=2)
        f = pr.Graphics_Indicators_Production(pr.data_ur_teh_oth_middle_year, name= 'Уровень техотходов по полугодиям', critery=2)
        plt.show()



# Тестирование
##############
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ICON_ADD = "../gui_icon/add.png"
    ICON_EDIT = "../gui_icon/edit.png"
    ICON_SEARCH = "../gui_icon/search.png"
    ICON_REFRESH = "../gui_icon/refresh.png"
    ICON_SCORE_M = "../gui_icon/score_m.png"
    ICON_SUM = "../gui_icon/sum.png"
    ICON_TRASH = "../gui_icon/trash.png"
    ICON_CALC = "../gui_icon/calc.png"
    ICON_HELP = "../gui_icon/help.png"
    ICON_ABOUT = "../gui_icon/about.png"
    ICON_QT = "../gui_icon/qt.png"


    run_about = MainWindow()
    #run_test = MyTest()
    #run_test.show()
    run_about.show()
    sys.exit(app.exec_())
