import endereco as e

class pessoa:
    def __init__(self):
        self.nome = " "
        self.e = e.endereco()
        self.celular = " "
        self.email = " "
    
    def cadastro_pessoa(self):
        self.nome = input("Informe o nome da pessoa: ")
        self.celular = input("Informe o celular da pessoa: ")
        self.email = input("Informe o email da pessoa")
        self.e.cadastrar_endereco()

    def exibir_pessoa(self):
        print(self.nome) 
        self.e.exibir_endereco()