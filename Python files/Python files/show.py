# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_show(object):
    def pay(self):
            try:
                        connection=sqlite3.connect("MyLaundry.db")
                        res= connection.execute("SELECT * FROM user")
                        con=connection.cursor()
                        ces=list(res)
                        print(ces)
                        user=(list(ces[0])[0])
                        passw=(list(ces[0])[1])
                        #data=[(user,passw)]
                        c=con.execute("SELECT * FROM Request WHERE username=? AND Password=?",(user,passw))
                        c=list(c)
                        for i in c:
                                a =list(i)[2]
                                b=list(i)[3]
                                c=list(i)[4]
                                d=list(i)[5]
                                e=list(i)[6]
                                print("\n\n\n\nuygjhv",*i)
                        if not(a==0 and b==0 and c==0 and d==0):
                                fin="Pant="+str(a//10)+"\nShirt="+str(b//8)+"\nKurti="+str(c//20)+"\nPunjabi="+str(d//20)
                                self.textEdit.setText(str(fin))
                        else:
                                self.textEdit.setText("Pant=1\nShirt=2\nKurti=3\nPunjabi=4")
                                connection.commit()
                                connection.close()
                    
    
            
            except:
                        print("Failed")

    def setupUi(self, show):
        show.setObjectName("show")
        show.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(show)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 20, 621, 401))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(610, 490, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.pay)
        show.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(show)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        show.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(show)
        self.statusbar.setObjectName("statusbar")
        show.setStatusBar(self.statusbar)

        self.retranslateUi(show)
        QtCore.QMetaObject.connectSlotsByName(show)

    def retranslateUi(self, show):
        _translate = QtCore.QCoreApplication.translate
        show.setWindowTitle(_translate("show", "MainWindow"))
        self.pushButton.setText(_translate("show", "Show"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    show = QtWidgets.QMainWindow()
    ui = Ui_show()
    ui.setupUi(show)
    show.show()
    sys.exit(app.exec_())
