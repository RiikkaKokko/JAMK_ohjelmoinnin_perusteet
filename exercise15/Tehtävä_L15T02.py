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

print(lines)
print("nimiä on yhteensä: " + str(count))

for name in set(lines):
    print(name + " on listassa " + str(lines.count(name)) + " kertaa")
