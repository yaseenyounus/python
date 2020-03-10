# Project Euler 3: Largest Prime Factor - What is the largest prime factor of the number 600851475143 ?

factors = []
prime = []

num = 24


def findFactors(num):
    factors = []
    for x in range(1, int(num/2) + 1):
        if num % x == 0:
            factors.append(x)
    return factors



def isPrime(factor):
    if len(factors) == 2:
        print("Yes, is prime")
        return True
    else: 
        print('No, not prime')
        return False


# finds factors of num that are also prime numbers
for x in findFactors(num):
    if len(findFactors(x)) == 2:
        prime.append(x)
        print()


print(prime)
print(findFactors(600851475143)) 











# take factors and check if prime
for x in factors:
    pass




