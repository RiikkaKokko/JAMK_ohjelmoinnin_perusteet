Arvosanat = []
arvosana = 0
number_of_empty_responses = 0

while True:
    data = (input("Kirjoita arvosana: "))
    arvosana += 1
    Arvosanat.append(data)
    if data == "":
        number_of_empty_responses += 1
        if number_of_empty_responses == 1:
            Arvosanat.remove("")
            #print(Arvosanat)
            ints = [int(item) for item in Arvosanat]
            break

uusi_lista = [i for i in ints if i > -1 and i < 6]
#print(uusi_lista)

keskiarvo = sum(uusi_lista) / len(uusi_lista)

print("Arvosanoja on yhteensä: " + str(arvosana - 1))
print("numeroiden keskiarvo on: " + str(keskiarvo))
