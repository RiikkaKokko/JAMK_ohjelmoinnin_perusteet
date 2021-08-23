#Oman funtkion esittely

def print_info():
    print("Info")

print_info()

def print_and_return_number():
    print("Info - returning 123")
    return 123

number = print_and_return_number()
print("print_and_return_number returned ", number)

def sum(number1, number2):
    return number1 + number2

number = sum(5, 11)
print("sum returned ", number)

# define a function that takes text as a parameter and modifies
# it before printing
def modify_text(text):
    text += ", this text is added by function"
    print(text)

text = "About to call modify_text"
modify_text(text)
print(text)

#Toisessa tiedostossa esitellyn funktion käyttäminen

from helper import *

number = sub(5, 11)
print("sub returned ", number)

# Tuntitehtävä 1

numero1= int(input("kirjoita yksi numero: "))
numero2= int(input("Kirjoita toinen numero: "))

print(sum(numero1, numero2))

# Tuntitehtävä 2

def funktio(firstname, surname):
    return firstname + " "+ surname

nimi=funktio("Riikka", "Kokko")
print(nimi)

