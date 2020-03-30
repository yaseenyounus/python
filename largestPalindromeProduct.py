# Project Euler #4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# racecar

def isPalindrome(word):
    count_backwards = -1
    for letter in word:
        # print(letter)
        # print(word[count_backwards])
        if letter == word[count_backwards]:
            count_backwards -= 1
            continue
        else:
            return False
            break
    return True
    print("Yes, palindrome")




# product of all 2 digit numbers 10 - 99
palindromes = []

for x in range(100, 1000):
    for y in range(100, 1000):
        if isPalindrome(str(x * y)):
            palindromes.append(x * y)
            print(f"Palindrome x: {x}, y: {y}")

print(palindromes)
print(max(palindromes))







