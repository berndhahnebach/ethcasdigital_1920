
# *******************************************************
# get the structured data
import urllib.request
cas_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSEdO-6644k0ZvsyYNQTYsls-aEBzmeEWtnZ9e8QIG8JQaE0RitsaGoKh8WtepXNNKliUN-HDln0LB9/pub?gid=0&single=true&output=csv"

with urllib.request.urlopen(cas_url) as response:
   cas_string_data = response.read()

cas_string_data = cas_string_data.decode("utf-8")
cas_string_data = cas_string_data.splitlines()
cas_structured_data = {}  # dictionary, nach listen wichtigster zusammengesetzter datentyp
for line in cas_string_data:
    splitted_line = line.split(",")
    cas_structured_data[splitted_line[0]] = splitted_line[1]

# print(cas_structured_data)

for key in cas_structured_data:
    try:
        cas_structured_data[key] = int(cas_structured_data[key])
    except:
        cas_structured_data[key] = float(cas_structured_data[key])

for key in cas_structured_data:
    print("Variable: ", key , " --> Value: ",  cas_structured_data[key])


# *******************************************************
# use the dtructured data

# count = 16
count = cas_structured_data["count"]

# start_width = 10
start_width = cas_structured_data["start_width"]

# height = 5
height = cas_structured_data["height"]

xstart = 0
ystart = 15

# zoom = 1.2
zoom = cas_structured_data["zoom"]



# *******************************************************
# kopie aus 

import svgwrite
from svgwrite import mm   
my_opart = svgwrite.Drawing("kurs_32_urllibusecase.svg")

xdelta = start_width
xkoord = xstart

# spalten in der zeile x
for x in range(count//2):

    # zeilen in der spalte y rechtecke in einer spalte zeichnen
    for y in range(count//2):

        # print(xdelta)

        # even (gerade), in zweiter zeile anfangen
        xevenkoord = xkoord
        # print(xevenkoord)
        ykoord = ystart + height + height * 2 * y
        my_even_col = my_opart.rect(
            insert=(xevenkoord*mm, ykoord*mm),
            size=(xdelta*mm, height*mm),
            fill='red',
        )
        my_opart.add(my_even_col)

        # odd (ungerade), in erster zeile anfangen
        xoddkoord = xkoord + xdelta
        # print(xoddkoord)
        ykoord = ystart + height * 2 * y
        my_odd_col = my_opart.rect(
            insert=(xoddkoord*mm, ykoord*mm),
            size=(xdelta*mm, height*mm),
            fill='black',
        )
        my_opart.add(my_odd_col)
        # print("")

    xkoord = xkoord + 2 * xdelta
    xdelta = xdelta * zoom


my_border = my_opart.rect(
    insert=(xstart*mm, ystart*mm),
    size=(xkoord*mm, count*height*mm),
    fill='white',
    fill_opacity=0.,  # sehr wichtig!
    stroke='black',
    stroke_width=1*mm
)
my_opart.add(my_border)


my_opart.save()



    
# decode a bytestring
# b"abcde".decode("utf-8")

"""
def is_float(value):
"""
