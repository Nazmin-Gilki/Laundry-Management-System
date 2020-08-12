# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pending_pay.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pending_pay(object):
    def setupUi(self, pending_pay):
        pending_pay.setObjectName("pending_pay")
        pending_pay.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(pending_pay)
        self.centralwidget.setObjectName("centralwidget")
        pending_pay.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(pending_pay)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        pending_pay.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(pending_pay)
        self.statusbar.setObjectName("statusbar")
        pending_pay.setStatusBar(self.statusbar)

        self.retranslateUi(pending_pay)
        QtCore.QMetaObject.connectSlotsByName(pending_pay)

    def retranslateUi(self, pending_pay):
        _translate = QtCore.QCoreApplication.translate
        pending_pay.setWindowTitle(_translate("pending_pay", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pending_pay = QtWidgets.QMainWindow()
    ui = Ui_pending_pay()
    ui.setupUi(pending_pay)
    pending_pay.show()
    sys.exit(app.exec_())
