from flask import Flask, jsonify, request
app = Flask(__name__)
musicas = [
    {
        'Artista': 'Filipe Ret',
        'Genero': 'Rap',
        'Musica': 'Deus Perdoa'
    },
    {
        'Artista': 'Mateca',
        'Genero': 'Rap',
        'Musica': 'Vivao'
    },
    {
        'Artista': 'Mc Cabelinho',
        'Genero': 'Rap',
        'Musica': 'X1'
    },
    {
        'Artista': 'Matue',
        'Genero': 'Rap',
        'Musica': 'Conexoes de mafia'
    },
    {
        'Artista': 'Teto',
        'Genero': 'Rap',
        'Musica': 'Minha vida e um filme'
    },
]

#URL Base - GET - http://localhost:7777/musicas

@app.route('/musicas', methods=['GET'])
def obter_musicas():
    return jsonify(musicas)

#GET COM ID - http://localhost:7777/musicas/1

@app.route('/musicas/<int:musica_id>', methods=['GET'])
def obter_musica_por_indice(musica_id):
    return jsonify(musicas[musica_id])

#POST http://localhost:7777/musicas

@app.route('/musicas', methods=['POST'])
def nova_musica():
    musica = request.get_json()
    musicas.append(musica)

    return jsonify(f' A musica: {musica} foi adicionada com sucesso!', 200)

#PUT Alterar cançao - http://localhost:7777/musicas/1

@app.route('/musicas/<int:musica_id>', methods=['PUT'])
def atualizar_musica(musica_id):
    musica_alterada = request.get_json()
    musicas[musica_id].update(musica_alterada)
    return jsonify(musicas[musica_id], 200)

#DELETE http://localhost:7777/musicas/1

@app.route('/musicas/<int:indice>', methods=['DELETE'])
def excluir_musica(indice):
    try:
        if musicas[indice] is not None:
            del musicas[indice]
            return jsonify(f'Foi excluído a postagem {musicas[indice]}', 200)
    except:
        return jsonify('Não foi possível encontrar a postagem para exclusão',404)



app.run(port=7777,host='localhost', debug=True)
