import utilitario as ut

def cadastro_funcionario():
    print("================================================")
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

    ut.salvar(matricula, nome, email, telefone, celular, endereco, numero_casa, bairro, cidade, uf, complemento, cargo, salario_bruto, setor)

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

def consulta():
    procura_nome = input("Informe um nome a consultar: ")
    ref_arquivo = open("arquivo.txt", "r")

    if "Nome" == procura_nome:
        print ("1") 

    ref_arquivo.close()   

def menu (cadastro_funcionario, exibir, consulta):
  print ("Sistema Empresarial")
  print ("1  - Cadastrar \n2  - Exibir \n3  - Consulta")

  opc = input ("Escolha uma das opções: ")

  if opc == "1":
      cadastro_funcionario()
  elif opc == "2":
      ut.exibir()
  elif opc == "3":
      consulta()
menu(cadastro_funcionario, ut.exibir,consulta)