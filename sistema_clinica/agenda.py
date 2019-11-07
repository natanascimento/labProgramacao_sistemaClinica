import medico as m
import paciente as p

class agenda:
    def __init__(self, medico, paciente, dia, mes, ano, hora, observacao=""):
        self.medico = medico
        self.paciente = paciente
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.hora = hora
        self.obs = observacao
        
    def exibir_agenda(self):
        print(self.medico.nome)
        print(self.paciente.nome)
        print(self.dia)
        print(self.mes)
        print(self.ano)
        print(self.obs)