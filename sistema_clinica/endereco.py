#Implementação Dia 24/10
import pickle

import endereco as e

dados_endereco = "endereco.pickle"

class endereco:
    def __init__(self):
        self.logradouro = " "
        self.numero = " "
        self.complemento = " "
        self.bairro = " "
        self.cidade = " "
        self.uf = " "

    def cadastrar_endereco (self):
        self.logradouro = input("Entre com o Endereco: ")
        self.numero = input("Entre com o numero do Endereço: ")
        self.complemento = input("Entre com o complemento do Endereço: ")
        self.bairro = input("Entre com o bairro do endereço: ")
        self.cidade = input("Entre com a cidade: ")
        self.uf = input("Informe a Unidade Federativa: ")

        #lista de input de dados 
        lista_endereco = [self.logradouro, self.numero, self.complemento, self.bairro, self.cidade, self.uf]

        #dump de dados no arquivo
        pickle.dump(lista_endereco, open (dados_endereco, "ab+"))

        print("Cadastro Realizado com Sucesso!")

        #exportando os dados
        self.endereco_save()
    
    def exibir_endereco (self):
        print ('logradouro, numero, complemento, bairro, cidade, uf]')
        with open ("endereco.txt", 'r') as arquivo:
            for linhas in arquivo:
                linhas_em_brancos = linhas.strip()
                print(linhas_em_brancos)
                
    #salvar endereco
    def endereco_save(self):
        with open ("endereco.txt", 'a') as dados:
            nova_lista = pickle.load(open(dados_endereco,"rb"))
            dados.write(str(nova_lista) + "\n")