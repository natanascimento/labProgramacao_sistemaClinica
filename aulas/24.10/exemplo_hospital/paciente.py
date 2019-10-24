import endereco as e

class paciente:
    def __init__(self):
        self.nome = " "
        self.rg = " "
        self.cpf = ""
        self.telefone = " "
        self.celular = " "
        self.convenio = " "
        self.email = " "
        self.e = e.endereco()

    def cadastrar_paciente (self):
        self.nome = input ("Informe o seu nome: ")
        self.rg = input("Informe o seu RG: ")
        self.cpf = input("Informe o seu CPF: ")
        self.telefone = input("Informe o seu telefone: ")
        self.celular = input("Informe o seu celular: ")
        self.convenio = input("Informe seu convenio: ")
        self.email = input("Informe seu email: ")
        self.e.cadastrar_endereco()

    def exibir_paciente (self):
        print(self.nome)

