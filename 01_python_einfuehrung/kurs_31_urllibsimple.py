import urllib.request

cas_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSEdO-6644k0ZvsyYNQTYsls-aEBzmeEWtnZ9e8QIG8JQaE0RitsaGoKh8WtepXNNKliUN-HDln0LB9/pub?gid=0&single=true&output=csv"


#download the data
with urllib.request.urlopen(cas_url) as susi:
   cas_string_data = susi.read()

# wandle in standard string
cas_string_data = cas_string_data.decode("utf-8")
print("\nRohe Daten:")
print(type(cas_string_data))
print(cas_string_data)


# trenne nach zeilen auf
cas_string_data_aufgeteilt = cas_string_data.splitlines()
print("\nNach Linien aufgetrennte Daten:")
print(cas_string_data_aufgeteilt)



# dictionary, nach listen wichtigster zusammengesetzter datentyp
# funtktioniert wie ein Woerterbuch
cas_structured_data = {}
for line in cas_string_data_aufgeteilt:
    splitted_line = line.split(",")
    cas_structured_data[splitted_line[0]] = splitted_line[1]

print("\nStrukturierte Daten in dictionary:")
print(cas_structured_data)

# wandle datenwerte in 
for key in cas_structured_data:
    try:
        cas_structured_data[key] = int(cas_structured_data[key])
    except:
        cas_structured_data[key] = float(cas_structured_data[key])

for key in cas_structured_data:
    print("Variable: ", key , " --> Value: ",  cas_structured_data[key])
