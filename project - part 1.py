import sys
sys.path.insert(0, 'path/to/your/dataCountry.py')

import dataCountry
import dataByGen

urlPais = "https://sig.tse.jus.br/ords/dwapr/seai/r/sig-eleicao-resultados/maiores-votacoes?p0_turno=1&session=214694431999301"
urlRegiao = "https://sig.tse.jus.br/ords/dwapr/seai/r/sig-eleicao-resultados/maiores-votacoes?p0_abrangencia=Regi%C3%A3o&clear=RP&session=205449690850665"
urlByGenero = 'https://sig.tse.jus.br/ords/dwapr/seai/r/sig-eleicao-resultados/g%C3%AAnero?session=208821330692616'

dataCountry.getData(urlPais)
dataByGen.getData(urlByGenero)
