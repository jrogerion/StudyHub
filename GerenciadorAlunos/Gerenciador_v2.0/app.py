from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)

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
        if os.path.exists(self.arquivo_json):
            with open(self.arquivo_json, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        return []
    
    def salvar_dados(self, alunos):
        with open(self.arquivo_json, "w", encoding="utf-8") as arquivo:
            json.dump(alunos, arquivo, indent=4, ensure_ascii=False)
    
    def adicionar_aluno(self, nome, notas):
        media = sum(notas) / len(notas)
        
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
        return aluno
    
    def listar_alunos(self):
        return self.carregar_dados()
    
    def calcular_situacao(self, media):
        return "Aprovado" if media >= 7.0 else "Reprovado"
    
    def mostrar_estatisticas(self):
        alunos = self.carregar_dados()
        if not alunos:
            return None
        
        medias = [aluno["media"] for aluno in alunos]
        media_geral = sum(medias) / len(medias)
        maior_media = max(medias)
        menor_media = min(medias)
        aprovados = sum(1 for aluno in alunos if aluno["situacao"] == "Aprovado")
        reprovados = len(alunos) - aprovados
        
        return {
            "total_alunos": len(alunos),
            "media_geral": round(media_geral, 2),
            "maior_media": maior_media,
            "menor_media": menor_media,
            "aprovados": aprovados,
            "reprovados": reprovados
        }
    
    def buscar_aluno(self, nome):
        alunos = self.carregar_dados()
        resultados = []
        
        for aluno in alunos:
            if nome.lower() in aluno["nome"].lower():
                resultados.append(aluno)
        
        return resultados

# Inicializa o gerenciador
gerenciador = GerenciadorAlunos("alunos.json")

# Rotas da aplicação
@app.route('/')
def index():
    alunos = gerenciador.listar_alunos()
    estatisticas = gerenciador.mostrar_estatisticas()
    return render_template('index.html', alunos=alunos, estatisticas=estatisticas)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        nome = request.form['nome']
        notas = [
            float(request.form['nota1']),
            float(request.form['nota2']),
            float(request.form['nota3']),
            float(request.form['nota4'])
        ]
        gerenciador.adicionar_aluno(nome, notas)
        return redirect(url_for('index'))
    return render_template('adicionar.html')

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'POST':
        nome = request.form['nome']
        resultados = gerenciador.buscar_aluno(nome)
        return render_template('buscar.html', resultados=resultados, busca=nome)
    return render_template('buscar.html')

if __name__ == '__main__':
    app.run(debug=True)