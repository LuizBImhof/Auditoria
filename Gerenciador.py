#!usr/bin/python

import datetime
import sqlite3
import time


class Gerenciador:

    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

    def get_data_atual(self):
        hora = time.time()
        dataatual = str(datetime.datetime.fromtimestamp(hora).strftime('%d-%m-%Y %H:%M:%S'))
        return dataatual

    # USUARIO
    def inserir_usuario(self, login, senha, apaga, escreve, nome):
        datacriacao = self.get_data_atual()

        self.cursor.execute(
            "INSERT INTO USUARIO (LOGIN, SENHA ,APAGA, ESCREVE, VENDAS, NOME, DATACRIACAO) VALUES (?,?,?,?,?,?,?)",
            (login, senha, apaga, escreve, 0, nome, datacriacao))
        self.conn.commit()


    def busca_usuario(self,login):
        usuario = None
        self.cursor.execute("SELECT LOGIN, SENHA, APAGA, ESCREVE, NOME, ATIVO, HANDLE FROM USUARIO WHERE LOGIN = ?",
                            (login,))
        for linha in cursor.fetchall():
            usuario = linha
        return usuario



    def busca_usuario_login_senha(self, login, senha):
        self.cursor.execute("SELECT LOGIN, SENHA FROM USUARIO")
        existe = 0
        usuario = ""
        for linha in cursor.fetchall():
            if(linha[0] == login):
                if(linha[1] == senha):
                    usuario = linha
                    existe = 1
        if (existe == 0):
            print("usuário ou senha incorreto")
            #retorna falso
        else:
            print(usuario)
            #retorna true


    def bloqueia_usuario(self, handle):
        self.cursor.execute("UPDATE USUARIO SET ATIVO = 0 WHERE HANDLE = ?",
                            (handle,))


#VENDA TODO
    def inserir_venda(self, cliente, vendedor, produto,):
        datacriacao = self.get_data_atual()

        self.cursor.execute(
            "INSERT INTO VENDA (LOGIN, SENHA ,APAGA, ESCREVE, VENDAS, NOME, DATACRIACAO) VALUES (?,?,?,?,?,?,?)",
            (login, senha, apaga, escreve, 0, nome, datacriacao))
        self.conn.commit()





#CIDADE
    def inserir_cidade(self, cep, nome, estado):
        datacriacao = self.get_data_atual()

        self.cursor.execute(
            "INSERT INTO CIDADE (CEP, NOME, ESTADO, DATACRIACAO) VALUES (?,?,?,?)",
            (cep, nome, estado, datacriacao))
        self.conn.commit()

    def busca_cidade_nome(self, nome):
        self.cursor.execute("SELECT * FROM CIDADE WHERE NOME LIKE '"+nome+"'")
        existe = 0
        cidade = ""
        for linha in cursor.fetchall():
            if(len(linha) > 0 ):
                cidade = linha
                existe = 1
        if(existe == 1):
            print(cidade)
            #retorna true e a cidade
        else:
            print("cidade inexistente")
            #retorna falso

#PRODUTO
    def inserir_produto(self, nome, descricao, preco, quantidade):
        datacriacao = self.get_data_atual()

        self.cursor.execute(
            "INSERT INTO PRODUTO (NOME, DESCRICAO, PRECO, ESTOQUE, DATACRIACAO) VALUES (?,?,?,?,?)",
            (nome, descricao, preco, quantidade, datacriacao))
        self.conn.commit()

    def busca_produto_nome(self, nome):
        self.cursor.execute("SELECT * FROM PRODUTO WHERE NOME LIKE '"+nome+"'")
        existe = 0
        produto = ""
        for linha in cursor.fetchall():
            if (len(linha) > 0):
                produto = linha
                existe = 1
        if (existe == 1):
            print(produto)
            # retorna true e o produto
        else:
            print("produto inexistente")
            # retorna falso

    #VENDA_PRODUTO TODO
    def inserir_venda_prod(self, login, senha, apaga, escreve, nome):
        datacriacao = self.get_data_atual()

        self.cursor.execute(
            "INSERT INTO USUARIO (LOGIN, SENHA ,APAGA, ESCREVE, VENDAS, NOME, DATACRIACAO) VALUES (?,?,?,?,?,?,?)",
            (login, senha, apaga, escreve, 0, nome, datacriacao))
        self.conn.commit()

    def __del__(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


conn = sqlite3.connect('BANCO.db')
cursor = conn.cursor()
gerenciaBD = Gerenciador(conn, cursor)
#gerenciaBD.inserir_usuario('admin', 'admin', 1, 1, 'luiz')
# gerenciaBD.busca_usuario_login_senha('admin','admin')