from flask import Flask, request, render_template
import pymongo as pm
from bson.objectid import ObjectId
import pandas as pd
import json
from escola.escola_alf import Escola


app = Flask(__name__)
    
connection = pm.MongoClient("mongodb://localhost:27017/")
database = connection["escola_db"]
    
alunos = database["Aluno"]
provas = database["Prova"]
    
 
@app.route("/cadastrar-aluno/", methods=["POST"])
def cadastrar_aluno():
    return Escola().cadastrar_aluno(aluno)
    
@app.route("/cadastrar-prova/", methods=["POST"])
def cadastrar_prova():
    return Escola().cadastrar_prova(prova)
        
    try:
        if len(dict_values['questoes']) >= 1 or len(dict_values['questoes']) <= 20:
            peso = 0
            for numero_questao in dict_values['questoes']:
                if dict_values["questoes"][numero_questao]['peso'] > 0:
                        peso += dict_values["questoes"][numero_questao]['peso']
                else:
                    return "As questões não podem ter peso menor que 0.001.", 400
            if peso != 10.0:
                return f"O peso final da prova deve ser 10.0! Peso atual: {peso}", 400
            else:
                provas.insert_one(dict_values)
                return "Prova cadastrada com sucesso.", 200
        else:
            return f"Prova deve conter de 1 à 20 questões. {qtd_questoes}", 400
    except Exception as error:
        return str(error.args)
    return "Não foi possível cadastrar esta prova.", 400
    
@app.route("/listar-alunos/", methods=["GET"])
def listar_alunos():
    df = pd.DataFrame(alunos.find())
    df = df.astype(str)
    return df.to_json(orient="records")
    
    
@app.route("/listar-provas/", methods=["GET"])
def listar_provas():
    df = pd.DataFrame(provas.find())
    df = df.drop(['questoes'], axis=1)
    df = df.astype(str)
        
    return df.to_json(orient="records")
    
@app.route("/listar-prova/questoes/", methods=["POST"])
def listar_questoes_prova():
    raw_request = request.data.decode("utf-8")
    dict_values = json.loads(raw_request)
    list_values = list(prova.find({'_id': ObjectId(dict_values['_id'])}))
    dictio = list_values[0]
    for values in dictio['questoes']:
        dictio.pop(values['correta'])
        
    return ""
        
if __name__ == "__main__":
    app.run(debug=True)