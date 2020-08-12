# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registerpage.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from successregi import Ui_successregi
from RegFaild import Ui_RegFaild
import sqlite3
import re

class Ui_registerpage(object):
    """
    def ins(self):
        data = [(self.lineEdit.text(), self.lineEdit_3.text() ,self.lineEdit_4.text(), self.lineEdit_2.text(), int(self.lineEdit_5.text()), int(self.lineEdit_6.text()), self.lineEdit_7.text(), int(self.lineEdit_8.text()))]
        conn = None
        c=None
        try:
            conn= sqlite3.connect('C:\\Python36\\Scripts\\MyLaundry.db')
            c= conn.cursor()
            print('opened')
        except:
            print("....")
        c.executemany("INSERT INTO Registration VALUES(?,?,?,?,?,?,?,?)",data)
        print('inserted')
        print(c.fetchone())
        conn.commit()
        conn.close()
    """
    def ins(self):
        
        try:
            data = [(self.lineEdit.text(), self.lineEdit_3.text() ,self.lineEdit_4.text(), self.lineEdit_2.text(), int(self.lineEdit_5.text()), int(self.lineEdit_6.text()), self.lineEdit_7.text(), int(self.lineEdit_8.text()))]
            conn=None
            c=None
            print(data)
            pasw=self.lineEdit_4.text()
            cpass=self.lineEdit_2.text()
            con=self.lineEdit_5.text()
            al=self.lineEdit_6.text()
            pin=self.lineEdit_8.text()
            print(pasw,cpass,con,al,pin)
            if (re.search((re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$")),pasw)) and (pasw==cpass) and ((re.compile("(0/91)?[7-9][0-9]{9}")).match(con) and len(con)==10) and (((re.compile("(0/91)?[7-9][0-9]{9}")).match(al)) or len(al)==10) and len(pin)==6:
                    conn= sqlite3.connect('C:\\Python36\\Scripts\\MyLaundry.db')
                    c= conn.cursor()
               
                    data = [(self.lineEdit.text(), self.lineEdit_3.text() ,pasw, cpass, int(con), int(al), self.lineEdit_7.text(), int(pin))]
                    c.executemany("INSERT INTO Registration VALUES(?,?,?,?,?,?,?,?)",data)
                    conn.commit()
                    conn.close()
                    self.wc=QtWidgets.QMainWindow()
                    self.ui=Ui_successregi()
                    self.ui.setupUi(self.wc)
                    self.wc.show()
                    print("Successfully registered")
            
            else:
                    self.wc=QtWidgets.QMainWindow()
                    self.ui=Ui_RegFaild()
                    self.ui.setupUi(self.wc)
                    self.wc.show()
                    print("Registeration Faied")
            
        except:
                self.wc=QtWidgets.QMainWindow()
                self.ui=Ui_RegFaild()
                self.ui.setupUi(self.wc)
                self.wc.show()
                print("Register Failed")
                
    def setupUi(self, registerpage):
        registerpage.setObjectName("registerpage")
        registerpage.resize(1026, 831)
        registerpage.setStyleSheet("")
        registerpage.setAnimated(False)
        registerpage.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(registerpage)
        self.centralwidget.setObjectName("centralwidget")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(150, 340, 201, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(470, 340, 231, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(470, 420, 231, 41))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(470, 40, 231, 41))
        self.lineEdit.setMinimumSize(QtCore.QSize(50, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 120, 171, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(470, 200, 231, 41))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(470, 120, 231, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 270, 263, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(470, 270, 231, 41))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 420, 171, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 200, 138, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 680, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        #self.pushButton.clicked.connect(self.openWindow1)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 40, 181, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 500, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(470, 500, 231, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(160, 590, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(470, 580, 231, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit_3.raise_()
        self.label_3.raise_()
        self.lineEdit_4.raise_()
        self.label_4.raise_()
        self.lineEdit_2.raise_()
        self.label_5.raise_()
        self.lineEdit_5.raise_()
        self.label_6.raise_()
        self.lineEdit_6.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.label_7.raise_()
        self.lineEdit_7.raise_()
        self.label_8.raise_()
        self.lineEdit_8.raise_()
        registerpage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(registerpage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1026, 26))
        self.menubar.setObjectName("menubar")
        registerpage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(registerpage)
        self.statusbar.setObjectName("statusbar")
        registerpage.setStatusBar(self.statusbar)

        self.retranslateUi(registerpage)
        QtCore.QMetaObject.connectSlotsByName(registerpage)

        self.pushButton.clicked.connect(lambda : self.ins())
        
    def retranslateUi(self, registerpage):
        _translate = QtCore.QCoreApplication.translate
        registerpage.setWindowTitle(_translate("registerpage", "MainWindow"))
        self.label_6.setText(_translate("registerpage", "Contact No"))
        self.label_2.setText(_translate("registerpage", "User Name"))
        self.label_4.setText(_translate("registerpage", "Confirm password"))
        self.label_5.setText(_translate("registerpage", "Alternate No"))
        self.label_3.setText(_translate("registerpage", "Password"))
        self.pushButton.setText(_translate("registerpage", "Submit"))
        self.label.setText(_translate("registerpage", "Full Name"))
        self.label_7.setText(_translate("registerpage", "Address"))
        self.label_8.setText(_translate("registerpage", "Pincode"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registerpage = QtWidgets.QMainWindow()
    ui = Ui_registerpage()
    ui.setupUi(registerpage)
    registerpage.show()
    sys.exit(app.exec_())
