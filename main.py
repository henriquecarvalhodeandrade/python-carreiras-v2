from flask import Flask, jsonify, render_template

app = Flask(__name__)

CAREERS = [
    {"title": "Desenvolvedor Python", "description": "Desenvolva aplicações web e sistemas com Python"},
    {"title": "Cientista de Dados", "description": "Analise dados e crie modelos de machine learning"},
    {"title": "Engenheiro de Backend", "description": "Construa APIs e sistemas escaláveis"},
    {"title": "DevOps Engineer", "description": "Automatize infraestrutura e deployments"},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/carreiras')
def carreiras():
    return render_template('carreiras.html', careers = CAREERS)

@app.route('/lista_carreiras')
def lista_carreiras():
    return jsonify(CAREERS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

