import os
from boletim.alunos import GerenciadorAlunos


# Simula adicão e listagem dos alunos
from boletim.alunos import GerenciadorAlunos

def test_integracao_adicionar_e_listar():
    gerenciador = GerenciadorAlunos("alunos.json")
    aluno_teste = {
        "nome": "Teste",
        "nota1": 8, "nota2": 7, "nota3": 9, "nota4": 8,
        "media": 8.0, "situacao": "Aprovado"
    }
    
    gerenciador.salvar_dados([aluno_teste])
    alunos = gerenciador.carregar_dados()
    
    assert alunos[0]["nome"] == "Teste"
    assert alunos[0]["situacao"] == "Aprovado"
    
   
   
    # Remover arquivo temp criado
    os.remove("alunos.json")