# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'status.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from show import Ui_show
import sqlite3
class Ui_status(object):
    
    def pay(self):
                try:
                        connection=sqlite3.connect("MyLaundry.db")
                        res= connection.execute("SELECT * FROM user")
                        con=connection.cursor()
                        ces=list(res)
                        print(ces)
                        user=(list(ces[0])[0])
                        passw=(list(ces[0])[1])
                        data="Completed"
                        c=con.execute("SELECT DISTINCT username FROM Payment")
                        print(list(c))
                        connection.commit()
                        connection.close()
                        self.wc=QtWidgets.QMainWindow()
                        self.ui=Ui_show()
                        self.ui.setupUi(self.wc)
                        self.wc.show()
    
            
                except:
                        print("Failed")
    
    def setupUi(self, status):
        status.setObjectName("status")
        status.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(status)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 60, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 190, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.pay)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(372, 190, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.pay)
        
        status.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(status)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        status.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(status)
        self.statusbar.setObjectName("statusbar")
        status.setStatusBar(self.statusbar)

        self.retranslateUi(status)
        QtCore.QMetaObject.connectSlotsByName(status)

    def retranslateUi(self, status):
        _translate = QtCore.QCoreApplication.translate
        status.setWindowTitle(_translate("status", "MainWindow"))
        self.label.setText(_translate("status", "Status"))
        self.pushButton.setText(_translate("status", "  Completed"))
        self.pushButton_2.setText(_translate("status", "Pending"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    status = QtWidgets.QMainWindow()
    ui = Ui_status()
    ui.setupUi(status)
    status.show()
    sys.exit(app.exec_())
