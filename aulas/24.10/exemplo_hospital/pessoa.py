class pessoa:
    def __init__(self):
        self.nome = " "
        self.celular = " "
        self.email = " "
    
    def cadastro_pessoa(self):
        self.nome = input("Informe o nome da pessoa: ")
        self.celular = input("Informe o celular da pessoa: ")
        self.email = input("Informe o email da pessoa")