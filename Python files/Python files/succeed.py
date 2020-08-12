# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'succeed.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_succeed(object):
    def setupUi(self, succeed):
        succeed.setObjectName("succeed")
        succeed.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(succeed)
        self.centralwidget.setObjectName("centralwidget")
        succeed.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(succeed)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        succeed.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(succeed)
        self.statusbar.setObjectName("statusbar")
        succeed.setStatusBar(self.statusbar)

        self.retranslateUi(succeed)
        QtCore.QMetaObject.connectSlotsByName(succeed)

    def retranslateUi(self, succeed):
        _translate = QtCore.QCoreApplication.translate
        succeed.setWindowTitle(_translate("succeed", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    succeed = QtWidgets.QMainWindow()
    ui = Ui_succeed()
    ui.setupUi(succeed)
    succeed.show()
    sys.exit(app.exec_())
