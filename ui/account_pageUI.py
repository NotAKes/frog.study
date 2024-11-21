# Form implementation generated from reading ui file 'ui/account_page.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AccountWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1237, 836)
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
        self.frame.setMinimumSize(QtCore.QSize(0, 500))
        self.frame.setMaximumSize(QtCore.QSize(250, 1000))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo = QtWidgets.QLabel(parent=self.frame)
        self.logo.setMaximumSize(QtCore.QSize(144, 144))
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.verticalLayout.addWidget(self.logo)
        self.ToMain = QtWidgets.QPushButton(parent=self.frame)
        self.ToMain.setStyleSheet("background:transparent;\n"
"color:white;\n"
"font-size:32px;\n"
"padding-left:4%;\n"
"text-align:left;\n"
"")
        self.ToMain.setObjectName("ToMain")
        self.verticalLayout.addWidget(self.ToMain)
        self.ToAccount = QtWidgets.QPushButton(parent=self.frame)
        self.ToAccount.setStyleSheet("background:transparent;\n"
"word-break:break-word;\n"
"color:white;\n"
"font-size:30px;\n"
"padding-left:4%;\n"
"text-align:left;\n"
"text-decoration:underline;")
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
        self.label = QtWidgets.QLabel(parent=self.frame_2)
        self.label.setGeometry(QtCore.QRect(10, 0, 471, 91))
        self.label.setStyleSheet("background:transparent;\n"
"color:white;\n"
"font-size:32px;\n"
"padding-left:4%;\n"
"text-align:left;\n"
"")
        self.label.setObjectName("label")
        self.SaveButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.SaveButton.setGeometry(QtCore.QRect(170, 410, 231, 61))
        self.SaveButton.setStyleSheet("background-color:rgb(110, 127, 158);\n"
"word-break:break-word;\n"
"color:white;\n"
"border-radius:10px;\n"
"font-size:27px;\n"
"padding-left:4%;\n"
"text-align:center;")
        self.SaveButton.setObjectName("SaveButton")
        self.NicknameEdit = QtWidgets.QLineEdit(parent=self.frame_2)
        self.NicknameEdit.setGeometry(QtCore.QRect(90, 190, 311, 31))
        self.NicknameEdit.setStyleSheet("background:rgb(132, 153, 189);\n"
"color:white;\n"
"font-size:18px;")
        self.NicknameEdit.setObjectName("NicknameEdit")
        self.label_8 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(80, 130, 161, 41))
        self.label_8.setStyleSheet("background:transparent;\n"
"color:white;\n"
"font-size:30px;\n"
"padding-left:4%;\n"
"text-align:left;\n"
"")
        self.label_8.setObjectName("label_8")
        self.favoriteClass = QtWidgets.QComboBox(parent=self.frame_2)
        self.favoriteClass.setGeometry(QtCore.QRect(90, 290, 311, 41))
        self.favoriteClass.setStyleSheet("QComboBox{background-color: rgb(110, 127, 158);\n"
"color:white;\n"
"font-size:20px;\n"
"border-radius: 10px;\n"
"}\n"
"QComboBox::down-arrow { padding-right: 40px; }\n"
"QComboBox::drop-down { margin-left: 40px;}\n"
" QComboBox QListView {\n"
"color:white; \n"
"background: rgb(110, 127, 158);\n"
"}")
        self.favoriteClass.setObjectName("favoriteClass")
        self.favoriteClass.addItem("")
        self.favoriteClass.addItem("")
        self.favoriteClass.addItem("")
        self.favoriteClass.addItem("")
        self.favoriteClass.addItem("")
        self.label_10 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(90, 240, 271, 41))
        self.label_10.setStyleSheet("background:transparent;\n"
"color:white;\n"
"font-size:30px;\n"
"padding-left:4%;\n"
"text-align:left;\n"
"")
        self.label_10.setObjectName("label_10")
        self.favoriteLabel = QtWidgets.QLabel(parent=self.frame_2)
        self.favoriteLabel.setGeometry(QtCore.QRect(90, 340, 311, 31))
        self.favoriteLabel.setStyleSheet("font-size:16px;\n"
"color:rgb(153, 164, 208);")
        self.favoriteLabel.setText("")
        self.favoriteLabel.setObjectName("favoriteLabel")
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setMinimumSize(QtCore.QSize(500, 800))
        self.frame_3.setMaximumSize(QtCore.QSize(800, 1500))
        self.frame_3.setStyleSheet("background:transparent;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(-10, 0, 471, 91))
        self.label_3.setStyleSheet("background:transparent;\n"
"color:white;\n"
"font-size:32px;\n"
"padding-left:4%;\n"
"text-align:left;\n"
"")
        self.label_3.setObjectName("label_3")
        self.overalllprogression = QtWidgets.QProgressBar(parent=self.frame_3)
        self.overalllprogression.setGeometry(QtCore.QRect(310, 670, 171, 31))
        self.overalllprogression.setStyleSheet("color:white;")
        self.overalllprogression.setProperty("value", 24)
        self.overalllprogression.setObjectName("overalllprogression")
        self.phys_progression = QtWidgets.QProgressBar(parent=self.frame_3)
        self.phys_progression.setGeometry(QtCore.QRect(320, 250, 171, 31))
        self.phys_progression.setStyleSheet("color:white;")
        self.phys_progression.setProperty("value", 24)
        self.phys_progression.setObjectName("phys_progression")
        self.math_progression = QtWidgets.QProgressBar(parent=self.frame_3)
        self.math_progression.setGeometry(QtCore.QRect(320, 140, 171, 31))
        self.math_progression.setStyleSheet("color:white;")
        self.math_progression.setProperty("value", 24)
        self.math_progression.setObjectName("math_progression")
        self.bio_progression = QtWidgets.QProgressBar(parent=self.frame_3)
        self.bio_progression.setGeometry(QtCore.QRect(320, 360, 171, 31))
        self.bio_progression.setStyleSheet("color:white;")
        self.bio_progression.setProperty("value", 24)
        self.bio_progression.setObjectName("bio_progression")
        self.chem_progression = QtWidgets.QProgressBar(parent=self.frame_3)
        self.chem_progression.setGeometry(QtCore.QRect(320, 470, 171, 31))
        self.chem_progression.setStyleSheet("color:white;")
        self.chem_progression.setProperty("value", 24)
        self.chem_progression.setObjectName("chem_progression")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 191, 51))
        self.label_2.setStyleSheet("background:transparent;\n"
"color:white;\n"
"font-size:29px;\n"
"padding-left:4%;\n"
"text-align:left;\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(30, 240, 151, 51))
        self.label_4.setStyleSheet("background:transparent;\n"
"color:white;\n"
"font-size:29px;\n"
"padding-left:4%;\n"
"text-align:left;\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(30, 350, 151, 51))
        self.label_5.setStyleSheet("background:transparent;\n"
"color:white;\n"
"font-size:29px;\n"
"padding-left:4%;\n"
"text-align:left;\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(30, 460, 151, 51))
        self.label_6.setStyleSheet("background:transparent;\n"
"color:white;\n"
"font-size:29px;\n"
"padding-left:4%;\n"
"text-align:left;\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(20, 650, 151, 51))
        self.label_7.setStyleSheet("background:transparent;\n"
"color:white;\n"
"font-size:29px;\n"
"padding-left:4%;\n"
"text-align:left;\n"
"")
        self.label_7.setObjectName("label_7")
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
        self.label.setText(_translate("MainWindow", "Информация об аккаунте"))
        self.SaveButton.setText(_translate("MainWindow", "Сохранить!"))
        self.label_8.setText(_translate("MainWindow", "Никнейм"))
        self.favoriteClass.setItemText(0, _translate("MainWindow", "-"))
        self.favoriteClass.setItemText(1, _translate("MainWindow", "Математика"))
        self.favoriteClass.setItemText(2, _translate("MainWindow", "Физика"))
        self.favoriteClass.setItemText(3, _translate("MainWindow", "Химия"))
        self.favoriteClass.setItemText(4, _translate("MainWindow", "Биология"))
        self.label_10.setText(_translate("MainWindow", "Любимый предмет"))
        self.label_3.setText(_translate("MainWindow", "Информация об успеваемости"))
        self.label_2.setText(_translate("MainWindow", "Математика"))
        self.label_4.setText(_translate("MainWindow", "Физика"))
        self.label_5.setText(_translate("MainWindow", "Биология"))
        self.label_6.setText(_translate("MainWindow", "Химия"))
        self.label_7.setText(_translate("MainWindow", "Общий"))
