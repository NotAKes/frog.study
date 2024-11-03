import sys
import sqlite3
from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtCore import QRectF
from PyQt6.QtWidgets import QLabel


class Paragraph_show(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.scrollArea = QtWidgets.QScrollArea()
        content_widget = QtWidgets.QWidget()
        self.scrollArea.setWidget(content_widget)
        self.scrollArea.setWidgetResizable(True)
        box1 = QtWidgets.QGridLayout(content_widget)
        self.main_label = QLabel()
        self.main_label.resize(10, 10)
        box1.addWidget(self.main_label)

        self.get_paragraph()
        box = QtWidgets.QHBoxLayout(self)

        box.addWidget(self.scrollArea)

    def get_paragraph(self):
        con = sqlite3.connect('paragraphs.sqlite')
        self.paragraphs = con.cursor().execute(""" """).fetchone()
        con.close()
        self.paragraphs = [f'wefiuhwefiojnwefijnwfijnwfijnw{QRectF(0, 0, 20, 20)}т\n\n\nijnwifojnwefijnweif']
        self.main_label.setText(self.paragraphs[0])



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Paragraph_show()
    window.show()
    sys.exit(app.exec())