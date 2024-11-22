# Form implementation generated from reading ui file 'ui/dialog.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(440, 362)
        Dialog.setStyleSheet("QDialog{background-color:rgb(54, 57, 76);}\n"
"QPushButton:hover{text-decoration:underline}")
        self.login_input = QtWidgets.QLineEdit(parent=Dialog)
        self.login_input.setGeometry(QtCore.QRect(120, 40, 301, 41))
        self.login_input.setStyleSheet("background:rgb(132, 153, 189);\n"
"color:white;\n"
"font-size:18px;")
        self.login_input.setObjectName("login_input")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(10, 50, 101, 21))
        self.label.setStyleSheet("color:white;\n"
"font-size:26px;")
        self.label.setObjectName("label")
        self.password_input = QtWidgets.QLineEdit(parent=Dialog)
        self.password_input.setGeometry(QtCore.QRect(120, 100, 301, 41))
        self.password_input.setStyleSheet("background:rgb(132, 153, 189);\n"
"color:white;\n"
"font-size:18px;")
        self.password_input.setObjectName("password_input")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 101, 31))
        self.label_2.setStyleSheet("color:white;\n"
"font-size:26px;")
        self.label_2.setObjectName("label_2")
        self.loginadmin_button = QtWidgets.QPushButton(parent=Dialog)
        self.loginadmin_button.setGeometry(QtCore.QRect(260, 210, 161, 41))
        self.loginadmin_button.setStyleSheet("background-color:rgb(110, 127, 158);\n"
"word-break:break-word;\n"
"color:white;\n"
"border-radius:5px;\n"
"font-size:18px;\n"
"padding-left:4%;\n"
"text-align:center;")
        self.loginadmin_button.setObjectName("loginadmin_button")
        self.loginstudent_button = QtWidgets.QPushButton(parent=Dialog)
        self.loginstudent_button.setGeometry(QtCore.QRect(260, 300, 161, 41))
        self.loginstudent_button.setStyleSheet("background-color:rgb(110, 127, 158);\n"
"word-break:break-word;\n"
"color:white;\n"
"border-radius:5px;\n"
"font-size:18px;\n"
"padding-left:4%;\n"
"text-align:center;")
        self.loginstudent_button.setObjectName("loginstudent_button")
        self.error_label = QtWidgets.QLabel(parent=Dialog)
        self.error_label.setGeometry(QtCore.QRect(20, 200, 201, 91))
        self.error_label.setStyleSheet("color:orange;\n"
"font-size:20px;\n"
"text-align: justify;\n"
"justify-content: center;")
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(320, 260, 41, 21))
        self.label_4.setStyleSheet("color:white;\n"
"font-size:18px;")
        self.label_4.setObjectName("label_4")
        self.password_button = QtWidgets.QPushButton(parent=Dialog)
        self.password_button.setGeometry(QtCore.QRect(110, 150, 171, 28))
        self.password_button.setStyleSheet("color:rgb(188, 211, 241);\n"
"word-break:break-word;\n"
"border-radius:5px;\n"
"font-size:18px;\n"
"padding-left:4%;\n"
"text-align:center;")
        self.password_button.setObjectName("password_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Логин"))
        self.label_2.setText(_translate("Dialog", "Пароль"))
        self.loginadmin_button.setText(_translate("Dialog", "Войти как админ"))
        self.loginstudent_button.setText(_translate("Dialog", "Войти как ученик"))
        self.label_4.setText(_translate("Dialog", "ИЛИ"))
        self.password_button.setText(_translate("Dialog", "Показать пароль?"))
