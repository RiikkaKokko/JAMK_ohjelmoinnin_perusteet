class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return self.name + " " + str(self.color)

    def miau(self):
        return self.name + " " + self.color


cat1 = Cat("kissa", "oranssi")
cat2 = Cat("cat", "musta")

print(cat1)
print(cat2)

print("kissa maukuu: ", cat1.miau())
print("toinen kissa maukuu: ", cat2.miau())
