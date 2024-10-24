import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from ui.main_pageUI import Ui_MainWindow
from PyQt6 import QtCore, QtWidgets
from math_window import MathWindow


# Наследуемся от виджета из PyQt6.QtWidgets и от класса с интерфейсом
class Mainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)
        self.math_button.clicked.connect(self.open_math)

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
