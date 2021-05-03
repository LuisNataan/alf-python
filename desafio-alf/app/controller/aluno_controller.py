from flask import Flask, request, render_template
import pymongo as pm
from bson.objectid import ObjectId
import pandas as pd
import json
from aluno.aluno_alf import Aluno

app = Flask(__name__) 

connection = pm.MongoClient("mongodb://localhost:27017/")
database = connection["escola_db"]

provas = database["Prova"]

@app.route("/realizar-prova/_id", methods=["POST"])
def realizar_prova(id):
    pass

@app.route("listar-prova/id", methods=["GET"])
def listar_prova(id):
    pass


if __name__ == "__main__":
    app.run(debug=True)