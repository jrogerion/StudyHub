import json
import os

class GerenciadorAlunos:
    def __init__(self, arquivo_json):
        self.arquivo_json = arquivo_json
        self.atualizar_dados()


    def atualizar_dados(self):
        alunos = self.carregar_dados()
        for aluno in alunos:
            if 'situacao' not in aluno:
                aluno['situacao'] = self.calcular_situacao(aluno['media'])
        self.salvar_dados(alunos)
    
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
            "media": round(media, 2),
            "situacao": self.calcular_situacao(media)
        }

        alunos = self.carregar_dados()
        alunos.append(aluno)
        self.salvar_dados(alunos)

        print(f"Aluno {nome} adicionado com sucesso!\n")


    # Lista todos os alunos cadastrados
    def listar_alunos(self):
        # Lista todos os alunos cadastrados no arquivo JSON.
        alunos = self.carregar_dados()
        if not alunos:
            print("Nenhum aluno cadastrado.")
            return

        print("\nLista de alunos:")
        for aluno in alunos:
            print(f"Nome: {aluno['nome']} | Notas: {aluno['nota1']}, {aluno['nota2']}, {aluno['nota3']}, {aluno['nota4']} | Média: {aluno['media']} | Situação: {aluno['situacao']}")
        print()

    
    # calcula a média do alunos
    def calcular_situacao(self, media):
        return "Aprovado" if media >= 7.0 else "Reprovado"
    

    # Mostra estatisticas

    def mostrar_estatisticas(self):
        alunos = self.carregar_dados()
        if not alunos:
            print("Nenhum aluno cadastrado.")
            return

        medias = [aluno["media"] for aluno in alunos]
        media_geral = sum(medias) / len(medias)
        maior_media = max(medias)
        menor_media = min(medias)
        aprovados = sum(1 for aluno in alunos if aluno["situacao"] == "Aprovado")
        reprovados = len(alunos) - aprovados

        print("\n=== Estatísticas ===")
        print(f"Total de alunos: {len(alunos)}")
        print(f"Média geral: {round(media_geral, 2)}")
        print(f"Maior média: {maior_media}")
        print(f"Menor média: {menor_media}")
        print(f"Aprovados: {aprovados}")
        print(f"Reprovados: {reprovados}")


    # Busca de alunos pelo nome
    def buscar_aluno(self):
        alunos = self.carregar_dados()
        if not alunos:
            print("Nenhum aluno cadastrado.")

        nome = input("Digite o nome do aluno que deseja buscar: ")
        encontrado = False

        for aluno in alunos:
            if nome.lower() in aluno["nome"].lower():
                encontrado = True
                print(f"Nome: {aluno['nome']} | Notas: {aluno['nota1']}, {aluno['nota2']}, {aluno['nota3']}, {aluno['nota4']} | Média: {aluno['media']} | Situação: {aluno['situacao']}")

        if not encontrado:
            print("Aluno não encontrado.")

    def menu(self):
        # Exibe o menu do programa.
        while True:
            print("\n=== Menu ===")
            print("1 - Adicionar Aluno")
            print("2 - Listar Alunos")
            print("3 - Buscar aluno: ")
            print("4 - Mostrar estatisticas")
            print("5 - Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                self.adicionar_aluno()
            elif opcao == "2":
                self.listar_alunos()
            elif opcao == "3":
                self.buscar_aluno()
            elif opcao == "4":
                self.mostrar_estatisticas()
            elif opcao == "5":
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida! Tente novamente.")


gerenciador = GerenciadorAlunos("alunos.json")
gerenciador.menu()

