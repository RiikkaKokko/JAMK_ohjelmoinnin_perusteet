# dictionary is a key-value pair collection
# declare a dictionary of books as ISBN as key and
# book name as value
cardict = {
    "ABC-123": "Skoda",
    "PEF-124": "BMW",
    "LOE-156": "Audi",
    "WER-123": "VW",
    "POL-093": "Mercedes-Benz",
    "FJK-056": "Opel",
    "PFG-903": "Mazda",
    "WXV-673": "KIA",
    "CJG-643": "Saab",
    "WDJ-352": "Toyota"
}
#print("Contents of the cardict is: ", cardict)

# autojen tiedot aakkosjärjestyksessä automerkin mukaan
automerkki=sorted(cardict.items(), key=lambda x: x[1])
print(automerkki)

# autojen tiedot aakkosjärjestyksessä rekisterinumeron mukaan
rekisterinumero=sorted(cardict.items(), key=lambda x: x[0])
print(rekisterinumero)
