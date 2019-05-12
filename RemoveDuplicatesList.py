import random

list = []

# Filling list with random integers
for x in range(10):
    list.append(random.randint(0, 10))

# Print the original list of random integers
print("Original List: {}".format(list))

# Looping through the list to check if number appears more than once. If so, remove it
for num in list:
    while list.count(num) > 1:
        list.remove(num)

# Print list after removing duplicates
print("After Removing Duplicates: {}").format(list)