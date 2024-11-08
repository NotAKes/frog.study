import sys
import sqlite3

from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton

from ui.main_pageUI import Ui_MainWindow
from PyQt6 import QtCore, QtWidgets
from study_windows import MathWindow, PhysWindow, BioWindow, ChemWindow
from service_windows import SettingsWindow, AccountWindow


# Наследуемся от виджета из PyQt6.QtWidgets и от класса с интерфейсом
class Mainwindow(QMainWindow, Ui_MainWindow):

    # FIXME НЕТ ЗАПРОСОВ В БД

    def __init__(self):

        super().__init__()
        # Инициализация и обновление данных
        self.setupUi(self)
        self.progress_update()
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
        if self.sender().text() == 'Перейти в свой аккаунт':
            self.second_form = AccountWindow(self)
        if self.sender().text() == 'Настройки':
            self.second_form = SettingsWindow(self)
        ex.close()

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


if __name__ == '__main__':  # запуск мейн окна
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    ex = Mainwindow()
    ex.show()
    sys.exit(app.exec())
