import pytest
from boletim.alunos import GerenciadorAlunos
import os


def test_calcular_situacao():
    gerenciador = GerenciadorAlunos("test.json")
    assert gerenciador.calcular_situacao(7.0) == "Aprovado"
    assert gerenciador.calcular_situacao(6.0) == "Reprovado"

 # Verificar carregamento de dados quando o arquivo não existe
def test_carregar_dados_arquivo_inexistente():
    gerenciador = GerenciadorAlunos("arquivo_inexistente.json")
    assert gerenciador.carregar_dados() == []
