from flask import request, json

class Escola:

    def cadastrar_aluno(self, aluno):
        raw_request = request.data.decode("utf-8")
        dict_values = json.loads(raw_request)
        try:
            id = alunos.insert_one(dict_values).inserted_id
            return f"Aluno {dict_values['nome']} foi cadastrado.\
                Com o número de matrícula: {id}", 200

        except Exception as error:
            return str(error.args)

        return "Não foi possível cadastrar este aluno.", 400

    def cadastrar_prova(self, prova, numero_questao=0, peso=0.0):
        raw_request = request.data.decode("utf-8")
        dict_values = json.loads(raw_request)
        qtd_questoes = len(dict_values['questoes'])

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
    
    def listar_alunos():
        df = pd.DataFrame(alunos.find())
        df = df.astype(str)
        return df.to_json(orient="records")


    def listar_provas():
        df = pd.DataFrame(provas.find())
        df = df.drop(['questoes'], axis=1)
        df = df.astype(str)
        
        return df.to_json(orient="records")
    