import svgwrite
from svgwrite import mm

my_opart = svgwrite.Drawing("kurs_22.svg")

xkoord = 50
ykoord = 20
breite = 10
hoehe = 30
linecolor = "green"
linethickness= 2

my_rect = my_opart.rect(
    insert=(xkoord*mm, ykoord*mm),
    size=(breite*mm, hoehe*mm),
    fill="yellow",
    stroke=linecolor,
    stroke_width=linethickness*mm,
)

my_rect_2 = my_opart.rect(
    insert=(100*mm, 20*mm),
    size=(20*mm, 50*mm),
    fill="blue",
    stroke="orange",
    stroke_width=2*mm,
)

my_opart.add(my_rect)
my_opart.add(my_rect_2)

my_opart.save()
