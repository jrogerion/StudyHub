# Importando modulos

import pytest
from boletim_json import GerenciadorAlunos
import os
import json

# Teste 1: Verificar carregamento de dados quando o arquivo não existe
def test_carregar_dados_arquivo_inexistente():
    gerenciador = GerenciadorAlunos("arquivo_inexistente.json")
    assert gerenciador.carregar_dados() == []

# Teste 2: Verificar carregamento de dados quando o arquivo existe
def test_carregar_dados_arquivo_existente():
    arquivo_json = "alunos.json"  # Arquivo já existente
    
    # Verifica se o arquivo existe. Se não existir vai encerrar o teste.
    if not os.path.exists(arquivo_json):
        pytest.fail(f"O arquivo {arquivo_json} não existe. Crie o arquivo com dados de teste antes de rodar este teste.")
    
    # Carrega os dados esperados do arquivo
    with open(arquivo_json, "r", encoding="utf-8") as arquivo:
        dados_esperados = json.load(arquivo)
    

    gerenciador = GerenciadorAlunos(arquivo_json)
    dados_carregados = gerenciador.carregar_dados()
    
    # Verifica se os dados carregados são iguais aos dados esperados
    assert dados_carregados == dados_esperados

#Teste 3: Verificar o cálculo da média
def test_calculo_media():
    notas = [7.5, 8.0, 6.5, 9.0]
    media = sum(notas) / len(notas)
    assert round(media, 2) == 7.75
