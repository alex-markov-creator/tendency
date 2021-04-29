#-*- coding: utf-8 -*-
# version 0.2a
# author: andrew.bezzubov - 07/03/2021
# email: ruizcontrol@yandex.ru, agb2019@list.ru
# https://github.com/alex-markov-creator/tendency.git
# GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""
about.py - окно с информацией о программе
"""
from PyQt5 import QtWidgets, QtGui

WIDTH = 370  # Ширина - глобальная пременная
HEIGHT = 385  # Высота - глобальная переменная
ICON_ABOUT = 'gui_icon/title_icon.png'  # Глобальная переменная - путь к файлу


##########################################################################
# Окно о программе
##########################################################################

class AboutDialog(QtWidgets.QDialog):
    """Класс диалогового окна о программе
    """

    def __init__(self, *args, **kwargs):
        """Инициализация
        """
        super(AboutDialog, self).__init__(*args, **kwargs)
        self.setWindowTitle('О программе')
        self.setFixedWidth(WIDTH)  # Глобальная переменная - ширина
        self.setFixedHeight(HEIGHT)  # Глобальная переменная - высота
        self.setWindowIcon(QtGui.QIcon(ICON_ABOUT))  # Глобальная переменная - путь к файлу
        q_btn = QtWidgets.QDialogButtonBox.Ok
        self.buttonBox = QtWidgets.QDialogButtonBox(q_btn)
        self.buttonBox.accepted.connect(self.accept)
        # self.buttonBox.rejected.connect(self.reject)
        layout = QtWidgets.QVBoxLayout()
        title = QtWidgets.QLabel("Информационная Система\nУправления Качеством")
        font = title.font()
        font.setPointSize(18)
        title.setFont(font)
        labelpic = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap(ICON_ABOUT)  # Глобальная переменная
        pixmap = pixmap.scaledToWidth(375)
        labelpic.setPixmap(pixmap)
        labelpic.setFixedHeight(350)
        layout.addWidget(title)
        layout.addWidget(QtWidgets.QLabel("version 0.2a\n"
                                "@GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007"
                                "\nauthor: andrew.bezzubov - 2021-2022 years"
                                "\nhttps://github.com/alex-markov-creator/tendency.git"
                                "\nemail: agb2019@list.ru.\n"
                                "\nGui - интерфейс для просмотра значений и графиков"
                                "\nпо показателям процессов системы менеджмента"
                                "\nкачества.\n"
                                ))
        layout.addWidget(labelpic)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

# Тестирование запуска
if __name__ == "__main__":
    import sys
    ICON_ABOUT = '../gui_icon/title_icon.png'  # Глобальная переменная - путь к файлу
    app = QtWidgets.QApplication(sys.argv)
    run_about = AboutDialog()
    run_about.show()
    sys.exit(app.exec_())
