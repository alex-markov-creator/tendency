#-*- coding: utf-8 -*-
# version 0.2a
# author: andrew.bezzubov - 07/03/2021
# email: ruizcontrol@yandex.ru, agb2019@list.ru
# https://github.com/alex-markov-creator/tendency.git
# GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""
===============================================================
# ПРЕДПОЛАГАЕМЫЕ ИЗМЕНЕНИЯ
"""
import sys
import os
import platform # информация о версии оси
#-------------------------------------------------------
# модуль для логирования(журналирования)
import logging
import logging.config # файл конфигурации
import logging.handlers # ротация логов
import traceback # трасировка сообщений об исключениях
#-------------------------------------------------------
# модуль для тестирования
import pytest
#-------------------------------------------------------
sys.path.append(os.path.realpath('..'))
import subprocess
import random

logging.config.fileConfig('logging.conf') # файл конфигурации
logger = logging.getLogger('indicators.gui_module') # возвращает объект логгера
logger.info(f'Started on platform {platform.platform()}') # logging

import pandas as pd
import matplotlib.pyplot as plt
import Indicators.Indicators_Process_B_7_5.production as pr
import Indicators.Indicators_Process_B_7_2.consumer as cm
import Indicators.Indicators_Process_B_7_3.project_and_develop as pad
import Indicators.Indicators_Process_B_7_4_and_O_8_2.control_production as cp
import Indicators.Indicators_Process_B_7_4_and_O_8_2.adhaesio as ad
import Indicators.Indicators_Process_B_7_7_and_B_7_5.results as rs
import Indicators.Indicators_Process_O_6_2.people as ppl

from PyQt5 import QtCore, QtWidgets, QtGui, QtSql, QtPrintSupport

from gui_module.about import AboutDialog
from gui_module.help import HelpWhat

from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

import string # модуль для работы с шаблонами
import jinja2 # модуль для работы с шаблонами

logger.info("Import OK!!!") # logging

try:
    logger.info("start initial assignment") # logging
    WIDTH = 1200  # Ширина главного окна
    HEIGHT = 800  # Высота главного окна

    ICON_TITLE = 'gui_icon/title_icon.png'  # Icon заголовка главного окна
    ICON_ADD = "gui_icon/add.png"  # Icon "Добавить"
    ICON_EDIT = "gui_icon/edit.png"  # Icon "Редактировать"
    ICON_SEARCH = "gui_icon/search.png"  # Icon "Поиск"
    ICON_REFRESH = "gui_icon/refresh.png"  # Icon "Обновить"
    ICON_SCORE_M = "gui_icon/score_m.png"  # Icon "Ежмесячные начисления"
    ICON_SUM = "gui_icon/sum.png"  # Icon "Ежегодные начисления"
    ICON_TRASH = "gui_icon/trash.png"  # Icon "Удалить"
    ICON_CALC = "gui_icon/calc.png"  # Icon "Общий подсчёт"
    ICON_HELP = "gui_icon/help.png"  # Icon "Справка"
    ICON_ABOUT = "gui_icon/about.png"  # Icon "О программме"
    ICON_QT = "gui_icon/qt.png"  # Icon "О Qt"

    ICON_FREE = "gui_icon/free_icon.png"  # Icon временная
    ICON_CMD = "gui_icon/ms-dos-batch-file-icon.png" # Icon терминального приложения
    ICON_FULLSCREEN = "gui_icon/fullscreen_icon_144319.png" # Icon режима окна
    ICON_SCREEN = "gui_icon/fullscreen_exit_icon_144320.png" # Icon режима окна

    ICON_GRAPHIC_001 = "gui_icon/Documents-CardiacMonitor-icon.png" # Icon режима окна
    ICON_GRAPHIC_002 = "gui_icon/line_chart_analysis_icon_183298.png" # Icon режима окна
    ICON_GRAPHIC_003 = "gui_icon/area_chart_icon_183308.png" # Icon режима окна
    ICON_GRAPHIC_004 = "gui_icon/Document-Chart-icon.png" # Icon режима окна
    ICON_GRAPHIC_005 = "gui_icon/5.png" # Icon режима окна
    ICON_GRAPHIC_006 = "gui_icon/Chart_icon-icons.com_51184.png" # Icon режима окна

    ICON_SAVE = "gui_icon/save_file_disk_open_searsh_loading_clipboard_1513.png" # Icon сохранения в файл
    ICON_PNG = "gui_icon/File-PNG-icon.png" # Icon сохранения в файл png
    ICON_TEST = "gui_icon/Documents-icon.png" # Icon запуска тестов
    ICON_EDIT_DATA_1 = "gui_icon/dossier-ardoise-documents-icon.png" # Icon редактирования БД
    ICON_EDIT_DATA_2 = "gui_icon/Document-icon.png" # Icon редактирования БД
    ICON_EDIT_DATA_3 = "gui_icon/Blue-Documents-icon.png" # Icon редактирования БД
    logger.info('OK! end initial assignment ') # logging

except:
    logger.error(f'FAILED! Data_Launch_Error: {sys.exc_info()[:2]}', exc_info=True) # logging

##########################################################################
# ОСНОВНОЕ ОКНО
##########################################################################
try:
    class MainWindow(QtWidgets.QMainWindow):
        """Класс главного окна
        """
        def __init__(self, *args, **kwargs):
            """
            Инициализация
            """
            super(MainWindow, self).__init__(*args, **kwargs)
            self.logger = logging.getLogger('indicators.gui_module.MainWindow')
            self.logger.info('__Init__ MainWindow')
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

            data_edit = data_menu.addMenu("&Редактировать")

            data_indicators = QtWidgets.QAction(QtGui.QIcon(ICON_EDIT_DATA_2),"&Показатели процессов", self,
                                                  shortcut=QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_1))
            data_indicators.triggered.connect(self.edit_indicators)

            data_incoming_control = QtWidgets.QAction(QtGui.QIcon(ICON_EDIT_DATA_3),"&Входной контроль", self,
                                                  shortcut=QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_2))
            data_incoming_control.triggered.connect(self.control_incoming)

            data_adhaesio = QtWidgets.QAction(QtGui.QIcon(ICON_EDIT_DATA_1),"&Контроль готовой продукции", self,
                                                  shortcut=QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_3))
            data_adhaesio.triggered.connect(self.adhaesio_data)

            data_edit.addAction(data_indicators)
            data_edit.addAction(data_incoming_control)
            data_edit.addAction(data_adhaesio)

            data_test = QtWidgets.QAction(QtGui.QIcon(ICON_TEST),"&Запуск тестов ...", self,
                                                  shortcut=QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_T))
            data_test.triggered.connect(self.test_data)
            data_menu.addAction(data_test)
            data_menu.addSeparator()

            data_exit = QtWidgets.QAction(QtGui.QIcon(ICON_FREE),"Выход ...", self,
                                                  shortcut=QtGui.QKeySequence(QtCore.Qt.ALT + QtCore.Qt.Key_F4))
            data_exit.triggered.connect(self.test_data)
            data_menu.addAction(data_exit)

            self.indicators_process_1 = QtWidgets.QAction(QtGui.QIcon(ICON_CMD),"adhaesio.py", self,
                                                  shortcut=QtGui.QKeySequence(QtCore.Qt.SHIFT + QtCore.Qt.Key_1))
            self.indicators_process_1.triggered.connect(self.on_adhaesio)
            process_menu.addAction(self.indicators_process_1)

            self.indicators_process_2 = QtWidgets.QAction(QtGui.QIcon(ICON_CMD),"production.py", self,
                                                  shortcut=QtGui.QKeySequence(QtCore.Qt.SHIFT + QtCore.Qt.Key_2))
            self.indicators_process_2.triggered.connect(self.on_production)
            process_menu.addAction(self.indicators_process_2)


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

             # АДГЕЗИЯ ПИРМА-З (ВЫБОРКА)
            btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_002), 'ПИРМА-З', self)
            btn_gr_view.triggered.connect(self.graphic_13)
            btn_gr_view.setStatusTip('Выборка последних n значений ПИРМА-З')
            toolbar_right.addAction(btn_gr_view)

            # АДГЕЗИЯ ПИРМА-Л
            btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_001), 'ПИРМА-Л', self)
            btn_gr_view.triggered.connect(self.graphic_2)
            btn_gr_view.setStatusTip('Графики показателей характеризующих адгезию ПИРМА-Л')
            toolbar_right.addAction(btn_gr_view)

            # АДГЕЗИЯ ПИРМА-Л (ВЫБОРКА)
            btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_002), 'ПИРМА-Л', self)
            btn_gr_view.triggered.connect(self.graphic_14)
            btn_gr_view.setStatusTip('Выборка последних n значений ПИРМА-Л')
            toolbar_right.addAction(btn_gr_view)

            # АДГЕЗИЯ ЛИТКОР-НН толщина 2.0 мм.
            btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_001), 'ЛИТКОР-НН толщина 2.0 мм', self)
            btn_gr_view.triggered.connect(self.graphic_3)
            btn_gr_view.setStatusTip('Графики показателей характеризующих адгезию ЛИТКОР-НН толщина 2.0 мм')
            toolbar_right.addAction(btn_gr_view)

            # АДГЕЗИЯ ЛИТКОР-НН толщина 2.0 мм. (ВЫБОРКА)
            btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_002), 'ЛИТКОР-НН толщина 2.0 мм', self)
            btn_gr_view.triggered.connect(self.graphic_15)
            btn_gr_view.setStatusTip('Выборка последних n значений ЛИТКОР-НН толщина 2.0 мм')
            toolbar_right.addAction(btn_gr_view)

            # АДГЕЗИЯ ЛИТКОР-НН толщина 1.9 мм.
            btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_001), 'ЛИТКОР-НН толщина 1.9 мм', self)
            btn_gr_view.triggered.connect(self.graphic_4)
            btn_gr_view.setStatusTip('Графики показателей характеризующих адгезию ЛИТКОР-НН толщина 1.9 мм')
            toolbar_right.addAction(btn_gr_view)

            # АДГЕЗИЯ ЛИТКОР-НН толщина 1.9 мм. (ВЫБОРКА)
            btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_002), 'ЛИТКОР-НН толщина 1.9 мм', self)
            btn_gr_view.triggered.connect(self.graphic_16)
            btn_gr_view.setStatusTip('Выборка последних n значений ЛИТКОР-НН толщина 1.9 мм')
            toolbar_right.addAction(btn_gr_view)

            # АДГЕЗИЯ ЛИТКОР-НН толщина 1.7 мм.
            btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_001), 'ЛИТКОР-НН толщина 1.7 мм', self)
            btn_gr_view.triggered.connect(self.graphic_5)
            btn_gr_view.setStatusTip('Графики показателей характеризующих адгезию ЛИТКОР-НН толщина 1.7 мм')
            toolbar_right.addAction(btn_gr_view)

            # АДГЕЗИЯ ЛИТКОР-НН толщина 1.7 мм. (ВЫБОРКА)
            btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_002), 'ЛИТКОР-НН толщина 1.7 мм', self)
            btn_gr_view.triggered.connect(self.graphic_17)
            btn_gr_view.setStatusTip('Выборка последних n значений ЛИТКОР-НН толщина 1.7 мм')
            toolbar_right.addAction(btn_gr_view)

            # АДГЕЗИЯ ЛИТКОР-НН толщина 1.0 мм.
            btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_001), 'ЛИТКОР-НН толщина 1.0 мм', self)
            btn_gr_view.triggered.connect(self.graphic_6)
            btn_gr_view.setStatusTip('Графики показателей характеризующих адгезию ЛИТКОР-НН толщина 1.0 мм')
            toolbar_right.addAction(btn_gr_view)

            # АДГЕЗИЯ ЛИТКОР-НН толщина 1.0 мм. (ВЫБОРКА)
            btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_002), 'ЛИТКОР-НН толщина 1.0 мм', self)
            btn_gr_view.triggered.connect(self.graphic_18)
            btn_gr_view.setStatusTip('Выборка последних n значений ЛИТКОР-НН толщина 1.0 мм')
            toolbar_right.addAction(btn_gr_view)

            # АДГЕЗИЯ ЛИТКОР-Л_тр_нефть
            btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_001), 'ЛИТКОР-Л_тр_нефть', self)
            btn_gr_view.triggered.connect(self.graphic_7)
            btn_gr_view.setStatusTip('Графики показателей характеризующих адгезию ЛИТКОР-Л для транснефти')
            toolbar_right.addAction(btn_gr_view)

            # АДГЕЗИЯ ЛИТКОР-Л_тр_нефть (ВЫБОРКА)
            btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_002), 'ЛИТКОР-Л_тр_нефть', self)
            btn_gr_view.triggered.connect(self.graphic_19)
            btn_gr_view.setStatusTip('Выборка последних n значений ЛИТКОР-Л для транснефти')
            toolbar_right.addAction(btn_gr_view)

            # АДГЕЗИЯ ЛИТКОР-Л_газ
            btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_001), 'ЛИТКОР-Л_газ', self)
            btn_gr_view.triggered.connect(self.graphic_8)
            btn_gr_view.setStatusTip('Графики показателей характеризующих адгезию ЛИТКОР-Л для газораспределения')
            toolbar_right.addAction(btn_gr_view)

            # АДГЕЗИЯ ЛИТКОР-Л_газ (ВЫБОРКА)
            btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_002), 'ЛИТКОР-Л_газ', self)
            btn_gr_view.triggered.connect(self.graphic_20)
            btn_gr_view.setStatusTip('Выборка последних n значений ЛИТКОР-Л для газораспределения')
            toolbar_right.addAction(btn_gr_view)

            # АДГЕЗИЯ ЛИТКОР-З_тр_нефть
            btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_001), 'ЛИТКОР-З_тр_нефть', self)
            btn_gr_view.triggered.connect(self.graphic_9)
            btn_gr_view.setStatusTip('Графики показателей характеризующих адгезию ЛИТКОР-З для транснефти')
            toolbar_right.addAction(btn_gr_view)

            # АДГЕЗИЯ ЛИТКОР-З_тр_нефть (ВЫБОРКА)
            btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_002), 'ЛИТКОР-З_тр_нефть', self)
            btn_gr_view.triggered.connect(self.graphic_21)
            btn_gr_view.setStatusTip('Выборка последних n значений ЛИТКОР-З для транснефти')
            toolbar_right.addAction(btn_gr_view)

            # АДГЕЗИЯ ЛИТКОР-З_газ
            btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_001), 'ЛИТКОР-З_газ', self)
            btn_gr_view.triggered.connect(self.graphic_10)
            btn_gr_view.setStatusTip('Графики показателей характеризующих адгезию ЛИТКОР-З для газораспределения')
            toolbar_right.addAction(btn_gr_view)

            # АДГЕЗИЯ ЛИТКОР-З_газ (ВЫБОРКА)
            btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_002), 'ЛИТКОР-З_газ', self)
            btn_gr_view.triggered.connect(self.graphic_22)
            btn_gr_view.setStatusTip('Выборка последних n значений ЛИТКОР-З для газораспределения')
            toolbar_right.addAction(btn_gr_view)

            # АДГЕЗИЯ БПИ толщина 2.0 мм
            btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_001), 'БПИ толщина 2.0 мм', self)
            btn_gr_view.triggered.connect(self.graphic_11)
            btn_gr_view.setStatusTip('Графики показателей характеризующих адгезию БПИ толщина 2.0 мм')
            toolbar_right.addAction(btn_gr_view)

            # АДГЕЗИЯ БПИ толщина 2.0 мм (ВЫБОРКА)
            btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_002), 'БПИ толщина 2.0 мм', self)
            btn_gr_view.triggered.connect(self.graphic_23)
            btn_gr_view.setStatusTip('Выборка последних n значений БПИ толщина 2.0 мм')
            toolbar_right.addAction(btn_gr_view)

            # АДГЕЗИЯ БПИ толщина 1.7 мм
            btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_001), 'БПИ толщина 1.7 мм', self)
            btn_gr_view.triggered.connect(self.graphic_12)
            btn_gr_view.setStatusTip('Графики показателей характеризующих адгезию БПИ толщина 1.7 мм')
            toolbar_right.addAction(btn_gr_view)

            # АДГЕЗИЯ БПИ толщина 1.7 мм (ВЫБОРКА)
            btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_GRAPHIC_002), 'БПИ толщина 1.7 мм', self)
            btn_gr_view.triggered.connect(self.graphic_24)
            btn_gr_view.setStatusTip('Выборка последних n значений БПИ толщина 1.7 мм')
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
            toolbar_top.setIconSize(QtCore.QSize(60,60))
            self.addToolBar(QtCore.Qt.TopToolBarArea, toolbar_top)
            statusbar = QtWidgets.QStatusBar()
            self.setStatusBar(statusbar)

            # Сохранить в файл результаты по адгезии
            btn_gr_view = QtWidgets.QAction(QtGui.QIcon(ICON_SAVE), 'Сохранить в файл результаты по адгезии', self)
            btn_gr_view_1 = QtWidgets.QAction(QtGui.QIcon(ICON_PNG), 'Сохранить в файл результаты по адгезии за квартал', self)
            btn_gr_view.triggered.connect(self.save_1)
            btn_gr_view_1.triggered.connect(self.save_2)
            btn_gr_view.setStatusTip('Сохранить результаты по адгезии')
            btn_gr_view.setStatusTip('Сохранить результаты по адгезии за квартал')
            toolbar_top.addAction(btn_gr_view)
            toolbar_top.addAction(btn_gr_view_1)

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
            self.tab_1 = QtWidgets.QScrollArea()
            self.tab_1.setWidgetResizable(True)
            tab.addTab(View_Process_Graphics(), "Графики показателей &процессов")
            tab.addTab(TabStr(),"&Сводные данные результатов расчётов")
            tab.addTab(self.tab_1, "Графики показателей &адгезии")
            tab.addTab(WidgetPlot(),"&Количество выпущенной п/б ленты")
            tab.setCurrentIndex(2)
            self.setCentralWidget(tab)
            content_widget = View_Adhaesio_Graphics()
            self.tab_1.setWidget(content_widget)

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
            plt.show()#график на экран

        def graphic_2(self):
            a = ad.LinearGraphic(ad._pl) # экземпляр класса линейного графика
            a.middle_value_text() # Aср
            plt.show()#график на экран

        def graphic_3(self):
            a = ad.LinearGraphic(ad._lnn_2_0) # экземпляр класса линейного графика
            a.middle_value_text() # Aср
            plt.show()#график на экран

        def graphic_4(self):
            a = ad.LinearGraphic(ad._lnn_1_9) # экземпляр класса линейного графика
            a.middle_value_text() # Aср
            plt.show()#график на экран

        def graphic_5(self):
            a = ad.LinearGraphic(ad._lnn_1_7) # экземпляр класса линейного графика
            a.middle_value_text() # Aср
            plt.show()#график на экран

        def graphic_6(self):
            a = ad.LinearGraphic(ad._lnn_1_0) # экземпляр класса линейного графика
            a.middle_value_text() # Aср
            plt.show()#график на экран

        def graphic_7(self):
            a = ad.LinearGraphic(ad._ll_tr_neft) # экземпляр класса линейного графика
            a.middle_value_text() # Aср
            plt.show()#график на экран

        def graphic_8(self):
            a = ad.LinearGraphic(ad._ll_gaz) # экземпляр класса линейного графика
            a.middle_value_text() # Aср
            plt.show()#график на экран

        def graphic_9(self):
            a = ad.LinearGraphic(ad._lz_tr_neft) # экземпляр класса линейного графика
            a.middle_value_text() # Aср
            plt.show()#график на экран

        def graphic_10(self):
            a = ad.LinearGraphic(ad._lz_gaz) # экземпляр класса линейного графика
            a.middle_value_text() # Aср
            plt.show()#график на экран

        def graphic_11(self):
            a = ad.LinearGraphic(ad._bpi_2_0) # экземпляр класса линейного графика
            a.middle_value_text() # Aср
            plt.show()#график на экран

        def graphic_12(self):
            a = ad.LinearGraphic(ad._bpi_1_7) # экземпляр класса линейного графика
            a.middle_value_text() # Aср
            plt.show()#график на экран

        def graphic_13(self):
            e = ad.TableGraphic(ad.pz) # экземпляр класса выборки последних значений
            plt.show()#график на экран

        def graphic_14(self):
            e = ad.TableGraphic(ad.pl) # экземпляр класса выборки последних значений
            plt.show()#график на экран

        def graphic_15(self):
            e = ad.TableGraphic(ad.lnn_2_0) # экземпляр класса выборки последних значений
            plt.show()#график на экран

        def graphic_16(self):
            e = ad.TableGraphic(ad.lnn_1_9) # экземпляр класса выборки последних значений
            plt.show()#график на экран

        def graphic_17(self):
            e = ad.TableGraphic(ad.lnn_1_7) # экземпляр класса выборки последних значений
            plt.show()#график на экран

        def graphic_18(self):
            e = ad.TableGraphic(ad.lnn_1_0) # экземпляр класса выборки последних значений
            plt.show()#график на экран

        def graphic_19(self):
            e = ad.TableGraphic(ad.ll_tr_neft) # экземпляр класса выборки последних значений
            plt.show()#график на экран

        def graphic_20(self):
            e = ad.TableGraphic(ad.ll_gaz) # экземпляр класса выборки последних значений
            plt.show()#график на экран

        def graphic_21(self):
            e = ad.TableGraphic(ad.lz_tr_neft) # экземпляр класса выборки последних значений
            plt.show()#график на экран

        def graphic_22(self):
            e = ad.TableGraphic(ad.lz_gaz) # экземпляр класса выборки последних значений
            plt.show()#график на экран

        def graphic_23(self):
            e = ad.TableGraphic(ad.bpi_2_0) # экземпляр класса выборки последних значений
            plt.show()#график на экран

        def graphic_24(self):
            e = ad.TableGraphic(ad.bpi_1_7) # экземпляр класса выборки последних значений
            plt.show()#график на экран

        def save_1(self):
            result = QtWidgets.QMessageBox.question(self,
                                                    "Подтверждение действия",
                                                    "Вы действительно хотите сохранить данные в файл?",
                                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                    QtWidgets.QMessageBox.No)
            if result == QtWidgets.QMessageBox.Yes:
                os.chdir('Indicators_Process_B_7_4_and_O_8_2')
                for i in ad._lst_adhaesio:
                    ad.Save_Data(i)
            else:
                pass

        def save_2(self):
            result = QtWidgets.QMessageBox.question(self,
                                                    "Подтверждение действия",
                                                    "Вы действительно хотите сохранить данные в файл?",
                                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                    QtWidgets.QMessageBox.No)
            if result == QtWidgets.QMessageBox.Yes:
                os.chdir('Indicators_Process_B_7_4_and_O_8_2')
                for i in ad.lst_adhaesio:
                    ad.Save_add_Data(i)
            else:
                pass


        def on_adhaesio(self):
            #тестирование данных модулей
            os.chdir('Indicators_Process_B_7_4_and_O_8_2')
            os.startfile('adhaesio.py')
            sys.exit(app.exec_())


        def on_production(self):
            #тестирование данных модулей
            os.chdir('Indicators_Process_B_7_5')
            os.startfile('production.py')
            sys.exit(app.exec_())

        def edit_base(self):
            pass

        def edit_indicators(self):
            pass

        def control_incoming(self):
            pass

        def adhaesio_data(self):
            pass

        def test_data(self):
            pass

    logger.info("OK! Load object class") # logging

except Exception:
    logger.error(f'FAILED! MainWindow_Error: {sys.exc_info()[:2]}') # logging

###Классы содержимого вкладок
try:
    class TabStr(QtWidgets.QWidget):
        def __init__(self):
            super().__init__()
            self.logger = logging.getLogger('indicators.gui_module.TabStr')
            self.logger.info('__Init__ TabStr')
            vbox = QtWidgets.QVBoxLayout()
            button_save = QtWidgets.QPushButton("Сохранить в *.pdf")
            button_save.clicked.connect(self.on_clicked_save_to_pdf)
            comboBox = QtWidgets.QComboBox()
            L = []
            L.append('Сводные данные за год')
            L.append('Сводные данные за полугодие')
            L.append('Процесс Б(7.5) "Производство продукции"')
            L.append('Процесс Б(7.5) "Производство продукции" - полугодие')
            for i in range(5, 23):
                L.append("Пункт {0}".format(i))
            comboBox.addItems(L)
            comboBox.activated[int].connect(self.on_clicked_view)
            x = 'Выберите пункт'
            self.textEdit = QtWidgets.QTextEdit(f'<b>{str(x)}</b>')
            vbox.addWidget(comboBox)
            vbox.addWidget(self.textEdit)
            vbox.addWidget(button_save)
            self.setLayout(vbox)
            self.setLayout(vbox) # передача ссылки родителю

        def on_clicked_view(self, v):
            try:
                if v==0:
                    x = 'Text'
                    self.textEdit.setText(f'<b>{str(x)}</b>')

                elif v ==2:
                    templateLoader = jinja2.FileSystemLoader(searchpath='./')
                    templateEnv = jinja2.Environment(loader=templateLoader)
                    TEMPLATE_FILE = 'process_b_7_5.html'
                    template = templateEnv.get_template(TEMPLATE_FILE)
                    x = template.render(
                        NAME_TABLE='Сводные данные за год: Процесс Б(7.5) "Производство продукции"',
                        PREV_YEAR = pr.prev_year,
                        NEXT_YEAR = pr.next_year,

                        n_13 = pr.n_13,# нумерация строк
                        n_14 = pr.n_14,# нумерация строк
                        n_15 = pr.n_15,# нумерация строк
                        n_16 = pr.n_16,# нумерация строк
                        n_17 = pr.n_17,# нумерация строк
                        n_18 = pr.n_18,# нумерация строк
                        n_19 = pr.n_19,# нумерация строк
                        n_20 = pr.n_20,# нумерация строк
                        # переменные уровня несоответствующей продукции
                        i_13_1_1 = pr.i_13_1_1,
                        i_13_2_1 = pr.i_13_2_1,
                        # переменные количества выпускаемой продукции
                        i_14_1_1 = pr.i_14_1_1,
                        i_14_1_2 = pr.i_14_1_2,
                        i_14_1_3 = pr.i_14_1_3,
                        i_14_1_4 = pr.i_14_1_4,
                        i_14_1_5 = pr.i_14_1_5,
                        i_14_2_1 = pr.i_14_2_1,
                        i_14_2_2 = pr.i_14_2_2,
                        i_14_2_3 = pr.i_14_2_3,
                        i_14_2_4 = pr.i_14_2_4,
                        i_14_2_5 = pr.i_14_2_5,
                        # переменные уровня расхода материала
                        i_15_1 = pr.i_15_1,
                        i_15_2 = pr.i_15_2,
                        # переменные уровня технических отходов
                        i_16_1 = pr.i_16_1,
                        i_16_2 = pr.i_16_2,
                        # переменные уровня неисправности оборудования
                        i_17_1 = pr.i_17_1,
                        i_17_2 = pr.i_17_2,
                        # переменные уровня простоя оборудования из-за качества
                        i_18_1 = pr.i_18_1,
                        i_18_2 = pr.i_18_2,
                        # переменные уровня простоя оборудования из-за непоставок
                        i_19_1 = pr.i_19_1,
                        i_19_2 = pr.i_19_2,
                        # переменные уровня отклонений продукции
                        i_20_1 = pr.i_20_1,
                        i_20_2 = pr.i_20_2,

                        NAME_TABLE_2='Изменение значений за год: Процесс Б(7.5) "Производство продукции"',


                        )
                    document = QtGui.QTextDocument()
                    document.setHtml(x)
                    self.textEdit.setDocument(document)

                elif v ==3:
                    templateLoader = jinja2.FileSystemLoader(searchpath='./')
                    templateEnv = jinja2.Environment(loader=templateLoader)
                    TEMPLATE_FILE = 'process_b_7_5.html'
                    template = templateEnv.get_template(TEMPLATE_FILE)
                    x = template.render(
                        NAME_TABLE='Сводные данные за полугодие: Процесс Б(7.5) "Производство продукции"',
                        PREV_YEAR = pr.prev_year,
                        NEXT_YEAR = pr.next_year,

                        n_13 = pr.n_13,# нумерация строк
                        n_14 = pr.n_14,# нумерация строк
                        n_15 = pr.n_15,# нумерация строк
                        n_16 = pr.n_16,# нумерация строк
                        n_17 = pr.n_17,# нумерация строк
                        n_18 = pr.n_18,# нумерация строк
                        n_19 = pr.n_19,# нумерация строк
                        n_20 = pr.n_20,# нумерация строк
                        # переменные уровня несоответствующей продукции
                        i_13_1_m_1 = pr.i_13_1_m_1,
                        i_13_2_m_1 = pr.i_13_2_m_1,
                        # переменные количества выпускаемой продукции
                        i_14_1_m_1 = pr.i_14_1_m_1,
                        i_14_1_m_2 = pr.i_14_1_m_2,
                        i_14_1_m_3 = pr.i_14_1_m_3,
                        i_14_1_m_4 = pr.i_14_1_m_4,
                        i_14_1_m_5 = pr.i_14_1_m_5,

                        i_14_2_m_1 = pr.i_14_2_m_1,
                        i_14_2_m_2 = pr.i_14_2_m_2,
                        i_14_2_m_3 = pr.i_14_2_m_3,
                        i_14_2_m_4 = pr.i_14_2_m_4,
                        i_14_2_m_5 = pr.i_14_2_m_5,
                        # переменные уровня расхода материала
                        i_15_m_1 = pr.i_15_m_1,
                        i_15_m_2 = pr.i_15_m_2,
                        # переменные уровня технических отходов
                        i_16_m_1 = pr.i_16_m_1,
                        i_16_m_2 = pr.i_16_m_2,
                        # переменные уровня неисправности оборудования
                        i_17_m_1 = pr.i_17_m_1,
                        i_17_m_2 = pr.i_17_m_2,
                        # переменные уровня простоя оборудования из-за качества
                        i_18_m_1 = pr.i_18_m_1,
                        i_18_m_2 = pr.i_18_m_2,
                        # переменные уровня простоя оборудования из-за непоставок
                        i_19_m_1 = pr.i_19_m_1,
                        i_19_m_2 = pr.i_19_m_2,
                        # переменные уровня отклонений продукции
                        i_20_m_1 = pr.i_20_m_1,
                        i_20_m_2 = pr.i_20_m_2,

                        NAME_TABLE_2='Изменение значений за полугодие: Процесс Б(7.5) "Производство продукции"',


                        )
                    document = QtGui.QTextDocument()
                    document.setHtml(x)
                    self.textEdit.setDocument(document)

                else:
                    self.textEdit.setText('Empty')

            except:
                logger.error(f'FAILED! TabStr().on_clicked_view()_Error: {sys.exc_info()[:2]}') # logging



        def on_clicked_save_to_pdf(self):
            # функция сохранения в файл
            printer = QtPrintSupport.QPrinter()
            printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
            printer.setOutputFileName("summary_data.pdf")
            self.textEdit.print_(printer)

    logger.info("OK! Load object class") # logging

except Exception:
    logger.error(f'FAILED! TabStr_Error: {sys.exc_info()[:2]}') # logging

### Классы встроенного matplotlib
try:
    class WidgetPlot(QtWidgets.QWidget):
        def __init__(self, *args, **kwargs):
            QtWidgets.QWidget.__init__(self, *args, **kwargs)
            self.logger = logging.getLogger('indicators.gui_module.WidgetPlot')
            self.logger.info('__Init__ WidgetPlot')
            self.setLayout(QtWidgets.QVBoxLayout())
            self.canvas = PlotCanvas(self, width=10, height=8)
            self.toolbar = NavigationToolbar(self.canvas, self)
            self.layout().addWidget(self.toolbar)
            self.layout().addWidget(self.canvas)

    logger.info("OK! Load object class") # logging

except Exception:
    logger.error(f'FAILED! WidgetPlot_Error: {sys.exc_info()[:2]}') # logging

try:
    class PlotCanvas(FigureCanvas):
        def __init__(self, parent=None, width=10, height=8, dpi=100):
            self.logger = logging.getLogger('indicators.gui_module.PlotCanvas')
            self.logger.info('__Init__ PlotCanvas')
            fig = Figure(figsize=(width, height), dpi=dpi)
            FigureCanvas.__init__(self, fig)
            self.setParent(parent)
            FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            FigureCanvas.updateGeometry(self)
            self.plot()

        def plot(self):
            data = pr.data_kol_vip_prod_year
            ax = self.figure.add_subplot(111)
            ax.plot(data, 'b-', linewidth=1.5)
            ax.set_title(r'Кол-во выпущенной п/б ленты в тоннах по годам', fontsize=16, y=1.05)
            ax.grid()
            self.show()
    logger.info("OK! Load object class") # logging

except Exception:
    logger.error(f'FAILED! PlotCanvas_Error: {sys.exc_info()[:2]}') # logging

try:
    class View_Adhaesio_Graphics(QtWidgets.QWidget):
        """
        ### Класс командных кнопок-ссылок отображения графиков показателей адгезии
        """
        def __init__(self, *args, **kwargs):
            QtWidgets.QWidget.__init__(self, *args, **kwargs)
            self.logger = logging.getLogger('indicators.gui_module.View_Adhaesio_Graphics')
            self.logger.info('__Init__ View_Adhaesio_Graphics')
            # box
            self.button_pz_01 = QtWidgets.QCommandLinkButton("Диаграмма корреляции")
            self.button_pz_01.clicked.connect(self.on_clicked_pz_01)
            self.button_pz_02 = QtWidgets.QCommandLinkButton("График погрешностей")
            self.button_pz_02.clicked.connect(self.on_clicked_pz_02)
            self.button_pz_03 = QtWidgets.QCommandLinkButton("Гистограмма распределения")
            self.button_pz_03.clicked.connect(self.on_clicked_pz_03)
            self.button_pz_04 = QtWidgets.QCommandLinkButton("Диаграмма распределения")
            self.button_pz_04.clicked.connect(self.on_clicked_pz_04)
            self.button_pz_05 = QtWidgets.QCommandLinkButton("Линейный график и линейная регрессия")
            self.button_pz_05.clicked.connect(self.on_clicked_pz_05)
            self.box = QtWidgets.QGroupBox("ПИРМА-З")
            self.bbox = QtWidgets.QVBoxLayout()
            self.bbox.addWidget(self.button_pz_01)
            self.bbox.addWidget(self.button_pz_02)
            self.bbox.addWidget(self.button_pz_03)
            self.bbox.addWidget(self.button_pz_04)
            self.bbox.addWidget(self.button_pz_05)
            self.box.setLayout(self.bbox)
            # box_1
            self.button_pl_01 = QtWidgets.QCommandLinkButton("Диаграмма корреляции")
            self.button_pl_01.clicked.connect(self.on_clicked_pl_01)
            self.button_pl_02 = QtWidgets.QCommandLinkButton("График погрешностей")
            self.button_pl_02.clicked.connect(self.on_clicked_pl_02)
            self.button_pl_03 = QtWidgets.QCommandLinkButton("Гистограмма распределения")
            self.button_pl_03.clicked.connect(self.on_clicked_pl_03)
            self.button_pl_04 = QtWidgets.QCommandLinkButton("Диаграмма распределения")
            self.button_pl_04.clicked.connect(self.on_clicked_pl_04)
            self.button_pl_05 = QtWidgets.QCommandLinkButton("Линейный график и линейная регрессия")
            self.button_pl_05.clicked.connect(self.on_clicked_pl_05)
            self.box_1 = QtWidgets.QGroupBox("ПИРМА-Л")
            self.bbox_1 = QtWidgets.QVBoxLayout()
            self.bbox_1.addWidget(self.button_pl_01)
            self.bbox_1.addWidget(self.button_pl_02)
            self.bbox_1.addWidget(self.button_pl_03)
            self.bbox_1.addWidget(self.button_pl_04)
            self.bbox_1.addWidget(self.button_pl_05)
            self.box_1.setLayout(self.bbox_1)
            # box_2
            self.button_lnn_2_0_01 = QtWidgets.QCommandLinkButton("Диаграмма корреляции")
            self.button_lnn_2_0_01.clicked.connect(self.on_clicked_lnn_2_0_01)
            self.button_lnn_2_0_02 = QtWidgets.QCommandLinkButton("График погрешностей")
            self.button_lnn_2_0_02.clicked.connect(self.on_clicked_lnn_2_0_02)
            self.button_lnn_2_0_03 = QtWidgets.QCommandLinkButton("Гистограмма распределения")
            self.button_lnn_2_0_03.clicked.connect(self.on_clicked_lnn_2_0_03)
            self.button_lnn_2_0_04 = QtWidgets.QCommandLinkButton("Диаграмма распределения")
            self.button_lnn_2_0_04.clicked.connect(self.on_clicked_lnn_2_0_04)
            self.button_lnn_2_0_05 = QtWidgets.QCommandLinkButton("Линейный график и линейная регрессия")
            self.button_lnn_2_0_05.clicked.connect(self.on_clicked_lnn_2_0_05)
            self.box_2 = QtWidgets.QGroupBox("ЛИТКОР-НН т.2.0")
            self.bbox_2 = QtWidgets.QVBoxLayout()
            self.bbox_2.addWidget(self.button_lnn_2_0_01)
            self.bbox_2.addWidget(self.button_lnn_2_0_02)
            self.bbox_2.addWidget(self.button_lnn_2_0_03)
            self.bbox_2.addWidget(self.button_lnn_2_0_04)
            self.bbox_2.addWidget(self.button_lnn_2_0_05)
            self.box_2.setLayout(self.bbox_2)
            # box_3
            self.button_lnn_1_9_01 = QtWidgets.QCommandLinkButton("Диаграмма корреляции")
            self.button_lnn_1_9_01.clicked.connect(self.on_clicked_lnn_1_9_01)
            self.button_lnn_1_9_02 = QtWidgets.QCommandLinkButton("График погрешностей")
            self.button_lnn_1_9_02.clicked.connect(self.on_clicked_lnn_1_9_02)
            self.button_lnn_1_9_03 = QtWidgets.QCommandLinkButton("Гистограмма распределения")
            self.button_lnn_1_9_03.clicked.connect(self.on_clicked_lnn_1_9_03)
            self.button_lnn_1_9_04 = QtWidgets.QCommandLinkButton("Диаграмма распределения")
            self.button_lnn_1_9_04.clicked.connect(self.on_clicked_lnn_1_9_04)
            self.button_lnn_1_9_05 = QtWidgets.QCommandLinkButton("Линейный график и линейная регрессия")
            self.button_lnn_1_9_05.clicked.connect(self.on_clicked_lnn_1_9_05)
            self.box_3 = QtWidgets.QGroupBox("ЛИТКОР-НН т.1.9")
            self.bbox_3 = QtWidgets.QVBoxLayout()
            self.bbox_3.addWidget(self.button_lnn_1_9_01)
            self.bbox_3.addWidget(self.button_lnn_1_9_02)
            self.bbox_3.addWidget(self.button_lnn_1_9_03)
            self.bbox_3.addWidget(self.button_lnn_1_9_04)
            self.bbox_3.addWidget(self.button_lnn_1_9_05)
            self.box_3.setLayout(self.bbox_3)
            # box_4
            self.button_lnn_1_7_01 = QtWidgets.QCommandLinkButton("Диаграмма корреляции")
            self.button_lnn_1_7_01.clicked.connect(self.on_clicked_lnn_1_7_01)
            self.button_lnn_1_7_02 = QtWidgets.QCommandLinkButton("График погрешностей")
            self.button_lnn_1_7_02.clicked.connect(self.on_clicked_lnn_1_7_02)
            self.button_lnn_1_7_03 = QtWidgets.QCommandLinkButton("Гистограмма распределения")
            self.button_lnn_1_7_03.clicked.connect(self.on_clicked_lnn_1_7_03)
            self.button_lnn_1_7_04 = QtWidgets.QCommandLinkButton("Диаграмма распределения")
            self.button_lnn_1_7_04.clicked.connect(self.on_clicked_lnn_1_7_04)
            self.button_lnn_1_7_05 = QtWidgets.QCommandLinkButton("Линейный график и линейная регрессия")
            self.button_lnn_1_7_05.clicked.connect(self.on_clicked_lnn_1_7_05)
            self.box_4 = QtWidgets.QGroupBox("ЛИТКОР-НН т.1.7")
            self.bbox_4 = QtWidgets.QVBoxLayout()
            self.bbox_4.addWidget(self.button_lnn_1_7_01)
            self.bbox_4.addWidget(self.button_lnn_1_7_02)
            self.bbox_4.addWidget(self.button_lnn_1_7_03)
            self.bbox_4.addWidget(self.button_lnn_1_7_04)
            self.bbox_4.addWidget(self.button_lnn_1_7_05)
            self.box_4.setLayout(self.bbox_4)
            # box_5
            self.button_lnn_1_0_01 = QtWidgets.QCommandLinkButton("Диаграмма корреляции")
            self.button_lnn_1_0_01.clicked.connect(self.on_clicked_lnn_1_0_01)
            self.button_lnn_1_0_02 = QtWidgets.QCommandLinkButton("График погрешностей")
            self.button_lnn_1_0_02.clicked.connect(self.on_clicked_lnn_1_0_02)
            self.button_lnn_1_0_03 = QtWidgets.QCommandLinkButton("Гистограмма распределения")
            self.button_lnn_1_0_03.clicked.connect(self.on_clicked_lnn_1_0_03)
            self.button_lnn_1_0_04 = QtWidgets.QCommandLinkButton("Диаграмма распределения")
            self.button_lnn_1_0_04.clicked.connect(self.on_clicked_lnn_1_0_04)
            self.button_lnn_1_0_05 = QtWidgets.QCommandLinkButton("Линейный график и линейная регрессия")
            self.button_lnn_1_0_05.clicked.connect(self.on_clicked_lnn_1_0_05)
            self.box_5 = QtWidgets.QGroupBox("ЛИТКОР-НН т.1.0")
            self.bbox_5 = QtWidgets.QVBoxLayout()
            self.bbox_5.addWidget(self.button_lnn_1_0_01)
            self.bbox_5.addWidget(self.button_lnn_1_0_02)
            self.bbox_5.addWidget(self.button_lnn_1_0_03)
            self.bbox_5.addWidget(self.button_lnn_1_0_04)
            self.bbox_5.addWidget(self.button_lnn_1_0_05)
            self.box_5.setLayout(self.bbox_5)
            # box_6
            self.button_ll_tr_neft_01 = QtWidgets.QCommandLinkButton("Диаграмма корреляции")
            self.button_ll_tr_neft_01.clicked.connect(self.on_clicked_ll_tr_neft_01)
            self.button_ll_tr_neft_02 = QtWidgets.QCommandLinkButton("График погрешностей")
            self.button_ll_tr_neft_02.clicked.connect(self.on_clicked_ll_tr_neft_02)
            self.button_ll_tr_neft_03 = QtWidgets.QCommandLinkButton("Гистограмма распределения")
            self.button_ll_tr_neft_03.clicked.connect(self.on_clicked_ll_tr_neft_03)
            self.button_ll_tr_neft_04 = QtWidgets.QCommandLinkButton("Диаграмма распределения")
            self.button_ll_tr_neft_04.clicked.connect(self.on_clicked_ll_tr_neft_04)
            self.button_ll_tr_neft_05 = QtWidgets.QCommandLinkButton("Линейный график и линейная регрессия")
            self.button_ll_tr_neft_05.clicked.connect(self.on_clicked_ll_tr_neft_05)
            self.box_6 = QtWidgets.QGroupBox("ЛИТКОР-Л_тр_нефть")
            self.bbox_6 = QtWidgets.QVBoxLayout()
            self.bbox_6.addWidget(self.button_ll_tr_neft_01)
            self.bbox_6.addWidget(self.button_ll_tr_neft_02)
            self.bbox_6.addWidget(self.button_ll_tr_neft_03)
            self.bbox_6.addWidget(self.button_ll_tr_neft_04)
            self.bbox_6.addWidget(self.button_ll_tr_neft_05)
            self.box_6.setLayout(self.bbox_6)
            # box_7
            self.button_ll_gaz_01 = QtWidgets.QCommandLinkButton("Диаграмма корреляции")
            self.button_ll_gaz_01.clicked.connect(self.on_clicked_ll_gaz_01)
            self.button_ll_gaz_02 = QtWidgets.QCommandLinkButton("График погрешностей")
            self.button_ll_gaz_02.clicked.connect(self.on_clicked_ll_gaz_02)
            self.button_ll_gaz_03 = QtWidgets.QCommandLinkButton("Гистограмма распределения")
            self.button_ll_gaz_03.clicked.connect(self.on_clicked_ll_gaz_03)
            self.button_ll_gaz_04 = QtWidgets.QCommandLinkButton("Диаграмма распределения")
            self.button_ll_gaz_04.clicked.connect(self.on_clicked_ll_gaz_04)
            self.button_ll_gaz_05 = QtWidgets.QCommandLinkButton("Линейный график и линейная регрессия")
            self.button_ll_gaz_05.clicked.connect(self.on_clicked_ll_gaz_05)
            self.box_7 = QtWidgets.QGroupBox("ЛИТКОР-Л_газ")
            self.bbox_7 = QtWidgets.QVBoxLayout()
            self.bbox_7.addWidget(self.button_ll_gaz_01)
            self.bbox_7.addWidget(self.button_ll_gaz_02)
            self.bbox_7.addWidget(self.button_ll_gaz_03)
            self.bbox_7.addWidget(self.button_ll_gaz_04)
            self.bbox_7.addWidget(self.button_ll_gaz_05)
            self.box_7.setLayout(self.bbox_7)
            # box_8
            self.button_lz_tr_neft_01 = QtWidgets.QCommandLinkButton("Диаграмма корреляции")
            self.button_lz_tr_neft_01.clicked.connect(self.on_clicked_lz_tr_neft_01)
            self.button_lz_tr_neft_02 = QtWidgets.QCommandLinkButton("График погрешностей")
            self.button_lz_tr_neft_02.clicked.connect(self.on_clicked_lz_tr_neft_02)
            self.button_lz_tr_neft_03 = QtWidgets.QCommandLinkButton("Гистограмма распределения")
            self.button_lz_tr_neft_03.clicked.connect(self.on_clicked_lz_tr_neft_03)
            self.button_lz_tr_neft_04 = QtWidgets.QCommandLinkButton("Диаграмма распределения")
            self.button_lz_tr_neft_04.clicked.connect(self.on_clicked_lz_tr_neft_04)
            self.button_lz_tr_neft_05 = QtWidgets.QCommandLinkButton("Линейный график и линейная регрессия")
            self.button_lz_tr_neft_05.clicked.connect(self.on_clicked_lz_tr_neft_05)
            self.box_8 = QtWidgets.QGroupBox("ЛИТКОР-З_тр_нефть")
            self.bbox_8 = QtWidgets.QVBoxLayout()
            self.bbox_8.addWidget(self.button_lz_tr_neft_01)
            self.bbox_8.addWidget(self.button_lz_tr_neft_02)
            self.bbox_8.addWidget(self.button_lz_tr_neft_03)
            self.bbox_8.addWidget(self.button_lz_tr_neft_04)
            self.bbox_8.addWidget(self.button_lz_tr_neft_05)
            self.box_8.setLayout(self.bbox_8)
            # box_9
            self.button_lz_gaz_01 = QtWidgets.QCommandLinkButton("Диаграмма корреляции")
            self.button_lz_gaz_01.clicked.connect(self.on_clicked_lz_gaz_01)
            self.button_lz_gaz_02 = QtWidgets.QCommandLinkButton("График погрешностей")
            self.button_lz_gaz_02.clicked.connect(self.on_clicked_lz_gaz_02)
            self.button_lz_gaz_03 = QtWidgets.QCommandLinkButton("Гистограмма распределения")
            self.button_lz_gaz_03.clicked.connect(self.on_clicked_lz_gaz_03)
            self.button_lz_gaz_04 = QtWidgets.QCommandLinkButton("Диаграмма распределения")
            self.button_lz_gaz_04.clicked.connect(self.on_clicked_lz_gaz_04)
            self.button_lz_gaz_05 = QtWidgets.QCommandLinkButton("Линейный график и линейная регрессия")
            self.button_lz_gaz_05.clicked.connect(self.on_clicked_lz_gaz_05)
            self.box_9 = QtWidgets.QGroupBox("ЛИТКОР-З_газ")
            self.bbox_9 = QtWidgets.QVBoxLayout()
            self.bbox_9.addWidget(self.button_lz_gaz_01)
            self.bbox_9.addWidget(self.button_lz_gaz_02)
            self.bbox_9.addWidget(self.button_lz_gaz_03)
            self.bbox_9.addWidget(self.button_lz_gaz_04)
            self.bbox_9.addWidget(self.button_lz_gaz_05)
            self.box_9.setLayout(self.bbox_9)
            # box_10
            self.button_bpi_2_0_01 = QtWidgets.QCommandLinkButton("Диаграмма корреляции")
            self.button_bpi_2_0_01.clicked.connect(self.on_clicked_bpi_2_0_01)
            self.button_bpi_2_0_02 = QtWidgets.QCommandLinkButton("График погрешностей")
            self.button_bpi_2_0_02.clicked.connect(self.on_clicked_bpi_2_0_02)
            self.button_bpi_2_0_03 = QtWidgets.QCommandLinkButton("Гистограмма распределения")
            self.button_bpi_2_0_03.clicked.connect(self.on_clicked_bpi_2_0_03)
            self.button_bpi_2_0_04 = QtWidgets.QCommandLinkButton("Диаграмма распределения")
            self.button_bpi_2_0_04.clicked.connect(self.on_clicked_bpi_2_0_04)
            self.button_bpi_2_0_05 = QtWidgets.QCommandLinkButton("Линейный график и линейная регрессия")
            self.button_bpi_2_0_05.clicked.connect(self.on_clicked_bpi_2_0_05)
            self.box_10 = QtWidgets.QGroupBox("БПИ_2_0")
            self.bbox_10 = QtWidgets.QVBoxLayout()
            self.bbox_10.addWidget(self.button_bpi_2_0_01)
            self.bbox_10.addWidget(self.button_bpi_2_0_02)
            self.bbox_10.addWidget(self.button_bpi_2_0_03)
            self.bbox_10.addWidget(self.button_bpi_2_0_04)
            self.bbox_10.addWidget(self.button_bpi_2_0_05)
            self.box_10.setLayout(self.bbox_10)
            # box_11
            self.button_bpi_1_7_01 = QtWidgets.QCommandLinkButton("Диаграмма корреляции")
            self.button_bpi_1_7_01.clicked.connect(self.on_clicked_bpi_1_7_01)
            self.button_bpi_1_7_02 = QtWidgets.QCommandLinkButton("График погрешностей")
            self.button_bpi_1_7_02.clicked.connect(self.on_clicked_bpi_1_7_02)
            self.button_bpi_1_7_03 = QtWidgets.QCommandLinkButton("Гистограмма распределения")
            self.button_bpi_1_7_03.clicked.connect(self.on_clicked_bpi_1_7_03)
            self.button_bpi_1_7_04 = QtWidgets.QCommandLinkButton("Диаграмма распределения")
            self.button_bpi_1_7_04.clicked.connect(self.on_clicked_bpi_1_7_04)
            self.button_bpi_1_7_05 = QtWidgets.QCommandLinkButton("Линейный график и линейная регрессия")
            self.button_bpi_1_7_05.clicked.connect(self.on_clicked_bpi_1_7_05)
            self.box_11 = QtWidgets.QGroupBox("БПИ_1_7")
            self.bbox_11 = QtWidgets.QVBoxLayout()
            self.bbox_11.addWidget(self.button_bpi_1_7_01)
            self.bbox_11.addWidget(self.button_bpi_1_7_02)
            self.bbox_11.addWidget(self.button_bpi_1_7_03)
            self.bbox_11.addWidget(self.button_bpi_1_7_04)
            self.bbox_11.addWidget(self.button_bpi_1_7_05)
            self.box_11.setLayout(self.bbox_11)
            # grid

            grid = QtWidgets.QGridLayout()
            grid.addWidget(self.box, 0, 0) # Добавляем компоненты
            grid.addWidget(self.box_1, 0, 1)
            grid.addWidget(self.box_2, 1, 0)
            grid.addWidget(self.box_3, 1, 1)
            grid.addWidget(self.box_4, 2, 0)
            grid.addWidget(self.box_5, 2, 1)
            grid.addWidget(self.box_6, 3, 0)
            grid.addWidget(self.box_7, 3, 1)
            grid.addWidget(self.box_8, 4, 0)
            grid.addWidget(self.box_9, 4, 1)
            grid.addWidget(self.box_10, 5, 0)
            grid.addWidget(self.box_11, 5, 1)

            self.setLayout(grid) # Передаем ссылку родителю

        def on_clicked_pz_01(self):
            """
            Функция запуска отображения диаграммы
            """
            f = ad.DependenceGraphic(ad._pz)
            plt.show()

        def on_clicked_pz_02(self):
            """
            Функция запуска отображения графика
            """
            d = ad.ErrorGraphic(ad._pz) # экземпляр класса графика погрешностей
            plt.show()

        def on_clicked_pz_03(self):
            """
            Функция запуска отображения графика
            """
            c = ad.DistributionHistogramm(ad._pz) # экземпляр класса гистограммы распределения
            plt.show()

        def on_clicked_pz_04(self):
            """
            Функция запуска отображения графика
            """
            b = ad.DistributionDiagramm(ad._pz) # экземпляр класса диаграммы распределения
            plt.show()

        def on_clicked_pz_05(self):
            """
            Функция запуска отображения графика
            """
            a = ad.LinearGraphic(ad._pz) # экземпляр класса линейного графика
            a.middle_value_text() # Aср
            a.regres_graphic() # построение графика линейной регресии
            plt.show()

        def on_clicked_pl_01(self):
            """
            Функция запуска отображения диаграммы _
            """
            f = ad.DependenceGraphic(ad._pl)
            plt.show()

        def on_clicked_pl_02(self):
            """
            Функция запуска отображения графика _
            """
            d = ad.ErrorGraphic(ad._pl) # экземпляр класса графика погрешностей
            plt.show()

        def on_clicked_pl_03(self):
            """
            Функция запуска отображения графика
            """
            c = ad.DistributionHistogramm(ad._pl) # экземпляр класса гистограммы распределения
            plt.show()

        def on_clicked_pl_04(self):
            """
            Функция запуска отображения графика
            """
            b = ad.DistributionDiagramm(ad._pl) # экземпляр класса диаграммы распределения
            plt.show()

        def on_clicked_pl_05(self):
            """
            Функция запуска отображения графика
            """
            a = ad.LinearGraphic(ad._pl) # экземпляр класса линейного графика
            a.middle_value_text() # Aср
            a.regres_graphic() # построение графика линейной регресии
            plt.show()

        def on_clicked_lnn_2_0_01(self):
            """
            Функция запуска отображения диаграммы _
            """
            f = ad.DependenceGraphic(ad._lnn_2_0)
            plt.show()

        def on_clicked_lnn_2_0_02(self):
            """
            Функция запуска отображения графика _
            """
            d = ad.ErrorGraphic(ad._lnn_2_0) # экземпляр класса графика погрешностей
            plt.show()

        def on_clicked_lnn_2_0_03(self):
            """
            Функция запуска отображения графика
            """
            c = ad.DistributionHistogramm(ad._lnn_2_0) # экземпляр класса гистограммы распределения
            plt.show()

        def on_clicked_lnn_2_0_04(self):
            """
            Функция запуска отображения графика
            """
            b = ad.DistributionDiagramm(ad._lnn_2_0) # экземпляр класса диаграммы распределения
            plt.show()

        def on_clicked_lnn_2_0_05(self):
            """
            Функция запуска отображения графика
            """
            a = ad.LinearGraphic(ad._lnn_2_0) # экземпляр класса линейного графика
            a.middle_value_text() # Aср
            a.regres_graphic() # построение графика линейной регресии
            plt.show()

        def on_clicked_lnn_1_9_01(self):
            """
            Функция запуска отображения диаграммы _
            """
            f = ad.DependenceGraphic(ad._lnn_1_9)
            plt.show()

        def on_clicked_lnn_1_9_02(self):
            """
            Функция запуска отображения графика _
            """
            d = ad.ErrorGraphic(ad._lnn_1_9) # экземпляр класса графика погрешностей
            plt.show()

        def on_clicked_lnn_1_9_03(self):
            """
            Функция запуска отображения графика
            """
            c = ad.DistributionHistogramm(ad._lnn_1_9) # экземпляр класса гистограммы распределения
            plt.show()

        def on_clicked_lnn_1_9_04(self):
            """
            Функция запуска отображения графика
            """
            b = ad.DistributionDiagramm(ad._lnn_1_9) # экземпляр класса диаграммы распределения
            plt.show()

        def on_clicked_lnn_1_9_05(self):
            """
            Функция запуска отображения графика
            """
            a = ad.LinearGraphic(ad._lnn_1_9) # экземпляр класса линейного графика
            a.middle_value_text() # Aср
            a.regres_graphic() # построение графика линейной регресии
            plt.show()

        def on_clicked_lnn_1_7_01(self):
            """
            Функция запуска отображения диаграммы _
            """
            f = ad.DependenceGraphic(ad._lnn_1_7)
            plt.show()

        def on_clicked_lnn_1_7_02(self):
            """
            Функция запуска отображения графика _
            """
            d = ad.ErrorGraphic(ad._lnn_1_7) # экземпляр класса графика погрешностей
            plt.show()

        def on_clicked_lnn_1_7_03(self):
            """
            Функция запуска отображения графика
            """
            c = ad.DistributionHistogramm(ad._lnn_1_7) # экземпляр класса гистограммы распределения
            plt.show()

        def on_clicked_lnn_1_7_04(self):
            """
            Функция запуска отображения графика
            """
            b = ad.DistributionDiagramm(ad._lnn_1_7) # экземпляр класса диаграммы распределения
            plt.show()

        def on_clicked_lnn_1_7_05(self):
            """
            Функция запуска отображения графика
            """
            a = ad.LinearGraphic(ad._lnn_1_7) # экземпляр класса линейного графика
            a.middle_value_text() # Aср
            a.regres_graphic() # построение графика линейной регресии
            plt.show()

        def on_clicked_lnn_1_0_01(self):
            """
            Функция запуска отображения диаграммы _
            """
            f = ad.DependenceGraphic(ad._lnn_1_0)
            plt.show()

        def on_clicked_lnn_1_0_02(self):
            """
            Функция запуска отображения графика _
            """
            d = ad.ErrorGraphic(ad._lnn_1_0) # экземпляр класса графика погрешностей
            plt.show()

        def on_clicked_lnn_1_0_03(self):
            """
            Функция запуска отображения графика
            """
            c = ad.DistributionHistogramm(ad._lnn_1_0) # экземпляр класса гистограммы распределения
            plt.show()

        def on_clicked_lnn_1_0_04(self):
            """
            Функция запуска отображения графика
            """
            b = ad.DistributionDiagramm(ad._lnn_1_0) # экземпляр класса диаграммы распределения
            plt.show()

        def on_clicked_lnn_1_0_05(self):
            """
            Функция запуска отображения графика
            """
            a = ad.LinearGraphic(ad._lnn_1_0) # экземпляр класса линейного графика
            a.middle_value_text() # Aср
            a.regres_graphic() # построение графика линейной регресии
            plt.show()

        def on_clicked_ll_tr_neft_01(self):
            """
            Функция запуска отображения диаграммы _
            """
            f = ad.DependenceGraphic(ad._ll_tr_neft)
            plt.show()

        def on_clicked_ll_tr_neft_02(self):
            """
            Функция запуска отображения графика _
            """
            d = ad.ErrorGraphic(ad._ll_tr_neft) # экземпляр класса графика погрешностей
            plt.show()

        def on_clicked_ll_tr_neft_03(self):
            """
            Функция запуска отображения графика
            """
            c = ad.DistributionHistogramm(ad._ll_tr_neft) # экземпляр класса гистограммы распределения
            plt.show()

        def on_clicked_ll_tr_neft_04(self):
            """
            Функция запуска отображения графика
            """
            b = ad.DistributionDiagramm(ad._ll_tr_neft) # экземпляр класса диаграммы распределения
            plt.show()

        def on_clicked_ll_tr_neft_05(self):
            """
            Функция запуска отображения графика
            """
            a = ad.LinearGraphic(ad._ll_tr_neft) # экземпляр класса линейного графика
            a.middle_value_text() # Aср
            a.regres_graphic() # построение графика линейной регресии
            plt.show()

        def on_clicked_ll_gaz_01(self):
            """
            Функция запуска отображения диаграммы _
            """
            f = ad.DependenceGraphic(ad._ll_gaz)
            plt.show()

        def on_clicked_ll_gaz_02(self):
            """
            Функция запуска отображения графика _
            """
            d = ad.ErrorGraphic(ad._ll_gaz) # экземпляр класса графика погрешностей
            plt.show()

        def on_clicked_ll_gaz_03(self):
            """
            Функция запуска отображения графика
            """
            c = ad.DistributionHistogramm(ad._ll_gaz) # экземпляр класса гистограммы распределения
            plt.show()

        def on_clicked_ll_gaz_04(self):
            """
            Функция запуска отображения графика
            """
            b = ad.DistributionDiagramm(ad._ll_gaz) # экземпляр класса диаграммы распределения
            plt.show()

        def on_clicked_ll_gaz_05(self):
            """
            Функция запуска отображения графика
            """
            a = ad.LinearGraphic(ad._ll_gaz) # экземпляр класса линейного графика
            a.middle_value_text() # Aср
            a.regres_graphic() # построение графика линейной регресии
            plt.show()

        def on_clicked_lz_tr_neft_01(self):
            """
            Функция запуска отображения диаграммы _
            """
            f = ad.DependenceGraphic(ad._lz_tr_neft)
            plt.show()

        def on_clicked_lz_tr_neft_02(self):
            """
            Функция запуска отображения графика _
            """
            d = ad.ErrorGraphic(ad._lz_tr_neft) # экземпляр класса графика погрешностей
            plt.show()

        def on_clicked_lz_tr_neft_03(self):
            """
            Функция запуска отображения графика
            """
            c = ad.DistributionHistogramm(ad._lz_tr_neft) # экземпляр класса гистограммы распределения
            plt.show()

        def on_clicked_lz_tr_neft_04(self):
            """
            Функция запуска отображения графика
            """
            b = ad.DistributionDiagramm(ad._lz_tr_neft) # экземпляр класса диаграммы распределения
            plt.show()

        def on_clicked_lz_tr_neft_05(self):
            """
            Функция запуска отображения графика
            """
            a = ad.LinearGraphic(ad._lz_tr_neft) # экземпляр класса линейного графика
            a.middle_value_text() # Aср
            a.regres_graphic() # построение графика линейной регресии
            plt.show()

        def on_clicked_lz_gaz_01(self):
            """
            Функция запуска отображения диаграммы _
            """
            f = ad.DependenceGraphic(ad._lz_gaz)
            plt.show()

        def on_clicked_lz_gaz_02(self):
            """
            Функция запуска отображения графика _
            """
            d = ad.ErrorGraphic(ad._lz_gaz) # экземпляр класса графика погрешностей
            plt.show()

        def on_clicked_lz_gaz_03(self):
            """
            Функция запуска отображения графика
            """
            c = ad.DistributionHistogramm(ad._lz_gaz) # экземпляр класса гистограммы распределения
            plt.show()

        def on_clicked_lz_gaz_04(self):
            """
            Функция запуска отображения графика
            """
            b = ad.DistributionDiagramm(ad._lz_gaz) # экземпляр класса диаграммы распределения
            plt.show()

        def on_clicked_lz_gaz_05(self):
            """
            Функция запуска отображения графика
            """
            a = ad.LinearGraphic(ad._lz_gaz) # экземпляр класса линейного графика
            a.middle_value_text() # Aср
            a.regres_graphic() # построение графика линейной регресии
            plt.show()

        def on_clicked_bpi_2_0_01(self):
            """
            Функция запуска отображения диаграммы _
            """
            f = ad.DependenceGraphic(ad._bpi_2_0)
            plt.show()

        def on_clicked_bpi_2_0_02(self):
            """
            Функция запуска отображения графика _
            """
            d = ad.ErrorGraphic(ad._bpi_2_0) # экземпляр класса графика погрешностей
            plt.show()

        def on_clicked_bpi_2_0_03(self):
            """
            Функция запуска отображения графика
            """
            c = ad.DistributionHistogramm(ad._bpi_2_0) # экземпляр класса гистограммы распределения
            plt.show()

        def on_clicked_bpi_2_0_04(self):
            """
            Функция запуска отображения графика
            """
            b = ad.DistributionDiagramm(ad._bpi_2_0) # экземпляр класса диаграммы распределения
            plt.show()

        def on_clicked_bpi_2_0_05(self):
            """
            Функция запуска отображения графика
            """
            a = ad.LinearGraphic(ad._bpi_2_0) # экземпляр класса линейного графика
            a.middle_value_text() # Aср
            a.regres_graphic() # построение графика линейной регресии
            plt.show()

        def on_clicked_bpi_1_7_01(self):
            """
            Функция запуска отображения диаграммы _
            """
            f = ad.DependenceGraphic(ad._bpi_1_7)
            plt.show()

        def on_clicked_bpi_1_7_02(self):
            """
            Функция запуска отображения графика _
            """
            d = ad.ErrorGraphic(ad._bpi_1_7) # экземпляр класса графика погрешностей
            plt.show()

        def on_clicked_bpi_1_7_03(self):
            """
            Функция запуска отображения графика
            """
            c = ad.DistributionHistogramm(ad._bpi_1_7) # экземпляр класса гистограммы распределения
            plt.show()

        def on_clicked_bpi_1_7_04(self):
            """
            Функция запуска отображения графика
            """
            b = ad.DistributionDiagramm(ad._bpi_1_7) # экземпляр класса диаграммы распределения
            plt.show()

        def on_clicked_bpi_1_7_05(self):
            """
            Функция запуска отображения графика
            """
            a = ad.LinearGraphic(ad._bpi_1_7) # экземпляр класса линейного графика
            a.middle_value_text() # Aср
            a.regres_graphic() # построение графика линейной регресии
            plt.show()
    logger.info("OK! Load object class") # logging

except Exception:
    logger.error(f'FAILED! View_Adhaesio_Graphics_Error: {sys.exc_info()[:2]}') # logging

try:
    class View_Process_Graphics(QtWidgets.QWidget):
        """
        ### Класс командных кнопок отображения графиков показателей адгезии
        """
        def __init__(self, *args, **kwargs):
            QtWidgets.QWidget.__init__(self, *args, **kwargs)
            self.logger = logging.getLogger('indicators.gui_module.View_Process_Graphics')
            self.logger.info('__Init__ View_Process_Graphics')
            self.box = QtWidgets.QGroupBox('Процесс Б(7.7) "Сбыт"')
            self.btn = QtWidgets.QPushButton()
            self.btn.setIcon(QtGui.QIcon(ICON_GRAPHIC_003))
            self.btn.setIconSize(QtCore.QSize(32, 32))
            self.btn_1 = QtWidgets.QPushButton()
            self.btn_1.setIcon(QtGui.QIcon(ICON_GRAPHIC_003))
            self.btn_1.setIconSize(QtCore.QSize(32, 32))
            self.btn_2 = QtWidgets.QPushButton()
            self.btn_2.setIcon(QtGui.QIcon(ICON_GRAPHIC_003))
            self.btn_2.setIconSize(QtCore.QSize(32, 32))
            self.btn_3 = QtWidgets.QPushButton()
            self.btn_3.setIcon(QtGui.QIcon(ICON_GRAPHIC_003))
            self.btn_3.setIconSize(QtCore.QSize(32, 32))
            self.btn_4 = QtWidgets.QPushButton()
            self.btn_4.setIcon(QtGui.QIcon(ICON_GRAPHIC_003))
            self.btn_4.setIconSize(QtCore.QSize(32, 32))
            self.btn_5 = QtWidgets.QPushButton()
            self.btn_5.setIcon(QtGui.QIcon(ICON_GRAPHIC_003))
            self.btn_5.setIconSize(QtCore.QSize(32, 32))
            self.btn_6 = QtWidgets.QPushButton()
            self.btn_6.setIcon(QtGui.QIcon(ICON_GRAPHIC_003))
            self.btn_6.setIconSize(QtCore.QSize(32, 32))
            self.btn_7 = QtWidgets.QPushButton()
            self.btn_7.setIcon(QtGui.QIcon(ICON_GRAPHIC_003))
            self.btn_7.setIconSize(QtCore.QSize(32, 32))
            self.btn_8 = QtWidgets.QPushButton()
            self.btn_8.setIcon(QtGui.QIcon(ICON_GRAPHIC_003))
            self.btn_8.setIconSize(QtCore.QSize(32, 32))
            self.btn_9 = QtWidgets.QPushButton()
            self.btn_9.setIcon(QtGui.QIcon(ICON_GRAPHIC_003))
            self.btn_9.setIconSize(QtCore.QSize(32, 32))
            self.bbox = QtWidgets.QHBoxLayout()
            self.bbox.addWidget(self.btn)
            self.bbox.addWidget(self.btn_1)
            self.bbox.addWidget(self.btn_2)
            self.bbox.addWidget(self.btn_3)
            self.bbox.addWidget(self.btn_4)
            self.bbox.addWidget(self.btn_5)
            self.bbox.addWidget(self.btn_6)
            self.bbox.addWidget(self.btn_7)
            self.bbox.addWidget(self.btn_8)
            self.bbox.addWidget(self.btn_9)
            self.box.setLayout(self.bbox)

            self.box_1 = QtWidgets.QGroupBox('Процесс Б(7.5) "Производство продукции"')
            self.b_7_5 = QtWidgets.QPushButton()
            self.b_7_5.setIcon(QtGui.QIcon(ICON_GRAPHIC_005))
            self.b_7_5.setIconSize(QtCore.QSize(32, 32))
            self.b_7_5.setToolTip("Количество выпущенной продукции по годам")
            self.b_7_5.setStatusTip('Количество выпущенной продукции по годам')
            self.b_7_5.clicked.connect(self.on_clicked_b_7_5)

            self.b_7_5_1 = QtWidgets.QPushButton()
            self.b_7_5_1.setIcon(QtGui.QIcon(ICON_GRAPHIC_006))
            self.b_7_5_1.setIconSize(QtCore.QSize(32, 32))
            self.b_7_5_1.setToolTip("Уровень неисправности оборудования по годам")
            self.b_7_5_1.setStatusTip('Уровень неисправности оборудования по годам')
            self.b_7_5_1.clicked.connect(self.on_clicked_b_7_5_1)

            self.b_7_5_2 = QtWidgets.QPushButton()
            self.b_7_5_2.setIcon(QtGui.QIcon(ICON_GRAPHIC_005))
            self.b_7_5_2.setIconSize(QtCore.QSize(32, 32))
            self.b_7_5_3 = QtWidgets.QPushButton()
            self.b_7_5_3.setIcon(QtGui.QIcon(ICON_GRAPHIC_006))
            self.b_7_5_3.setIconSize(QtCore.QSize(32, 32))
            self.b_7_5_4 = QtWidgets.QPushButton()
            self.b_7_5_4.setIcon(QtGui.QIcon(ICON_GRAPHIC_005))
            self.b_7_5_4.setIconSize(QtCore.QSize(32, 32))
            self.b_7_5_5 = QtWidgets.QPushButton()
            self.b_7_5_5.setIcon(QtGui.QIcon(ICON_GRAPHIC_006))
            self.b_7_5_5.setIconSize(QtCore.QSize(32, 32))
            self.b_7_5_6 = QtWidgets.QPushButton()
            self.b_7_5_6.setIcon(QtGui.QIcon(ICON_GRAPHIC_005))
            self.b_7_5_6.setIconSize(QtCore.QSize(32, 32))



            self.b_7_5_7 = QtWidgets.QPushButton()
            self.b_7_5_7.setIcon(QtGui.QIcon(ICON_GRAPHIC_006))
            self.b_7_5_7.setIconSize(QtCore.QSize(32, 32))
            self.b_7_5_7.setToolTip("Количество выпущенной продукции по полугодиям")
            self.b_7_5_7.setStatusTip('Количество выпущенной продукции по полугодиям')
            self.b_7_5_7.clicked.connect(self.on_clicked_b_7_5_7)

            self.b_7_5_8 = QtWidgets.QPushButton()
            self.b_7_5_8.setIcon(QtGui.QIcon(ICON_GRAPHIC_005))
            self.b_7_5_8.setIconSize(QtCore.QSize(32, 32))
            self.b_7_5_8.setToolTip("Уровень неисправности оборудования по полугодиям")
            self.b_7_5_8.setStatusTip('Уровень неисправности оборудования по полугодиям')
            self.b_7_5_8.clicked.connect(self.on_clicked_b_7_5_8)

            self.b_7_5_9 = QtWidgets.QPushButton()
            self.b_7_5_9.setIcon(QtGui.QIcon(ICON_GRAPHIC_006))
            self.b_7_5_9.setIconSize(QtCore.QSize(32, 32))
            self.b_7_5_10 = QtWidgets.QPushButton()
            self.b_7_5_10.setIcon(QtGui.QIcon(ICON_GRAPHIC_005))
            self.b_7_5_10.setIconSize(QtCore.QSize(32, 32))
            self.b_7_5_11 = QtWidgets.QPushButton()
            self.b_7_5_11.setIcon(QtGui.QIcon(ICON_GRAPHIC_006))
            self.b_7_5_11.setIconSize(QtCore.QSize(32, 32))
            self.b_7_5_12 = QtWidgets.QPushButton()
            self.b_7_5_12.setIcon(QtGui.QIcon(ICON_GRAPHIC_005))
            self.b_7_5_12.setIconSize(QtCore.QSize(32, 32))
            self.b_7_5_13 = QtWidgets.QPushButton()
            self.b_7_5_13.setIcon(QtGui.QIcon(ICON_GRAPHIC_006))
            self.b_7_5_13.setIconSize(QtCore.QSize(32, 32))

            self.bbox_1 = QtWidgets.QHBoxLayout()
            self.bbox_1.addWidget(self.b_7_5)
            self.bbox_1.addWidget(self.b_7_5_1)
            self.bbox_1.addWidget(self.b_7_5_2)
            self.bbox_1.addWidget(self.b_7_5_3)
            self.bbox_1.addWidget(self.b_7_5_4)
            self.bbox_1.addWidget(self.b_7_5_5)
            self.bbox_1.addWidget(self.b_7_5_6)
            self.bbox_1.addWidget(self.b_7_5_7)
            self.bbox_1.addWidget(self.b_7_5_8)
            self.bbox_1.addWidget(self.b_7_5_9)
            self.bbox_1.addWidget(self.b_7_5_10)
            self.bbox_1.addWidget(self.b_7_5_11)
            self.bbox_1.addWidget(self.b_7_5_12)
            self.bbox_1.addWidget(self.b_7_5_13)

            self.box_1.setLayout(self.bbox_1)

            self.box_2 = QtWidgets.QGroupBox("Наименование показателя_2")
            self.btn_2 = QtWidgets.QPushButton("Отобразить график процесса")
            self.bbox_2 = QtWidgets.QHBoxLayout()
            self.bbox_2.addWidget(self.btn_2)
            self.box_2.setLayout(self.bbox_2)

            self.box_3 = QtWidgets.QGroupBox("Наименование показателя_3")
            self.btn_3 = QtWidgets.QPushButton("Отобразить график процесса")
            self.bbox_3 = QtWidgets.QHBoxLayout()
            self.bbox_3.addWidget(self.btn_3)
            self.box_3.setLayout(self.bbox_3)

            self.box_4 = QtWidgets.QGroupBox("Наименование показателя_4")
            self.btn_4 = QtWidgets.QPushButton("Отобразить график процесса")
            self.bbox_4 = QtWidgets.QHBoxLayout()
            self.bbox_4.addWidget(self.btn_4)
            self.box_4.setLayout(self.bbox_4)

            self.box_5 = QtWidgets.QGroupBox("Наименование показателя_5")
            self.btn_5 = QtWidgets.QPushButton("Отобразить график процесса")
            self.bbox_5 = QtWidgets.QHBoxLayout()
            self.bbox_5.addWidget(self.btn_5)
            self.box_5.setLayout(self.bbox_5)

            self.box_6 = QtWidgets.QGroupBox("Наименование показателя_6")
            self.btn_6 = QtWidgets.QPushButton("Отобразить график процесса")
            self.bbox_6 = QtWidgets.QHBoxLayout()
            self.bbox_6.addWidget(self.btn_6)
            self.box_6.setLayout(self.bbox_6)

            self.box_7 = QtWidgets.QGroupBox("Наименование показателя_7")
            self.btn_7 = QtWidgets.QPushButton("Отобразить график процесса")
            self.bbox_7 = QtWidgets.QHBoxLayout()
            self.bbox_7.addWidget(self.btn_7)
            self.box_7.setLayout(self.bbox_7)

            grid = QtWidgets.QGridLayout()            # Создаем сетку
            grid.addWidget(self.box, 0, 0)             # Добавляем компоненты
            grid.addWidget(self.box_1, 0, 1)
            grid.addWidget(self.box_2, 1, 0)
            grid.addWidget(self.box_3, 1, 1)
            grid.addWidget(self.box_4, 2, 0)
            grid.addWidget(self.box_5, 2, 1)
            grid.addWidget(self.box_6, 3, 0)
            grid.addWidget(self.box_7, 3, 1)
            self.setLayout(grid)                    # Передаем ссылку родителю

        def on_clicked_b_7_5(self):
            """
            Функция запуска отображения диаграммы _
            """
            a = pr.Graphics_Number_Production(pr.data_number_year, name= 'Количество выпущенной п/б ленты  по годам')
            plt.show()

        def on_clicked_b_7_5_1(self):
            """
            Функция запуска отображения диаграммы _
            """
            b = pr.Graphics_Indicators_Production(pr.data_ur_neispr_obor_year, name= 'Уровень неисправности оборудования по годам')
            plt.show()

        def on_clicked_b_7_5_7(self):
            """
            Функция запуска отображения диаграммы _
            """
            a = pr.Graphics_Number_Production(pr.data_number_middle_year, name= 'Количество выпущенной п/б ленты  по полугодиям')
            plt.show()

        def on_clicked_b_7_5_8(self):
            """
            Функция запуска отображения диаграммы _
            """
            b = pr.Graphics_Indicators_Production(pr. data_ur_neispr_obor_middle_year, name= 'Уровень неисправности оборудования по полугодиям')
            plt.show()

    logger.info("OK! Load object class") # logging

except Exception:
    logger.error(f'FAILED! View_Process_Graphics_Error: {sys.exc_info()[:2]}') # logging

logger.info(f"OK! Module on {platform.platform()}") # logging

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
