import random


class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return self.brand + " " + str(self.model) + " " + str(self.price)


brands = ["Skoda", "Audi", "Volvo", "BMW", "Ford", "Opel", "Skoda", "VW"]
autot = []

for car in brands:
    obj = Car(car, "", random.randint(1000, 10000))
    autot.append(obj)
    #print(obj)

hinta = []

for car in autot:
    print(car)
    hinta.append(car.price)
print(hinta)

Yhteishinta = sum(hinta)
print("autojen yhteihinta on: " + str(Yhteishinta) + " euroa")
