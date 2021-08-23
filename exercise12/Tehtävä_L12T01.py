class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + " " + str(self.age)


person1 = Human("Jouni", 27)
person2 = Human("Jaakko", 28)

print(person1)
print(person2)
