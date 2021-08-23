from vehicle import Vehicle

# declare an object 'car' from 'Vehicle' class
car = Vehicle("Datsun", "100A", 998, 12)

# declare an object 'car' from 'Vehicle' class
car = Vehicle("Datsun", "100A", 998, 12)

# declare another vehicle
car2 = Vehicle("Toyota", "Celica", 1588, 43)

# print cars
print(car)
print(car2)

# use Vehicle.horsepower function to get power as hp
print("car power is: ", car.horsepower(), "hp")
print("car2 power is: ", car2.horsepower(), "hp")
