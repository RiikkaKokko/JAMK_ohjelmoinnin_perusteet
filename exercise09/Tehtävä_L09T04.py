etunimi = list(input("Kirjoita etunimesi "))
sukunimi = (input("Kirjoita sukunimesi "))
etunimi_list=[]
sukunimi_list=[]
etunimi_list.append(etunimi)
sukunimi_list.append(sukunimi)
ensimmäinen_krijain_lista=[]
ensimmäinen_kirjain= etunimi[0]

for etunimi in etunimi_list:
    for char in etunimi:
        ensimmäinen_krijain_lista.append(ensimmäinen_kirjain)

print(''.join(ensimmäinen_krijain_lista))

for sukunimi in sukunimi_list:
    reverse=sukunimi[::-1]
    print(reverse)

