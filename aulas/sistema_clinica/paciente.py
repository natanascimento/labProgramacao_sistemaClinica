#Implementação Dia 24/10
import pickle
import pessoa as p

dados_paciente = "paciente_info.pickle"

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

        lista_paciente = [self.rg, self. cpf, self.telefone, self.convenio, self.idade, self.nome, self.celular, self.email, self.e.logradouro, self.e.numero, self.e.complemento, self.e.bairro, self.e.cidade, self.e.uf]

        #dump dos dados
        pickle.dump(lista_paciente, open (dados_paciente, "ab+"))
        
        #exportando dados
        self.salvar_paciente()
        
    def exibir_paciente (self):
        #super().exibir_pessoa()
        with open ("paciente.txt", 'r') as arquivo:
            for linhas in arquivo:
                linhas_em_brancos = linhas.strip()
                print(linhas_em_brancos)

    #salvar medico
    def salvar_paciente (self):
        with open ("paciente.txt", 'a') as dados:
            nova_lista = pickle.load(open(dados_paciente,"rb"))
            dados.write(str(nova_lista) + "\n")
