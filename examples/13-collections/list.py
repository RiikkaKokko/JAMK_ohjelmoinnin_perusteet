# declare a list of numbers and initialize
list = [5, 10, 15]

# append adds new item to the end of the list
list.append(100)

# insert new item to the middle of the list
list.insert(1, 7)

# print the contents of the list
print("List contents: ", list)

# list items can be accessed via [] operator
# note that index in [] is zero based
print("List element at index 1: ", list[1])

# index to access list can be negative
# negative index means beginning from the end of the list
print("List element at index -1: ", list[-1])

# list item can be changed with [] operator
list[1] = 60

# index can be also specified as a range
# range parameters are start index (inclusive) and end index (exclusive)
print("List elements at range 2:5: ", list[2:5])

# remove item from the list
# only a first occurrence of the item is removed
list.remove(10)
print("List contents after 10 was removed: ", list)

# pop function allows to remove a specific item
list.pop(1)
print("List contents after pop(1): ", list)

# another way to remove item at index is 'del'
del list[1]
print("List contents after del list[1]: ", list)

# clear removes all items from the list
list.clear()


# declare list of names and print
namelist = ["Joe", "Sally", "Liam", "Robert", "Emma", "Isabella"]
print(namelist)

# loop thru a list
for name in namelist:
    print(name)

# use 'len' function to determine list length
print("namelist length is: ", len(namelist))


# check if item exists
if "Liam" in namelist:
    print("Yes, 'Liam' is in the names list")

# note that modifying the 'anothernamelist' also modifies the 'namelist'
# as both variables reference the same list
anothernamelist = namelist
anothernamelist[0] = "Roger"
print(namelist)

# if you need another copy, use list copy function
anothernamelist = namelist.copy()
anothernamelist[0] = "Harris"
anothernamelist[-1] = "Mary"
print("Contents of namelist: ", namelist)
print("Contents of anothernamelist: ", anothernamelist)

# join list to another
combinedlist = namelist + anothernamelist
# another way is to use list 'extend' function
#combinedlist = namelist.copy()
#combinedlist.extend(anothernamelist)
print("Contents of combinedlist: ", combinedlist)
