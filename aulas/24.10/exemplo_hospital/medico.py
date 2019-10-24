class medico:
    def __init__(self):
        self.nome = " "
        self.crm = " "
        self.endereco = " "
        self.numero = " "
        self.complemento = " "
        self.bairro = " "
        self.cidade = " "
        self.uf = " "
        self.celular1 = " "
        self.celular2 = " "
        self.email = " "
    def cadastrar_medico(self):
        self.nome = input("Informe o nome do médico: ")
        self.crm = input("Informe o CRM do médico: ")
        self.endereco = input("Informe o endereco do médico: ")
        self.numero = input("Informe o numero do endereco do médico: ")
        self.complemento = input ("Informe o complemento do endereco do médico: ")
        self.bairro = input("Informe o bairro do médico: ")
        self.cidade = input("Informe a cidade do médico: ")
        self.uf = input("Informe a Unidade Federativa do médico: ")
        self.celular1 = input("Informe o celular principal do médico: ")
        self.celular2 = input("Informe o segundo celular do médico: ")
        self.email = input("Informe o email do médico: ")