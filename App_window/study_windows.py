import sqlite3
import sys
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QIcon
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import Qt
from ui.study_pageUI import Ui_Form_Study
from ui.paragraph_pageUI import Ui_Form_Paragraph


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


class ParagraphWindow(QWidget, Ui_Form_Paragraph):
    def __init__(self, title, *args):
        super().__init__()
        self.title_text = title
        self.setupUi(self)
        self.setWindowTitle('One-frog.Study')
        self.setWindowIcon(QIcon('logo.png'))
        self.title.setText(self.title_text)
        ## FIXME
        # self.markasread.setAlignment(Qt.AlignmentFlag.AlignRight)


if __name__ == '__main__':  # запуск мейн окна
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    main = ParagraphWindow('tewr')

    main.show()
    sys.exit(app.exec())
