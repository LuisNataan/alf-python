from flask import Flask, request, render_template
import pandas as pd
import MySQLdb
import json
import datetime

app = Flask(__name__)

conn = MySQLdb.connect(db="flask_db", host="localhost", port=3306, user="root")
conn.autocommit(True)
cursor = conn.cursor()

@app.route("/consulta-score/<cpf>", methods=["GET"])
def consultar_score(cpf):
    try:
        sql = f"SELECT * FROM pessoas WHERE cpf = {cpf}"
        cursor.execute(sql)
        df = pd.DataFrame(cursor.fetchall(), columns=[i[0] for i in cursor.description])
        
        if verficar_idade(df['data_nascimento'][0]) >= 18:
            return f"Seu score é de {df['score'][0]}!", 200
            
        else:
           return "Não foi possível consultar seu SCORE, pois sua idade é menor que 18 anos."
    except Exception as error:
        return str(error.args)
    
    return "Não foi possível consultar seu SCORE. Seu CPF não foi encontrado.", 404

@app.route("/consulta-divida/<cpf>", methods=["GET"])
def consultar_divida(cpf):
    try:
        sql = f"SELECT * FROM pessoas WHERE cpf = {cpf}"
        cursor.execute(sql)
        df = pd.DataFrame(cursor.fetchall(), columns=[i[0] for i in cursor.description])
        
        if verficar_idade(df['data_nascimento'][0]) >= 18:
            if df['divida'][0] == 0.00:
                return "Parabéns. Você não possui dívidas."
            return f"Sua dívida é de R${df['divida'][0]}", 200    

        else:
           return "Não foi possível consultar sua dívida, pois sua idade é menor que 18 anos."
    except Exception as error:
        return str(error.args)
    return "Não foi possível consultar sua dívida. Seu CPF não foi encontrado.", 404

@app.route("/pagar-divida/<cpf>", methods=["PUT"])
def efetuar_pagamento_divida(cpf):
    try:
        sql = f"""UPDATE pessoas SET divida = 0, score = 1000 WHERE cpf = {cpf}"""
        affected_rows = cursor.execute(sql)
        
        if affected_rows > 0:
            return "Sua conta foi paga. Seu SCORE aumentou."

    except Exception as error:
        return str(error.args)
    return "Não foi possível executar a ação requirida."
        
def verficar_idade(nascimento):
    nascimento = pd.to_datetime(nascimento)
    data_atual = datetime.date.today()
    return data_atual.year - nascimento.year - ((data_atual.month, data_atual.day) < (nascimento.month, nascimento.day))


if __name__ == "__main__":
    app.run(debug=True)