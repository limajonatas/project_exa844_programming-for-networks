import json
from flask import Flask

app = Flask(__name__)

# Lê o arquivo JSON
with open('dataAll.json', 'r') as f:
    data = json.load(f)

# Define uma rota que retorna o conteúdo do arquivo JSON
@app.route('/')
def get_data():
    return data

# Define uma rota que retorna o conteúdo do arquivo JSON por Raça
@app.route('/race')
def get_race():
    return data['by_race']

# Define uma rota que retorna o conteúdo do arquivo JSON por gênero
@app.route('/gender')
def get_gender():
    return data['by_gender']

# Define uma rota que retorna o conteúdo do arquivo JSON por gênero
@app.route('/gender/<year>')
def get_gender_by_year(year):
    value = [aux for aux in data['by_gender'] if aux['ano'] == year]
    if(value):
        return value[0]
    else:
        return 'Não encontrado'

# Define uma rota que retorna o conteúdo do arquivo JSON por gênero
@app.route('/race/<year>')
def get_race_by_year(year):
    value = [aux for aux in data['by_race'] if aux['ano'] == year]
    if(value):
        return value[0]
    else:
        return 'Não encontrado'

if __name__ == '__main__':
    app.run()