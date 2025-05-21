from boletim.alunos import GerenciadorAlunos

# Adiciona dois alunos e verifica estatísticas
def test_fluxo_completo():
    gerenciador = GerenciadorAlunos("alunos.json")
    
    gerenciador.salvar_dados([
        {"nome": "Aluno1", "nota1": 6, "nota2": 6, "nota3": 6, "nota4": 6, "media": 6.0, "situacao": "Reprovado"},
        {"nome": "Aluno2", "nota1": 8, "nota2": 8, "nota3": 8, "nota4": 8, "media": 8.0, "situacao": "Aprovado"}
    ])
    
    alunos = gerenciador.carregar_dados()
    assert len(alunos) == 2
    assert alunos[0]["situacao"] == "Reprovado"
    assert alunos[1]["situacao"] == "Aprovado"