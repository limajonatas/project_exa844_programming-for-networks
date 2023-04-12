import urllib.request
import string
from bs4 import BeautifulSoup


def getData(url):
    page = urllib.request.urlopen(url)
    html = str(page.read().decode("utf-8"))

    soup = BeautifulSoup(html, "lxml")
    votacaoPreta = 0
    votacaoBranca = 0
    votacaoParda = 0
    totalVotacao = 0
    candidatosPretos = 0
    candidatosBrancos = 0
    candidatosPardos = 0
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
                        if tds[cont - 1].text == "Branca":
                            votacaoBranca = int(
                                tds[cont].text.translate(
                                    str.maketrans("", "", string.punctuation)
                                )
                            )
                        if tds[cont - 1].text == "Preta":
                            votacaoPreta = int(
                                tds[cont].text.translate(
                                    str.maketrans("", "", string.punctuation)
                                )
                            )
                        if tds[cont - 1].text == "Parda":
                            votacaoParda = int(
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
                        if tds[cont - 1].text == "Preta":
                            candidatosPretos = int(
                                tds[cont].text.translate(
                                    str.maketrans("", "", string.punctuation)
                                )
                            )
                        if tds[cont - 1].text == "Branca":
                            candidatosBrancos = int(
                                tds[cont].text.translate(
                                    str.maketrans("", "", string.punctuation)
                                )
                            )
                        if tds[cont - 1].text == "Parda":
                            candidatosPardos = int(
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

    date["qtd_votos"].append({"votosBrancos": votacaoBranca})
    date["qtd_votos"].append({"votosPretos": votacaoPreta})
    date["qtd_votos"].append({"votosPardos": votacaoParda})
    date["qtd_votos"].append({"total": totalVotacao})

    date["qtd_candidatos"].append({"candidatosPretos": candidatosPretos})
    date["qtd_candidatos"].append({"candidatosBrancos": candidatosBrancos})
    date["qtd_candidatos"].append({"candidatosPardos": candidatosPardos})
    date["qtd_candidatos"].append({"total": totalCandidaturas})
    return date;
