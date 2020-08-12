# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'payment.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from succeed import Ui_succeed
from pending_pay import Ui_pending_pay

class Ui_payment(object):
    def openWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_succeed()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow1(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_pending_pay()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def setupUi(self, payment):
        payment.setObjectName("payment")
        payment.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(payment)
        self.centralwidget.setObjectName("centralwidget")
        self.sus_bt = QtWidgets.QPushButton(self.centralwidget)
        self.sus_bt.setGeometry(QtCore.QRect(180, 150, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sus_bt.setFont(font)
        self.sus_bt.setObjectName("sus_bt")

        self.sus_bt.clicked.connect(self.openWindow)
        
        self.penp_bt = QtWidgets.QPushButton(self.centralwidget)
        self.penp_bt.setGeometry(QtCore.QRect(380, 150, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.penp_bt.setFont(font)
        self.penp_bt.setObjectName("penp_bt")

        self.penp_bt.clicked.connect(self.openWindow1)
        
        payment.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(payment)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        payment.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(payment)
        self.statusbar.setObjectName("statusbar")
        payment.setStatusBar(self.statusbar)

        self.retranslateUi(payment)
        QtCore.QMetaObject.connectSlotsByName(payment)

    def retranslateUi(self, payment):
        _translate = QtCore.QCoreApplication.translate
        payment.setWindowTitle(_translate("payment", "MainWindow"))
        self.sus_bt.setText(_translate("payment", "Succeed"))
        self.penp_bt.setText(_translate("payment", "pending"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    payment = QtWidgets.QMainWindow()
    ui = Ui_payment()
    ui.setupUi(payment)
    payment.show()
    sys.exit(app.exec_())
