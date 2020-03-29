# Project Euler 3: Largest Prime Factor - What is the largest prime factor of the number 600851475143 ?


###
# Original Solution (brute force) - works but to slow with big numbers
###
# factors = []
# prime = []

# num = 24


# def findFactors(num):
#     factors = []
#     for x in range(1, int(num/2) + 1):
#         if num % x == 0:
#             factors.append(x)
#     return factors


# def isPrime(factor):
#     if len(factors) == 2:
#         print("Yes, is prime")
#         return True
#     else:
#         print('No, not prime')
#         return False


# # finds factors of num that are also prime numbers
# for x in findFactors(num):
#     if len(findFactors(x)) == 2:
#         prime.append(x)
#         print()


# print(prime)
# print(findFactors(600851475143))

###
###

###
# New Solution - find prime numbers from smallest to largest, then find largest prime factor of 600851475143
###

num = 35
factors = []
primes = []


def findFactors(num):
    for x in range(1, int(num/2) + 1):
        if num % x == 0:
            factors.append(x)
    return factors


def findPrimes(num):
    if num > 1:
        for x in range(2, num):
            if num % x == 0:
                print("not prime")
                break
            else:
                print("yes, prime")
                primes.append(x)


# print(findFactors(34))

# for x in findFactors(34):
#     findPrimes(x)

# print(primes)

print(findPrimes(11))
