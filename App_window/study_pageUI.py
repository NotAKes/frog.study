# Form implementation generated from reading ui file 'ui/study_pageUI.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form_Study(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1132, 732)
        Form.setStyleSheet("QWidget{background:rgb(54, 57, 76);}\n"
"QPushButton{color:white;\n"
"background:transparent;\n"
"font-size:20px;}\n"
"QPushButton:hover{\n"
"text-decoration:underline;}\n"
"QScrollArea{border:1px solid  rgb(231, 251, 255);}")
        self.title = QtWidgets.QLabel(parent=Form)
        self.title.setGeometry(QtCore.QRect(410, 10, 281, 81))
        self.title.setStyleSheet("color:white;\n"
"font-size:40px;\n"
"text-align:center;")
        self.title.setObjectName("title")
        self.main = QtWidgets.QWidget(parent=Form)
        self.main.setGeometry(QtCore.QRect(20, 110, 1081, 751))
        self.main.setObjectName("main")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.author = QtWidgets.QWidget(parent=self.main)
        self.author.setObjectName("author")
        self.authorscrollArea = QtWidgets.QScrollArea(parent=self.author)
        self.authorscrollArea.setGeometry(QtCore.QRect(20, 40, 441, 541))
        self.authorscrollArea.setStyleSheet("")
        self.authorscrollArea.setWidgetResizable(True)
        self.authorscrollArea.setObjectName("authorscrollArea")
        self.authorlayout = QtWidgets.QWidget()
        self.authorlayout.setGeometry(QtCore.QRect(0, 0, 439, 539))
        self.authorlayout.setObjectName("authorlayout")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.authorlayout)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.authorscrollArea.setWidget(self.authorlayout)
        self.label_2 = QtWidgets.QLabel(parent=self.author)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(80, -10, 311, 50))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.author)
        self.user = QtWidgets.QWidget(parent=self.main)
        self.user.setObjectName("user")
        self.userScrollArea = QtWidgets.QScrollArea(parent=self.user)
        self.userScrollArea.setGeometry(QtCore.QRect(0, 40, 461, 541))
        self.userScrollArea.setWidgetResizable(True)
        self.userScrollArea.setObjectName("userScrollArea")
        self.userlayout = QtWidgets.QWidget()
        self.userlayout.setGeometry(QtCore.QRect(0, 0, 459, 539))
        self.userlayout.setObjectName("userlayout")
        self.userScrollArea.setWidget(self.userlayout)
        self.label_4 = QtWidgets.QLabel(parent=self.user)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(40, -10, 381, 50))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.user)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title.setText(_translate("Form", "Математика"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">Авторские статьи</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">Пользовательские статьи</span></p></body></html>"))
