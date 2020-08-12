# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Request.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from completed import Ui_completed
from pending import Ui_pending


class Ui_Request(object):
    def openWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_completed()
        self.ui.setupUi(self.window)
        self.window.show()
    def openWindow1(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_pending()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, Request):
        Request.setObjectName("Request")
        Request.resize(926, 600)
        self.centralwidget = QtWidgets.QWidget(Request)
        self.centralwidget.setObjectName("centralwidget")
        self.com_bt = QtWidgets.QPushButton(self.centralwidget)
        self.com_bt.setGeometry(QtCore.QRect(210, 180, 93, 28))
        self.com_bt.setObjectName("com_bt")

        self.com_bt.clicked.connect(self.openWindow)
        
        self.pe_bt = QtWidgets.QPushButton(self.centralwidget)
        self.pe_bt.setGeometry(QtCore.QRect(480, 180, 93, 28))
        self.pe_bt.setObjectName("pe_bt")

        self.pe_bt.clicked.connect(self.openWindow1)
        
        Request.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Request)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 926, 26))
        self.menubar.setObjectName("menubar")
        Request.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Request)
        self.statusbar.setObjectName("statusbar")
        Request.setStatusBar(self.statusbar)

        self.retranslateUi(Request)
        QtCore.QMetaObject.connectSlotsByName(Request)

    def retranslateUi(self, Request):
        _translate = QtCore.QCoreApplication.translate
        Request.setWindowTitle(_translate("Request", "MainWindow"))
        self.com_bt.setText(_translate("Request", "Completed"))
        self.pe_bt.setText(_translate("Request", "pending"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Request = QtWidgets.QMainWindow()
    ui = Ui_Request()
    ui.setupUi(Request)
    Request.show()
    sys.exit(app.exec_())
