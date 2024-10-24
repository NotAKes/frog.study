from PyQt6.QtWidgets import QWidget
from ui.math_pageUI import Ui_Form_Math


class MathWindow(QWidget, Ui_Form_Math):
    def __init__(self, *args):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)
        # self.pushButton.clicked.connect(self.run)

    def run(self):
        pass