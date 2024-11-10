import sys
import sqlite3

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton

from ui.settings_pageUI import Ui_Form_Settings
from ui.main_pageUI import Ui_MainWindow
from PyQt6 import QtCore, QtWidgets
from study_windows import MathWindow, PhysWindow, BioWindow, ChemWindow


class Mainwindow(QMainWindow, Ui_MainWindow):

    # FIXME НЕТ ЗАПРОСОВ В БД

    def __init__(self):

        super().__init__()
        # Инициализация и обновление данных
        self.setupUi(self)
        self.setWindowTitle('One-frog.Study')
        self.setWindowIcon(QIcon('logo.png'))
        self.progress_update()
        self.ToSettings.clicked.connect(self.open_service_window)
        self.send_button.clicked.connect(self.send_article)
        self.math_button.clicked.connect(self.open_study_window)
        self.senders_text.setPlaceholderText('Написать здесь...')

    def progress_update(self):

        con = sqlite3.connect('db_name.sqlite')
        # Выполнение запроса и получение результатов по успеваемости
        self.student_progress = con.cursor().execute(""" """).fetchall()
        # Запись успеваемости в шкалы успеваемости каждого предмета
        # # TODO: доделать запись
        # # self.math_progression.setValue()
        # # self.phys_progression.setValue()
        # # self.bio_progression.setValue()
        # # self.chem_progression.setValue()
        con.close()

    # Функции открытия других окон
    # # TODO: доделать окна

    def open_study_window(self):
        if self.sender().text() == 'Математика':
            self.second_form = MathWindow(self)
        if self.sender().text() == 'Физика':
            self.second_form = PhysWindow(self)
        if self.sender().text() == 'Химия':
            self.second_form = ChemWindow(self)
        if self.sender().text() == 'Биология':
            self.second_form = BioWindow(self)
        self.second_form.show()

    def open_service_window(self):
        # if self.sender().text() == 'Перейти в свой аккаунт':
        # self.second_form = AccountWindow()
        if self.sender().text() == 'Настройки':
            self.second_form = SettingsWindow()
            self.second_form.show()
        self.close()

    # Отправка кастомных статей по разным предметам
    def send_article(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Выбрать файл', '',
            'Текстовый (*.txt)')[0]
        if fname[-4:] != '.txt':
            return
        with open(fname, encoding='utf-8') as file:
            text = file.readlines()
            for i in text:
                self.senders_text.setText(self.senders_text.toPlainText() + i)
        con = sqlite3.connect('db_name.sqlite')
        # Запись кастомной статьи в Бд
        con.cursor().execute(""" """).fetchall()
        con.commit()
        con.close()


class SettingsWindow(QMainWindow, Ui_Form_Settings):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('One-frog.Study')
        self.setWindowIcon(QIcon('logo.png'))
        self.textBrowser.setOpenExternalLinks(True)
        self.ToMain.clicked.connect(self.tomain)

    def tomain(self):  # функция для возращения на домашнюю страницу
        self.mainwindow = Mainwindow()
        self.mainwindow.show()
        self.close()


# class AccountWindow(QWidget, Ui_Form_Math):
#     def __init__(self, *args):
#         super().__init__()
#         # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
#         pass


if __name__ == '__main__':  # запуск мейн окна
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    main = Mainwindow()

    main.show()
    sys.exit(app.exec())
