# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegFaild.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegFaild(object):
    def setupUi(self, RegFaild):
        RegFaild.setObjectName("RegFaild")
        RegFaild.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(RegFaild)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, -30, 411, 131))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.f_bt = QtWidgets.QPushButton(self.centralwidget)
        self.f_bt.setGeometry(QtCore.QRect(350, 530, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.f_bt.setFont(font)
        self.f_bt.setObjectName("f_bt")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 80, 531, 441))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("unlike.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName("label_2")
        RegFaild.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RegFaild)
        self.statusbar.setObjectName("statusbar")
        RegFaild.setStatusBar(self.statusbar)

        self.retranslateUi(RegFaild)
        QtCore.QMetaObject.connectSlotsByName(RegFaild)

    def retranslateUi(self, RegFaild):
        _translate = QtCore.QCoreApplication.translate
        RegFaild.setWindowTitle(_translate("RegFaild", "MainWindow"))
        self.label.setText(_translate("RegFaild", "Registration Failed!"))
        self.f_bt.setText(_translate("RegFaild", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegFaild = QtWidgets.QMainWindow()
    ui = Ui_RegFaild()
    ui.setupUi(RegFaild)
    RegFaild.show()
    sys.exit(app.exec_())
