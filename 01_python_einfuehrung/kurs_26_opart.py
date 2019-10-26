import svgwrite
from svgwrite import mm   

my_opart = svgwrite.Drawing("kurs_27_opart.svg")


count = 16
anfangsbreite = 10
hoehe = 10
xstart = 5
ystart = 5
zoom = 0.75


xdelta = anfangsbreite
xkoord = xstart

# spalten in der zeile x
for x in range(count//2):

    # zeilen in der spalte y rechtecke in einer spalte zeichnen
    for y in range(count//2):

        # print(xdelta)

        # even (gerade), in zweiter zeile anfangen
        xevenkoord = xkoord
        # print(xevenkoord)
        ykoord = ystart + hoehe + hoehe * 2 * y
        my_even_col = my_opart.rect(
            insert=(xevenkoord*mm, ykoord*mm),
            size=(xdelta*mm, hoehe*mm),
            fill='black',
        )
        my_opart.add(my_even_col)

        # odd (ungerade), in erster zeile anfangen
        xoddkoord = xkoord + xdelta
        # print(xoddkoord)
        ykoord = ystart + hoehe * 2 * y
        my_odd_col = my_opart.rect(
            insert=(xoddkoord*mm, ykoord*mm),
            size=(xdelta*mm, hoehe*mm),
            fill='black',
        )
        my_opart.add(my_odd_col)
        # print("")

    xkoord = xkoord + 2 * xdelta
    xdelta = xdelta * zoom


# rahmen um alles
xkoord = xkoord - xstart
my_border = my_opart.rect(
    insert=(xstart*mm, ystart*mm),
    size=(xkoord*mm, count*hoehe*mm),
    fill='white',
    fill_opacity=0.,  # sehr wichtig!
    stroke='black',
    stroke_width=1*mm
)
my_opart.add(my_border)


my_opart.save()
