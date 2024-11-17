import sqlite3
import sys
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QIcon
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import Qt
from ui.study_pageUI import Ui_Form_Study

class StudyWindow(QWidget, Ui_Form_Study):
    def __init__(self, sclass, *args):
        super().__init__()
        self.sclass = sclass
        self.setupUi(self)
        self.setWindowTitle('One-frog.Study')
        self.setWindowIcon(QIcon('logo.png'))
        self.title.setText(self.sclass)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
    def get_paragraphs(self):
        con = sqlite3.connect('db_name.sqlite')
        # Выполнение запроса и получение всех результатов
        self.paragraphs = con.cursor().execute(""" """).fetchall()
        con.close()

