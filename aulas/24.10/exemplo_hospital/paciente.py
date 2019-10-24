class paciente:
    def __init__(self):
        self.nome = " "
        self.rg = " "
        self.cpf = ""
        self.endereco = " "
        self.numero = " "
        self.complemento = " "
        self.bairro = " "
        self.cidade = " "
        self.telefone = " "
        self.celular = " "
        self.convenio = " "
        self.email = " "

    def cadastrar_paciente (self):
        self.nome = input ("Informe o seu nome: ")
        self.rg = input("Informe o seu RG: ")
        self.cpf = input("Informe o seu CPF: ")
        self.endereco = input("Informe o seu endereço: ")
        self.numero = input("Informe o numero do seu endereço: ")
        self.complemento = input("Informe o complemento do seu endereço")
        self.bairro = input("Informe o seu bairro: ")
        self.cidade = input("Informe a sua cidade: ")
        self.telefone = input("Informe o seu telefone: ")
        self.celular = input("Informe o seu celular: ")
        self.convenio = input("Informe seu convenio: ")
        self.email = input("Informe seu email: ")

    def exibir_paciente (self):
        print(self.nome)

