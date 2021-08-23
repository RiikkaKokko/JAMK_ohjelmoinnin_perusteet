number= int(input("Kirjoita luku väliltä 1-10"))

for i in range(number):
    print("Luvun " + str(i+1) + " neliö on ", str((i+1)*(i+1)))
