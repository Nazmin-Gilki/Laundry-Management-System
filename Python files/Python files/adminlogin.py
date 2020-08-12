# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminlogin.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from module2 import Ui_module2
from LogFailed import Ui_LogFailed
class Ui_adminlogin(object):
    def Validity(self):
        uname=self.lineEdit.text()
        passw=self.lineEdit_2.text()
        try:
            if uname=="Alex" and passw=="Alex!123":
                self.wc=QtWidgets.QMainWindow()
                self.ui=Ui_module2()
                self.ui.setupUi(self.wc)
                self.wc.show()
            else:
                self.wc=QtWidgets.QMainWindow()
                self.ui=Ui_LogFailed()
                self.ui.setupUi(self.wc)
                self.wc.show()
        except:
                self.wc=QtWidgets.QMainWindow()
                self.ui=Ui_LogFailed()
                self.ui.setupUi(self.wc)
                self.wc.show()
            
        
    def setupUi(self, adminlogin):
        
        adminlogin.setObjectName("adminlogin")
        adminlogin.resize(947, 789)
        self.centralwidget = QtWidgets.QWidget(adminlogin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 480, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 570, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(490, 480, 231, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(490, 570, 231, 41))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 700, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.Validity)
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 951, 451))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("l3.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        adminlogin.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(adminlogin)
        self.statusbar.setObjectName("statusbar")
        adminlogin.setStatusBar(self.statusbar)

        self.retranslateUi(adminlogin)
        QtCore.QMetaObject.connectSlotsByName(adminlogin)

    def retranslateUi(self, adminlogin):
        _translate = QtCore.QCoreApplication.translate
        adminlogin.setWindowTitle(_translate("adminlogin", "MainWindow"))
        self.label.setText(_translate("adminlogin", "Username"))
        self.label_2.setText(_translate("adminlogin", "Password"))
        self.pushButton.setText(_translate("adminlogin", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminlogin = QtWidgets.QMainWindow()
    ui = Ui_adminlogin()
    ui.setupUi(adminlogin)
    adminlogin.show()
    sys.exit(app.exec_())
