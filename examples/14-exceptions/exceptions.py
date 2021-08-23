# Nollalla jakaminen ei onnistu, tulee virhe

#number1 = 100
#number2 = 0
#result = number1 / number2
#print("Result is ", result)

# Jos kysytään numeroita, mutta käyttäjä syöttää aakkosia/merkkejä, tulee virhe

number = int(input("Give a number: "))
print("you entered: ", number)

# Listassa ei ole niin paljon elementtejä, kuin yritetään tulostaa
#numbers = [ 1, 2, 3, 4, 5 ]
#print("Last number is ", numbers[5])

try:
    number1 = 100
    number2 = 0
    result = number1 / number2
    print("Result is ", result)
except ZeroDivisionError:
    print("Can't divide by zero!")


try:
    number = int(input("Give a number: "))
    print("you entered: ", number)
except ValueError:
    print("Unable to convert to number")
except:
    print("Something else went wrong :(")


try:
    numbers = [ 1, 2, 3, 4, 5 ]
    print("Last number is ", numbers[5])
except IndexError:
    print("Wrong index used in accessing list")


def safe_division(x, y):
    if y == 0:
        raise Exception("Exception from safe_division")
    return x / y

try:
    result = safe_division(100, 0)
except:
    print("safe_division raised an exception")


def someday_something_here():
    raise NotImplementedError("This function is not implemented currently")

someday_something_here()
