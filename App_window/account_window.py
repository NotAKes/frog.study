
from ui.account_pageUI import Ui_Account_Form
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from PyQt6 import QtCore, QtWidgets
import sqlite3


class AccountWindow(QMainWindow, Ui_Account_Form):
    def __init__(self, *args):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)

        # self.pushButton.clicked.connect(self.run)


    def run(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = AccountWindow()
    window.show()
    sys.exit(app.exec())
