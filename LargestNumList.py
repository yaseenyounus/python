import random

numList = []
max = numList[0]

# Inserts random numbers into list ranging from 1 to 100
for x in range(100):
    numList.append(random.randrange(1, 101))

# Loops through the list and compares every element to the max to find a new max
for x in numList:
    if x > max:
        max = x
# Prints the max value of the list
print(max)


