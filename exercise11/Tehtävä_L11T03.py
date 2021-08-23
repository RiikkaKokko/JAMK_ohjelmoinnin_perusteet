nimi_lista=[]
nimi=0
number_of_empty_responses = 0
while True:
    data = input("Kirjoita oppilaan nimi: ")
    nimi += 1
    #print(nimi)
    nimi_lista.append(data)
    if data == "":
        number_of_empty_responses += 1
        if number_of_empty_responses == 1:
            nimi_lista.remove("")
            print(nimi_lista)
            print(nimi - 1)
            break

