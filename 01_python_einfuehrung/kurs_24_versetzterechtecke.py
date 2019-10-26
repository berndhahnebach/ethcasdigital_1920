import svgwrite
from svgwrite import mm   

my_opart = svgwrite.Drawing("kurs_24_versetzterechtecke.svg")


count = 8
breite = 20
hoehe = breite  # zum besseren Verstaendnis im code hoehe geschrieben und nicht breite
xstart = 15
ystart = 15


# rechtecke
for x in range(count):

    xkoord = xstart + breite * x

    if x % 2 == 0:
        # even (gerade), in unterer zeile rechteck zeichnen
        ykoord = ystart + hoehe
        color_fill = 'red'
    else:
        # odd (ungerade), in oberer zeile rechteck zeichnen
        ykoord = ystart
        color_fill = 'blue'

    my_odd_line = my_opart.rect(
        insert=(xkoord*mm, ykoord*mm),
        size=(breite*mm, hoehe*mm),
        fill=color_fill,
    )
    my_opart.add(my_odd_line)


# rahmen um alle rechtecke
my_border = my_opart.rect(
    insert=(xstart*mm, ystart*mm),
    size=(count*breite*mm, 2*hoehe*mm),
    fill="white",
    fill_opacity=0.,  # tranzparent, sehr wichtig!
    stroke="green",
    stroke_width=2*mm
)
my_opart.add(my_border)


my_opart.save()
