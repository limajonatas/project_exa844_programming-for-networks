import json
import dataCountry
import dataByGender
import dataByRace

def readData(path):
    with open(path, "r") as file:
        lines = file.readlines()
        file.close()
    return lines

print("Starting the program...")
urlPais = "https://sig.tse.jus.br/ords/dwapr/seai/r/sig-eleicao-resultados/maiores-votacoes?p0_turno=1&session=214694431999301"
# urlRegion = "https://sig.tse.jus.br/ords/dwapr/seai/r/sig-eleicao-resultados/maiores-votacoes?p0_abrangencia=Regi%C3%A3o&clear=RP&session=205449690850665"

print("Getting data from the country...")
votes = dict()
votes["ano"] = "2022"
votes["candidatos"] = dataCountry.getData(urlPais)

dateAll = dict()
dateAll["votes"] = votes
dateAll["by_gender"] = []
dateAll["by_race"] = []
print("Getting data from the country by gender...", end="")

lines = readData("seedsDataByGender.txt")
for line in lines:
    date = dataByGender.getData(line)
    dateAll["by_gender"].append(date)
    print(".", end="")

print("Getting data from the country by gender...", end="")

lines = readData("seedsDataByRace.txt")
for line in lines:
    date = dataByRace.getData(line)
    dateAll["by_race"].append(date)
    print(".", end="")

print(".")
file = open("dataAll.json", "w")
string = json.dumps(dateAll, indent=4, ensure_ascii=False).encode("utf-8")
file.write(string.decode())
file.close()
print("Done!")
print("file dataAll.json created!")
