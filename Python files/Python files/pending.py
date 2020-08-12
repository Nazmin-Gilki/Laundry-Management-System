# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pending.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pending(object):
    def setupUi(self, pending):
        pending.setObjectName("pending")
        pending.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(pending)
        self.centralwidget.setObjectName("centralwidget")
        pending.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(pending)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        pending.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(pending)
        self.statusbar.setObjectName("statusbar")
        pending.setStatusBar(self.statusbar)

        self.retranslateUi(pending)
        QtCore.QMetaObject.connectSlotsByName(pending)

    def retranslateUi(self, pending):
        _translate = QtCore.QCoreApplication.translate
        pending.setWindowTitle(_translate("pending", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pending = QtWidgets.QMainWindow()
    ui = Ui_pending()
    ui.setupUi(pending)
    pending.show()
    sys.exit(app.exec_())
