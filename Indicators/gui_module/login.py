##-*- coding: utf-8 -*-
# version 0.2a
# author: andrew.bezzubov - 07/03/2021
# email: ruizcontrol@yandex.ru, agb2019@list.ru
# https://github.com/alex-markov-creator/tendency.git
# GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""
===============================================================
login.py - модуль для отображения логин-окна.
# ПРЕДПОЛАГАЕМЫЕ ИЗМЕНЕНИЯ в последующих версиях:
# - реализовать возможность сохранения установленного значения флажка "Отображать заставку" перед последующим запуском
# ПОСЛЕДУЮЩИЕ ВЕРСИИ(варианты):
# - добавить иконку в виде двери со стрелочкой на кнопку "Войти"
"""
from PyQt5 import QtWidgets, QtGui, QtCore

WIDTH = 310  # Ширина
HEIGHT = 150  # Высота
FONT_RESIZE = 8  # Размер шрифта
PASSWORD = "0000"  # ПАРОЛЬ
ICON_LOGIN = 'icon/login.png'  # Директория иконки


##########################################################################
# Окно ввода пароля
##########################################################################
class LoginDialog(QtWidgets.QDialog):
    """Класс диалогового окна для входа в приложение
    """

    def __init__(self, *args, **kwargs):
        """Инициализация
        """
        super(LoginDialog, self).__init__(*args, **kwargs)
        self.setFixedWidth(WIDTH)  # Глобальная переменная
        self.setFixedHeight(HEIGHT)  # Глобальная переменная
        layout = QtWidgets.QVBoxLayout()
        self.passinput = QtWidgets.QLineEdit()

        self.passinput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passinput.setPlaceholderText("Введите пароль")
        self.passinput.setText(PASSWORD)  # Пароль для тестирования
        self.passinput.setToolTip("Ввод пароля")
        self.passinput.setWhatsThis("Текстовое поле для ввода пароля")
        self.QBtn = QtWidgets.QPushButton("Войти")
        self.QBtn.setCursor(QtCore.Qt.PointingHandCursor)  # смена курсора
        self.QBtn.setWhatsThis("Кнопка входа в приложение")
        self.QChek = QtWidgets.QCheckBox("Отображать заставку при запуске")
        self.QChek.setCheckState(QtCore.Qt.Checked)
        self.QBtn.setStyleSheet("font-weight: bold")
        self.setWindowTitle('Идентификация')
        self.setWindowIcon(QtGui.QIcon(ICON_LOGIN))  # Глобальная переменная
        self.QBtn.clicked.connect(self.login)
        title = QtWidgets.QGroupBox("Вы - администратор, пароль - " + "'" + PASSWORD + "'")  # Глобальная переменная
        title.setFont(QtGui.QFont("Sansserif ", FONT_RESIZE))  # Глобальная переменная
        title.setStyleSheet("font-weight: bold")
        layout.addWidget(title)
        title_layout = QtWidgets.QVBoxLayout()
        title_layout.addWidget(self.passinput)
        title_layout.addWidget(self.QChek)
        title.setLayout(title_layout)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)
        self.passinput.selectAll() # выделение пароля
    def login(self):
        """Проверка пароля
        """
        if self.passinput.text() == PASSWORD:

            self.accept()
        else:

            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Неправильный пароль')


# Тестирование
if __name__ == "__main__":
    import sys

    ICON_LOGIN = '../icon/login.png'  # Глобальная переменная
    app = QtWidgets.QApplication(sys.argv)
    passdlg = LoginDialog()
    passdlg.show()
    sys.exit(app.exec_())
