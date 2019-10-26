import svgwrite
from svgwrite import mm

my_opart = svgwrite.Drawing("kurs_23.svg")

xkoord = 50
ykoord = 20
breite = 10

for zaehler in range(10):

    xkoord = 2 * breite * zaehler

    my_rect = my_opart.rect(
        insert=(xkoord*mm, ykoord*mm),
        size=(breite*mm, breite*mm),
        fill="red",
    )
    my_opart.add(my_rect)


my_opart.save()
