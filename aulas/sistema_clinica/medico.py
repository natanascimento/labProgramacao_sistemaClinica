#Implementação Dia 24/10

import pessoa as p

class medico (p.pessoa):
    def __init__(self):
        self.crm = " "
        self.celular2 = " "
        super().__init__()

    def cadastrar_medico(self):
        self.crm = input("Informe o CRM do médico: ")
        self.celular2 = input("Informe o segundo celular do médico: ")
        super().cadastro_pessoa()
    
    def exibir_medico (self):
        super().exibir_pessoa()