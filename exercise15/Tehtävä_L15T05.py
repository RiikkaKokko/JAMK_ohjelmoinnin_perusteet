import random
numbers = list(range(1, 41))
random.shuffle(numbers)
print(numbers[:7])

filename="lotto.txt"
file=open(filename, "w")
file.write(str(numbers[:7]))
file.close()