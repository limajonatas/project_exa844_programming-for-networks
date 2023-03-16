import json
import dataCountry
import dataByGender

print("Starting the program...")
urlPais = "https://sig.tse.jus.br/ords/dwapr/seai/r/sig-eleicao-resultados/maiores-votacoes?p0_turno=1&session=214694431999301"
urlRegion = "https://sig.tse.jus.br/ords/dwapr/seai/r/sig-eleicao-resultados/maiores-votacoes?p0_abrangencia=Regi%C3%A3o&clear=RP&session=205449690850665"

print("Getting data from the country...")
votes = dict()
votes["ano"] = "2022"
votes["candidatos"] = dataCountry.getData(urlPais)

dateAll = dict()
dateAll["votes"] = votes
dateAll["ByGender"] = []
print("Getting data from the country by gender...", end="")
with open("seedsDateByGender.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        date = dataByGender.getData(linha)
        dateAll["ByGender"].append(date)
        print(".", end="")

print(".")
file = open("dataAll.txt", "w")
string = json.dumps(dateAll, indent=4, ensure_ascii=False).encode("utf-8")
file.write(string.decode())
file.close()
print("Done!")
print("file dateAll.txt created!")
