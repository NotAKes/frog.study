import sqlite3
import sys
from PyQt6.QtWidgets import QWidget
from PyQt6 import QtCore, QtWidgets
from ui.math_pageUI import Ui_Form_Math


class SettingsWindow(QWidget, Ui_Form_Math):
    def __init__(self, *args):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        pass


class AccountWindow(QWidget, Ui_Form_Math):
    def __init__(self, *args):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        pass
