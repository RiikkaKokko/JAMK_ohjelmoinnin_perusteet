number_list=[]
for i in range(7):
    print(("Kirjoita tämän päivän sademäärä"))
    item=int(input())
    number_list.append(item)

kokonaissademäärä=0
for x in number_list:
    kokonaissademäärä=kokonaissademäärä+ x
print(kokonaissademäärä)
