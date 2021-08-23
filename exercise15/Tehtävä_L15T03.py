try:
    file = open("nimet.txt", "r", encoding='utf-8')
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    count = 0
    for line in lines:
        count += 1
except:
    print("Failed to read file: " + file)
finally:
    file.close()

# print(lines)
print("nimiä on yhteensä: " + str(count))

aakkosjärjestys = sorted(lines)
print(aakkosjärjestys)

aakkosjärjestys_unnique = sorted(list(set(aakkosjärjestys)))

for name in aakkosjärjestys_unnique:
    print(name + " on listassa " + str(aakkosjärjestys.count(name)) + " kertaa")
