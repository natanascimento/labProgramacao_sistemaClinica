import endereco as e

class endereco:
    def __init__(self):
        self.logradouro = " "
        self.numero = " "
        self.complemento = " "
        self.bairro = " "
        self.cidade = " "
        self.uf = " "

    def cadastrar_endereco (self):
        self.logradouro = input("Entre com o Endereco: ")
        self.numero = input("Entre com o numero do Endereço: ")
        self.complemento = input("Entre com o complemento do Endereço: ")
        self.bairro = input("Entre com o bairro do endereço: ")
        self.cidade = input("Entre com a cidade: ")
        self.uf = input("Informe a Unidade Federativa: ")
    
    def exibir_endereco (self):
        print(self.logradouro)
        print(self.numero)
        print(self.complemento)
        print(self.bairro)
        print(self.cidade)
        print(self.uf)