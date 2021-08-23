# declare set of names and print
nameset = {"Joe", "Sally", "Liam", "Robert", "Emma", "Isabella"}
print("Contents of nameset is: ", nameset)

# print contents of the set in for loop
for name in nameset:
    print(name)

# check length of the set
print("Length of the set is: ", len(nameset))

# check if certain item is in the set
name = "Sally"
print(name + " is in set: ", name in nameset)

# items in set cannot be modified but can be added and removed
# use add function to add new item
nameset.add("Bella")
print("Contents of nameset after add is: ", nameset)

# update function allows to add multiple items to the set
nameset.update({"Harry", "Elisa", "Pocahontas"})
print("Contents of nameset after update is: ", nameset)

# items can be removed with remove or discard function
# remove function will raise an error if item is not in a set
# discard function works the same as remove but will not raise an error
# if item is not found
nameset.remove("Liam")
#nameset.discard("Liam")
print("Contents of nameset after remove is: ", nameset)

