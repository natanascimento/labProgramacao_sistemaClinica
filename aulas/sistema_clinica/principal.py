#Implementação Dia 24/10

import paciente as p
import medico as m

class menu ():
    def __init__(self):
        self.cod = " "
        self.p = p.paciente()
        self.m = m.medico()

    def main_menu(self):
        print ("Sistema de Clinica Médica")
        print ("1  - Cadastrar Paciente \n2  - Consulta Paciente")

        self.cod = input("Informe a opção de entrada no menu: ")

        if self.cod == "1":
            self.p.cadastrar_paciente()
            self.m.cadastrar_medico()

        if self.cod == "2":
            self.p.exibir_paciente()
    
main = menu()
main.main_menu()

