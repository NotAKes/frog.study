import sys
import sqlite3
from hashlib import sha256
from PyQt6.QtGui import QIcon, QFont, QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QWidget, QVBoxLayout, QDialog, \
    QLineEdit
from ui.settings_pageUI import Ui_Form_Settings
from ui.main_pageUI import Ui_MainWindow
from ui.account_pageUI import Ui_AccountWindow
from ui.study_pageUI import Ui_Form_Study
from ui.paragraph_pageUI import Ui_Form_Paragraph
from ui.login_pageUI import Ui_LoginWindow
from PyQt6 import QtCore, QtWidgets

text_size = 17


class LoginWindow(QDialog, Ui_LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('One-frog.Study')
        self.setWindowIcon(QIcon('logo_favicon.png'))
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_button.clicked.connect(self.change_visibility)
        self.loginstudent_button.clicked.connect(self.login_as_student)
        self.loginadmin_button.clicked.connect(self.login_as_admin)

    def login_as_student(self):
        self.second_form = Mainwindow(1)
        self.second_form.show()
        self.close()

    def login_as_admin(self):
        con = sqlite3.connect('db_name.sqlite')
        # Выполнение запроса и получение
        self.admin = con.cursor().execute(f""" SELECT id, password FROM users
                                                                        WHERE is_admin = 1 AND username = '{self.login_input.text()}'""").fetchone()
        con.close()
        if not bool(self.admin):
            self.error_label.setText('Неверный логин \nили пароль')
            return
        if not sha256(self.password_input.text().encode('utf-8')).hexdigest() == self.admin[1]:
            self.error_label.setText('Неверный логин \nили пароль')
            return
        self.second_form = Mainwindow(self.admin[0])
        self.second_form.show()
        self.close()

    def change_visibility(self):
        if self.password_input.echoMode() == QLineEdit.EchoMode.Password:
            self.password_button.setText('Скрыть пароль?')
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_button.setText('Показать пароль?')
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)


class Mainwindow(QMainWindow, Ui_MainWindow):

    # FIXME НЕТ ЗАПРОСОВ В БД

    def __init__(self, id):
        super().__init__()
        # Инициализация и обновление данных
        self.id = id
        self.setupUi(self)
        pixmap = QPixmap('logo_main.png')
        self.logo.setPixmap(pixmap)
        self.setWindowTitle('One-frog.Study')
        self.setWindowIcon(QIcon('logo_favicon.png'))
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
        self.student_progress = con.cursor().execute(f""" SELECT math_progression,phys_progression,bio_progression,chem_progression FROM users
                                                                        WHERE id = '{self.id}'""").fetchone()
        # Запись успеваемости в шкалы успеваемости каждого предмета
        self.math_progression.setValue(self.student_progress[0])
        self.phys_progression.setValue(self.student_progress[1])
        self.bio_progression.setValue(self.student_progress[2])
        self.chem_progression.setValue(self.student_progress[3])
        con.close()

    # Функции открытия других окон
    def open_study_window(self):
        self.second_form = StudyWindow(self.sender().text())
        self.second_form.show()

    def open_service_window(self):
        if self.sender().text() == 'Мой аккаунт':
            self.second_form = AccountWindow(self.id)
        elif self.sender().text() == 'Настройки':
            self.second_form = SettingsWindow(self.id)
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
    def __init__(self, id, *args):
        super().__init__()
        self.id = id
        self.setupUi(self)
        pixmap = QPixmap('logo_main.png')
        self.logo.setPixmap(pixmap)
        self.setWindowTitle('One-frog.Study')
        self.setWindowIcon(QIcon('logo_favicon.png'))
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
            self.second_form = AccountWindow(self.id)
        elif self.sender().text() == 'Главная':
            self.second_form = Mainwindow(self.id)
        self.second_form.show()
        self.close()


class AccountWindow(QMainWindow, Ui_AccountWindow):
    def __init__(self, id, *args):
        super().__init__()
        self.id = id
        self.setupUi(self)
        pixmap = QPixmap('logo_main.png')
        self.logo.setPixmap(pixmap)
        self.setWindowTitle('One-frog.Study')
        self.setWindowIcon(QIcon('logo_favicon.png'))
        self.ToMain.clicked.connect(self.open_service_window)
        self.ToSettings.clicked.connect(self.open_service_window)

    def open_service_window(self):
        if self.sender().text() == 'Настройки':
            self.second_form = SettingsWindow(self.id)
        elif self.sender().text() == 'Главная':
            self.second_form = Mainwindow(self.id)
        self.second_form.show()
        self.close()


class StudyWindow(QWidget, Ui_Form_Study):
    def __init__(self, sclass, *args):
        super().__init__()
        self.sclass = sclass
        self.setupUi(self)

        self.get_paragraphs_title()
        self.fill_scrollareas('author', self.paragraphs_title_authors)
        self.setWindowTitle('One-frog.Study')
        self.setWindowIcon(QIcon('logo_favicon.png'))
        self.title.setText(self.sclass)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def fill_scrollareas(self, author, authors_list):
        authors_list = authors_list
        self.vbox = QVBoxLayout()
        self.widget = QWidget()
        for i in authors_list:
            self.button = QPushButton(i[0])
            self.button.clicked.connect(self.open_paragraph_window)
            self.vbox.addWidget(self.button)
        self.widget.setLayout(self.vbox)
        if author == 'author':
            self.authorscrollArea.setWidget(self.widget)
        elif author == 'user':
            self.userScrollArea.setWidget(self.widget)

    def get_paragraphs_title(self):
        con = sqlite3.connect('db_name.sqlite')
        # Выполнение запроса и получение
        self.paragraphs_title_authors = con.cursor().execute(f""" SELECT title FROM articles
                                                                 WHERE sclass = '{self.sclass}' """).fetchall()
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
        self.goback.setIcon(QIcon('arrow_back.png'))
        self.setWindowTitle('One-frog.Study')
        self.setWindowIcon(QIcon('logo_favicon.png'))
        self.title.setText(self.title_text)
        self.markasread.clicked.connect(self.changestatus)
        con = sqlite3.connect('db_name.sqlite')
        #
        self.paragraph_info = con.cursor().execute(f""" SELECT paragraph_text, id, is_read FROM articles
                                                                         WHERE title = '{self.title_text}' """).fetchone()
        con.close()
        if bool(self.paragraph_info[2]):
            self.markasread.setChecked(True)
            self.markasread.setText('Параграф прочитан')
        self.paragraph_id = self.paragraph_info[1]
        self.paragraph.setText(self.paragraph_info[0])
        font = QFont()
        font.setPointSize(text_size)
        self.paragraph.setFont(font)

    def changestatus(self):
        con = sqlite3.connect('db_name.sqlite')
        if self.markasread.text() == 'Параграф не прочитан':
            self.markasread.setText('Параграф прочитан')

            con.cursor().execute(f"""UPDATE articles 
                                    SET is_read = 1 
                                    WHERE id = {self.paragraph_id}""")
            con.commit()
        elif self.markasread.text() == 'Параграф прочитан':
            con.cursor().execute(f"""UPDATE articles 
                                                SET is_read = 0 
                                                WHERE id = {self.paragraph_id}""")
            con.commit()
            self.markasread.setText('Параграф не прочитан')
        # Запросы на обновление процента выполнения по отдельному предмету
        # Получаем количество помеченных параграфов. Далее делим это количество на число всех параграфов, далее умножаем на 100 и округляем до целого
        percentage = round((con.cursor().execute(f""" SELECT count(*) FROM articles 
                                                    WHERE sclass = '{self.sclass}' and  is_read = 1""").fetchall()[0][
                                0] / con.cursor().execute(
            f""" SELECT count(*) FROM articles
                                                    WHERE sclass = '{self.sclass}'""").fetchall()[0][0]) * 100)
        print(percentage)
        con.close()

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
    main = LoginWindow()
    main.show()
    sys.exit(app.exec())
