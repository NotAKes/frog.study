import sys
import sqlite3
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QLabel
from ui.settings_pageUI import Ui_Form_Settings
from ui.main_pageUI import Ui_MainWindow
from ui.account_pageUI import Ui_AccountWindow
from PyQt6 import QtCore, QtWidgets
# from paragraph_page import Paragraph_show
from study_windows import StudyWindow

text_size = 1555


class Mainwindow(QMainWindow, Ui_MainWindow):

    # FIXME НЕТ ЗАПРОСОВ В БД

    def __init__(self):
        super().__init__()
        # Инициализация и обновление данных
        self.setupUi(self)
        self.setWindowTitle('One-frog.Study')
        self.setWindowIcon(QIcon('logo.png'))
        self.progress_update()
        self.ToSettings.clicked.connect(self.open_service_window)
        self.ToAccount.clicked.connect(self.open_service_window)
        self.send_button.clicked.connect(self.load_article)
        self.confirm_send.clicked.connect(self.send_article)
        for i in self.study_buttons.buttons():
            i.clicked.connect(self.open_study_window)
        self.title_edit.setPlaceholderText('Заголовок статьи...')
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
        self.second_form = StudyWindow(self.sender().text())
        self.second_form.show()

    def open_service_window(self):
        if self.sender().text() == 'Мой аккаунт':
            self.second_form = AccountWindow()
        if self.sender().text() == 'Настройки':
            self.second_form = SettingsWindow()
        self.second_form.show()
        self.close()

    # Отправка кастомных статей по разным предметам
    def load_article(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Выбрать файл', '',
            'Текстовый (*.txt)')[0]

        if fname[-4:] != '.txt':
            self.senders_text.setText(
                'Неподдерживаемый формат. Обрабатываются текстовые файлы(.txt) с кодировкой utf-8')
            return
        try:
            with open(fname, encoding='utf-8') as file:
                text = file.readlines()
                for i in text:
                    self.senders_text.setText(self.senders_text.toPlainText() + i)
        except UnicodeDecodeError:
            self.senders_text.setText(
                'Неподдерживаемый формат. Обрабатываются текстовые файлы(.txt) с кодировкой utf-8')
            return

    def send_article(self):
        con = sqlite3.connect('db_name.sqlite')
        # Запись кастомной статьи в Бд
        con.cursor().execute(""" """).fetchall()
        con.commit()
        con.close()


class SettingsWindow(QMainWindow, Ui_Form_Settings):
    def __init__(self, *args):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle('One-frog.Study')
        self.setWindowIcon(QIcon('logo.png'))
        self.textBrowser.setOpenExternalLinks(True)
        self.text_size.setValue(17)
        self.text_size.valueChanged.connect(self.fontsize_update)
        self.text_size.setMinimum(12)
        self.text_size.setMaximum(32)
        self.ToMain.clicked.connect(self.open_service_window)
        self.ToAccount.clicked.connect(self.open_service_window)

    def fontsize_update(self):
        global text_size
        text_size = self.text_size.value()

    def open_service_window(self):
        if self.sender().text() == 'Мой аккаунт':
            self.second_form = AccountWindow()
        elif self.sender().text() == 'Главная':
            self.second_form = Mainwindow()
        self.second_form.show()
        self.close()


class AccountWindow(QMainWindow, Ui_AccountWindow):
    def __init__(self, *args):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle('One-frog.Study')
        self.setWindowIcon(QIcon('logo.png'))
        self.ToMain.clicked.connect(self.open_service_window)
        self.ToSettings.clicked.connect(self.open_service_window)

    def open_service_window(self):
        if self.sender().text() == 'Настройки':
            self.second_form = SettingsWindow()
        elif self.sender().text() == 'Главная':
            self.second_form = Mainwindow()
        self.second_form.show()
        self.close()


def get_fontsize():
    return text_size


if __name__ == '__main__':  # запуск мейн окна
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    main = Mainwindow()

    main.show()
    sys.exit(app.exec())
