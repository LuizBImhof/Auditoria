# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Inicio.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from teste import *
class Ui_Inicio(object):
    def setupUi(self, Inicio):
        Inicio.setObjectName("MainWindow")
        Inicio.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Inicio)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.abreOutra)
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        Inicio.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Inicio)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Inicio.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Inicio)
        self.statusbar.setObjectName("statusbar")
        Inicio.setStatusBar(self.statusbar)

        self.retranslateUi(Inicio)
        QtCore.QMetaObject.connectSlotsByName(Inicio)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Início - Nome do sistema de vendas - user"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))

    def abreOutra(self):
        self.nova = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.nova)
        self.nova.show()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Inicio = QtWidgets.QMainWindow()
    ui = Ui_Inicio()
    ui.setupUi(Inicio)
    Inicio.show()
    sys.exit(app.exec_())

