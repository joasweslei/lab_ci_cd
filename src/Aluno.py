class Aluno:
    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome

    def calcula_aprovacao(self, nota, faltas):
        # Regra: nota mínima 7.0 e máximo 10 faltas
        return nota >= 7.0 and faltas <= 10