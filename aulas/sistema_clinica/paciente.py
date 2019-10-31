#Implementação Dia 24/10

import pessoa as p

class paciente (p.pessoa):
    def __init__(self):
        self.rg = " "
        self.cpf = ""
        self.telefone = " "
        self.convenio = " "
        self.idade = " "
        super().__init__()

    def cadastrar_paciente (self):
        self.rg = input("Informe o RG do paciente: ")
        self.cpf = input("Informe o CPF do paciente: ")
        self.telefone = input("Informe o telefone do paciente: ")
        self.convenio = input("Informe o convenio do paciente: ")
        self.idade = input("Informe a idade do paciente :")
        super().cadastro_pessoa()

    def exibir_paciente (self):
        super().exibir_pessoa()

