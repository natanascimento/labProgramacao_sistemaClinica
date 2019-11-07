#Implementação Dia 24/10
import pickle

import pessoa as p
import endereco as end

dados_medico = "medico_info.pickle"

class medico (p.pessoa):
    def __init__(self):
        self.crm = " "
        self.celular2 = " "
        super().__init__()

    def cadastrar_medico(self):
        self.crm = input("Informe o CRM do médico: ")
        self.celular2 = input("Informe o segundo celular do médico: ")
        super().cadastro_pessoa()

        #lista de informacoes 
        lista_medico = [self.crm, self.celular2, self.nome, self.celular, self.email, self.e.logradouro, self.e.numero, self.e.complemento, self.e.bairro, self.e.cidade, self.e.uf]
    
        #dump dos dados
        pickle.dump(lista_medico, open (dados_medico, "ab+"))
        
        #exportando dados
        self.salvar_medico()

    def exibir_medico (self):
        #super().exibir_pessoa()
        with open ("medico.txt", 'r') as arquivo:
            for linhas in arquivo:
                linhas_em_brancos = linhas.strip()
                print(linhas_em_brancos)

    #salvar medico
    def salvar_medico (self):
        with open ("medico.txt", 'a') as dados:
            nova_lista = pickle.load(open(dados_medico,"rb"))
            dados.write(str(nova_lista) + "\n")