from Gerenciador import gerenciaBD

class Controlador:

    usuario = ""
    apaga = 0
    escreve = 0
    vendedor = ""
    gerenciaBD.inserir_usuario("a","a",0,0,"a")
    def __init__(self, usuario, apaga, escreve, nome):
        self.usuario = usuario
        self.apaga = apaga
        self.escreve = escreve
        self.vendedor = nome

    # login = input("cep: ")
    # senha = input("pass: ")

    # gerenciaBD.busca_usuario_login_senha(login, senha)
    # gerenciaBD.inserir_cidade('08163365986',"Rio do Sul", "SC")
    # gerenciaBD.busca_cidade_nome("rio do sul")
    # gerenciaBD.inserir_produto("Produto1", "um produto qualquer", 9.5, 10)
    # gerenciaBD.busca_produto_nome("produto12")
