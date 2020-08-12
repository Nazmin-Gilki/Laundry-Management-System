# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'completed.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_completed(object):
    def setupUi(self, completed):
        completed.setObjectName("completed")
        completed.resize(926, 600)
        self.centralwidget = QtWidgets.QWidget(completed)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 130, 331, 161))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        completed.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(completed)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 926, 26))
        self.menubar.setObjectName("menubar")
        completed.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(completed)
        self.statusbar.setObjectName("statusbar")
        completed.setStatusBar(self.statusbar)

        self.retranslateUi(completed)
        QtCore.QMetaObject.connectSlotsByName(completed)

    def retranslateUi(self, completed):
        _translate = QtCore.QCoreApplication.translate
        completed.setWindowTitle(_translate("completed", "MainWindow"))
        self.label.setText(_translate("completed", "Hello"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    completed = QtWidgets.QMainWindow()
    ui = Ui_completed()
    ui.setupUi(completed)
    completed.show()
    sys.exit(app.exec_())
