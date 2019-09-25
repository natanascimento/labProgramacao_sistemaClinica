

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
  salario = float(input('Salário do funcionário: '))
  setor = str(input('Setor do funcionário: '))

  lista_funcionario = [matricula, nome, email, telefone, celular, endereco, numero_casa, bairro, cidade, uf, complemento, cargo, salario, setor]

  print ("Cadastro efetuado com sucesso!")

  salvar()
'''
def calcular_inss(salario):
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
  

def calcular_irrf(salario):
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
'''

def salvar():
    with open("info.txt", "a") as arquivo: 
        arquivo.write("Matricula: " + matricula)
        arquivo.write("\nNome: " + nome)
        arquivo.write("\nEmail: " + email)
        arquivo.write("\nTelefone: " + telefone)
        arquivo.write("\nCelular: " + celular)
        arquivo.write("\nEndereco: " + endereco)
        arquivo.write("\nNumero da Residencia: " + numero_casa)
        arquivo.write("\Bairro: " + bairro)
        arquivo.write("\nCidade: " + cidade)
        arquivo.write("\nUF: " + uf)
        arquivo.write("\nComplemento: " + complemento)
        arquivo.write("\nCargo: " + cargo)
        arquivo.write("\nSalario: " + salario)
        arquivo.write("\nSetor: " + setor)

    arquivo.close()

def exibir():
    arquivo = open("info.txt", "r")
    texto = arquivo.read()
    print(texto)
    arquivo.close()
  
def menu (cadastro_funcionario,salvar, exibir):
  print ("Sistema de Clinica Médica")
  print ("1  - Cadastrar \n2  - Consultar  \n3  - Exibir")

  opc = input ("Escolha uma das opções: ")

  if opc == "1":
      cadastro_funcionario()
  elif opc == "2":
      salvar()
  elif opc == "3":
      exibir()
      
menu(cadastro_funcionario,salvar, exibir)