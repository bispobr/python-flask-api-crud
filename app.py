from flask import Flask,jsonify,request

app = Flask(__name__)

livros = [
    {
        'id':1,
        'titulo': 'Manual de Persuação do FBI',
        'autor': 'Jack Schafer'
    },
    {
        'id':2,
        'titulo': '48 leis do poder',
        'autor': 'Robert Greene'
    },
    {
        'id':3,
        'titulo': 'O Poder do habito',
        'autor': 'Charles Duhigg'
    },
]

@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify (livros)


@app.route('/livros/<int:id>',methods = ['GET'])
def livros_by_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_by_id(id):
    livro_modificado= request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_modificado)
            return jsonify(livros[indice])

@app.route('/livros',methods=['POST'])
def cadastar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['DELETE'])
def remover_Livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
           del livros[indice]

    return jsonify(livros)


app.run(port = 5000,host='localhost',debug=True)