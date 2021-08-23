filename = "files-example.txt"
file = open(filename, "w")
file.write("Creating a file with Python!")
file.close()


# trying to write a file directly to drive root will cause a PermissionError
filename = "files-example.txt"
try:
    file = open("C:\\" + filename, "w")
    # in Linux/Mac, try
    # file = open("/" + filename, "w")
    file.write("trying to write to drive root, its not going to work :(")
    file.close()
except:
    print("Failed to create file to drive root")


import os.path

# get the user home folder, create a new folder and write the file there
path = os.path.expanduser("~/files-example")
if not os.path.exists(path): os.makedirs(path)
path += "/"

file = open(path + filename, "w")
file.write("Files example, writing file to users home folder")
file.close()


filename = "multiline-text.txt"
lines = [ "First line\n", "Second line\n", "Third line\n" ]
try:
    file = open(path + filename, "w")
    file.writelines(lines)
except Exception as e:
    print("Failed to write file: " + filename)
finally:
    file.close()


lines = [""]
try:
    file = open(path + filename, "r")
    lines = file.readlines()
except:
    print("Failed to read file: " + filename)
finally:
    file.close()

print(lines)

# Omien tietotyyppien tallettaminen tiedostoon

# import the pickle library to save/load custom datatypes to file
import pickle

# import the Vehicle class from another source file
from vehicle import Vehicle

# declare a list of Vehicle objects
vehicles = []
vehicles.append(Vehicle("Datsun", "Sunny", 1197, 29))
vehicles.append(Vehicle("BMW", "M5", 4899, 294))
vehicles.append(Vehicle("Toyota", "Supra", 2999, 200))
vehicles.append(Vehicle("Plymouth", "Cuda", 6845, 597))

# print the contents of vehicle list
for vehicle in vehicles:
    print(vehicle)


# write a list of Vehicles into the vehicles.dat
# the pickle library will save the list objects in binary format
# hence we use the 'dat' filename extension instead of txt
# also note that output file is opened with "wb" (write binary) mode
filename = "vehicles.dat"
try:
    file = open(path + filename, "wb")
    pickle.dump(vehicles, file, pickle.HIGHEST_PROTOCOL)
except:
    print("Failed to write file: " + filename)
finally:
    file.close()

# objects are now saved into the file, clear the list
vehicles.clear()


# try to load the objects back from the file
try:
    file = open(path + filename, "rb")
    vehicles = pickle.load(file)
except:
    print("Failed to read file: " + filename)
finally:
    file.close()

# print list contents to confirm that objects were loaded into the list
for vehicle in vehicles:
    print(vehicle)

