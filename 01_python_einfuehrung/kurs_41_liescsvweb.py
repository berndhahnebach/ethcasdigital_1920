# *******************************************************************
# daten von webserver herunterladen und in datancontainer speichern

# url auf webserver
cas_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS7IvjYMPz6WHaTUPaHmfc6t9CH3Gma8EljQ5TzuCEirIBGxF5MECRcLEpORJo2h71dvZA_Yeu730dW/pub?gid=0&single=true&output=csv"

# download data und konvertierung in dictionary mit werten in listen
import pandas
data = pandas.read_csv(cas_url).to_dict("list")
# https://stackoverflow.com/questions/52547805/how-to-convert-dataframe-to-dictionary-in-pandas-without-index/52547870
# print(data)

# Kontrollausgabe der datan
for key, value in data.items():
    print(key, " --> ", value)
print("\n")

    
# Ausgabe zum beseren Verstaendnis
for key, value in data.items():
    print(key, " --> ", value[0:2])
    # obere Grenze ist in Python in der Bereichsangabe nicht dabei!
