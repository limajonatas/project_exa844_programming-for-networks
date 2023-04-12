import urllib.request
import string
from bs4 import BeautifulSoup


def getData(url):
    page = urllib.request.urlopen(url)
    html = str(page.read().decode("utf-8"))

    soup = BeautifulSoup(html, "lxml")
    votosEnsinoFundamentalCompleto = 0
    votosEnsinoMedioCompleto = 0
    votosEnsinoSuperiorIncompleto = 0
    votosEnsinoSuperiorCompleto = 0
    totalVotos = 0
    candidatosEnsinoMedioCompleto = 0
    candidatosEnsinoSuperiorIncompleto = 0
    candidatosEnsinoSuperiorCompleto = 0
    candidatosEnsinoFundamentalCompleto = 0
    totalCandidaturas = 0

    tables = soup.findAll("table", {"class": "t-Report-report"})
    for table in tables:
        tbody = table.find("tbody")
        if tbody:
            trs = tbody.findAll("tr")
            for tr in trs:
                tds = tr.findAll("td")
                cont = 0
                for td in tds:
                    header = td.attrs.get("headers")
                    if (
                        header[0] == "QT_VOTOS_NOMINAIS"
                    ):  # se for a coluna de votos nominais  verifica qual é a coluna anterior
                        if tds[cont - 1].text == "Ensino Fundamental completo":
                            votosEnsinoFundamentalCompleto = int(
                                tds[cont].text.translate(
                                    str.maketrans("", "", string.punctuation)
                                )
                            )
                        elif tds[cont - 1].text == "Ensino Médio completo":
                            votosEnsinoMedioCompleto = int(
                                tds[cont].text.translate(
                                    str.maketrans("", "", string.punctuation)
                                )
                            )
                        elif tds[cont - 1].text == "Ensino Superior incompleto":
                            votosEnsinoSuperiorIncompleto = int(
                                tds[cont].text.translate(
                                    str.maketrans("", "", string.punctuation)
                                )
                            )
                        elif tds[cont - 1].text == "Ensino Superior completo":
                            votosEnsinoSuperiorCompleto = int(
                                tds[cont].text.translate(
                                    str.maketrans("", "", string.punctuation)
                                )
                            )
                        elif tds[cont - 1].text == "":  # total
                            totalVotos = int(
                                tds[cont].text.translate(
                                    str.maketrans("", "", string.punctuation)
                                )
                            )

                    if header[0] == "QT_CANDIDATO":
                        if tds[cont - 1].text == "Ensino Fundamental completo":
                            candidatosEnsinoFundamentalCompleto = int(
                                tds[cont].text.translate(
                                    str.maketrans("", "", string.punctuation)
                                )
                            )
                        elif tds[cont - 1].text == "Ensino Médio Completo":
                            candidatosEnsinoMedioCompleto = int(
                                tds[cont].text.translate(
                                    str.maketrans("", "", string.punctuation)
                                )
                            )
                        elif tds[cont - 1].text == "Ensino Superior incompleto":
                            candidatosEnsinoSuperiorIncompleto = int(
                                tds[cont].text.translate(
                                    str.maketrans("", "", string.punctuation)
                                )
                            )
                        elif tds[cont - 1].text == "Ensino Superior completo":
                            candidatosEnsinoSuperiorCompleto = int(
                                tds[cont].text.translate(
                                    str.maketrans("", "", string.punctuation)
                                )
                            )
                        elif tds[cont - 1].text == "":
                            totalCandidaturas = int(
                                tds[cont].text.translate(
                                    str.maketrans("", "", string.punctuation)
                                )
                            )

                    cont = cont + 1

    date = dict()
    date["ano"] = (
        soup.find("div", {"id": "ano"}).find("span", {"class": "t-valor"}).text
    )
    date["qtd_votos"] = []
    date["qtd_candidatos"] = []

    date["qtd_votos"].append(
        {"votosEnsinoFundamentalCompleto": votosEnsinoFundamentalCompleto}
    )
    date["qtd_votos"].append({"votosEnsinoMedioCompleto": votosEnsinoMedioCompleto})
    date["qtd_votos"].append(
        {"votosEnsinoSuperiorIncompleto": votosEnsinoSuperiorIncompleto}
    )
    date["qtd_votos"].append(
        {"votosEnsinoSuperiorCompleto": votosEnsinoSuperiorCompleto}
    )
    date["qtd_votos"].append({"total": totalVotos})

    date["qtd_candidatos"].append(
        {"candidatosEnsinoFundamentalCompleto": candidatosEnsinoFundamentalCompleto}
    )
    date["qtd_candidatos"].append(
        {"candidatosEnsinoMedioCompleto": candidatosEnsinoMedioCompleto}
    )
    date["qtd_candidatos"].append(
        {"candidatosEnsinoSuperiorIncompleto": candidatosEnsinoSuperiorIncompleto}
    )
    date["qtd_candidatos"].append(
        {"candidatosEnsinoSuperiorCompleto": candidatosEnsinoSuperiorCompleto}
    )
    date["qtd_candidatos"].append({"total": totalCandidaturas})
    return date
