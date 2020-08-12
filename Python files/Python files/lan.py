# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lan.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from login import Ui_login
from registerpage import Ui_registerpage

class Ui_mainWindow(object):
    def openWindow1(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_login()
        self.ui.setupUi(self.window)
        self.window.show()
    def openWindow2(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_registerpage()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1056, 797)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 50, 911, 471))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Laundry.png"))
        self.label.setObjectName("label")
        self.Login = QtWidgets.QPushButton(self.centralwidget)
        self.Login.setGeometry(QtCore.QRect(180, 590, 171, 51))
        self.Login.setObjectName("Login")

        self.Login.clicked.connect(self.openWindow1)

        self.Register = QtWidgets.QPushButton(self.centralwidget)
        self.Register.setGeometry(QtCore.QRect(720, 590, 171, 51))
        self.Register.setObjectName("Register")
        
        self.Register.clicked.connect(self.openWindow2)
        
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1056, 26))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.Login.setText(_translate("mainWindow", "Login"))
        self.Register.setText(_translate("mainWindow", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
