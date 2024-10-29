import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui.main_pageUI import Ui_MainWindow
from PyQt6 import QtCore, QtWidgets
from math_window import MathWindow


# Наследуемся от виджета из PyQt6.QtWidgets и от класса с интерфейсом
class Mainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Получение успеваемости на каждом уроке
        self.progress_update()
        self.setupUi(self)
        self.math_button.clicked.connect(self.open_math)



    def progress_update(self):
        con = sqlite3.connect('student_progress.sqlite')
        # Выполнение запроса и получение всех результатов
        self.student_progress = con.cursor().execute(""" """).fetchall()
        con.close()

    def open_math(self):
        self.second_form = MathWindow(self)
        self.second_form.show()


if __name__ == '__main__':
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    ex = Mainwindow()
    ex.show()
    sys.exit(app.exec())
