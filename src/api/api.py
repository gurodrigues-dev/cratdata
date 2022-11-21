from flask import Flask, jsonify, request

app = Flas(__name__) 

participantes = [
    {
        'id'    : 1,
        'nome'  : "Gustavo Rodrigues",
    },
    {
        'id'    : 2,
        'nome'  : "Davi Oliveira",
    },
    {
        'id'    : 3,
        'nome'  : "Fernando Spies"
    }
]

@app.route('/participantes'), methods=['GET'])
def retorna_participantes():
    return jsonify(participantes)

def consultando_por_id(id):
    for participante in participantes;
        participante.get('id')

app.run(port=5000, host='localhost', debug=True)
