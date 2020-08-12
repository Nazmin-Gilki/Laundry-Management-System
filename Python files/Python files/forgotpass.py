# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forgotpass.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_forgotpass(object):
    def setupUi(self, forgotpass):
        forgotpass.setObjectName("forgotpass")
        forgotpass.resize(854, 668)
        self.centralwidget = QtWidgets.QWidget(forgotpass)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(460, 350, 211, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(460, 430, 211, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 550, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 440, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 340, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 851, 311))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("fp.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName("label_3")
        forgotpass.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(forgotpass)
        self.statusbar.setObjectName("statusbar")
        forgotpass.setStatusBar(self.statusbar)

        self.retranslateUi(forgotpass)
        QtCore.QMetaObject.connectSlotsByName(forgotpass)

    def retranslateUi(self, forgotpass):
        _translate = QtCore.QCoreApplication.translate
        forgotpass.setWindowTitle(_translate("forgotpass", "MainWindow"))
        self.pushButton.setText(_translate("forgotpass", "Submit"))
        self.label_2.setText(_translate("forgotpass", "Confirm password"))
        self.label.setText(_translate("forgotpass", "Enter new password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    forgotpass = QtWidgets.QMainWindow()
    ui = Ui_forgotpass()
    ui.setupUi(forgotpass)
    forgotpass.show()
    sys.exit(app.exec_())
