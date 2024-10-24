# Form implementation generated from reading ui file 'main_page.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1237, 859)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        MainWindow.setStyleSheet("background-color:rgb(54, 57, 76);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("QFrame, QPushButton{\n"
"border:none;}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 500))
        self.frame.setMaximumSize(QtCore.QSize(250, 500))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_7.setStyleSheet("background:transparent;\n"
"text-decoration:underline;\n"
"color:white;\n"
"font-size:32px;\n"
"padding-left:4%;\n"
"text-align:left;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_5.setStyleSheet("background:transparent;\n"
"word-break:break-word;\n"
"color:white;\n"
"font-size:30px;\n"
"padding-left:4%;\n"
"text-align:left;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_6.setStyleSheet("background:transparent;\n"
"word-break:break-word;\n"
"color:white;\n"
"font-size:30px;\n"
"padding-left:4%;\n"
"text-align:left;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(500, 800))
        self.frame_2.setMaximumSize(QtCore.QSize(800, 1500))
        self.frame_2.setStyleSheet("background:transparent;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.math_button = QtWidgets.QPushButton(parent=self.frame_2)
        self.math_button.setGeometry(QtCore.QRect(50, 140, 451, 61))
        self.math_button.setStyleSheet("QPushButton{background-color :rgb(110, 127, 158);\n"
"color:white;\n"
"font-size:30px;\n"
"padding-left:20%;\n"
"text-align:left;\n"
"border-radius: 10px;}\n"
"QPushButton:hover{\n"
"background-color :rgb(128, 149, 184);}")
        self.math_button.setObjectName("math_button")
        self.math_progression = QtWidgets.QProgressBar(parent=self.frame_2)
        self.math_progression.setGeometry(QtCore.QRect(370, 160, 118, 23))
        self.math_progression.setStyleSheet("color:white;")
        self.math_progression.setProperty("value", 10)
        self.math_progression.setObjectName("math_progression")
        self.label = QtWidgets.QLabel(parent=self.frame_2)
        self.label.setGeometry(QtCore.QRect(70, 50, 411, 42))
        self.label.setStyleSheet("font-size:30px;\n"
"color:white;")
        self.label.setObjectName("label")
        self.math_button.raise_()
        self.label.raise_()
        self.math_progression.raise_()
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setMinimumSize(QtCore.QSize(500, 800))
        self.frame_3.setMaximumSize(QtCore.QSize(800, 1500))
        self.frame_3.setStyleSheet("background:transparent;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.progressBar_4 = QtWidgets.QProgressBar(parent=self.frame_3)
        self.progressBar_4.setGeometry(QtCore.QRect(340, 380, 118, 23))
        self.progressBar_4.setProperty("value", 0)
        self.progressBar_4.setObjectName("progressBar_4")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 140, 451, 61))
        self.pushButton_2.setStyleSheet("QPushButton{background-color :rgb(110, 127, 158);\n"
"color:white;\n"
"font-size:30px;\n"
"padding-left:20%;\n"
"text-align:left;\n"
"border-radius: 10px;}\n"
"QPushButton:hover{\n"
"background-color :rgb(128, 149, 184);}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.progressBar_2 = QtWidgets.QProgressBar(parent=self.frame_3)
        self.progressBar_2.setGeometry(QtCore.QRect(340, 160, 118, 23))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_3 = QtWidgets.QProgressBar(parent=self.frame_3)
        self.progressBar_3.setGeometry(QtCore.QRect(340, 270, 118, 23))
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName("progressBar_3")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 250, 451, 61))
        self.pushButton_3.setStyleSheet("QPushButton{background-color :rgb(110, 127, 158);\n"
"color:white;\n"
"font-size:30px;\n"
"padding-left:20%;\n"
"text-align:left;\n"
"border-radius: 10px;}\n"
"QPushButton:hover{\n"
"background-color :rgb(128, 149, 184);}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 360, 451, 61))
        self.pushButton_4.setStyleSheet("QPushButton{background-color :rgb(110, 127, 158);\n"
"color:white;\n"
"font-size:30px;\n"
"padding-left:20%;\n"
"text-align:left;\n"
"border-radius: 10px;}\n"
"\n"
"QPushButton:hover{\n"
"background-color :rgb(128, 149, 184);}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 411, 42))
        self.label_2.setStyleSheet("font-size:30px;\n"
"color:white;")
        self.label_2.setObjectName("label_2")
        self.pushButton_4.raise_()
        self.progressBar_4.raise_()
        self.pushButton_2.raise_()
        self.progressBar_2.raise_()
        self.pushButton_3.raise_()
        self.progressBar_3.raise_()
        self.label_2.raise_()
        self.horizontalLayout.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1237, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_7.setText(_translate("MainWindow", "Главная"))
        self.pushButton_5.setText(_translate("MainWindow", "Перейти в \n"
"свой аккаунт"))
        self.pushButton_6.setText(_translate("MainWindow", "Настройки"))
        self.math_button.setText(_translate("MainWindow", "Математика"))
        self.label.setText(_translate("MainWindow", "Продолжить обучение по..."))
        self.pushButton_2.setText(_translate("MainWindow", "Химия"))
        self.pushButton_3.setText(_translate("MainWindow", "Физика"))
        self.pushButton_4.setText(_translate("MainWindow", "Биология"))
        self.label_2.setText(_translate("MainWindow", "Изучить новую область"))
