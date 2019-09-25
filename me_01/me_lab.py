import pickle

dados_funcionario = "funcionario.pickle"
dados_setor = "setor.pickle"
dados_salario = "salario.pickle"

def cadastro_funcionario():
  matricula = int(input('Matricula do funcionário: '))
  nome = str(input('Nome do funcionário: '))
  email = str(input('Email do funcionário: '))
  telefone = int(input('Telefone do funcionário: '))
  celular = int(input('Celular do funcionário: '))
  endereco = str(input('Endereço: '))
  numero_casa = int(input('Número da casa:'))
  bairro  = str(input('Bairro: '))
  cidade = str(input('Cidade: '))
  uf = str(input('Unidade Federativa:'))
  complemento = str(input('Complemento: '))
  cargo = str(input('Cargo: '))
  salario_bruto = float(input('Salário do funcionário: '))
  setor = str(input('Setor do funcionário: '))

  lista_funcionario = [matricula, nome, email, telefone, celular, endereco, numero_casa, bairro, cidade, uf, complemento, cargo, salario_bruto, setor]
  
  pickle.dump(lista_funcionario, open (dados_funcionario, "wb"))
  print ("Cadastro efetuado com sucesso!")

  #Exportando para o arquivo ao realizar o cadastro
  funcionario_info()

def calcular_inss(salario_bruto):
  inss = 0
  if salario_bruto <= 1693.72:
    inss = salario_bruto * 0.08
  elif salario_bruto > 1693.72 and salario_bruto <= 2822.90:
    inss = salario_bruto * 0.09
  elif salario_bruto > 2822.90 and salario_bruto <= 5645.80:
    inss = salario_bruto * 0.11
  elif salario_bruto > 5645.80:
    inss = 621.04
  return inss
  
def calcular_irrf(salario_bruto):
  irrf = 0
  if salario_bruto < 1903.98:
    irrf = 0
  elif salario_bruto > 1903.98 and salario_bruto < 2826.66:
    irrf = salario_bruto * 0.075
  elif salario_bruto >= 2826.66 and salario_bruto < 3751.06:
    irrf = salario_bruto * 0.15
  elif salario_bruto >= 3751.06 and salario_bruto < 4664.69:
   irrf = salario_bruto * 0.225
  elif salario_bruto >= 4664.69:
    irrf = salario_bruto * 0.275
  return irrf

#Realizar o dump no arquivo dos funcionários
def funcionario_info():
  with open ("funcionarios.txt", 'a') as dados:
    nova_lista = pickle.load(open(dados_funcionario,"rb"))
    dados.write(str(nova_lista) + "\n")

#Listar os Funcionários
def listar_funcionarios():
  print ("[matricula, nome, email, telefone, celular, endereco, numero_casa, bairro, cidade, uf, complemento, cargo, salario_bruto, setor]")
  with open ("funcionarios.txt", 'r') as arquivo:
    for linha in arquivo:
      linhas_em_brancos = linha.strip()
      print(linhas_em_brancos)
'''
#Consultar utilizando nome
def consulta():
  procura_nome = input("Informe um nome a consultar: ")
  ref_arquivo = open("funcionarios.txt", "r")
  for linha in ref_arquivo:
    valores = linha.split()

    if valores[1] == "Natan":
      print (1)
    
  ref_arquivo.close()
'''
def consulta():
    pos_i = 0 # variável provisória de índice
    pos_j = 0 # idem

    procura_nome = input("Informe um nome a consultar: ")

    lista = open("funcionarios.txt", "r")
    lista = lista.read()
    for i in range (len(lista)): # procurar em todas as listas internas
        for j in range (i): # procurar em todos os elementos nessa lista
            if procura_nome in lista[i][j]: # se encontrarmos elemento 
              pos_i = i # guardamos o índice i
              pos_j = j # e o índice j
              break
            break
    return(pos_i, pos_j)


def menu (cadastro_funcionario, exibir, lista_funcionario):
  print ("Sistema de Clinica Médica")
  print ("1  - Cadastrar \n2  - Consulta \n3 - Listar Funcionários")

  opc = input ("Escolha uma das opções: ")

  if opc == "1":
      cadastro_funcionario()
  elif opc == "2":
      consulta()
  elif opc == "3":
      listar_funcionarios()
      
menu(cadastro_funcionario, consulta, listar_funcionarios)



