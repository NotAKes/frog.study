import sys
import sqlite3
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QLabel, QWidget, QVBoxLayout
from ui.settings_pageUI import Ui_Form_Settings
from ui.main_pageUI import Ui_MainWindow
from ui.account_pageUI import Ui_AccountWindow
from ui.study_pageUI import Ui_Form_Study
from ui.paragraph_pageUI import Ui_Form_Paragraph
from PyQt6 import QtCore, QtWidgets

text_size = 17


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
        elif self.sender().text() == 'Настройки':
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
        self.text_size.setValue(text_size)
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


class StudyWindow(QWidget, Ui_Form_Study):
    def __init__(self, sclass, *args):
        super().__init__()
        self.sclass = sclass
        self.setupUi(self)
        self.get_paragraphs_title()
        self.fill_scrollareas('author', [str(i) for i in range(10)])
        self.fill_scrollareas('user', [str(i) for i in range(10, 20)])
        self.setWindowTitle('One-frog.Study')
        self.setWindowIcon(QIcon('logo.png'))
        self.title.setText(self.sclass)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def fill_scrollareas(self, author, authors_list):
        authors_list = authors_list
        self.vbox = QVBoxLayout()
        self.widget = QWidget()
        for i in authors_list:
            self.button = QPushButton(i)
            self.button.clicked.connect(self.open_paragraph_window)
            self.vbox.addWidget(self.button)
        self.widget.setLayout(self.vbox)
        if author == 'author':
            self.authorscrollArea.setWidget(self.widget)
        elif author == 'user':
            self.userScrollArea.setWidget(self.widget)

    def get_paragraphs_title(self):
        con = sqlite3.connect('db_name.sqlite')
        # Выполнение запроса и получение всех результатов
        self.paragraphs_title_authors = con.cursor().execute(""" """).fetchall()
        self.paragraphs_title_users = con.cursor().execute(""" """).fetchall()
        con.close()

    def open_paragraph_window(self):
        self.second_form = ParagraphWindow(self.sender().text(), self.sclass)
        self.second_form.show()
        self.close()


class ParagraphWindow(QWidget, Ui_Form_Paragraph):
    def __init__(self, title, sclass, *args):
        super().__init__()
        self.title_text = title
        self.sclass = sclass
        self.setupUi(self)
        self.goback.clicked.connect(self.open_study_window)
        self.setWindowTitle('One-frog.Study')
        self.setWindowIcon(QIcon('logo.png'))
        self.title.setText(self.title_text)
        self.markasread.clicked.connect(self.changestatus)
        self.paragraph.setText('wefewfwefwefwefwefwef')
        font = QFont()
        font.setPointSize(text_size)
        self.paragraph.setFont(font)

    def changestatus(self):
        if self.markasread.text() == 'Параграф не прочитан':
            self.markasread.setText('Параграф прочитан')
            ## TODO ЗАПРОС В БД
        elif self.markasread.text() == 'Параграф прочитан':
            ## TODO ЗАПРОС В БД
            self.markasread.setText('Параграф не прочитан')

    def open_study_window(self):
        self.second_form = StudyWindow(self.sclass)
        self.second_form.show()
        self.close()


if __name__ == '__main__':  # запуск мейн окна
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    main = Mainwindow()
    main.show()
    sys.exit(app.exec())
