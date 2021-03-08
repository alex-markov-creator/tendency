#-*- coding: utf-8 -*-
# version 0.2a
# author: andrew.bezzubov - 07/03/2021
# email: ruizcontrol@yandex.ru, agb2019@list.ru
# https://github.com/alex-markov-creator/tendency.git
# GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""
===============================================================
indicators.py -запуск основного окна приложения.
# ПРЕДПОЛАГАЕМЫЕ ИЗМЕНЕНИЯ
# - решить проблему исчезновения экрана заставки при нажатии кнопок манипулятора "мышь"
# возможный вариант решения: многопоточные приложения
# - выделить в отдельный поток загрузку БД и загрузку главного окна программы
# возможный вариант решения: многопоточные приложения класс QThread
# ПОСЛЕДУЮЩИЕ ВЕРСИИ(варианты):
# - чтение аннотации из файла и генерация нескольких вариантов отображения
"""
import sys
import os

import time

from PyQt5 import QtCore, QtWidgets, QtGui, QtSql
from PyQt5 import QtMultimedia

from gui_module.login import LoginDialog  # ИМПОРТ ОКНА ИДЕНТИФИКАЦИИ
from gui_module.gui import *  # ИМПОРТ ГЛАВНОГО ОКНА

app = QtWidgets.QApplication(sys.argv)  # аргументы командной строки
pass_dlg = LoginDialog()  # окно идентификации

class MyWindow(QtWidgets.QDialog):
    """Класс диалогового окна экрана заставки
    """

    def __init__(self):
        super().__init__()
        #####################################################
        # ВЫВОД СТАРТОВОГО ЗВУКА
        #####################################################
        # Инициализируем подсистему вывода звуковых эффектов
        self.sndEffect = QtMultimedia.QSoundEffect()
        self.sndEffect.setVolume(1)
        # Задаем файл-источник
        fn = QtCore.QUrl.fromLocalFile(os.path.abspath("gui_sound/start.wav"))
        self.sndEffect.setSource(fn)
        self.sndEffect.setLoopCount(1)



    @staticmethod
    def load_data(sp):
        """Функция загрузки базы данных и заставки
        """
        if pass_dlg.QChek.isChecked():
            for i in range(1, 4):  # пауза перед запуском

                sp.showMessage('"Я знаю только то, что я ничего не знаю"'
                               "\n                                                                                            "
                               'Сократ',
                               QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.black)
                QtWidgets.qApp.processEvents()  # Запускаем оборот цикла(выход в основной цикл) для избежания зацикливания ("зависания")
                time.sleep(1)

        window.loaddata()  # обновление состояния БД


if pass_dlg.exec_() == QtWidgets.QDialog.Accepted:  # условие валидации пароля

    ################################################################
    # ОТОБРАЖЕНИЕ ЗАСТАВКИ
    ################################################################
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap("gui_images/girl.jpg"))  # файл для отображения
    splash.setCursor(QtCore.Qt.BusyCursor)  # смена курсора
    if pass_dlg.QChek.isChecked():  # True или False, флажок отображать заставку
        splash.show()  # Отображаем заставку
    splach_screen = MyWindow()  # экран заставки
    ###########################################################################
    # ОТОБРАЖЕНИЕ ГЛАВНОГО ОКНА, ЗАСТАВКИ, ПОЗИЦИОНИРОВАНИЕ ГЛАВНОГО ОКНА И ПРОИГРЫВАНИЕ МУЗЫКИ
    ###########################################################################
    window = MainWindow()  # главное окно
    window.move(window.width() * -2, 0)  # расположение точно по центру экрана
    window.setWindowIcon(window.ico)  # значок для окна
    desktop = QtWidgets.QApplication.desktop()  # расположение точно по центру экрана
    x = (desktop.width() - window.frameSize().width()) // 2  # расположение точно по центру экрана
    y = (desktop.height() - window.frameSize().height()) // 2  # расположение точно по центру экрана
    window.move(x, y)  # расположение точно по центру экрана
    splach_screen.load_data(splash)  # Отображаем данные заставки
    splash.finish(splach_screen)  # Скрываем заставку
    splach_screen.sndEffect.play()  # Проигрываем музыку
    window.show()  # window.showMaximized()  # в максимальный размер экрана


sys.exit(app.exec_())  # бесконечный цикл для отображения
