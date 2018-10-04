import sqlite3
import time
import datetime
import os.path



def criar_tabela():
    pass


def cria_cliente(nome):
    conn = sqlite3.connect('venda.db')
    c = conn.cursor()
    data = str(datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y'))
    nome = nome
    cidade = 3
    bairro = 'centro'
    numeroendereco = 502
    saldo = 0
    ativo = 1
    cpf = 108163365986

    c.execute("INSERT INTO CLIENTE (NOME, CIDADE, BAIRRO, NUMERO_ENDERECO, NASCIMENTO, SALDO, ATIVO, CPF) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
              (nome, cidade, bairro, numeroendereco, data, saldo, ativo, cpf))

    conn.commit()

nome1 = input("Digita o nome")
cria_cliente(nome1)
