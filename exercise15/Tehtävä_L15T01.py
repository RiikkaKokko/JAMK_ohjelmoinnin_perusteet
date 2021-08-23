sukunimet = []

while True:
    sukunimi = input("Kirjoita sukunimi: ")
    if sukunimi == "":
        break
    sukunimet.append(sukunimi)

#print(sukunimet)


filename = "sukunimet.txt"

try:
    for i, name in enumerate(sukunimet):
        if i==0:
            mode='w'
        else:
            mode='a'
        with open(filename, mode) as file:
            file.write(name+'\n')
except Exception as e:
    print("Tiedoston tallentaminen ei onnistu ")
finally:
    file.close()

try:
    file = open(filename, "r")
    lines = file.readlines()
    for line in lines:
        print(line.strip())
except:
    print("Failed to read file: " + filename)
finally:
    file.close()


