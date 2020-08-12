# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'successregi.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_successregi(object):
    def setupUi(self, successregi):
        successregi.setObjectName("successregi")
        successregi.resize(800, 804)
        self.centralwidget = QtWidgets.QWidget(successregi)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 10, 601, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 680, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 80, 641, 551))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("thumbsup.png"))
        self.label_2.setObjectName("label_2")
        successregi.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(successregi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        successregi.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(successregi)
        self.statusbar.setObjectName("statusbar")
        successregi.setStatusBar(self.statusbar)

        self.retranslateUi(successregi)
        QtCore.QMetaObject.connectSlotsByName(successregi)

    def retranslateUi(self, successregi):
        _translate = QtCore.QCoreApplication.translate
        successregi.setWindowTitle(_translate("successregi", "MainWindow"))
        self.label.setText(_translate("successregi", "You are successfully registered!"))
        self.pushButton.setText(_translate("successregi", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    successregi = QtWidgets.QMainWindow()
    ui = Ui_successregi()
    ui.setupUi(successregi)
    successregi.show()
    sys.exit(app.exec_())
