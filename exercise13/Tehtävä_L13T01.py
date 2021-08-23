
Rekisterinumerot=[]

while True:
    rekisterinumero = input("Kirjoita auton rekisterinumero: ")
    Rekisterinumerot.append(rekisterinumero)
    if rekisterinumero == "":
        Rekisterinumerot.remove("")
        break

print(sorted(Rekisterinumerot))