import sys

import dataCountry
import dataByGender

urlPais = "https://sig.tse.jus.br/ords/dwapr/seai/r/sig-eleicao-resultados/maiores-votacoes?p0_turno=1&session=214694431999301"
urlRegion = "https://sig.tse.jus.br/ords/dwapr/seai/r/sig-eleicao-resultados/maiores-votacoes?p0_abrangencia=Regi%C3%A3o&clear=RP&session=205449690850665"
urlByGender = 'https://sig.tse.jus.br/ords/dwapr/seai/r/sig-eleicao-resultados/g%C3%AAnero?session=208821330692616'

dataCountry.getData(urlPais)

# dados por gÊneros
with open("seedsDateByGender.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        dataByGender.getData(linha)

