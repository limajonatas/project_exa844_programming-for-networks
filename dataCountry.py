import urllib.request
import string
import json
from bs4 import BeautifulSoup
def getData(url):
    page = urllib.request.urlopen(url)
    html = str(page.read().decode("utf-8"))

    soup = BeautifulSoup(html, "lxml")
    candidatos = []
    candidatosJson = dict()
    total = 0

    table = soup.find("table", {"class": "t-Report-report"})
    if table:
        tbody = table.find("tbody")
        if tbody:
            trs = tbody.findAll("tr")
            for tr in trs:
                tds = tr.findAll("td")
                candidato = dict()
                for td in tds:
                    header = td.attrs.get("headers")
                    if header[0] == "NM_CANDIDATO":
                        candidato["nome"] = td.text
                    if header[0] == "SG_PARTIDO":
                        candidato["partido"] = td.text
                    if header[0] == "QT_VOTOS_NOMINAIS":
                        candidato["votos"] = td.text.translate(
                            str.maketrans("", "", string.punctuation)
                        )

                if candidato.get("nome") != "":
                    candidatos.append(candidato)
                else:
                    total = candidato.get("votos")

    totalVotos = 0
    for candidato in candidatos:
        totalVotos = totalVotos + int(candidato.get("votos"))

    candidatosJson["candidatos"] = candidatos
    jsonStr = json.dumps(candidatosJson, indent=4, ensure_ascii=False)
    print(jsonStr)
    print("somados: ", totalVotos)
    print("total: ", total)


# print(soup.prettify())
