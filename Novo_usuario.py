# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Novo_usuario.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Gerenciador import gerenciaBD

class Ui_usuario(object):
    def setupUi(self, usuario):
        usuario.setObjectName("usuario")
        usuario.resize(396, 188)
        self.gridLayout_2 = QtWidgets.QGridLayout(usuario)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(usuario)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(False)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(usuario)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(usuario)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.senha_ins = QtWidgets.QLineEdit(usuario)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.senha_ins.sizePolicy().hasHeightForWidth())
        self.senha_ins.setSizePolicy(sizePolicy)
        self.senha_ins.setEchoMode(QtWidgets.QLineEdit.Password)
        self.senha_ins.setObjectName("senha_ins")
        self.gridLayout.addWidget(self.senha_ins, 2, 1, 1, 1)
        self.nome_ins = QtWidgets.QLineEdit(usuario)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nome_ins.sizePolicy().hasHeightForWidth())
        self.nome_ins.setSizePolicy(sizePolicy)
        self.nome_ins.setObjectName("nome_ins")
        self.gridLayout.addWidget(self.nome_ins, 0, 1, 1, 1)
        self.apaga_check = QtWidgets.QCheckBox(usuario)
        self.apaga_check.setObjectName("apaga_check")
        self.gridLayout.addWidget(self.apaga_check, 3, 0, 1, 1)
        self.inclui_check = QtWidgets.QCheckBox(usuario)
        self.inclui_check.setObjectName("inclui_check")
        self.gridLayout.addWidget(self.inclui_check, 3, 1, 1, 1)
        self.login_ins = QtWidgets.QLineEdit(usuario)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_ins.sizePolicy().hasHeightForWidth())
        self.login_ins.setSizePolicy(sizePolicy)
        self.login_ins.setObjectName("login_ins")
        self.gridLayout.addWidget(self.login_ins, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(usuario)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ok_btn = QtWidgets.QPushButton(usuario)
        self.ok_btn.setObjectName("ok_btn")
        self.ok_btn.clicked.connect(self.incluir_usuario)
        self.horizontalLayout.addWidget(self.ok_btn)
        self.limpar_btn = QtWidgets.QPushButton(usuario)
        self.limpar_btn.setObjectName("limpar_btn")
        self.limpar_btn.clicked.connect(self.limpar)
        self.horizontalLayout.addWidget(self.limpar_btn)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 1, 1, 1)

        self.retranslateUi(usuario)
        QtCore.QMetaObject.connectSlotsByName(usuario)

    def retranslateUi(self, usuario):
        _translate = QtCore.QCoreApplication.translate
        usuario.setWindowTitle(_translate("usuario", "Novo usuário "))
        self.label_3.setText(_translate("usuario", "Novo Usuário"))
        self.label.setText(_translate("usuario", "Nome"))
        self.label_2.setText(_translate("usuario", "Senha"))
        self.apaga_check.setText(_translate("usuario", "Permite Apagar"))
        self.inclui_check.setText(_translate("usuario", "Permite Incluir"))
        self.label_4.setText(_translate("usuario", "Login"))
        self.ok_btn.setText(_translate("usuario", "OK"))
        self.limpar_btn.setText(_translate("usuario", "Limpar"))


    def incluir_usuario(self):

        nome = self.nome_ins.text()
        login = self.login_ins.text()
        senha = self.senha_ins.text()
        apaga = int(self.apaga_check.isChecked())
        inclui = int(self.inclui_check.isChecked())

        if (not nome or not login or not senha):
            QMessageBox.warning(usuario,'Erro encontrado', 'Informações obrigatórias não preenchidas')
        else:
            gerenciaBD.inserir_usuario(login, senha, apaga, inclui, nome)
            userNovo = gerenciaBD.busca_usuario_todo(login)
            print(userNovo)
            usuario.hide()


    def limpar(self):
        self.nome_ins.clear()
        self.senha_ins.clear()
        self.login_ins.clear()
        self.apaga_check.setChecked(False)
        self.inclui_check.setChecked(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    usuario = QtWidgets.QWidget()
    ui = Ui_usuario()
    ui.setupUi(usuario)
    usuario.show()
    sys.exit(app.exec_())

