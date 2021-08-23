luvut=[]
numero=0
number_of_empty_responses = 0

while True:
    data =input("Kirjoita luku: ")
    numero += 1
    luvut.append(data)
    if data == "":
        number_of_empty_responses += 1
        if number_of_empty_responses == 1:
            #print(numero - 1)
            luvut.remove("")
            ints = [int(item) for item in luvut]
            break

print("numeroita on yhteensä: " + str(numero-1))
summa=sum(ints)
print("numeroiden summa on: " + str(summa))