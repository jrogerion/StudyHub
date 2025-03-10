import json
import os

# Nome do arquivo JSON
json_file = "students.json"

def load_data():
    # Carrega os dados do arquivo JSON.
    if os.path.exists(json_file):
        with open(json_file, "r", encoding="utf-8") as file:
            return json.load(file)
    return []  # Retorna uma lista vazia se o arquivo não existir

def save_data(students):
    # Salva os dados no arquivo JSON.
    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4, ensure_ascii=False)

def add_student():
    # Adiciona um novo aluno ao arquivo JSON.
    name = input("Nome do aluno: ")
    grades = []

    for i in range(1, 5):
        while True:
            try:
                grade = float(input(f"Digite a nota {i}: "))
                if 0 <= grade <= 10:
                    grades.append(grade)
                    break
                else:
                    print("A nota deve estar entre 0 e 10.")
            except ValueError:
                print("Entrada inválida! Digite um número válido.")

    average = sum(grades) / len(grades)  # Calcula a média

    student = {
        "name": name,
        "grade1": grades[0],
        "grade2": grades[1],
        "grade3": grades[2],
        "grade4": grades[3],
        "average": round(average, 2)
    }

    students = load_data()
    students.append(student)
    save_data(students)

    print(f"Aluno {name} adicionado com sucesso!\n")

def list_students():
    # Lista todos os alunos cadastrados no arquivo JSON.
    students = load_data()
    if not students:
        print("Nenhum aluno cadastrado.")
        return

    print("\nLista de alunos:")
    for student in students:
        print(f"Nome: {student['name']} | Notas: {student['grade1']}, {student['grade2']}, {student['grade3']}, {student['grade4']} | Média: {student['average']}")
    print()

def menu():
    # Exibe o menu do programa.
    while True:
        print("\n=== Menu ===")
        print("1. Adicionar Aluno")
        print("2. Listar Alunos")
        print("3. Sair")
        
        option = input("Escolha uma opção: ")
        
        if option == "1":
            add_student()
        elif option == "2":
            list_students()
        elif option == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# chama a função principal
if __name__ == "__main__":
    menu()
