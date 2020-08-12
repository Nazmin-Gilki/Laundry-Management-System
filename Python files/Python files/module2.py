# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'module2.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Request import Ui_Request
from payment import Ui_payment
from complaints import Ui_complaints


class Ui_module2(object):
    def openWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Request()
        self.ui.setupUi(self.window)
        self.window.show()
    def openWindow1(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_payment()
        self.ui.setupUi(self.window)
        self.window.show()
    def openWindow2(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_complaints()
        self.ui.setupUi(self.window)
        self.window.show()



    def setupUi(self, module2):
        module2.setObjectName("module2")
        module2.resize(1068, 600)
        self.centralwidget = QtWidgets.QWidget(module2)
        self.centralwidget.setObjectName("centralwidget")
        self.rq_bt = QtWidgets.QPushButton(self.centralwidget)
        self.rq_bt.setGeometry(QtCore.QRect(250, 440, 101, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rq_bt.setFont(font)
        self.rq_bt.setObjectName("rq_bt")

        self.rq_bt.clicked.connect(self.openWindow)


        
        self.py_bt = QtWidgets.QPushButton(self.centralwidget)
        self.py_bt.setGeometry(QtCore.QRect(620, 440, 101, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.py_bt.setFont(font)
        self.py_bt.setObjectName("py_bt")

        
        self.py_bt.clicked.connect(self.openWindow1)


        
        self.c_bt = QtWidgets.QPushButton(self.centralwidget)
        self.c_bt.setGeometry(QtCore.QRect(440, 500, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.c_bt.setFont(font)
        self.c_bt.setObjectName("c_bt")

        
        self.c_bt.clicked.connect(self.openWindow2)



        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 981, 381))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("l4.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 380, 981, 16))
        self.label_2.setObjectName("label_2")
        module2.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(module2)
        self.statusbar.setObjectName("statusbar")
        module2.setStatusBar(self.statusbar)

        self.retranslateUi(module2)
        QtCore.QMetaObject.connectSlotsByName(module2)

    def retranslateUi(self, module2):
        _translate = QtCore.QCoreApplication.translate
        module2.setWindowTitle(_translate("module2", "MainWindow"))
        self.rq_bt.setText(_translate("module2", "Request"))
        self.py_bt.setText(_translate("module2", "Payment"))
        self.c_bt.setText(_translate("module2", "Complaints"))
        self.label_2.setText(_translate("module2", "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    module2 = QtWidgets.QMainWindow()
    ui = Ui_module2()
    ui.setupUi(module2)
    module2.show()
    sys.exit(app.exec_())
