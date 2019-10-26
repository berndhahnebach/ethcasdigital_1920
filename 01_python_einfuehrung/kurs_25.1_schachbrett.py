import svgwrite
from svgwrite import mm   

my_opart = svgwrite.Drawing("kurs_25.1.svg")


count = 8
breite = 20
hoehe = breite
xstart = 15
ystart = 15


# da mit einem x-durchlauf zwei zeilen erstellt werden,
# brauchen wir nur count durch 2 Schleifendurchlaeufe in y
for y in range(count//2): 

    for x in range(count):

        xkoord = xstart + breite * x

        if x % 2 == 0:
            # even (gerade), in unterer zeile rechteck zeichnen
            ykoord = ystart + hoehe + hoehe * y * 2
            color_fill = 'red'
        else:
            # odd (ungerade), in oberer zeile rechteck zeichnen
            ykoord = ystart + hoehe * y * 2
            color_fill = 'black'

        my_odd_line = my_opart.rect(
            insert=(xkoord*mm, ykoord*mm),
            size=(breite*mm, hoehe*mm),
            fill=color_fill,
        )
        my_opart.add(my_odd_line)


# rahmen um schachbrett
my_border = my_opart.rect(
    insert=(xstart*mm, ystart*mm),
    size=(count*breite*mm, count*breite*mm),
    fill="white",
    fill_opacity=0.,  # tranzparent, sehr wichtig!
    stroke="green",
    stroke_width=2*mm
)
my_opart.add(my_border)


my_opart.save()
