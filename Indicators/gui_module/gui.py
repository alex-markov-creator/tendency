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
import subprocess
import random

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

from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

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
ICON_CMD = "gui_icon/ms-dos-batch-file-icon.png" # Иконка терминального приложения
ICON_FULLSCREEN = "gui_icon/fullscreen_icon_144319.png" # Иконка режима окна
ICON_SCREEN = "gui_icon/fullscreen_exit_icon_144320.png" # Иконка режима окна

ICON_GRAPHIC_001 = "gui_icon/Documents-CardiacMonitor-icon.png" # Иконка режима окна
ICON_SAVE = "gui_icon/save_file_disk_open_searsh_loading_clipboard_1513.png" # Иконка сохранения в файл
ICON_TEST = "gui_icon/Documents-icon.png" # Иконка запуска тестов
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
        data_menu = self.menuBar().addMenu("&БД")
        process_menu = self.menuBar().addMenu("&Модули")
        preferences_menu = self.menuBar().addMenu("&Настройки")
        help_menu = self.menuBar().addMenu("&Справка")
        self.setWindowTitle("tendency v.0.2a")
        self.setMinimumSize(WIDTH, HEIGHT)
        self.ico = QtGui.QIcon(ICON_TITLE)

        #######################################################################
        # ГЛАВНОЕ МЕНЮ
        #######################################################################
        data_edit = QtWidgets.QAction(QtGui.QIcon(ICON_TEST),"Редактировать", self,
                                              shortcut=QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_T))
        data_edit.triggered.connect(self.edit_base)
        data_menu.addAction(data_edit)

        data_test = QtWidgets.QAction(QtGui.QIcon(ICON_TEST),"Запуск тестов ...", self,
                                              shortcut=QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_T))
        data_test.triggered.connect(self.test_data)
        data_menu.addAction(data_test)
        data_menu.addSeparator()

        data_exit = QtWidgets.QAction(QtGui.QIcon(ICON_FREE),"Выход ...", self,
                                              shortcut=QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_T))
        data_exit.triggered.connect(self.test_data)
        data_menu.addAction(data_exit)

        indicators_process_1 = QtWidgets.QAction(QtGui.QIcon(ICON_CMD),"Адгезия", self,
                                              shortcut=QtGui.QKeySequence(QtCore.Qt.SHIFT + QtCore.Qt.Key_1))
        indicators_process_1.triggered.connect(self.on_adhaesio)
        process_menu.addAction(indicators_process_1)


        fullscreen_action = QtWidgets.QAction(QtGui.QIcon(ICON_FULLSCREEN), "Полноэкранный режим", self,
                                              shortcut=QtGui.QKeySequence(QtCore.Qt.SHIFT + QtCore.Qt.Key_F))
        fullscreen_action.triggered.connect(self.fullscreen_run)
        preferences_menu.addAction(fullscreen_action)

        normalscreen_action = QtWidgets.QAction(QtGui.QIcon(ICON_SCREEN), "Нормальный режим", self,
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

        ######################################################################
        # ПАНЕЛЬ ИНСТРУМЕНТОВ
        ######################################################################
        toolbar_right = QtWidgets.QToolBar()
        self.addToolBar(QtCore.Qt.RightToolBarArea, toolbar_right)
        statusbar = QtWidgets.QStatusBar()
        self.setStatusBar(statusbar)
        # АДГЕЗИЯ ПИРМА-З
        btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_001), 'ПИРМА-З', self)
        btn_gr_view.triggered.connect(self.graphic_1)
        btn_gr_view.setStatusTip('Графики показателей характеризующих адгезию  ПИРМА-З')
        toolbar_right.addAction(btn_gr_view)
        # АДГЕЗИЯ ПИРМА-Л
        btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_001), 'ПИРМА-Л', self)
        btn_gr_view.triggered.connect(self.graphic_2)
        btn_gr_view.setStatusTip('Графики показателей характеризующих адгезию ПИРМА-Л')
        toolbar_right.addAction(btn_gr_view)

        # АДГЕЗИЯ ЛИТКОР-НН толщина 2.0 мм.
        btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_001), 'ЛИТКОР-НН толщина 2.0 мм', self)
        btn_gr_view.triggered.connect(self.graphic_3)
        btn_gr_view.setStatusTip('Графики показателей характеризующих адгезию ЛИТКОР-НН толщина 2.0 мм')
        toolbar_right.addAction(btn_gr_view)

        # АДГЕЗИЯ ЛИТКОР-НН толщина 1.9 мм.
        btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_001), 'ЛИТКОР-НН толщина 1.9 мм', self)
        btn_gr_view.triggered.connect(self.graphic_4)
        btn_gr_view.setStatusTip('Графики показателей характеризующих адгезию ЛИТКОР-НН толщина 1.9 мм')
        toolbar_right.addAction(btn_gr_view)

        # АДГЕЗИЯ ЛИТКОР-НН толщина 1.7 мм.
        btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_001), 'ЛИТКОР-НН толщина 1.7 мм', self)
        btn_gr_view.triggered.connect(self.graphic_5)
        btn_gr_view.setStatusTip('Графики показателей характеризующих адгезию ЛИТКОР-НН толщина 1.7 мм')
        toolbar_right.addAction(btn_gr_view)

        # АДГЕЗИЯ ЛИТКОР-НН толщина 1.0 мм.
        btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_001), 'ЛИТКОР-НН толщина 1.0 мм', self)
        btn_gr_view.triggered.connect(self.graphic_6)
        btn_gr_view.setStatusTip('Графики показателей характеризующих адгезию ЛИТКОР-НН толщина 1.0 мм')
        toolbar_right.addAction(btn_gr_view)

        # АДГЕЗИЯ ЛИТКОР-Л_тр_нефть
        btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_001), 'ЛИТКОР-Л_тр_нефть', self)
        btn_gr_view.triggered.connect(self.graphic_7)
        btn_gr_view.setStatusTip('Графики показателей характеризующих адгезию ЛИТКОР-Л для транснефти')
        toolbar_right.addAction(btn_gr_view)

        # АДГЕЗИЯ ЛИТКОР-Л_газ
        btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_001), 'ЛИТКОР-Л_газ', self)
        btn_gr_view.triggered.connect(self.graphic_8)
        btn_gr_view.setStatusTip('Графики показателей характеризующих адгезию ЛИТКОР-Л для газораспределения')
        toolbar_right.addAction(btn_gr_view)

        # АДГЕЗИЯ ЛИТКОР-З_тр_нефть
        btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_001), 'ЛИТКОР-З_тр_нефть', self)
        btn_gr_view.triggered.connect(self.graphic_9)
        btn_gr_view.setStatusTip('Графики показателей характеризующих адгезию ЛИТКОР-З для транснефти')
        toolbar_right.addAction(btn_gr_view)

        # АДГЕЗИЯ ЛИТКОР-З_газ
        btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_001), 'ЛИТКОР-З_газ', self)
        btn_gr_view.triggered.connect(self.graphic_10)
        btn_gr_view.setStatusTip('Графики показателей характеризующих адгезию ЛИТКОР-З для газораспределения')
        toolbar_right.addAction(btn_gr_view)

        # АДГЕЗИЯ БПИ толщина 2.0 мм
        btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_001), 'БПИ толщина 2.0 мм', self)
        btn_gr_view.triggered.connect(self.graphic_11)
        btn_gr_view.setStatusTip('Графики показателей характеризующих адгезию БПИ толщина 2.0 мм')
        toolbar_right.addAction(btn_gr_view)

        # АДГЕЗИЯ БПИ толщина 1.7 мм
        btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_001), 'БПИ толщина 1.7 мм', self)
        btn_gr_view.triggered.connect(self.graphic_12)
        btn_gr_view.setStatusTip('Графики показателей характеризующих адгезию БПИ толщина 1.7 мм')
        toolbar_right.addAction(btn_gr_view)

        toolbar_bottom = QtWidgets.QToolBar()
        self.addToolBar(QtCore.Qt.BottomToolBarArea, toolbar_bottom)
        statusbar = QtWidgets.QStatusBar()
        self.setStatusBar(statusbar)

        btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_FREE), 'Графики', self)
        btn_gr_view.triggered.connect(self.graphic_1)
        btn_gr_view.setStatusTip('Отобразить графики')
        toolbar_bottom.addAction(btn_gr_view)

        toolbar_top = QtWidgets.QToolBar()
        self.addToolBar(QtCore.Qt.TopToolBarArea, toolbar_top)
        statusbar = QtWidgets.QStatusBar()
        self.setStatusBar(statusbar)

        # Сохранить в файл результаты по адгезии
        btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_SAVE), 'Сохранить в файл результаты по адгезии', self)
        btn_gr_view.triggered.connect(self.save_1)
        btn_gr_view.setStatusTip('Сохранить результаты по адгезии за квартал')
        toolbar_top.addAction(btn_gr_view)

        toolbar_left = QtWidgets.QToolBar()
        self.addToolBar(QtCore.Qt.LeftToolBarArea, toolbar_left)
        statusbar = QtWidgets.QStatusBar()
        self.setStatusBar(statusbar)

        btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_FREE), 'Графики', self)
        btn_gr_view.triggered.connect(self.graphic_1)
        btn_gr_view.setStatusTip('Отобразить графики')
        toolbar_left.addAction(btn_gr_view)

        #######################################################################
        # ПОЗИЦИОНИРОВАНИЕ
        #######################################################################

        self.centralWidget = QtWidgets.QWidget()
        tab = QtWidgets.QTabWidget(self.centralWidget)
        self.setCentralWidget(tab)
        tab.addTab(TabStr(),"&Результаты расчётов")
        tab.addTab(WidgetPlot(), "&Графики")
        tab.setCurrentIndex(0)

        #######################################################################
        # Экземпляры классов для позиционирования графиков matplotlib
        #######################################################################
        """
        m = WidgetPlot()
        vbox.addWidget(self.label_1)
        vbox.addWidget(m)
        """
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

    def graphic_1(self):
        a = ad.LinearGraphic(ad._pz) # экземпляр класса линейного графика
        a.middle_value_text() # Aср
        #a.regres_graphic() # построение графика линейной регресии
        #b = ad.DistributionDiagramm(ad._pz) # экземпляр класса диаграммы распределения
        #c = ad.DistributionHistogramm(ad._pz) # экземпляр класса гистограммы распределения
        #d = ad.ErrorGraphic(ad._pz) # экземпляр класса графика погрешностей
        #e = ad.TableGraphic(ad.pz) # экземпляр класса выборки последних значений
        #f = ad.DependenceGraphic(ad._pz)
        plt.show()#график на экран

    def graphic_2(self):
        a = ad.LinearGraphic(ad._pl) # экземпляр класса линейного графика
        a.middle_value_text() # Aср
        #a.regres_graphic() # построение графика линейной регресии
        #b = ad.DistributionDiagramm(ad._pl) # экземпляр класса диаграммы распределения
        #c = ad.DistributionHistogramm(ad._pl) # экземпляр класса гистограммы распределения
        #d = ad.ErrorGraphic(ad._pl) # экземпляр класса графика погрешностей
        #e = ad.TableGraphic(ad.pl) # экземпляр класса выборки последних значений
        #f = ad.DependenceGraphic(ad._pl)
        plt.show()#график на экран

    def graphic_3(self):
        a = ad.LinearGraphic(ad._lnn_2_0) # экземпляр класса линейного графика
        a.middle_value_text() # Aср
        #a.regres_graphic() # построение графика линейной регресии
        #b = ad.DistributionDiagramm(ad._lnn_2_0) # экземпляр класса диаграммы распределения
        #c = ad.DistributionHistogramm(ad._lnn_2_0) # экземпляр класса гистограммы распределения
        #d = ad.ErrorGraphic(ad._lnn_2_0) # экземпляр класса графика погрешностей
        #e = ad.TableGraphic(ad.lnn_2_0) # экземпляр класса выборки последних значений
        #f = ad.DependenceGraphic(ad._lnn_2_0)
        plt.show()#график на экран

    def graphic_4(self):
        a = ad.LinearGraphic(ad._lnn_1_9) # экземпляр класса линейного графика
        a.middle_value_text() # Aср
        #a.regres_graphic() # построение графика линейной регресии
        #b = ad.DistributionDiagramm(ad._lnn_1_9) # экземпляр класса диаграммы распределения
        #c = ad.DistributionHistogramm(ad._lnn_1_9) # экземпляр класса гистограммы распределения
        #d = ad.ErrorGraphic(ad._lnn_1_9) # экземпляр класса графика погрешностей
        #e = ad.TableGraphic(ad.lnn_1_9) # экземпляр класса выборки последних значений
        #f = ad.DependenceGraphic(ad._lnn_1_9)
        plt.show()#график на экран

    def graphic_5(self):
        a = ad.LinearGraphic(ad._lnn_1_7) # экземпляр класса линейного графика
        a.middle_value_text() # Aср
        #a.regres_graphic() # построение графика линейной регресии
        #b = ad.DistributionDiagramm(ad._lnn_1_7) # экземпляр класса диаграммы распределения
        #c = ad.DistributionHistogramm(ad._lnn_1_7) # экземпляр класса гистограммы распределения
        #d = ad.ErrorGraphic(ad._lnn_1_7) # экземпляр класса графика погрешностей
        #e = ad.TableGraphic(ad.lnn_1_7) # экземпляр класса выборки последних значений
        #f = ad.DependenceGraphic(ad._lnn_1_7)
        plt.show()#график на экран

    def graphic_6(self):
        a = ad.LinearGraphic(ad._lnn_1_0) # экземпляр класса линейного графика
        a.middle_value_text() # Aср
        #a.regres_graphic() # построение графика линейной регресии
        #b = ad.DistributionDiagramm(ad._lnn_1_0) # экземпляр класса диаграммы распределения
        #c = ad.DistributionHistogramm(ad._lnn_1_0) # экземпляр класса гистограммы распределения
        #d = ad.ErrorGraphic(ad._lnn_1_0) # экземпляр класса графика погрешностей
        #e = ad.TableGraphic(ad.lnn_1_0) # экземпляр класса выборки последних значений
        #f = ad.DependenceGraphic(ad._lnn_1_0)
        plt.show()#график на экран

    def graphic_7(self):
        a = ad.LinearGraphic(ad._ll_tr_neft) # экземпляр класса линейного графика
        a.middle_value_text() # Aср
        #a.regres_graphic() # построение графика линейной регресии
        #b = ad.DistributionDiagramm(ad._ll_tr_neft) # экземпляр класса диаграммы распределения
        #c = ad.DistributionHistogramm(ad._ll_tr_neft) # экземпляр класса гистограммы распределения
        #d = ad.ErrorGraphic(ad._ll_tr_neft) # экземпляр класса графика погрешностей
        #e = ad.TableGraphic(ad.ll_tr_neft) # экземпляр класса выборки последних значений
        #f = ad.DependenceGraphic(ad._ll_tr_neft)
        plt.show()#график на экран

    def graphic_8(self):
        a = ad.LinearGraphic(ad._ll_gaz) # экземпляр класса линейного графика
        a.middle_value_text() # Aср
        #a.regres_graphic() # построение графика линейной регресии
        #b = ad.DistributionDiagramm(ad._ll_gaz) # экземпляр класса диаграммы распределения
        #c = ad.DistributionHistogramm(ad._ll_gaz) # экземпляр класса гистограммы распределения
        #d = ad.ErrorGraphic(ad._ll_gaz) # экземпляр класса графика погрешностей
        #e = ad.TableGraphic(ad.ll_gaz) # экземпляр класса выборки последних значений
        #f = ad.DependenceGraphic(ad._ll_gaz)
        plt.show()#график на экран

    def graphic_9(self):
        a = ad.LinearGraphic(ad._lz_tr_neft) # экземпляр класса линейного графика
        a.middle_value_text() # Aср
        #a.regres_graphic() # построение графика линейной регресии
        #b = ad.DistributionDiagramm(ad._lz_tr_neft) # экземпляр класса диаграммы распределения
        #c = ad.DistributionHistogramm(ad._lz_tr_neft) # экземпляр класса гистограммы распределения
        #d = ad.ErrorGraphic(ad._lz_tr_neft) # экземпляр класса графика погрешностей
        #e = ad.TableGraphic(ad.lz_tr_neft) # экземпляр класса выборки последних значений
        #f = ad.DependenceGraphic(ad._lz_tr_neft)
        plt.show()#график на экран

    def graphic_10(self):
        a = ad.LinearGraphic(ad._lz_gaz) # экземпляр класса линейного графика
        a.middle_value_text() # Aср
        #a.regres_graphic() # построение графика линейной регресии
        #b = ad.DistributionDiagramm(ad._lz_gaz) # экземпляр класса диаграммы распределения
        #c = ad.DistributionHistogramm(ad._lz_gaz) # экземпляр класса гистограммы распределения
        #d = ad.ErrorGraphic(ad._lz_gaz) # экземпляр класса графика погрешностей
        #e = ad.TableGraphic(ad.lz_gaz) # экземпляр класса выборки последних значений
        #f = ad.DependenceGraphic(ad._lz_gaz)
        plt.show()#график на экран

    def graphic_11(self):
        a = ad.LinearGraphic(ad._bpi_2_0) # экземпляр класса линейного графика
        a.middle_value_text() # Aср
        #a.regres_graphic() # построение графика линейной регресии
        #b = ad.DistributionDiagramm(ad._bpi_2_0) # экземпляр класса диаграммы распределения
        #c = ad.DistributionHistogramm(ad._bpi_2_0) # экземпляр класса гистограммы распределения
        #d = ad.ErrorGraphic(ad._bpi_2_0) # экземпляр класса графика погрешностей
        #e = ad.TableGraphic(ad.bpi_2_0) # экземпляр класса выборки последних значений
        #f = ad.DependenceGraphic(ad._bpi_2_0)
        plt.show()#график на экран

    def graphic_12(self):
        a = ad.LinearGraphic(ad._bpi_1_7) # экземпляр класса линейного графика
        a.middle_value_text() # Aср
        #a.regres_graphic() # построение графика линейной регресии
        #b = ad.DistributionDiagramm(ad._bpi_1_7) # экземпляр класса диаграммы распределения
        #c = ad.DistributionHistogramm(ad._bpi_1_7) # экземпляр класса гистограммы распределения
        #d = ad.ErrorGraphic(ad._bpi_1_7) # экземпляр класса графика погрешностей
        #e = ad.TableGraphic(ad.bpi_1_7) # экземпляр класса выборки последних значений
        #f = ad.DependenceGraphic(ad._bpi_1_7)
        plt.show()#график на экран

    def save_1(self):
        pass

    def on_adhaesio(self):
        #тестирование данных модулей
        os.chdir('Indicators_Process_B_7_4_and_O_8_2')
        os.startfile('adhaesio.py')

    def edit_base(self):
        pass

    def test_data(self):
        pass

###Классы содержимого вкладок
class TabStr(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        vbox = QtWidgets.QVBoxLayout()
        comboBox = QtWidgets.QComboBox()
        L = []
        for i in range(1, 11):
            L.append("Пункт {0}".format(i))
        comboBox.addItems(L)
        comboBox.activated[int].connect(self.on_clicked_view)
        x = pr.data_ur_neispr_obor_middle_year
        self.textEdit = QtWidgets.QTextEdit(f'<b>{str(x)}</b>')
        vbox.addWidget(comboBox)
        vbox.addWidget(self.textEdit)
        self.setLayout(vbox)
        self.setLayout(vbox) # передача ссылки родителю

    def on_clicked_view(self, v):
        print(v)
        print(type(v))
        if v==0:
            x = pr.data_kol_vip_prod_year
            self.textEdit.setText(f'<b>{str(x)}</b>')
        elif v ==1:
            x = 'Text'
            self.textEdit.setText(f'<b>{str(x)}</b>')
        else:
            self.textEdit.setText('Empty')


    def save_to_file(self):
        # функция сохранения в файл
        pass

### Классы встроенного matplotlib
class WidgetPlot(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.comboBox = QtWidgets.QComboBox()
        L = []
        for i in range(1, 11):
            L.append("Пункт {0}".format(i))
        self.comboBox.addItems(L)
        self.comboBox.activated[int].connect(self.on_clicked_view)
        self.canvas = PlotCanvas(self, width=10, height=8)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.layout().addWidget(self.comboBox)
        self.layout().addWidget(self.toolbar)
        self.layout().addWidget(self.canvas)

    def on_clicked_view(self, v):
        print(v)
        print(type(v))
        data = pr.data_kol_vip_prod_middle_year

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=10, height=8, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()

    def plot(self):
        data = pr.data_kol_vip_prod_year
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-', linewidth=0.5)
        ax.set_title('PyQt Matplotlib Example')
        #graphic_middle_seven = pr.Graphics_Number_Production(pr.data_number_middle_year, name= 'Количество выпущенной п/б ленты  по полугодиям')
        self.show()

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
