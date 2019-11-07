#Implementação Dia 24/10
#Modificação dia 07/11/2019

import paciente as p
import medico as m
import endereco as end
import funcionario as func
import agenda as a

class menu ():
    def __init__(self):
        self.cod = " "
        self.p = p.paciente()
        self.m = m.medico()
        self.end = end.endereco()

    def main_menu(self):
        print ("Sistema de Clinica Médica")
        print ("1  - Medico \n2  - Paciente \n3  - Funcionario\n4  - Agenda")

        self.cod = input("Informe a opção de entrada no menu: ")

        #Medico
        if self.cod == "1":
            print ("1  - Cadastrar Medico \n2  - Exibir Medico")

            self.sec_cod = input("Informe a opção de entrada no menu: ")

            if self.sec_cod == "1":
                self.m.cadastrar_medico()
            
            if self.sec_cod == "2":
                self.m.exibir_medico()

        #Paciente
        if self.cod == "2":
            print ("1  - Cadastrar Paciente \n2  - Exibir Paciente")

            self.sec_cod = input("Informe a opção de entrada no menu: ")

            if self.sec_cod == "1":
                self.p.cadastrar_paciente()
            
            if self.sec_cod == "2":
                self.p.exibir_paciente()

        #Funcionario 
        if self.cod == "3":
            print ("1  - Cadastrar Funcionario \n2  - Exibir Funcionario")

            self.sec_cod = input("Informe a opção de entrada no menu: ")

            if self.sec_cod == "1":
                self.p.cadastrar_paciente()
            
            if self.sec_cod == "2":
                self.p.exibir_paciente()

        #Agenda
        if self.cod == "4":
            print ("1  - Cadastrar Paciente \n2  - Exibir Paciente")

            self.sec_cod = input("Informe a opção de entrada no menu: ")

            if self.sec_cod == "1":
                self.a.cadastrar_agenda()
            
            if self.sec_cod == "2":
                self.a.exibir_agenda()

main = menu()
main.main_menu()

