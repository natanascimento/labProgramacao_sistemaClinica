import pessoa as p


class funcionario (p.pessoa):
    def __init__(self):
        self.matricula = " "
        self.cargo = " "
        self.setor = " "
        self.cpf = " "
        super().__init__()

    def cadastrar_funcionario(self):
        self.matricula = input("Entre com a matricula: ")
        self.cargo = input("Entre com o cargo: ")
        self.setor = input("Entre com o setor: ")
        self.cpf = input("Entre com o CPF: ")
        super().cadastro_pessoa()

    def exibir_funcionario(self):
        super().exibir_pessoa()
        print(self.matricula)
        print(self.cargo)
        print(self.setor)
        print(self.cpf)