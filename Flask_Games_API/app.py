import json
import os
from flask import Flask, jsonify, request

app = Flask(__name__)

ARQUIVO_JSON = 'catalogo.json'

def salvar_arquivo(dados):
    """Sobrescreve o arquivo físico com a lista mais atualizada"""
    with open(ARQUIVO_JSON, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

def carregar_arquivo():
    """Lê o arquivo do computador. Se não existir, cria com dados padrão"""
    if os.path.exists(ARQUIVO_JSON): 
        with open(ARQUIVO_JSON, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)

    banco_de_jogos = [
        {"id": 1, "titulo": "Minecraft", "genero": "Aventura", "preco": 99.90, "avaliacao": 4.9},
        {"id": 2, "titulo": "Hollow Knight", "genero": "Aventura", "preco": 39.99, "avaliacao": 4.9},
        {"id": 3, "titulo": "Fortnite", "genero": "Aventura", "preco": 0.00, "avaliacao": 4.7},
        {"id": 4, "titulo": "Ori and the Will of the Wisps", "genero": "Aventura", "preco": 49.99, "avaliacao": 4.9},
        {"id": 5, "titulo": "A Short Hike", "genero": "Aventura", "preco": 15.99, "avaliacao": 4.9},
        {"id": 6, "titulo": "Firewatch", "genero": "Aventura", "preco": 24.99, "avaliacao": 4.7},
        {"id": 7, "titulo": "Disco Elysium", "genero": "Aventura", "preco": 59.99, "avaliacao": 4.8},
        {"id": 8, "titulo": "What Remains of Edith Finch", "genero": "Aventura", "preco": 24.99, "avaliacao": 4.9},
        {"id": 9, "titulo": "Subnautica",  "genero": "Aventura", "preco": 49.99, "avaliacao": 4.8},
        {"id": 10, "titulo": "The Stanley Parable Ultra Deluxe", "genero": "Aventura", "preco": 39.99, "avaliacao": 4.9},
        {"id": 11, "titulo": "Clair Obscur: Expedition 33", "genero": "Aventura", "preco": 199.99, "avaliacao": 4.9},
        {"id": 12, "titulo": "Hollow Knight: Silksong",  "genero": "Aventura", "preco": 67.99, "avaliacao": 4.8},
        {"id": 13, "titulo": "It Takes Two", "genero": "Aventura", "preco": 99.90, "avaliacao": 4.9},
        {"id": 14, "titulo": "Red Dead Redemption 2", "genero": "Aventura", "preco": 187.95, "avaliacao": 4.9},
        {"id": 15, "titulo": "God of War", "genero": "Aventura", "preco": 119.99, "avaliacao": 4.9}
    ]
    
    salvar_arquivo(banco_de_jogos)
    return banco_de_jogos

banco_de_jogos = carregar_arquivo()

@app.route('/api/jogos', methods=['GET', 'POST'])
def gerenciar_jogos():
    
    if request.method == 'POST':
        dados_recebidos = request.get_json()

        if len(banco_de_jogos) > 0:
            novo_id = banco_de_jogos[-1]["id"] + 1
        else: 
            novo_id = 1

        novo_jogo = {
            "id": novo_id,
            "titulo": dados_recebidos.get("titulo"),
            "genero": dados_recebidos.get("genero"),
            "preco": dados_recebidos.get("preco"),
            "avaliacao": dados_recebidos.get("avaliacao")
        }

        banco_de_jogos.append(novo_jogo)
        salvar_arquivo(banco_de_jogos)
        return jsonify(novo_jogo), 201

    else: 
        return jsonify(banco_de_jogos)

@app.route('/api/jogos/<int:id_do_jogo>', methods=['GET', 'DELETE', 'PUT'])
def gerenciar_jogo_especifico(id_do_jogo):
    for jogo in banco_de_jogos: 
        if jogo["id"] == id_do_jogo:

            if request.method == 'PUT':
                dados_recebidos = request.get_json()

                jogo['titulo'] = dados_recebidos.get('titulo', jogo['titulo'])
                jogo['genero'] = dados_recebidos.get('genero', jogo['genero'])
                jogo['preco'] = dados_recebidos.get('preco', jogo['preco'])
                jogo['avaliacao'] = dados_recebidos.get('avaliacao', jogo['avaliacao'])

                salvar_arquivo(banco_de_jogos)
                return jsonify({
                    "mensagem": "Jogo atualizado com sucesso!",
                    "jogo": jogo
                }), 200
            
            elif request.method == 'DELETE':
                banco_de_jogos.remove(jogo)
                salvar_arquivo(banco_de_jogos)
                return jsonify({"mensagem": f"O jogo '{jogo['titulo']}' foi removido com sucesso!"}), 200
            
            else: 
                return jsonify({jogo})

    return jsonify({"erro": "Jogo não encontrado no sistema"}), 404

if __name__ == '__main__':
    app.run(debug=True)