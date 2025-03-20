import json
import os

class GerenciadorAlunos:
    def __init__(self, arquivo_json):
        self.arquivo_json = arquivo_json
    
    def carregar_dados(self):
        # Carrega os dados do arquivo JSON.
        if os.path.exists(self.arquivo_json):
            with open(self.arquivo_json, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        return []  # Retorna uma lista vazia se o arquivo não existir

    def salvar_dados(self, alunos):
        # Salva os dados no arquivo JSON.
        with open(self.arquivo_json, "w", encoding="utf-8") as arquivo:
            json.dump(alunos, arquivo, indent=4, ensure_ascii=False)

    def adicionar_aluno(self):
        # Adiciona um novo aluno ao arquivo JSON.
        nome = input("Nome do aluno: ")
        notas = []

        for i in range(1, 5):
            while True:
                try:
                    nota = float(input(f"Digite a nota {i}: "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("A nota deve estar entre 0 e 10.")
                except ValueError:
                    print("Entrada inválida! Digite um número válido.")

        media = sum(notas) / len(notas)  # Calcula a média

        aluno = {
            "nome": nome,
            "nota1": notas[0],
            "nota2": notas[1],
            "nota3": notas[2],
            "nota4": notas[3],
            "media": round(media, 2)
        }

        alunos = self.carregar_dados()
        alunos.append(aluno)
        self.salvar_dados(alunos)

        print(f"Aluno {nome} adicionado com sucesso!\n")

    def listar_alunos(self):
        # Lista todos os alunos cadastrados no arquivo JSON.
        alunos = self.carregar_dados()
        if not alunos:
            print("Nenhum aluno cadastrado.")
            return

        print("\nLista de alunos:")
        for aluno in alunos:
            print(f"Nome: {aluno['nome']} | Notas: {aluno['nota1']}, {aluno['nota2']}, {aluno['nota3']}, {aluno['nota4']} | Média: {aluno['media']}")
        print()

    def menu(self):
        # Exibe o menu do programa.
        while True:
            print("\n=== Menu ===")
            print("1. Adicionar Aluno")
            print("2. Listar Alunos")
            print("3. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                self.adicionar_aluno()
            elif opcao == "2":
                self.listar_alunos()
            elif opcao == "3":
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida! Tente novamente.")

# Função principal
if __name__ == "__main__":
    gerenciador = GerenciadorAlunos("alunos.json")
    gerenciador.menu()

# -- Possíveis novas funcionalidades --

# Adicionar relatórios estatisticos
# Buscar aluno por nome
# Editar alunos já cadastrados
# Excluir um 

# -- Testes com Pytest --

# Testar carregamento de dados
# Verificar se o método adicionar_aluno adiiona corretamente um aluno a lista
# e se os dados são salvos no arquivo JSON

# Listar a listagem de alunos
# Verificar se o metodo listar_alunos exibe corretaemnte os alunos cadastrados

# Testar o cálculo da media
# Verificar se a média das notas é calculada corretamente

# Testar a validadçao das notas
# Verificar se o metodo adicionar_aluno valida corretamente as notas (entre 0 e 10)