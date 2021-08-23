while True:
    luku = input("Kirjoita numero")
    try:
        luku = int(luku)
        print('This is a int')
        filename1=("Integers.txt")
        file1=open(filename1, "w")
        file1.write(str(luku))
        file1.close()
    except:
        try:
            luku = float(luku)
            print('This is a float')
            filename="Floats.txt"
            file=open(filename, "w")
            file.write(str(luku))
            file.close()
        except:
            break


