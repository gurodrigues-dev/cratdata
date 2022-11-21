from flask import Flask, jsonify, request

app = Flask(__name__) 

participantes = [
    {
        'id'      : 1,
        'nome'    : "Gustavo Rodrigues",
        'votacao' : 1001
    },

    {
        'id'      : 2,
        'nome'    : "Davi Oliveira",
        'votacao' : 1001
    },

    {
        'id'      : 3,
        'nome'    : "Otaviano Almeida",
        'votacao' : 1002
    },

    {
        'id'      : 4,
        'nome'    : "Paulo Vinicius",
        'votacao' : 1002
    },

    {
        'id'      : 5,
        'nome'    : "Jose Gabriel",
        'votacao' : 1003
    },

    {
        'id'      : 6,
        'nome'    : "Alessandra Pereira",
        'votacao' : 1003
    }
]

@app.route('/', methods=['GET'])
def main_page():
    return "Esta é a home, por favor tente acessar /participantes ou /votacoes"

@app.route('/participantes', methods=['GET'])
def retorna_participantes():
    return jsonify(participantes)

@app.route('/participantes/<int:id>', methods=['GET'])
def consultando_por_id(id):
    for participante in participantes:
        if participante.get('id') == id:
            return jsonify(participante)

@app.route('/votacao/<int:votacao>', methods=['GET'])
def retorna_votacoes(votacao):

    list = []

    for participante in participantes:
        if votacao.get('votacao') == votacao:
            print(participante)

        return jsonify(list)

app.run(port=5000, host='localhost', debug=True)

