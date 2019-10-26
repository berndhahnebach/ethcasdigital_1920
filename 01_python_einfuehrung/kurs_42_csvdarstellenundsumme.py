# *******************************************************************
# daten von webserver herunterladen und in datancontainer speichern

# url auf webserver
cas_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS7IvjYMPz6WHaTUPaHmfc6t9CH3Gma8EljQ5TzuCEirIBGxF5MECRcLEpORJo2h71dvZA_Yeu730dW/pub?gid=0&single=true&output=csv"

# download data und konvertierung in dictionary mit werten in listen
import pandas as pd
data = pd.read_csv(cas_url).to_dict("list")
# print(data)

"""
# Kontrollausgabe der datan
for key, value in data.items():
    print(key, " --> ", value)
print("\n")
"""

# Ausgabe er ersten beiden Werte je Spalte
for key, value in data.items():
    print(key, " --> ", value[0:2])


# *******************************************************************
# tueren visualisieren, tuerflaechen berechnen und aufsummieren
tuerhoehen = data["OverallHeight"]
tuerbreiten = data["OverallWidth"]

import svgwrite
tuergrafik = svgwrite.Drawing("kurs_42.svg")

xlage = 10
flaechensumme = 0
for zaehler in range(len(tuerhoehen)):
    
    hoehe = tuerhoehen[zaehler]/100  # cm
    breite = tuerbreiten[zaehler]/100  # cm
    flaeche = tuerhoehen[zaehler] * tuerbreiten[zaehler] * 1E-6  # in m2 
    # print(flaeche)
    flaechensumme = flaechensumme + flaeche

    # if Bedingung in Abhaengigkeit der flaeche
    if flaeche < 1.9 :
        fuellfarbe = "red"
    elif 1.9 <= flaeche < 2.1:
        fuellfarbe = "green"
    elif 2.1 <= flaeche < 2.4:
        fuellfarbe = "blue"
    elif 2.4 <= flaeche < 3:
        fuellfarbe = "yellow"
    else:
        fuellfarbe = "black"
    
    tuerrect = tuergrafik.rect(
        insert=(xlage, 30),
        size=(breite, hoehe),
        fill=fuellfarbe,
    )
    tuergrafik.add(tuerrect)
    
    xlage = xlage + 20

tuergrafik.save()

print("\nTuersumme: ", round(flaechensumme, 2), "m2")
