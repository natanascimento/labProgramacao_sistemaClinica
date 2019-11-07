import pickle
import pessoa as p

dados_funcionario = "dados_funcionario.pickle"

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

        #lista de funcionario
        lista_funcionario = [self.matricula, self.cargo, self.setor, self.cpf, self.nome, self.celular, self.email, self.e.logradouro, self.e.numero, self.e.complemento, self.e.bairro, self.e.cidade, self.e.uf]

        #dump funcionario
        pickle.dump(lista_funcionario, open(dados_funcionario, 'ab+'))

        #exportando dados
        self.salvar_funcionario()

    def exibir_funcionario(self):
        #super().exibir_pessoa()
        with open ("funcionario.txt", 'r') as arquivo:
            for linhas in arquivo:
                linhas_em_brancos = linhas.strip()
                print(linhas_em_brancos)

    def salvar_funcionario (self):
        with open("funcionario.txt", 'a') as dados:
            nova_lista = pickle.load(open(dados_funcionario, 'rb'))
            dados.write(str(nova_lista) + "\n")