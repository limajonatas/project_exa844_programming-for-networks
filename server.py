import json
from flask import Flask

app = Flask(__name__)

# Lê o arquivo JSON
with open("dataAll.json", "r") as f:
    data = json.load(f)


# Define uma rota que retorna o conteúdo do arquivo JSON
@app.route("/")
def get_data():
    if data:
        return data
    else:
        return "Não encontrado"


# Define uma rota que retorna o conteúdo do arquivo JSON por Cor/Raça
@app.route("/race")
def get_race():
    by_race = data["by_race"]
    if by_race:
        return by_race
    else:
        return "Não encontrado"


# Define uma rota que retorna o conteúdo do arquivo JSON por gênero
@app.route("/gender")
def get_gender():
    by_gender = data["by_gender"]
    if by_gender:
        return by_gender
    else:
        return "Não encontrado"


# Define uma rota que retorna o conteúdo do arquivo JSON por grau de instrução
@app.route("/educationLevel")
def get_education_level():
    by_education_level = data["by_education_level"]
    if by_education_level:
        return by_education_level
    else:
        return "Não encontrado"


# Define uma rota que retorna o conteúdo do arquivo JSON por gênero e ano
@app.route("/gender/<year>")
def get_gender_by_year(year):
    value = [aux for aux in data["by_gender"] if aux["ano"] == year]
    if value:
        return value[0]
    else:
        return "Não encontrado"


# Define uma rota que retorna o conteúdo do arquivo JSON por cor/raça e ano
@app.route("/race/<year>")
def get_race_by_year(year):
    value = [aux for aux in data["by_race"] if aux["ano"] == year]
    if value:
        return value[0]
    else:
        return "Não encontrado"


# Define uma rota que retorna o conteúdo do arquivo JSON por grau de instrução e ano
@app.route("/educationLevel/<year>")
def get_education_level_by_year(year):
    value = [aux for aux in data["by_education_level"] if aux["ano"] == year]
    if value:
        return value[0]
    else:
        return "Não encontrado"


if __name__ == "__main__":
    app.run()
