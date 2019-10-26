import svgwrite
from svgwrite import mm   

my_opart = svgwrite.Drawing("kurs_21_einfachesrechteck_ovar.svg")

my_rect = my_opart.rect(
    insert=(20*mm, 20*mm),
    size=(20*mm, 50*mm),
    fill="yellow",
    stroke="orange",
    stroke_width=2*mm,
)
my_opart.add(my_rect)

# save to svg file
my_opart.save()
