class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return self.brand + " " + str(self.model) + " " + str(self.price)


car1 = Car("Skoda", "Octavia", 3000)
car2 = Car("Audi", "A4", 4000)
car3 = Car("Volvo", "V70", 5000)

print(car1, car2, car3)

print((car1.price + car2.price + car3.price))


