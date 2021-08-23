ikä= int(input("How old are you?"))
if ikä <= 12:
    print("child")
elif ikä >= 13 and  ikä <= 19:
    print("teen")
elif ikä >= 20 and ikä <=65:
    print("adult")
else:
    print("senior")