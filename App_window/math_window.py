import sqlite3
import sys
from PyQt6.QtWidgets import QWidget
from PyQt6 import QtCore, QtWidgets
from ui.math_pageUI import Ui_Form_Math


class MathWindow(QWidget, Ui_Form_Math):
    def __init__(self, *args):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)

        # self.pushButton.clicked.connect(self.run)

    def get_paragraphs(self):
        con = sqlite3.connect('db_name.sqlite')
        # Выполнение запроса и получение всех результатов
        self.paragraphs = con.cursor().execute(""" """).fetchall()
        con.close()


    def run(self):
        pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MathWindow()
    window.show()
    sys.exit(app.exec())