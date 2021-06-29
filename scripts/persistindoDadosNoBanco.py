from pymongo import MongoClient

db = MongoClient('localhost',27017)

#salvando dados do pilo no banco de dados
def salvaDadosNaBase(info_piloto):
    banco = db.projeto_formula1
    dados = banco.pilotos.insert_one(info_piloto)
    print('Dados do Piloto Savol com sucesso')
    print(dados.inserted_id)
