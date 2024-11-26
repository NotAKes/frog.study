# Form implementation generated from reading ui file 'ui/main_page.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1243, 818)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        MainWindow.setStyleSheet("background-color:rgb(54, 57, 76);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("QFrame, QPushButton{\n"
"border:none;}\n"
"QPushButton:hover{text-decoration:underline}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 600))
        self.frame.setMaximumSize(QtCore.QSize(250, 1000))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo = QtWidgets.QLabel(parent=self.frame)
        self.logo.setMaximumSize(QtCore.QSize(144, 144))
        self.logo.setText("")
        self.logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.logo.setObjectName("logo")
        self.verticalLayout.addWidget(self.logo)
        self.ToMain = QtWidgets.QPushButton(parent=self.frame)
        self.ToMain.setStyleSheet("background:transparent;\n"
"color:white;\n"
"font-size:32px;\n"
"padding-left:4%;\n"
"text-align:left;\n"
"text-decoration:underline;")
        self.ToMain.setObjectName("ToMain")
        self.verticalLayout.addWidget(self.ToMain)
        self.ToAccount = QtWidgets.QPushButton(parent=self.frame)
        self.ToAccount.setStyleSheet("background:transparent;\n"
"word-break:break-word;\n"
"color:white;\n"
"font-size:30px;\n"
"padding-left:4%;\n"
"text-align:left;")
        self.ToAccount.setObjectName("ToAccount")
        self.verticalLayout.addWidget(self.ToAccount)
        self.ToSettings = QtWidgets.QPushButton(parent=self.frame)
        self.ToSettings.setStyleSheet("background:transparent;\n"
"word-break:break-word;\n"
"color:white;\n"
"font-size:30px;\n"
"padding-left:4%;\n"
"text-align:left;")
        self.ToSettings.setObjectName("ToSettings")
        self.verticalLayout.addWidget(self.ToSettings)
        self.horizontalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(500, 800))
        self.frame_2.setMaximumSize(QtCore.QSize(800, 1500))
        self.frame_2.setStyleSheet("background:transparent;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.math_button = QtWidgets.QPushButton(parent=self.frame_2)
        self.math_button.setGeometry(QtCore.QRect(50, 150, 451, 61))
        self.math_button.setStyleSheet("QPushButton{background-color :rgb(110, 127, 158);\n"
"color:white;\n"
"font-size:30px;\n"
"padding-left:20%;\n"
"text-align:left;\n"
"border-radius: 10px;}\n"
"QPushButton:hover{\n"
"background-color :rgb(128, 149, 184);}")
        self.math_button.setObjectName("math_button")
        self.study_buttons = QtWidgets.QButtonGroup(MainWindow)
        self.study_buttons.setObjectName("study_buttons")
        self.study_buttons.addButton(self.math_button)
        self.math_progression = QtWidgets.QProgressBar(parent=self.frame_2)
        self.math_progression.setGeometry(QtCore.QRect(370, 170, 118, 23))
        self.math_progression.setStyleSheet("color:white;")
        self.math_progression.setProperty("value", 10)
        self.math_progression.setObjectName("math_progression")
        self.label = QtWidgets.QLabel(parent=self.frame_2)
        self.label.setGeometry(QtCore.QRect(70, 50, 411, 42))
        self.label.setStyleSheet("font-size:35px;\n"
"color:white;")
        self.label.setObjectName("label")
        self.chem_button = QtWidgets.QPushButton(parent=self.frame_2)
        self.chem_button.setGeometry(QtCore.QRect(50, 280, 451, 61))
        self.chem_button.setStyleSheet("QPushButton{background-color :rgb(110, 127, 158);\n"
"color:white;\n"
"font-size:30px;\n"
"padding-left:20%;\n"
"text-align:left;\n"
"border-radius: 10px;}\n"
"QPushButton:hover{\n"
"background-color :rgb(128, 149, 184);}")
        self.chem_button.setObjectName("chem_button")
        self.study_buttons.addButton(self.chem_button)
        self.phys_button = QtWidgets.QPushButton(parent=self.frame_2)
        self.phys_button.setGeometry(QtCore.QRect(50, 410, 451, 61))
        self.phys_button.setStyleSheet("QPushButton{background-color :rgb(110, 127, 158);\n"
"color:white;\n"
"font-size:30px;\n"
"padding-left:20%;\n"
"text-align:left;\n"
"border-radius: 10px;}\n"
"QPushButton:hover{\n"
"background-color :rgb(128, 149, 184);}")
        self.phys_button.setObjectName("phys_button")
        self.study_buttons.addButton(self.phys_button)
        self.bio_button = QtWidgets.QPushButton(parent=self.frame_2)
        self.bio_button.setGeometry(QtCore.QRect(50, 540, 451, 61))
        self.bio_button.setStyleSheet("QPushButton{background-color :rgb(110, 127, 158);\n"
"color:white;\n"
"font-size:30px;\n"
"padding-left:20%;\n"
"text-align:left;\n"
"border-radius: 10px;}\n"
"\n"
"QPushButton:hover{\n"
"background-color :rgb(128, 149, 184);}")
        self.bio_button.setObjectName("bio_button")
        self.study_buttons.addButton(self.bio_button)
        self.chem_progression = QtWidgets.QProgressBar(parent=self.frame_2)
        self.chem_progression.setGeometry(QtCore.QRect(370, 300, 118, 23))
        self.chem_progression.setStyleSheet("color:white;")
        self.chem_progression.setProperty("value", 10)
        self.chem_progression.setObjectName("chem_progression")
        self.phys_progression = QtWidgets.QProgressBar(parent=self.frame_2)
        self.phys_progression.setGeometry(QtCore.QRect(370, 430, 118, 23))
        self.phys_progression.setStyleSheet("color:white;")
        self.phys_progression.setProperty("value", 10)
        self.phys_progression.setObjectName("phys_progression")
        self.bio_progression = QtWidgets.QProgressBar(parent=self.frame_2)
        self.bio_progression.setGeometry(QtCore.QRect(370, 560, 118, 23))
        self.bio_progression.setStyleSheet("color:white;")
        self.bio_progression.setProperty("value", 10)
        self.bio_progression.setObjectName("bio_progression")
        self.update_progress = QtWidgets.QPushButton(parent=self.frame_2)
        self.update_progress.setGeometry(QtCore.QRect(344, 620, 141, 51))
        self.update_progress.setStyleSheet("QPushButton{font-size:16px;\n"
"text-decoration:underline;\n"
"color:rgb(153, 164, 208);}\n"
"QPushButton::hover{color:rgb(167, 179, 226)}")
        self.update_progress.setObjectName("update_progress")
        self.admin_warning = QtWidgets.QLabel(parent=self.frame_2)
        self.admin_warning.setGeometry(QtCore.QRect(60, 750, 341, 51))
        self.admin_warning.setStyleSheet("font-size:16px;\n"
"color:rgb(153, 164, 208);")
        self.admin_warning.setObjectName("admin_warning")
        self.label.raise_()
        self.chem_button.raise_()
        self.math_button.raise_()
        self.math_progression.raise_()
        self.phys_button.raise_()
        self.bio_button.raise_()
        self.chem_progression.raise_()
        self.phys_progression.raise_()
        self.bio_progression.raise_()
        self.update_progress.raise_()
        self.admin_warning.raise_()
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setMinimumSize(QtCore.QSize(500, 800))
        self.frame_3.setMaximumSize(QtCore.QSize(800, 1500))
        self.frame_3.setStyleSheet("background:transparent;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(70, 50, 411, 42))
        self.label_2.setStyleSheet("font-size:35px;\n"
"color:white;")
        self.label_2.setObjectName("label_2")
        self.confirm_send = QtWidgets.QPushButton(parent=self.frame_3)
        self.confirm_send.setGeometry(QtCore.QRect(300, 720, 191, 51))
        self.confirm_send.setStyleSheet("QPushButton{background-color :rgb(110, 127, 158);\n"
"color:white;\n"
"font-size:25px;\n"
"padding-left:20%;\n"
"text-align:left;\n"
"border-radius: 10px;}\n"
"QPushButton:hover{\n"
"background-color :rgb(128, 149, 184);}")
        self.confirm_send.setObjectName("confirm_send")
        self.send_button = QtWidgets.QPushButton(parent=self.frame_3)
        self.send_button.setGeometry(QtCore.QRect(80, 210, 411, 41))
        self.send_button.setStyleSheet("QPushButton{background-color :rgb(110, 127, 158);\n"
"color:white;\n"
"font-size:25px;\n"
"padding-left:20%;\n"
"text-align:center;\n"
"border-radius: 10px;}\n"
"QPushButton:hover{\n"
"background-color :rgb(128, 149, 184);}")
        self.send_button.setObjectName("send_button")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(230, 260, 101, 31))
        self.label_3.setStyleSheet("QLabel{\n"
"color:white;\n"
"font-size:25px;\n"
"padding-left:20%;\n"
"text-align:center;\n"
"border-radius: 10px;}")
        self.label_3.setObjectName("label_3")
        self.senders_text = QtWidgets.QTextEdit(parent=self.frame_3)
        self.senders_text.setGeometry(QtCore.QRect(80, 300, 411, 301))
        self.senders_text.setStyleSheet("color:white;\n"
"font-size:25px;\n"
"background:rgb(117, 126, 168);\n"
"border: 2px solid rgb(52, 56, 75);")
        self.senders_text.setObjectName("senders_text")
        self.sclass_pick = QtWidgets.QComboBox(parent=self.frame_3)
        self.sclass_pick.setGeometry(QtCore.QRect(300, 630, 191, 51))
        self.sclass_pick.setStyleSheet("background-color: rgb(110, 127, 158);\n"
"color:white;\n"
"font-size:20px;\n"
"border-radius: 10px")
        self.sclass_pick.setObjectName("sclass_pick")
        self.sclass_pick.addItem("")
        self.sclass_pick.addItem("")
        self.sclass_pick.addItem("")
        self.sclass_pick.addItem("")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(60, 620, 211, 51))
        self.label_4.setStyleSheet("font-size:22px;\n"
"color:white;")
        self.label_4.setObjectName("label_4")
        self.title_edit = QtWidgets.QLineEdit(parent=self.frame_3)
        self.title_edit.setGeometry(QtCore.QRect(80, 150, 411, 41))
        self.title_edit.setStyleSheet("color:white;\n"
"font-size:25px;\n"
"background:rgb(117, 126, 168);\n"
"border: 2px solid rgb(52, 56, 75);")
        self.title_edit.setObjectName("title_edit")
        self.success_label = QtWidgets.QLabel(parent=self.frame_3)
        self.success_label.setGeometry(QtCore.QRect(60, 720, 231, 71))
        self.success_label.setStyleSheet("color:rgb(145, 255, 143);\n"
"font-size:16px;\n"
"text-align: justify;\n"
"justify-content: center;")
        self.success_label.setText("")
        self.success_label.setObjectName("success_label")
        self.error_label = QtWidgets.QLabel(parent=self.frame_3)
        self.error_label.setGeometry(QtCore.QRect(60, 670, 181, 51))
        self.error_label.setStyleSheet("color:orange;\n"
"font-size:19px;\n"
"text-align: justify;\n"
"justify-content: center;")
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        self.horizontalLayout.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ToMain.setText(_translate("MainWindow", "Главная"))
        self.ToAccount.setText(_translate("MainWindow", "Мой аккаунт"))
        self.ToSettings.setText(_translate("MainWindow", "Настройки"))
        self.math_button.setText(_translate("MainWindow", "Математика"))
        self.label.setText(_translate("MainWindow", "Вперёд к знаниям!"))
        self.chem_button.setText(_translate("MainWindow", "Химия"))
        self.phys_button.setText(_translate("MainWindow", "Физика"))
        self.bio_button.setText(_translate("MainWindow", "Биология"))
        self.update_progress.setText(_translate("MainWindow", "Обновить данные"))
        self.admin_warning.setText(_translate("MainWindow", "*Вы вошли как админ. \n"
" В полях отображается успеваемость ученика"))
        self.label_2.setText(_translate("MainWindow", "Отправить статью"))
        self.confirm_send.setText(_translate("MainWindow", "Отправить!"))
        self.send_button.setText(_translate("MainWindow", "Загрузить файл"))
        self.label_3.setText(_translate("MainWindow", "ИЛИ"))
        self.senders_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.sclass_pick.setItemText(0, _translate("MainWindow", "Математика"))
        self.sclass_pick.setItemText(1, _translate("MainWindow", "Физика"))
        self.sclass_pick.setItemText(2, _translate("MainWindow", "Биология"))
        self.sclass_pick.setItemText(3, _translate("MainWindow", "Химия"))
        self.label_4.setText(_translate("MainWindow", "Выберите область:"))