# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from forgotpass import Ui_forgotpass
from module3 import Ui_module3
from LogFailed import Ui_LogFailed
from forgotpass import Ui_forgotpass
import sqlite3
from un import user
class Ui_login(object):
    def openWindow1(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_forgotpass()
        self.ui.setupUi(self.window)
        self.window.show()
    def Validity(self):
        #try:
            uname=self.lineEdit.text()
            passw=self.lineEdit_2.text()
            connection = sqlite3.connect("MyLaundry.db")
            res= connection.execute("SELECT * FROM Registration WHERE Username = ? AND Password = ?",(uname,passw))
            if (len(res.fetchall()) > 0):
                data=[(self.lineEdit.text(),self.lineEdit_2.text())]
                connection.executemany("INSERT INTO user VALUES(?,?)",data)
    
                connection.commit()
                connection.close()
                self.wc=QtWidgets.QMainWindow()
                self.ui=Ui_module3()
                self.ui.setupUi(self.wc)
                self.wc.show()
            else:
                self.wc1=QtWidgets.QMainWindow()
                self.ui=Ui_LogFailed()
                self.ui.setupUi(self.wc1)
                self.wc1.show()
        #except:
                self.wc2=QtWidgets.QMainWindow()
                self.ui=Ui_LogFailed()
                self.ui.setupUi(self.wc2)
                self.wc2.show()
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(983, 778)
        login.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(login)
        self.centralwidget.setObjectName("centralwidget")
        self.Login = QtWidgets.QPushButton(self.centralwidget)
        self.Login.setGeometry(QtCore.QRect(90, 680, 201, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Login.setFont(font)
        self.Login.setObjectName("Login")

        self.Login.clicked.connect(self.Validity)

        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(530, 480, 291, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(530, 580, 291, 41))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 680, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.openWindow1)

        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 480, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 570, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(420, 10, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 961, 351))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("l1.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(False)
        self.label_4.setOpenExternalLinks(False)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 440, 961, 16))
        self.label_5.setObjectName("label_5")
        login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(login)
        self.statusbar.setObjectName("statusbar")
        login.setStatusBar(self.statusbar)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "MainWindow"))
        self.Login.setText(_translate("login", "Login"))
        self.pushButton_2.setText(_translate("login", "Forgot Password"))
        self.label.setText(_translate("login", "Username"))
        self.label_2.setText(_translate("login", "Password"))
        self.label_3.setText(_translate("login", "Login"))
        self.label_5.setText(_translate("login", "---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QMainWindow()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())
