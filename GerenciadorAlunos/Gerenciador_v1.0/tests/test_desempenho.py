from boletim.alunos import GerenciadorAlunos
import time

def test_calculos():
    gerenciador = GerenciadorAlunos("alunos.json")
    
    inicio = time.time()
    for _ in range(1000):
        gerenciador.calcular_situacao(7.0)
    
    duracao = time.time() - inicio
    assert duracao < 0.1  # 1000 cálculos devem ser rápidos