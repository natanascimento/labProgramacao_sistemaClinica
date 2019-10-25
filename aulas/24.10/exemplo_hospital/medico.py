import endereco as e

class medico:
    def __init__(self):
        self.nome = " "
        self.crm = " "
        self.celular1 = " "
        self.celular2 = " "
        self.email = " "
        self.e = e.endereco()

    def cadastrar_medico(self):
        self.nome = input("Informe o nome do médico: ")
        self.crm = input("Informe o CRM do médico: ")
        self.celular1 = input("Informe o celular principal do médico: ")
        self.celular2 = input("Informe o segundo celular do médico: ")
        self.email = input("Informe o email do médico: ")
        self.e.cadastrar_endereco()
        