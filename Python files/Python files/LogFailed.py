# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogFailed.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LogFailed(object):
    def setupUi(self, LogFailed):
        LogFailed.setObjectName("LogFailed")
        LogFailed.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(LogFailed)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 220, 451, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        LogFailed.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LogFailed)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        LogFailed.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LogFailed)
        self.statusbar.setObjectName("statusbar")
        LogFailed.setStatusBar(self.statusbar)

        self.retranslateUi(LogFailed)
        QtCore.QMetaObject.connectSlotsByName(LogFailed)

    def retranslateUi(self, LogFailed):
        _translate = QtCore.QCoreApplication.translate
        LogFailed.setWindowTitle(_translate("LogFailed", "MainWindow"))
        self.label.setText(_translate("LogFailed", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; color:#fa0000;\">                      Login Failed</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogFailed = QtWidgets.QMainWindow()
    ui = Ui_LogFailed()
    ui.setupUi(LogFailed)
    LogFailed.show()
    sys.exit(app.exec_())
