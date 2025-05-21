import os
from boletim.alunos import GerenciadorAlunos


# Verifica se atende aos requisitos básicos
def test_requisitos():
    gerenciador = GerenciadorAlunos("aceitacao.json")
    
    assert gerenciador.calcular_situacao(7.0) == "Aprovado"  # Requisito: média >= 7 aprova
    assert gerenciador.carregar_dados() == []  # Requisito: lista vazia inicial

    # remover arquivo temp criado
    os.remove("aceitacao.json")