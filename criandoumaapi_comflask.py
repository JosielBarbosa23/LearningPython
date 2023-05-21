from flask import Flask, jsonify, request
app = Flask(__name__)
postagens = [
    {
        'titulo': 'Minha historia',
        'autor': 'Lucas Diniz'
    },
    {
        'titulo': 'A importancia da fisioterapia',
        'autor': 'Antonio Ronaldo'
    },
    {
        'titulo': 'Direito securitario',
        'autor': 'Victor Alencar'
    },    
]
#Rota padrão - GET http://localhost:5000/

@app.route('/')
def obter_postagens():
    return jsonify(postagens)

#Rota GET com ID http://localhost:5000/postagem/1

@app.route('/postagem/<int:indice>', methods=['GET'])
def obter_postagem_por_indice(indice):
    return jsonify(postagens[indice])

#Criar postagem com POST - http://localhost:5000/postagem

@app.route('/postagem', methods=['POST'])
def nova_postagem():
    postagem = request.get_json()
    postagens.append(postagem)

    return jsonify(postagem, 200)

#EXCLUIR RECURSO - http://localhost:5000/postagem/1

@app.route('/postagem/<int:indice>', methods=['DELETE'])
def excluir_postagem(indice):
    try:
        if postagens[indice] is not None:
            del postagens[indice]
            return jsonify(f'Foi excluído a postagem {postagens[indice]}', 200)
    except:
        return jsonify('Não foi possível encontrar a postagem para exclusão',404)

app.run(port=5000,host='localhost',debug=True)
