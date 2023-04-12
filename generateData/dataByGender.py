import urllib.request
import string
from bs4 import BeautifulSoup


def getData(url):
    page = urllib.request.urlopen(url)
    html = str(page.read().decode("utf-8"))

    soup = BeautifulSoup(html, "lxml")
    votacaoFeminino = 0
    votacaoMasculino = 0
    totalVotacao = 0
    candidatosFeminino = 0
    candidatosMasculino = 0
    totalCandidaturas = 0
    
    
    tables = soup.findAll("table", {"class": "t-Report-report"})
    for table in tables:
        tbody = table.find("tbody")
        if tbody:
            # print(tbody.prettify())
            trs = tbody.findAll("tr")
            for tr in trs:
                tds = tr.findAll("td")
                cont = 0
                for td in tds:
                    header = td.attrs.get("headers")
                    if (
                        header[0] == "QT_VOTOS_NOMINAIS"
                    ):  # se for a coluna de votos nominais  verifica se a coluna anterior é feminino ou masculino
                        if tds[cont - 1].text == "Feminino":
                            votacaoFeminino = int(
                                tds[cont].text.translate(
                                    str.maketrans("", "", string.punctuation)
                                )
                            )
                        if tds[cont - 1].text == "Masculino":
                            votacaoMasculino = int(
                                tds[cont].text.translate(
                                    str.maketrans("", "", string.punctuation)
                                )
                            )
                        if tds[cont - 1].text == "":
                            totalVotacao = int(
                                tds[cont].text.translate(
                                    str.maketrans("", "", string.punctuation)
                                )
                            )

                    if header[0] == "QT_CANDIDATO":
                        if tds[cont - 1].text == "Feminino":
                            candidatosFeminino = int(
                                tds[cont].text.translate(
                                    str.maketrans("", "", string.punctuation)
                                )
                            )
                        if tds[cont - 1].text == "Masculino":
                            candidatosMasculino = int(
                                tds[cont].text.translate(
                                    str.maketrans("", "", string.punctuation)
                                )
                            )
                        if tds[cont - 1].text == "":
                            totalCandidaturas = int(
                                tds[cont].text.translate(
                                    str.maketrans("", "", string.punctuation)
                                )
                            )

                    cont = cont + 1

    date = dict();
    date["ano"] = soup.find("div", {"id": "ano"}).find("span", {"class": "t-valor"}).text
    date["qtd_votos"] = []
    date["qtd_candidatos"] = []

    date["qtd_votos"].append({"votosFemininos": votacaoFeminino})
    date["qtd_votos"].append({"votosMasculinos": votacaoMasculino})
    date["qtd_votos"].append({"total": totalVotacao})

    date["qtd_candidatos"].append({"candidatosFemininos": candidatosFeminino})
    date["qtd_candidatos"].append({"candidatosMasculinos": candidatosMasculino})
    date["qtd_candidatos"].append({"total": totalCandidaturas})
    return date;
