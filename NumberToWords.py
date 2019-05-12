int_form = input("Enter a number: ")

str_form = []

num_to_words = {
    1 : "One",
    2 : "Two",
    3 : "Three",
    4 : "Four",
    5 : "Five",
    6 : "Six",
    7 : "Seven",
    8 : "Eight",
    9 : "Nine",
}

for char in int_form:
    str_form.append(num_to_words[int(char)])

for x in str_form:
    print(x, end=" ")
    
