# Project Euler 6 : finds the difference between the sum of the squares and the square of the sums of the first 100 natural numbers

sum_squares = 0
square_sum = 0

max_number = 101 #using 101 so it includes 100 in the range below

for x in range(max_number): # so it includes 10
    sum_squares += x ** 2

for x in range(max_number):
    square_sum += x
square_sum = square_sum ** 2

print(square_sum - sum_squares)