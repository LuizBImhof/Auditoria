# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Controlador
from Inicio import *

from Gerenciador import gerenciaBD


class Ui_Login(object):


    def setupLogin(self, Login):
        self.tentativa = 0
        Login.setObjectName("Login")
        Login.resize(518, 248)
        Login.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Login)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.sistema_lbl = QtWidgets.QLabel(Login)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.sistema_lbl.setFont(font)
        self.sistema_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.sistema_lbl.setObjectName("sistema_lbl")
        self.verticalLayout.addWidget(self.sistema_lbl)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.usuario_lbl = QtWidgets.QLabel(Login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usuario_lbl.sizePolicy().hasHeightForWidth())
        self.usuario_lbl.setSizePolicy(sizePolicy)
        self.usuario_lbl.setObjectName("usuario_lbl")
        self.horizontalLayout.addWidget(self.usuario_lbl)
        self.usuario_ins = QtWidgets.QLineEdit(Login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usuario_ins.sizePolicy().hasHeightForWidth())
        self.usuario_ins.setSizePolicy(sizePolicy)
        self.usuario_ins.setObjectName("usuario_ins")
        self.horizontalLayout.addWidget(self.usuario_ins)
        self.senha_lbl = QtWidgets.QLabel(Login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.senha_lbl.sizePolicy().hasHeightForWidth())
        self.senha_lbl.setSizePolicy(sizePolicy)
        self.senha_lbl.setObjectName("senha_lbl")
        self.horizontalLayout.addWidget(self.senha_lbl)
        self.senha_ins = QtWidgets.QLineEdit(Login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.senha_ins.sizePolicy().hasHeightForWidth())
        self.senha_ins.setSizePolicy(sizePolicy)
        self.senha_ins.setEchoMode(QtWidgets.QLineEdit.Password)
        self.senha_ins.setObjectName("senha_ins")
        self.horizontalLayout.addWidget(self.senha_ins)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.erro_lbl = QtWidgets.QLabel(Login)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.erro_lbl.setFont(font)
        self.erro_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.erro_lbl.setObjectName("erro_lbl")
        self.horizontalLayout_2.addWidget(self.erro_lbl)
        self.ok_btn = QtWidgets.QPushButton(Login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok_btn.sizePolicy().hasHeightForWidth())
        self.ok_btn.setSizePolicy(sizePolicy)
        self.ok_btn.setObjectName("ok_btn")
        self.ok_btn.clicked.connect(self.logar)
        self.horizontalLayout_2.addWidget(self.ok_btn)
        self.cancel_btn = QtWidgets.QPushButton(Login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_btn.sizePolicy().hasHeightForWidth())
        self.cancel_btn.setSizePolicy(sizePolicy)
        self.cancel_btn.setObjectName("cancel_btn")
        self.cancel_btn.clicked.connect(self.limpar)
        self.horizontalLayout_2.addWidget(self.cancel_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):

        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login - Sistema de vendas"))
        self.sistema_lbl.setText(_translate("Login", "NOME DO SISTEMA"))
        self.usuario_lbl.setText(_translate("Login", "Usuário:"))
        self.senha_lbl.setText(_translate("Login", "Senha:"))
        self.erro_lbl.setText(_translate("Login", ""))
        self.ok_btn.setText(_translate("Login", "OK"))
        self.cancel_btn.setText(_translate("Login", "Limpar"))


    def logar(self):
        _translate = QtCore.QCoreApplication.translate
        usuarioins = self.usuario_ins.text()
        senhains = self.senha_ins.text()
        logado = 0
        msg_erro = ""
        usuarioLogado = gerenciaBD.busca_usuario_login(usuarioins)
        print (self.tentativa)

        if (usuarioLogado == None):
            msg_erro = "Usuário inexistente, tente novamente"
            self.erro_lbl.setText(_translate("Login", msg_erro))
        else:
            usuario = usuarioLogado[0]
            senha = usuarioLogado[1]
            apaga = usuarioLogado[2]
            escreve = usuarioLogado[3]
            nome = usuarioLogado[4]
            ativo = usuarioLogado[5]
            handle_usuario = usuarioLogado[6]
            print(usuario, senha, apaga, escreve, nome, ativo)
            if (ativo == 0):
                msg_erro = "Usuario bloqueado, entre em contato com o administrador."
                self.ok_btn.setEnabled(False)

            elif(senha == senhains):
                print("Logado")
                logado = 1
                self.tentativa = 0
                self.abreTelaInicial()
            else:
                self.tentativa = self.tentativa + 1

                msg_erro = "Senha incorreta, tente novamente " + str(self.tentativa)


                if (self.tentativa >= 3):
                    self.ok_btn.setEnabled(False)
                    gerenciaBD.bloqueia_usuario(handle_usuario)
                    msg_erro = "Usuario bloqueado, entre em contato com o administrador."


        self.erro_lbl.setText(_translate("Login", msg_erro))


    def abreTelaInicial(self):
        self.nova = QtWidgets.QMainWindow()
        self.ui = Ui_Inicio()
        self.ui.setupUi(self.nova)
        self.nova.show()
        Login.hide()

    def limpar(self):
        _translate = QtCore.QCoreApplication.translate
        self.senha_ins.clear()
        self.usuario_ins.clear()
        self.erro_lbl.setText(_translate("Login", ""))
        self.ok_btn.setEnabled(True)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupLogin(Login)
    Login.show()
    sys.exit(app.exec_())

