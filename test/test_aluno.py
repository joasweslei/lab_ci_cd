from src.aluno import Aluno

def test_aprovacao_sucesso():
    aluno = Aluno("001", "Maria")
    assert aluno.calcula_aprovacao(8.0, 5) == True

def test_reprovacao_nota():
    aluno = Aluno("002", "Pedro")
    assert aluno.calcula_aprovacao(6.0, 5) == False

def test_reprovacao_faltas():
    aluno = Aluno("003", "Joana")
    assert aluno.calcula_aprovacao(9.0, 15) == False