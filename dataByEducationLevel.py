import urllib.request
import string
import json
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
    date["dados"] = []
    date["dados"].append(
        {"votosEnsinoFundamentalCompleto": votosEnsinoFundamentalCompleto}
    )
    date["dados"].append({"votosEnsinoMedioCompleto": votosEnsinoMedioCompleto})
    date["dados"].append(
        {"votosEnsinoSuperiorIncompleto": votosEnsinoSuperiorIncompleto}
    )
    date["dados"].append({"votosEnsinoSuperiorCompleto": votosEnsinoSuperiorCompleto})
    date["dados"].append({"totalVotos": totalVotos})
    date["dados"].append(
        {"candidatosEnsinoFundamentalCompleto": candidatosEnsinoFundamentalCompleto}
    )
    date["dados"].append(
        {"candidatosEnsinoMedioCompleto": candidatosEnsinoMedioCompleto}
    )
    date["dados"].append(
        {"candidatosEnsinoSuperiorIncompleto": candidatosEnsinoSuperiorIncompleto}
    )
    date["dados"].append(
        {"candidatosEnsinoSuperiorCompleto": candidatosEnsinoSuperiorCompleto}
    )
    date["dados"].append({"totalCandidaturas": totalCandidaturas})
    return date
