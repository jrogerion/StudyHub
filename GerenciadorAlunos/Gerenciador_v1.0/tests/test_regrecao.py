from boletim.alunos import GerenciadorAlunos

def test_regressao_funcionalidades():
    gerenciador = GerenciadorAlunos("alunos.json")
    
    # Verifica se funcionalidades principais continuam iguais
    assert gerenciador.calcular_situacao(7.0) == "Aprovado"  # Não quebrou cálculo
    assert isinstance(gerenciador.carregar_dados(), list)  # Continua retornando lista