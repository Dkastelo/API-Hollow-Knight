from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # criando uma aplicação para hospedar a api

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////personagens.db'
db = SQLAlchemy(app) 

espiritos = [
    {
        "id": 1,
        "nome": "Coveiro",
        "genero": "Masculino",
        "vivo": False,
        "locais": "Dirtmouth"
    },
    {
        "id": 2,
        "nome": "Joni",
        "genero": "Feminino",
        "vivo": False,
        "locais": "Penhascos Uivantes"
    },
    {
        "id": 3,
        "nome": "A Descentente do Traidor",
        "genero": "Feminino",
        "vivo": False,
        "locais": "Jardins da Rainha"
    },
    {
        "id": 4,
        "nome": "Revek",
        "genero": "Feminino",
        "vivo": False,
        "locais": "Clareira dos Espíritos"
    },
    {
        "id": 5,
        "nome": "Millybug",
        "genero": "Desconhecido",
        "vivo": False,
        "locais": "Clareira dos Espíritos"
    },
    {
        "id": 6,
        "nome": "Caspian",
        "genero": "Masculino",
        "vivo": False,
        "locais": "Clareira das Espíritos"
    },
    {
        "id": 7,
        "nome": "Dr Chagax",
        "genero": "Masculino",
        "vivo": False,
        "locais": "Clareira das Espíritos"
    },
    {
        "id": 8,
        "nome": "Atra",
        "genero": "Masculino",
        "vivo": False,
        "locais": "Clareira das Espíritos"
    },
    {
        "id": 9,
        "nome": "Garro",
        "genero": "Masculino",
        "vivo": False,
        "locais": "Clareira das Espíritos"
    },
    {
        "id": 10,
        "nome": "Kcin",
        "genero": "Masculino",
        "vivo": False,
        "locais": "Clareira das Espíritos"
    },
    {
        "id": 11,
        "nome": "Grohac",
        "genero": "Masculino",
        "vivo": False,
        "locais": "Clareira das Espíritos"
    },
    {
        "id": 12,
        "nome": "Hex",
        "genero": "Masculino",
        "vivo": False,
        "locais": "Clareira das Espíritos"
    },
    {
        "id": 13,
        "nome": "Guerreiro de Mil Ferões",
        "genero": "Masculino",
        "vivo": False,
        "locais": "Clareira das Espíritos"
    },
    {
        "id": 14,
        "nome": "Karina",
        "genero": "Feminino",
        "vivo": False,
        "locais": "Clareira das Espíritos"
    },
    {
        "id": 15,
        "nome": "Perpetos Noo",
        "genero": "Desconhecido",
        "vivo": False,
        "locais": "Clareira das Espíritos"
    },
    {
        "id": 16,
        "nome": "Molten",
        "genero": "Masculino",
        "vivo": False,
        "locais": "Clareira das Espíritos"
    },
    {
        "id": 17,
        "nome": "Magnos Strong",
        "genero": "Masculino",
        "vivo": False,
        "locais": "Clareira das Espíritos"
    },
    {
        "id": 18,
        "nome": "Waldie",
        "genero": "Masculino",
        "vivo": False,
        "locais": "Clareira das Espíritos"
    },
    {
        "id": 19,
        "nome": "Wayner",
        "genero": "Masculino",
        "vivo": False,
        "locais": "Clareira das Espíritos"
    },
    {
        "id": 20,
        "nome": "Wyatt",
        "genero": "Masculino",
        "vivo": False,
        "locais": "Clareira das Espíritos"
    },
    {
        "id": 21,
        "nome": "Thistlewind",
        "genero": "Desconhecido",
        "vivo": False,
        "locais": "Clareira das Espíritos"
    },
    {
        "id": 22,
        "nome": "Boss",
        "genero": "Masculino",
        "vivo": False,
        "locais": "Clareira das Espíritos"
    },
    {
        "id": 23,
        "nome": "Poggy Thorax",
        "genero": "Masculino",
        "vivo": False,
        "locais": "Clareira das Espíritos"
    },
    {
        "id": 24,
        "nome": "Marissa",
        "genero": "Feminino",
        "vivo": False,
        "locais": "Casa dos Prazeres"
    },
    {
        "id": 25,
        "nome": "Rainha da Colmeia Vespa",
        "genero": "Feminino",
        "vivo": False,
        "locais": "Colmeia"
    },
    {
        "id": 26,
        "nome": "Caelif & Fera Orthop",
        "genero": "Masculino",
        "vivo": False,
        "locais": "Jardins da Rainha"
    },
    {
        "id": 27,
        "nome": "Espírito de Cloth",
        "genero": "Feminino",
        "vivo": False,
        "locais": "Jardins da Rainha"
    }
]

# consultar todos os espiritos
@app.route('/espiritos', methods=['GET'])
def obter_espirito():
    return jsonify(espiritos)


# consultar por ID
@app.route('/espiritos/<int:id>', methods=['GET'])
def obter_espirito_por_ID(id):
    for espirito in espiritos:
        if espirito.get('id') == id:
            return jsonify(espirito)
        else:
            return jsonify({"erro": "Espírito não encontrado"}), 404


# editar um espirito por id
@app.route('/espiritos/<int:id>', methods=['PUT'])
def editar_espirito_por_id(id):
    espirito_alterado = request.get_json()
    for indice, espirito in enumerate(espiritos):
        if espiritos.get('id') == id:
            espiritos[indice].update(espirito_alterado)
            return jsonify(espiritos[indice])
        else:
            return jsonify({"erro": "Espírito não encontrado"}), 404


# adicionar um espirito
@app.route('/espiritos', methods=['POST'])
def adicionar_um_espirito():
    novo_espirito = request.get_json()
    espiritos.append(novo_espirito)

    return jsonify(espiritos)


# excluir espiritos
@app.route('/espiritos/<int:id>', methods=['DELETE'])
def excluir_espirito(id):
    for indice, espirito in enumerate(espiritos):
        if espiritos.get('id') == id:
            del espiritos[indice]
        else:
            return jsonify({"erro": "Espírito não encontrado"}), 404

    return jsonify(espiritos)


comerciantes = [
    {
        "id": 1,
        "nome": "Salubra",
        "genero": "Feminino",
        "vivo": True,
        "locais": "Encruzilhada Esquecida"
    },
    {
        "id": 2,
        "nome": "Confessora Jiji",
        "genero": "Feminino",
        "vivo": True,
        "locais": "Dirtmouth"
    },
    {
        "id": 3,
        "nome": "Divine",
        "genero": "Feminino",
        "vivo": True,
        "locais": "Dirtmouth"
    },
    {
        "id": 4,
        "nome": "Iselda",
        "genero": "Feminino",
        "vivo": True,
        "locais": "Dirtmouth"
    },
    {
        "id": 5,
        "nome": "Come Pernas",
        "genero": "Masculino",
        "vivo": True,
        "locais": "Ermos Fúngicos"
    },
    {
        "id": 6,
        "nome": "Pequeno Tolo",
        "genero": "Masculino",
        "vivo": True,
        "locais": "Coliseu"
    },
    {
        "id": 7,
        "nome": "Millibelle",
        "genero": "Feminino",
        "vivo": True,
        "locais": "Cânion da Névoa, Casa do Prazer"
    },
    {
        "id": 8,
        "nome": "Forjador de Ferrões",
        "genero": "Masculino",
        "vivo": True,
        "locais": "Cidade das Lágrimas, Caminho Verde"
    },
    {
        "id": 9,
        "nome": "Colecionador de Relíquias Lemm",
        "genero": "Masculino",
        "vivo": True,
        "locais": "Cidade das Lágrimas"
    },
    {
        "id": 10,
        "nome": "Sly",
        "genero": "Masculino",
        "vivo": True,
        "locais": "Encruzilhada Esquecida, Dirtmouth"
    },
    {
        "id": 11,
        "nome": "Jinn Alma de Aço",
        "genero": "Feminino",
        "vivo": True,
        "locais": "Dirtmouth"
    },
    {
        "id": 12,
        "nome": "Tuk",
        "genero": "Feminino",
        "vivo": True,
        "locais": "Hidrovia Real"
    }
]

# consultar todos os comerciantes
@app.route('/comerciantes', methods=['GET'])
def obter_comerciantes():
    return jsonify(comerciantes)


# consultar por ID
@app.route('/comerciantes/<int:id>', methods=['GET'])
def obter_comerciante_por_ID(id):
    for comerciante in comerciantes:
        if comerciante.get('id') == id:
            return jsonify(comerciante)
        else:
            return jsonify({"erro": "Comerciante não encontrado"}), 404


# editar um comerciante por id
@app.route('/comerciantes/<int:id>', methods=['PUT'])
def editar_comerciante_por_id(id):
    comerciante_alterado = request.get_json()
    for indice, comerciante in enumerate(comerciantes):
        if comerciantes.get('id') == id:
            comerciantes[indice].update(comerciante_alterado)
            return jsonify(comerciante[indice])
        else: 
            return jsonify({"erro": "Comerciante não encontrado"}), 404


# adicionar um comerciante
@app.route('/comerciantes', methods=['POST'])
def adicionar_um_comerciante():
    novo_comerciante = request.get_json()
    comerciantes.append(novo_comerciante)

    return jsonify(comerciantes)


# excluir comerciante
@app.route('/comerciantes/<int:id>', methods=['DELETE'])
def excluir_comerciante(id):
    for indice, comerciante in enumerate(comerciantes):
        if comerciante.get('id') == id:
            del comerciantes[indice]
        else:
            return jsonify({"erro": "Comerciante não encontrado"}), 404

    return jsonify(comerciantes)


variados = [
    {
        "id": 1,
        "nome": "Bardoon",
        "genero": "Masculino",
        "vivo": True,
        "locais": "Nordas do Reino"
    },
    {
        "id": 2,
        "nome": "Criador de Máscaras",
        "genero": "Desconhecido",
        "vivo": True,
        "locais": "Ninho Profundo"
    },
    {
        "id": 3,
        "nome": "Parteira",
        "genero": "Feminino",
        "vivo": True,
        "locais": "Aldeia Distante"
    },
    {
        "id": 4,
        "nome": "Profeta do Musgo",
        "genero": "Desconhecido",
        "vivo": True,
        "locais": "Ermos Fúngicos"
    },
    {
        "id": 5,
        "nome": "Myla",
        "genero": "Feminino",
        "vivo": False,
        "locais": "Encruzilhada Esquecida"
    },
    {
        "id": 6,
        "nome": "Nymm",
        "genero": "Masculino",
        "vivo": True,
        "locais": "Dirtmouth"
    },
    {
        "id": 7,
        "nome": "Inseto Ancião",
        "genero": "Masculino",
        "vivo": True,
        "locais": "Dirtmouth"
    },
    {
        "id": 8,
        "nome": "Emilitia",
        "genero": "Feminino",
        "vivo": True,
        "locais": "Cidade das Lágrimas"
    },
    {
        "id": 9,
        "nome": "Flurke Eremita",
        "genero": "Feminino",
        "vivo": True,
        "locais": "Cova de Lixo"
    },
    {
        "id": 10,
        "nome": "Corcel Grimm",
        "genero": "Desconhecido",
        "vivo": True,
        "locais": "Dirtmouth"
    },
    {
        "id": 11,
        "nome": "O Último Besouro",
        "genero": "Masculino",
        "vivo": True,
        "locais": "Estações de Besouro"
    },
    {
        "id": 12,
        "nome": "Mariposa Sem Nome",
        "genero": "Desconhecido",
        "vivo": True,
        "locais": "Clareira dos Espíritos"
    },
    {
        "id": 13,
        "nome": "Dama Branca",
        "genero": "Feminino",
        "vivo": True,
        "locais": "Jardins da Rainha"
    },
    {
        "id": 14,
        "nome": "Willoh",
        "genero": "Feminino",
        "vivo": True,
        "locais": "Estação da Rainha"
    }
]

# consultar todos os variados
@app.route('/variados', methods=['GET'])
def obter_variados():
    return jsonify(variados)


# consultar por ID
@app.route('/variados/<int:id>', methods=['GET'])
def obter_variado_por_ID(id):
    for variado in variados:
        if variado.get('id') == id:
            return jsonify(variado)
        else: 
            return jsonify({"erro": "Personagem não encontrado"}), 404


# editar um variado por nome
@app.route('/variados/<int:id>', methods=['PUT'])
def editar_variado_por_id(id):
    variado_alterado = request.get_json()
    for indice, variado in enumerate(variados):
        if variado.get('id') == id:
            variados[indice].update(variado_alterado)
            return jsonify(variados[indice])
        else:
            return jsonify({"erro": "Personagem não encontrado"}), 404


# adicionar um variado
@app.route('/variados', methods=['POST'])
def adicionar_um_variado():
    novo_variado = request.get_json()
    variados.append(novo_variado)

    return jsonify(variados)


# excluir variado
@app.route('/variados/<int:id>', methods=['DELETE'])
def excluir_variado(id):
    for indice, variado in enumerate(variados):
        if variado.get('id') == id:
            del variados[indice]
        else:
            return jsonify({"erro": "Personagem não encontrado"}), 404

    return jsonify(variados)


andarilhos = [
    {
      "id": 1,
      "nome": "Cloth",
      "genero": "Feminino",
      "vivo": False,
      "locais": [
        "Ermos Fúngicos",
        "Ninho Profundo",
        "Bacia Antiga",
        "Jardins da Rainha",
        "Dirtmouth"
      ]
    },
    {
      "id": 2,
      "nome": "Cornifer",
      "genero": "Masculino",
      "vivo": True,
      "locais": [
        "Encruzilhada Esquecida",
        "Caminho Verde",
        "Ermos Fúngicos",
        "Cânion da Névoa",
        "Ninho Profundo",
        "Pico de Cristal",
        "Bacia Antiga",
        "Cidade das Lágrimas",
        "Penhascos Uivantes",
        "Bordas do Reino",
        "Jardins da Rainha",
        "Hidrovia Real"
      ]
    },
    {
      "id": 3,
      "nome": "Hornet",
      "genero": "Feminino",
      "vivo": True,
      "locais": [
        "Caminho Verde",
        "Cidade das Lágrimas",
        "Bordas do Reino",
        "O Abismo",
        "Encruzilhada Esquecida",
        "Ninho Profundo"
      ]
    },
    {
      "id": 4,
      "nome": "Quirrel",
      "genero": "Masculino",
      "vivo": False,
      "locais": [
        "Encruzilhada Esquecida",
        "Caminho Verde",
        "Ermos Fúngicos",
        "Cidade das Lágrimas",
        "Pico de Cristal",
        "Ninho Profundo",
        "Lago Azul"
      ]
    },
    {
      "id": 5,
      "nome": "Tiso",
      "genero": "Masculino",
      "vivo": True,
      "locais": [
        "Dirtmouth",
        "Encruzilhada Esquecida",
        "Terra do Descanso",
        "Bordas do Reino"
      ]
    },
    {
      "id": 6,
      "nome": "Zote o Poderoso",
      "genero": "Masculino",
      "vivo": True,
      "locais": [
        "Caminho Verde",
        "Dirtmouth",
        "Cidade das Lágrimas",
        "Ninho Profundo",
        "Bordas do Reino"
      ]
    },
    {
      "id": 7,
      "nome": "Senhor Cogumelo",
      "genero": "Masculino",
      "vivo": True,
      "locais": [
        "Ermos Fúngicos",
        "Bordas do Reino",
        "Ninho Profundo",
        "Penhascos Uivantes",
        "Bacia Antiga"
      ]
    }
]

# consultar todos os andarilhos
@app.route('/andarilhos', methods=['GET'])
def obter_andarilhos():
    return jsonify(andarilhos)


# consultar por ID
@app.route('/andarilhos/<int:id>', methods=['GET'])
def obter_andarilho_por_ID(id):
    for andarilho in andarilhos:
        if andarilho.get('id') == id:
            return jsonify(andarilho)
        else: 
            return jsonify({"erro": "Personagem não encontrado"}), 404


# editar um andarilho por id
@app.route('/andarilhos/<int:id>', methods=['PUT'])
def editar_andarilho_por_id(id):
    andarilho_alterado = request.get_json()
    for indice, andarilho in enumerate(andarilhos):
        if andarilho.get('id') == id:
            andarilhos[indice].update(andarilho_alterado)
            return jsonify(andarilhos[indice])
        else:
            return jsonify({"erro": "Personagem não encontrado"}), 404


# adicionar um andarilho
@app.route('/andarilhos', methods=['POST'])
def adicionar_um_andarilho():
    novo_andarilho = request.get_json()
    variados.append(novo_andarilho)

    return jsonify(andarilhos)


# excluir andarilho
@app.route('/andarilhos/<int:id>', methods=['DELETE'])
def excluir_andarilho(id):
    for indice, andarilho in enumerate(andarilhos):
        if andarilho.get('id') == id:
            del andarilhos[indice]
        else:
            return jsonify({"erro": "Personagem não encontrado"}), 404

    return jsonify(andarilhos)


missoes = [
    {
      "id": 1,
      "nome": "Bretta",
      "genero": "Feminino",
      "vivo": True,
      "locais": ["Ermos Fúngicos", "Dirtmouth"],
      "recompensas": ["Fragmento de Máscara"]
    },
    {
      "id": 2,
      "nome": "Brumm",
      "genero": "Masculino",
      "vivo": True,
      "locais": ["Dirtmouth", "Aldeia Distante"],
      "recompensas": ["Chama Grimm"]
    },
    {
      "id": 3,
      "nome": "A Pranteadora Cinzenta",
      "genero": "Feminino",
      "vivo": True,
      "locais": ["Terra do Descanso"],
      "recompensas": ["Fragmento de Máscara"]
    },
    {
      "id": 4,
      "nome": "Pailarva",
      "genero": "Masculino",
      "vivo": True,
      "locais": ["Encruzilhada Esquecida"],
      "recompensas": [
        "Geo",
        "Fragmento de Máscara",
        "Canção das Larvas",
        "Ovo Rançoso",
        "Minério Pálido",
        "Ídolo do Rei",
        "Selo de Hollownest",
        "Energia da Larva Mosca"
      ]
    },
    {
      "id": 5,
      "nome": "Vidente",
      "genero": "Feminino",
      "vivo": False,
      "locais": ["Terra do Descanso"],
      "recompensas": [
        "Selo de Hollownest",
        "Clareira dos Espíritos",
        "Minério Pálido",
        "Portador de Sonhos",
        "Fragmento de Receptáculo",
        "Portal dos Sonhos",
        "Ovo Arcano",
        "Fragmento de Máscara",
        "Ferrão dos Sonhos (Despertado)"
      ]
    },
    {
      "id": 6,
      "nome": "O Caçador",
      "genero": "Masculino",
      "vivo": True,
      "locais": ["Caminho Verde"],
      "recompensas": ["A Marca do Caçador"]
    },
    {
      "id": 7,
      "nome": "Mestre da Trupe Grimm",
      "genero": "Masculino",
      "vivo": True,
      "locais": ["Dirtmouth"],
      "recompensas": ["Encaixe de Amuleto", "Criança Grimm"]
    },
    {
      "id": 8,
      "nome": "Buscadora de Deuses",
      "genero": "Feminino",
      "vivo": True,
      "locais": ["Cova de Lixo", "Lar dos Deuses"],
      "recompensas": ["Lar dos Deuses"]
    }
]


# consultar todos
@app.route('/missoes', methods=['GET'])
def obter_missoes():
    return jsonify(missoes)


# consultar por ID
@app.route('/missoes/<int:id>', methods=['GET'])
def obter_missao_por_ID(id):
    for missao in missoes:
        if missao.get('id') == id:
            return jsonify(missao)
        else: 
            return jsonify({"erro": "Personagem não encontrado"}), 404


# editar um por id
@app.route('/missoes/<int:id>', methods=['PUT'])
def editar_missao_por_id(id):
    missao_alterado = request.get_json()
    for indice, missao in enumerate(missoes):
        if missao.get('id') == id:
            missoes[indice].update(missao_alterado)
            return jsonify(missoes[indice])
        else:
            return jsonify({"erro": "Personagem não encontrado"}), 404


# adicionar um personagem
@app.route('/missoes', methods=['POST'])
def adicionar_um_personagem():
    novo_personagem = request.get_json()
    missoes.append(novo_personagem)

    return jsonify(missoes)


# excluir personagem
@app.route('/missoes/<int:id>', methods=['DELETE'])
def excluir_personagem(id):
    for indice, personagem in enumerate(missoes):
        if personagem.get('id') == id:
            del missoes[indice]
        else:
            return jsonify({"erro": "Personagem não encontrado"}), 404

    return jsonify(missoes)


guerreiros_dos_sonhos = [
    {
      "id": 1,
      "nome": "Elder Hu",
      "genero": "Masculino",
      "vivo": False,
      "locais": "Ermos Fúngicos"
    },
    {
      "id": 2,
      "nome": "Galien",
      "genero": "Masculino",
      "vivo": False,
      "locais": "Ninho Profundo"
    },
    {
      "id": 3,
      "nome": "Gorb",
      "genero": "Feminino",
      "vivo": False,
      "locais": "Penhascos Uivantes"
    },
    {
      "id": 4,
      "nome": "Markoth",
      "genero": "Masculino",
      "vivo": False,
      "locais": "Bordas do Reino"
    },
    {
      "id": 5,
      "nome": "Marmu",
      "genero": "Masculino",
      "vivo": False,
      "locais": "Jardins da Rainha"
    },
    {
      "id": 6,
      "nome": "Sem Olhos",
      "genero": "Feminino",
      "vivo": False,
      "locais": "Caminho Verde"
    },
    {
      "id": 7,
      "nome": "Xero",
      "genero": "Masculino",
      "vivo": False,
      "locais": "Terra do Descanso"
    }
]

# consultar todos
@app.route('/guerreiros_dos_sonhos', methods=['GET'])
def obter_guerreiros_dos_sonhos():
    return jsonify(guerreiros_dos_sonhos)


# consultar por ID
@app.route('/guerreiros_dos_sonhos/<int:id>', methods=['GET'])
def obter_guerreiro_por_ID(id):
    for guerreiro in guerreiros_dos_sonhos:
        if guerreiro.get('id') == id:
            return jsonify(guerreiros_dos_sonhos)
        else: 
            return jsonify({"erro": "Personagem não encontrado"}), 404


# editar um por id
@app.route('/guerreiros_dos_sonhos/<int:id>', methods=['PUT'])
def editar_guerreiro_por_id(id):
    guerreiro_alterado = request.get_json()
    for indice, guerreiro in enumerate(guerreiros_dos_sonhos):
        if guerreiro.get('id') == id:
            guerreiros_dos_sonhos[indice].update(guerreiro_alterado)
            return jsonify(guerreiros_dos_sonhos[indice])
        else:
            return jsonify({"erro": "Personagem não encontrado"}), 404


# adicionar um guerreiro
@app.route('/guerreiros_dos_sonhos', methods=['POST'])
def adicionar_um_guerreiro():
    novo_guerreiro = request.get_json()
    guerreiros_dos_sonhos.append(novo_guerreiro)

    return jsonify(guerreiros_dos_sonhos)


# excluir guerreiro
@app.route('/guerreiros_dos_sonhos/<int:id>', methods=['DELETE'])
def excluir_guerreiro(id):
    for indice, guerreiro in enumerate(guerreiros_dos_sonhos):
        if guerreiro.get('id') == id:
            del guerreiros_dos_sonhos[indice]
        else:
            return jsonify({"erro": "Personagem não encontrado"}), 404

    return jsonify(guerreiros_dos_sonhos)


app.run(port=5000, host='localhost', debug=True)
