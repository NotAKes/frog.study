# Form implementation generated from reading ui file 'ui/register_pageUI.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_RegWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(445, 364)
        Dialog.setStyleSheet("QDialog{background-color:rgb(54, 57, 76);}\n"
"QPushButton:hover{text-decoration:underline}")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(20, 40, 101, 21))
        self.label.setStyleSheet("color:white;\n"
"font-size:26px;")
        self.label.setObjectName("label")
        self.regadmin_button = QtWidgets.QPushButton(parent=Dialog)
        self.regadmin_button.setGeometry(QtCore.QRect(270, 280, 161, 41))
        self.regadmin_button.setStyleSheet("background-color:rgb(110, 127, 158);\n"
"word-break:break-word;\n"
"color:white;\n"
"border-radius:5px;\n"
"font-size:18px;\n"
"padding-left:4%;\n"
"text-align:center;")
        self.regadmin_button.setObjectName("regadmin_button")
        self.password_button = QtWidgets.QPushButton(parent=Dialog)
        self.password_button.setGeometry(QtCore.QRect(120, 210, 171, 28))
        self.password_button.setStyleSheet("color:rgb(188, 211, 241);\n"
"word-break:break-word;\n"
"border-radius:5px;\n"
"font-size:18px;\n"
"padding-left:4%;\n"
"text-align:center;")
        self.password_button.setObjectName("password_button")
        self.password_input = QtWidgets.QLineEdit(parent=Dialog)
        self.password_input.setGeometry(QtCore.QRect(130, 90, 301, 41))
        self.password_input.setStyleSheet("background:rgb(132, 153, 189);\n"
"color:white;\n"
"font-size:18px;")
        self.password_input.setObjectName("password_input")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 101, 31))
        self.label_2.setStyleSheet("color:white;\n"
"font-size:26px;")
        self.label_2.setObjectName("label_2")
        self.login_input = QtWidgets.QLineEdit(parent=Dialog)
        self.login_input.setGeometry(QtCore.QRect(130, 30, 301, 41))
        self.login_input.setStyleSheet("background:rgb(132, 153, 189);\n"
"color:white;\n"
"font-size:18px;")
        self.login_input.setObjectName("login_input")
        self.password_input_2 = QtWidgets.QLineEdit(parent=Dialog)
        self.password_input_2.setGeometry(QtCore.QRect(130, 150, 301, 41))
        self.password_input_2.setStyleSheet("background:rgb(132, 153, 189);\n"
"color:white;\n"
"font-size:18px;")
        self.password_input_2.setObjectName("password_input_2")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 101, 51))
        self.label_3.setStyleSheet("color:white;\n"
"font-size:20px;")
        self.label_3.setObjectName("label_3")
        self.error_label = QtWidgets.QLabel(parent=Dialog)
        self.error_label.setGeometry(QtCore.QRect(40, 250, 201, 91))
        self.error_label.setStyleSheet("color:orange;\n"
"font-size:20px;\n"
"text-align: justify;\n"
"justify-content: center;")
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Логин"))
        self.regadmin_button.setText(_translate("Dialog", "Зарегать админа"))
        self.password_button.setText(_translate("Dialog", "Показать пароль?"))
        self.label_2.setText(_translate("Dialog", "Пароль"))
        self.label_3.setText(_translate("Dialog", "Повторите\n"
"пароль"))
