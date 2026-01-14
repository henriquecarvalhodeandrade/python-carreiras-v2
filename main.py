from flask import Flask, jsonify, render_template
from database import carrega_vagas_db

app = Flask(__name__)
vagas = carrega_vagas_db()

@app.route('/')
def hello():
    return render_template('home.html', vagas=vagas)

@app.route('/vagas')
def lista_vagas():
    return jsonify(vagas)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

