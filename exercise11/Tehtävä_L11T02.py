kysymys=input("Muutetaanko farenheitit celsiuksiksi vai celsiu-asteet fahrenheitiksi?")
asteet=float(input("Kirjoita asteet"))


if kysymys == "fahrenheitit celsiuksiksi":
    celsius=(asteet-32)*5/9
    print(celsius)
else:
    fahrenheit=(asteet* 9/5) + 32
    print(fahrenheit)