# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_payment.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from online import Ui_online
import sqlite3
import online

class Ui_user_payment(object):
    def pay(self):
        try:
                connection=sqlite3.connect("MyLaundry.db")
                res= connection.execute("SELECT * FROM user")
                con=connection.cursor()
                ces=list(res)
                print(ces)
                user=(list(ces[0])[0])
                passw=(list(ces[0])[1])
                data = [(user,passw,"Pending")]
                c=con.executemany("INSERT INTO Payment  VALUES(?,?,?)",data)
                connection.commit()
                connection.close()
            
        except:
                print("Failed")
        
                
    def openWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_online()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def setupUi(self, user_payment):
        user_payment.setObjectName("user_payment")
        user_payment.resize(901, 600)
        self.centralwidget = QtWidgets.QWidget(user_payment)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, -20, 801, 401))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pay.jpg"))
        self.label.setObjectName("label")
        self.up_bt = QtWidgets.QPushButton(self.centralwidget)
        self.up_bt.setGeometry(QtCore.QRect(120, 370, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.up_bt.setFont(font)
        self.up_bt.setObjectName("up_bt")

        self.up_bt.clicked.connect(self.openWindow)

        
        self.cd_bt = QtWidgets.QPushButton(self.centralwidget)
        self.cd_bt.setGeometry(QtCore.QRect(530, 370, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cd_bt.setFont(font)
        self.cd_bt.setObjectName("cd_bt")
        self.cd_bt.clicked.connect(self.pay)
        user_payment.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(user_payment)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 901, 26))
        self.menubar.setObjectName("menubar")
        user_payment.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(user_payment)
        self.statusbar.setObjectName("statusbar")
        user_payment.setStatusBar(self.statusbar)

        self.retranslateUi(user_payment)
        QtCore.QMetaObject.connectSlotsByName(user_payment)

    def retranslateUi(self, user_payment):
        _translate = QtCore.QCoreApplication.translate
        user_payment.setWindowTitle(_translate("user_payment", "MainWindow"))
        self.up_bt.setText(_translate("user_payment", "Online"))
        self.cd_bt.setText(_translate("user_payment", "Cashon Delivery"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    user_payment = QtWidgets.QMainWindow()
    ui = Ui_user_payment()
    ui.setupUi(user_payment)
    user_payment.show()
    sys.exit(app.exec_())
