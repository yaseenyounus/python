# Project Euler 2 : find the sum of all the even fibonacci numbers less than/equal to 4 million

# 1 2 3 5 8 13 21

sum_even = 0
a, b = 1, 2
while b <= 4000000:
        a, b = b, a + b
        if a % 2 ==0:
                sum_even += a

print(a, b, sum_even)
