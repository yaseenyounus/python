# Project Euler 1 : This program takes numbers that are multiples of 3 or 5 under 1000, and then prints the total

number = 1000
total = 0

for x in range(number):
    if x % 3 == 0 or x % 5 ==0:
        total += x

print(total)
