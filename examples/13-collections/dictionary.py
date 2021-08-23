# dictionary is a key-value pair collection
# declare a dictionary of books as ISBN as key and
# book name as value
bookdict = {
    12345678: "Book 1",
    12345679: "Book 2",
    12345680: "Book 3",
    12345681: "Book 4",
    12345682: "Book 5",
}
print("Contents of the bookdict is: ", bookdict)

# access dictionary items with brackets and key
bookname = bookdict[12345680]
#bookname = bookdict.get(12345680)
print("Book is: " + bookname)

# print all keys in the dictionary
for isbn in bookdict:
    print(isbn)

# print all values in the dictionary
for bookname in bookdict.values():
    print(bookname)

# print keys and values in the dictionary
for isbn, bookname in bookdict.items():
    print(isbn, bookname)

# check if specific key exists in dictionary
if 12345679 in bookdict:
    print("12345679 found in bookdict")

# add item to dictionary
bookdict[422344] = "New Book"
print("Contents of the bookdict after adding new item is: ", bookdict)

# remove item with pop and key
bookdict.pop(12345678)
print("Contents of the bookdict after pop is: ", bookdict)


