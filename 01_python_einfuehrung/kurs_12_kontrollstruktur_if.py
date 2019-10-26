# if Kontrollstruktur

x = int(input("Bitte eine ganze Zahl eingeben: "))

if x < 0:
    x = 0
    print("Negative Zahle, Wert zu Null gesetzt")
elif x == 0:
    print("Wert ist Null")
elif x == 1:
    print("Wert ist Eins")
else:
    print("Wert grösser Eins")

print("x hat den Wert: ", x)