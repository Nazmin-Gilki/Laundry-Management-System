# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'donepage.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_donepage(object):
    def Query(self):
        try:
            conn=None
            c=None
            conn= sqlite3.connect('C:\\Python36\\Scripts\\MyLaundry.db')
            connection=sqlite3.connect("MyLaundry.db")
            res= connection.execute("SELECT * FROM user")
            ces=list(res)
            user=(list(ces[0])[0])
            passw=(list(ces[0])[1])
            c= conn.cursor()
            r= conn.execute("SELECT Username FROM Registration WHERE Username = ? AND Password=?",(user,passw))
            add=((list(r)[0])[0])
            data=[(add,self.textEdit.toPlainText())]
            c.executemany("INSERT INTO Queries  VALUES(?,?)",data)
            conn.commit()
            conn.close()
        except:
            print("failed")
    def setupUi(self, donepage):
        donepage.setObjectName("donepage")
        donepage.resize(956, 728)
        self.centralwidget = QtWidgets.QWidget(donepage)
        self.centralwidget.setObjectName("centralwidget")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(270, 80, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.ok = QtWidgets.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(410, 260, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ok.setFont(font)
        self.ok.setObjectName("ok")
        self.ok.clicked.connect(self.Query)
       
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(230, 140, 451, 81))
        self.textEdit.setObjectName("textEdit")
        donepage.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(donepage)
        self.statusbar.setObjectName("statusbar")
        donepage.setStatusBar(self.statusbar)

        self.retranslateUi(donepage)
        QtCore.QMetaObject.connectSlotsByName(donepage)

    def retranslateUi(self, donepage):
        _translate = QtCore.QCoreApplication.translate
        donepage.setWindowTitle(_translate("donepage", "MainWindow"))
        self.label_15.setText(_translate("donepage", "Any Queries Or Complaints"))
        self.ok.setText(_translate("donepage", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    donepage = QtWidgets.QMainWindow()
    ui = Ui_donepage()
    ui.setupUi(donepage)
    donepage.show()
    sys.exit(app.exec_())
