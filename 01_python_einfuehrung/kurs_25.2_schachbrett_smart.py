import svgwrite
from svgwrite import mm   

my_opart = svgwrite.Drawing("kurs_25.2.svg")


anzahl = 8
breite = 20
hoehe = breite
xstart = 15
ystart = 15


# in einem durchlauf werden zwei zeilen und zwei spalten erstellt,
# daher anzahl durch 2 Schleifendurchlaeufe
for zeile in range(anzahl//2): 

    for spalte in range(anzahl//2):

        # in unterer zeile rechteck zeichnen
        xukoord = xstart + breite * spalte * 2
        yukoord = ystart + hoehe + hoehe * zeile * 2
        re_zeile_oben = my_opart.rect(
            insert=(xukoord*mm, yukoord*mm),
            size=(breite*mm, hoehe*mm),
            fill="red",
        )
        my_opart.add(re_zeile_oben)

        # in oberer zeile rechteck zeichnen
        xokoord = xstart + breite + breite * spalte * 2
        yokoord = ystart + hoehe * zeile * 2
        re_zeile_unten = my_opart.rect(
            insert=(xokoord*mm, yokoord*mm),
            size=(breite*mm, hoehe*mm),
            fill="black",
        )
        my_opart.add(re_zeile_unten)


# rahmen
my_border = my_opart.rect(
    insert=(xstart*mm, ystart*mm),
    size=(anzahl*breite*mm, anzahl*breite*mm),
    fill="white",
    fill_opacity=0.,  # tranzparent, sehr wichtig!
    stroke="green",
    stroke_width=2*mm
)
my_opart.add(my_border)

my_opart.save()
