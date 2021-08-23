# Muuttujien esittely

number = 5
accountbalance = 110.54
print(number)
print(accountbalance)

# Muuttujien käsittely operaattoreilla

number = 55
number2 = number + 2
# value of number2 is now 57
print("number2 is ", number2)

#Muuttujien tyyppi

# Python assigns an automatic type for each variable
# the variable type can be checked with type()
print("Type of the variable 'number' is ", type(number))
print("Type of the variable 'accountbalance' is ", type(accountbalance))

# Merkkijonot

# strings
# initialize string from text in quotes
name = "Riikka"
lastName = "Kokko"

# initialize string from another string
fullName = name

# add strings to string
fullName = name + " " + lastName
print(fullName)

# use Format function
age = 26
fullName = "First name: {}. Last name: {}. Age: {}".format(name, lastName, age)
print(fullName)


# access characters in a string
text = "ABC"
a = text[0]
b = text[1]
c = text[2]
print("Second char is " + b)

# print text length into console
print("Text length is " + str(len(text)) + " characters.")


# compare strings
text2 = "ABD"
if text == text2:
    print("Texts are identical.")
else:
    print("Texts are not identical")

# read text from console
line = input("Enter a line of text: ")
print("You entered " + line)

# read numeric value to variable 'number'
# note that if user enters text that cannot be converted to a number, an
# error is generated. We will later learn how to handle these situations
line = input("Enter a number: ")
number = int(line)
print("Number is ", number)

# Count
lst= [1,2,3,4,5,3,2,1,3,5,5,3,4,5]
x=lst.count(3)
print("number 3 count:" + str(x))

# startswith / endswith

text= "Writing code is so fun!"
y = text.startswith("Writing")
print(y)

ends = text.endswith("so")
print(ends)

# replace

replacing = text.replace("so", "not")
print(replacing)

# lower/upper

text_lower = "THIS TEXT SHOULD BE LOWER CASE!"
lower_text = text_lower.lower()
print(lower_text)

text_upper = "But this text should be upper case!"
upper_text =text_upper.upper()
print(upper_text)

# Split

txt = "let's split this text"
split_txt = txt.split()
print(split_txt)