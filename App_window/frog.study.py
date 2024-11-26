import sys
import sqlite3
from hashlib import sha256
from xlsxwriter.workbook import Workbook
from PyQt6.QtGui import QIcon, QFont, QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QWidget, QVBoxLayout, QDialog, \
    QLineEdit
from settings_pageUI import Ui_Form_Settings
from main_pageUI import Ui_MainWindow
from account_pageUI import Ui_AccountWindow
from study_pageUI import Ui_Form_Study
from edit_pageUI import Ui_Form_Edit
from paragraph_pageUI import Ui_Form_Paragraph
from login_pageUI import Ui_LoginWindow
from reg_pageUI import Ui_RegWindow
from PyQt6 import QtCore, QtWidgets

# Стандартный размер текста и словарь для облегчения работы с бд
text_size = 17
dict_of_sclass = {
    'Математика': 'math_progression',
    'Физика': 'phys_progression',
    'Биология': 'bio_progression',
    'Химия': 'chem_progression',
}


class LoginWindow(QDialog, Ui_LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # описание окна
        self.setWindowTitle('One-frog.Study')
        self.setWindowIcon(QIcon('logo_favicon.png'))
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_button.clicked.connect(self.change_visibility)
        self.loginstudent_button.clicked.connect(self.login_as_student)
        self.loginadmin_button.clicked.connect(self.login_as_admin)

    def login_as_student(self):
        # вход ученика
        self.second_form = Mainwindow(1, False)  # для входа ученику пароль не требуется
        self.second_form.show()
        self.close()

    def login_as_admin(self):
        # вход админа
        con = sqlite3.connect('db_name.sqlite')
        # Выполнение запроса и получение
        self.admin = con.cursor().execute(f""" SELECT id, password FROM users
                                            WHERE is_admin = 1 AND username = '{self.login_input.text()}'""").fetchone()
        con.close()
        if not bool(self.admin):
            self.error_label.setText('Неверный логин \nили пароль')  # сообщаем об ошибке если поля пустые
            return
        # сравнения шифра введенного пароля с паролем в бд
        if not sha256(self.password_input.text().encode('utf-8')).hexdigest() == self.admin[1]:
            self.error_label.setText('Неверный логин \nили пароль')
            return
        self.second_form = Mainwindow(self.admin[0], True)
        self.second_form.show()
        self.close()

    def change_visibility(self):  # функционал показа/скрытия пароля
        if self.password_input.echoMode() == QLineEdit.EchoMode.Password:
            self.password_button.setText('Скрыть пароль?')
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_button.setText('Показать пароль?')
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)


class RegiseradminWindow(QDialog, Ui_RegWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # описание окна
        self.setWindowTitle('One-frog.Study')
        self.setWindowIcon(QIcon('logo_favicon.png'))
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.regadmin_button.clicked.connect(self.regadmin)
        self.password_button.clicked.connect(self.change_visibility)

    def regadmin(self):
        self.error_label.setText('')
        # ошибка, если пустой логин
        if not self.login_input.text():
            self.error_label.setText('Некорректный логин')
            return
        # ошибка, если пароли не совпадают
        if not (self.password_input.text() == self.password_input_2.text()):
            self.error_label.setText('Пароли не \nсовпадают')
            return
        # запрос и обновление
        con = sqlite3.connect('db_name.sqlite')
        check_name = con.cursor().execute(f""" SELECT id from users
                                                        WHERE username = '{self.login_input.text()}'""").fetchone()
        if bool(check_name):  # ошибка, если логин уже существует
            self.error_label.setText('Такое имя уже существует')
            return
        # запись
        progression = con.cursor().execute("""SELECT math_progression,phys_progression, 
                                    bio_progression,chem_progression, overall_progression from users""").fetchone()
        # запрос с записью всего в поля нового админа
        con.cursor().execute(f"""INSERT INTO users(username, password, is_admin, 
        math_progression,phys_progression,bio_progression,chem_progression, overall_progression) 
        VALUES('{self.login_input.text()}','{sha256(self.password_input.text().encode('utf-8')).hexdigest()}',
        1,{progression[0]},{progression[1]},{progression[2]},{progression[3]},{progression[4]})""")
        con.commit()
        con.close()
        self.second_form = LoginWindow()  # Открытие окна логина
        self.second_form.show()
        self.close()

    def change_visibility(self):  # функционал показа/скрытия пароля
        if self.password_input.echoMode() == QLineEdit.EchoMode.Password:
            self.password_button.setText('Скрыть пароль?')
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
            self.password_input_2.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_button.setText('Показать пароль?')
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
            self.password_input_2.setEchoMode(QLineEdit.EchoMode.Password)


class Mainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self, id, is_admin):
        super().__init__()
        # Инициализация и обновление данных
        self.id = id
        self.is_admin = is_admin
        self.setupUi(self)  # описание окна, введение информации о пользователе
        if not self.is_admin:
            self.admin_warning.hide()
        pixmap = QPixmap('logo_main.png')
        self.logo.setPixmap(pixmap)
        self.setWindowTitle('One-frog.Study')
        self.setWindowIcon(QIcon('logo_favicon.png'))
        self.progress_update()
        self.ToSettings.clicked.connect(self.open_service_window)
        self.ToAccount.clicked.connect(self.open_service_window)
        self.send_button.clicked.connect(self.load_article)
        self.confirm_send.clicked.connect(self.send_article)
        self.update_progress.clicked.connect(self.progress_update)
        for i in self.study_buttons.buttons():
            i.clicked.connect(self.open_study_window)
        self.title_edit.setPlaceholderText('Заголовок статьи...')
        self.senders_text.setPlaceholderText('Написать здесь...')

    def progress_update(self):

        con = sqlite3.connect('db_name.sqlite')
        # Выполнение запроса и получение результатов по успеваемости
        self.student_progress = con.cursor().execute(f""" SELECT math_progression,phys_progression,
                                                        bio_progression,chem_progression FROM users
                                                                        WHERE id = '{self.id}'""").fetchone()
        # Запись успеваемости в шкалы успеваемости каждого предмета
        self.math_progression.setValue(self.student_progress[0])
        self.phys_progression.setValue(self.student_progress[1])
        self.bio_progression.setValue(self.student_progress[2])
        self.chem_progression.setValue(self.student_progress[3])
        con.close()

    # Функции открытия других окон
    def open_study_window(self):
        # откртие окна со статьями
        self.second_form = StudyWindow(self.sender().text(), self.id, self.is_admin)
        self.second_form.show()

    def open_service_window(self):
        # открытие других окон типа mainwindow
        if self.sender().text() == 'Мой аккаунт':
            self.second_form = AccountWindow(self.id, self.is_admin)
        elif self.sender().text() == 'Настройки':
            self.second_form = SettingsWindow(self.id, self.is_admin)
        self.second_form.show()
        self.close()

    # Отправка кастомных статей по разным предметам
    def load_article(self):
        # подгрузка файла от пользователя
        fname = QFileDialog.getOpenFileName(
            self, 'Выбрать файл', '',
            'Текстовый (*.txt)')[0]
        # обработка ошибок
        if fname[-4:] != '.txt':
            self.senders_text.setText(
                'Неподдерживаемый формат. Обрабатываются текстовые файлы(.txt) с кодировкой utf-8')
            return
        try:
            with open(fname, encoding='utf-8') as file:
                text = file.readlines()
                for i in text:
                    self.senders_text.setText(self.senders_text.toPlainText() + i)  # внесение текста статьи в поле
        except UnicodeDecodeError:
            self.senders_text.setText(
                'Неподдерживаемый формат. Обрабатываются текстовые файлы(.txt) с кодировкой utf-8')
            return

    def send_article(self):
        self.error_label.setText('')
        # ошибка, если поля пустые
        if not self.title_edit.text() or not self.senders_text.toPlainText():
            self.error_label.setText('Заполните все поля\nдля загрузки')
            return
        con = sqlite3.connect('db_name.sqlite')
        # Запись кастомной статьи в Бд
        con.cursor().execute(f"""INSERT INTO articles(sclass, title, paragraph_text, author_id) 
                             VALUES('{self.sclass_pick.currentText()}',
                                    '{self.title_edit.text()}',
                                    '{self.senders_text.toPlainText()}',
                                     {self.id})""").fetchall()
        con.commit()
        con.close()
        self.success_label.setText('Успешно!\nДля обновления успеваемости\nперейдите на страницу статьи')


class SettingsWindow(QMainWindow, Ui_Form_Settings):
    def __init__(self, id, is_admin, *args):
        super().__init__()
        self.id = id
        self.is_admin = is_admin
        self.setupUi(self)  # описание окна, введение информации о пользователе
        if not self.is_admin:
            self.reg_admin_btn.hide()
        self.get_nickname()
        pixmap = QPixmap('logo_main.png')
        self.logo.setPixmap(pixmap)
        self.setWindowTitle('One-frog.Study')
        self.setWindowIcon(QIcon('logo_favicon.png'))
        self.textBrowser.setOpenExternalLinks(True)
        self.text_size.setValue(text_size)
        self.text_size.valueChanged.connect(self.fontsize_update)
        self.text_size.setMinimum(12)
        self.text_size.setMaximum(32)
        for i in self.change_window.buttons():
            i.clicked.connect(self.open_window)

    def get_nickname(self):
        #  Получение ника, подставления айди, если ника нет
        con = sqlite3.connect('db_name.sqlite')
        nickname = con.cursor().execute(f""" SELECT username FROM users
                                                     WHERE id = {self.id} """).fetchone()[0]
        con.commit()
        con.close()
        if nickname:
            self.nickname.setText('Вы вошли как: ' + nickname)
        else:
            self.nickname.setText('Вы вошли как: id:' + str(self.id))

    def fontsize_update(self):
        # Изменение размера шрифта пользователем
        global text_size
        text_size = self.text_size.value()

    def open_window(self):
        # Смена окон
        if self.sender().text() == 'Мой аккаунт':
            self.second_form = AccountWindow(self.id, self.is_admin)
        elif self.sender().text() == 'Главная':
            self.second_form = Mainwindow(self.id, self.is_admin)
        elif self.sender().text() == 'Создать админский аккаунт':
            self.second_form = RegiseradminWindow()
        elif self.sender().text() == 'Войти в другой аккаунт?':
            self.second_form = LoginWindow()
        self.second_form.show()
        self.close()


class AccountWindow(QMainWindow, Ui_AccountWindow):
    def __init__(self, id, is_admin, *args):
        super().__init__()
        self.id = id
        self.is_admin = is_admin
        self.setupUi(self)  # описание окна, введение информации о пользователе
        if not self.is_admin:
            self.admin_frame.hide()
            self.download_button.hide()
        self.get_account_info()
        self.progress_scale_update()
        pixmap = QPixmap('logo_main.png')
        self.logo.setPixmap(pixmap)
        self.setWindowTitle('One-frog.Study')
        self.setWindowIcon(QIcon('logo_favicon.png'))
        self.ToMain.clicked.connect(self.open_service_window)
        self.ToSettings.clicked.connect(self.open_service_window)
        self.SaveButton_username.clicked.connect(self.update_account_info)
        self.SaveButton_passwd.clicked.connect(self.update_password)
        self.password_button.clicked.connect(self.change_visibility)
        self.download_button.clicked.connect(self.download_exel)

    # Запись в экселевский файл
    def download_exel(self):
        workbook = Workbook('results.xlsx')
        worksheet = workbook.add_worksheet()
        con = sqlite3.connect('db_name.sqlite')
        table = con.cursor().execute("""SELECT sclass,title,is_read from articles """)  # запрос на статьи
        for i, value in enumerate(['sclass', 'title', 'is_read']):  # заголовки в верхних ячейках
            worksheet.write(0, i, value)
        # запись статей
        for i, row in enumerate(table):
            for j, value in enumerate(row):
                worksheet.write(i + 1, j, value)
        # запрос на успеваемость
        table = con.cursor().execute("""SELECT math_progression,phys_progression, 
                                    bio_progression,chem_progression, overall_progression from users """).fetchone()
        for i, value in enumerate(['math_progression', 'phys_progression', 'bio_progression',
                                   'chem_progression', 'overall_progression']):  # заголовки в верхних ячейках
            worksheet.write(0, i + 4, value)
        # запись процетов успеваемости
        for i, value in enumerate(table):
            worksheet.write(1, i + 4, value)
        workbook.close()
        self.success_label_exel.setText('Успешно!')

    def update_password(self):
        self.error_label.setText('')
        # ошибка если пароли не совпадают
        if not (self.password_edit1.text() == self.password_edit2.text()):
            self.error_label.setText('Пароли не \nсовпадают')
            return
        # запрос и обновление
        con = sqlite3.connect('db_name.sqlite')
        con.cursor().execute(f"""UPDATE users
                                 SET password = '{sha256(self.password_edit1.text().encode('utf-8')).hexdigest()}'
                                 WHERE id = {self.id}""")
        con.commit()
        con.close()
        self.success_label.setText('Успешно!')

    def change_visibility(self):  # функционал показа/скрытия пароля
        if self.password_edit1.echoMode() == QLineEdit.EchoMode.Password:
            self.password_button.setText('Скрыть пароль?')
            self.password_edit1.setEchoMode(QLineEdit.EchoMode.Normal)
            self.password_edit2.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_button.setText('Показать пароль?')
            self.password_edit1.setEchoMode(QLineEdit.EchoMode.Password)
            self.password_edit2.setEchoMode(QLineEdit.EchoMode.Password)

    def get_account_info(self):
        con = sqlite3.connect('db_name.sqlite')
        # Выполнение запроса и получение информации об аккаунте
        self.NicknameEdit.setText(con.cursor().execute(f""" SELECT username FROM users
                                                                     WHERE id = {self.id} """).fetchone()[0])
        self.favoriteLabel.setText('Текущий любимый: ' + con.cursor().execute(f""" SELECT favorite FROM users
                                                                     WHERE id = {self.id} """).fetchone()[0])
        con.close()

    def update_account_info(self):
        con = sqlite3.connect('db_name.sqlite')
        # Выполнение запроса и изменение никнейма и любимого предмета
        con.cursor().execute(f"""UPDATE users
                                 SET username = '{self.NicknameEdit.text()}'
                                 WHERE id = {self.id}""")
        con.cursor().execute(f"""UPDATE users
                                 SET favorite = '{self.favoriteClass.currentText()}'
                                 WHERE id = {self.id}""")
        con.commit()
        con.close()
        self.get_account_info()

    def progress_scale_update(self):

        con = sqlite3.connect('db_name.sqlite')
        # Выполнение запроса и получение результатов по успеваемости
        self.student_progress = con.cursor().execute(f""" SELECT math_progression,phys_progression,bio_progression,
                                                                chem_progression,overall_progression FROM users
                                                                        WHERE id = '{self.id}'""").fetchone()
        # Запись успеваемости в шкалы успеваемости каждого предмета
        self.math_progression.setValue(self.student_progress[0])
        self.phys_progression.setValue(self.student_progress[1])
        self.bio_progression.setValue(self.student_progress[2])
        self.chem_progression.setValue(self.student_progress[3])
        self.overalllprogression.setValue(self.student_progress[4])
        con.close()

    def open_service_window(self):
        # открытие других окон
        if self.sender().text() == 'Настройки':
            self.second_form = SettingsWindow(self.id, self.is_admin)
        elif self.sender().text() == 'Главная':
            self.second_form = Mainwindow(self.id, self.is_admin)
        self.second_form.show()
        self.close()


class StudyWindow(QWidget, Ui_Form_Study):
    def __init__(self, sclass, id, is_admin, *args):
        super().__init__()
        self.id = id
        self.is_admin = is_admin
        self.sclass = sclass
        self.setupUi(self)  # описание окна, введение информации о пользователе
        self.get_paragraphs_title()
        self.fill_scrollareas('author', self.paragraphs_title_authors)
        self.fill_scrollareas('user', self.paragraphs_title_users)
        self.setWindowTitle('One-frog.Study')
        self.setWindowIcon(QIcon('logo_favicon.png'))
        self.title.setText(self.sclass)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def fill_scrollareas(self, author, authors_list):
        # получение списков статей+заполнение 2 qscrollarea по авторству
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
        # Выполнение запроса и получение 2 списков названий статей по авторству
        self.paragraphs_title_authors = con.cursor().execute(f""" SELECT title FROM articles
                                                         WHERE sclass = '{self.sclass}' AND author_id = 0""").fetchall()
        self.paragraphs_title_users = con.cursor().execute(f""" SELECT title FROM articles
                                                         WHERE sclass = '{self.sclass}' AND author_id != 0""").fetchall()
        con.close()

    def open_paragraph_window(self):
        # откртие окна со статьей
        self.second_form = ParagraphWindow(self.sender().text(), self.sclass, self.id, self.is_admin)
        self.second_form.show()
        self.close()


class ParagraphWindow(QWidget, Ui_Form_Paragraph):
    def __init__(self, title, sclass, id, is_admin, *args):
        super().__init__()
        self.id = id
        self.title_text = title
        self.sclass = sclass
        self.is_admin = is_admin
        self.setupUi(self)  # описание окна, введение информации о пользователе
        self.update_progress()
        self.goback.clicked.connect(self.open_study_window)
        self.goback.setIcon(QIcon('arrow_back.png'))
        self.edit_btn.setIcon(QIcon('edit_article.png'))
        self.edit_btn.clicked.connect(self.edit_article)
        self.delete_btn.setIcon(QIcon('delete_article.png'))
        self.delete_btn.clicked.connect(self.delete_article)
        self.setWindowTitle('One-frog.Study')
        self.setWindowIcon(QIcon('logo_favicon.png'))
        self.title.setText(self.title_text)
        self.markasread.clicked.connect(self.changestatus)
        con = sqlite3.connect('db_name.sqlite')
        # Получаем информацию о параграфе для дальнейшей обработки
        self.paragraph_info = con.cursor().execute(f""" SELECT paragraph_text, id, is_read FROM articles
                                                        WHERE title = '{self.title_text}' """).fetchone()
        con.close()
        # Помечаем параграф как прочитанный или непрочитанный
        if bool(self.paragraph_info[2]):
            self.markasread.setChecked(True)  # отмечаем чекбокс и меняем текст, если прочитано
            self.markasread.setText('Параграф прочитан')
        self.paragraph_id = self.paragraph_info[1]
        self.paragraph.setText(self.paragraph_info[0])
        font = QFont()
        font.setPointSize(text_size)  # Изменяем размер текста, на указанный пользователем
        self.paragraph.setFont(font)

    def changestatus(self):
        # Считываем изменения в чекбоксе
        # Меняем статуст статьи
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
        con.close()
        self.update_progress()

    def update_progress(self):
        con = sqlite3.connect('db_name.sqlite')
        # Запросы на обновление процента выполнения по отдельному предмету
        # Получаем количество помеченных параграфов. Далее делим это количество на число всех параграфов, далее умножаем
        # на 100 и округляем до целого
        sclass_read = con.cursor().execute(f""" SELECT count(*) FROM articles 
                                                WHERE sclass = '{self.sclass}' and  is_read = 1""").fetchall()[0][0]
        sclass_all = con.cursor().execute(f""" SELECT count(*) FROM articles
                                               WHERE sclass = '{self.sclass}'""").fetchall()[0][0]
        percentage_of_sclass = round(sclass_read / sclass_all * 100)
        # Запросы на обновление процента выполнения по всем предметам
        # Аналогично
        overall_read = con.cursor().execute(f""" SELECT count(*) FROM articles 
                                                 WHERE is_read = 1""").fetchall()[0][0]
        overall_all = con.cursor().execute(f""" SELECT count(*) FROM articles""").fetchall()[0][0]  # запросы вернут int
        percentage_overall = round(overall_read / overall_all * 100)

        # Обновление данных
        con.execute(f"""UPDATE users 
                        SET {dict_of_sclass[self.sclass]} = {percentage_of_sclass}""")
        con.execute(f"""UPDATE users 
                        SET overall_progression = {percentage_overall}""")
        con.commit()
        con.close()

    def delete_article(self):
        if not self.is_admin:
            self.error_label.setText('Недостаточно прав')  # сообщаем об ошибке если поля пустые
            return
        con = sqlite3.connect('db_name.sqlite')
        con.execute(f"""Delete from articles where id = '{self.paragraph_id}'""")
        con.commit()
        con.close()
        self.open_study_window()

    def edit_article(self):
        if not self.is_admin:
            self.error_label.setText('Недостаточно прав')  # сообщаем об ошибке если поля пустые
            return
        self.second_form = EditWindow(self.title_text, self.sclass, self.id, self.paragraph_id, self.is_admin,
                                      self.paragraph_info[0])
        self.second_form.show()
        self.close()

    def open_study_window(self):
        # возращение к странице со статьями
        self.second_form = StudyWindow(self.sclass, self.id, self.is_admin)
        self.second_form.show()
        self.close()


class EditWindow(QWidget, Ui_Form_Edit):
    def __init__(self, title, sclass, id, paragraph_id, is_admin, text, *args):
        super().__init__()
        self.id = id
        self.paragraph_id = paragraph_id
        self.title_text = title
        self.sclass = sclass
        self.is_admin = is_admin
        self.setupUi(self)  # описание окна, введение информации о пользователе
        self.senders_text.setText(text)
        self.title_edit.setText(self.title_text)
        self.send_button.clicked.connect(self.load_article)
        self.confirm_send.clicked.connect(self.send_article)

        self.setWindowTitle('One-frog.Study')
        self.setWindowIcon(QIcon('logo_favicon.png'))
        self.goback.clicked.connect(self.open_study_window)
        self.goback.setIcon(QIcon('arrow_back.png'))

    def send_article(self):
        self.error_label.setText('')
        self.success_label.setText('')
        # ошибка, если поля пустые
        if not self.title_edit.text() or not self.senders_text.toPlainText():
            self.error_label.setText('Заполните все поля\nдля загрузки')
            return
        con = sqlite3.connect('db_name.sqlite')
        # Запись кастомной статьи в Бд
        con.cursor().execute(f"""UPDATE articles
                                 SET paragraph_text = '{self.senders_text.toPlainText()}', 
                                 title = '{self.title_edit.text()}'
                                 WHERE id = {self.paragraph_id}""")
        con.commit()
        con.close()
        self.success_label.setText('Успешно!')

    def load_article(self):
        # подгрузка файла от пользователя
        fname = QFileDialog.getOpenFileName(
            self, 'Выбрать файл', '',
            'Текстовый (*.txt)')[0]
        # обработка ошибок
        if fname[-4:] != '.txt':
            self.senders_text.setText(
                'Неподдерживаемый формат. Обрабатываются текстовые файлы(.txt) с кодировкой utf-8')
            return
        try:
            with open(fname, encoding='utf-8') as file:
                text = file.readlines()
                self.senders_text.setText('')
                for i in text:
                    self.senders_text.setText(self.senders_text.toPlainText() + i)  # внесение текста статьи в поле
        except UnicodeDecodeError:
            self.senders_text.setText(
                'Неподдерживаемый формат. Обрабатываются текстовые файлы(.txt) с кодировкой utf-8')
            return

    def open_study_window(self):
        # возращение к странице со статьями
        self.second_form = StudyWindow(self.sclass, self.id, self.is_admin)
        self.second_form.show()
        self.close()


if __name__ == '__main__':  # запуск мейн окна
    # адаптация окон
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    main = LoginWindow()
    main.show()
    sys.exit(app.exec())
