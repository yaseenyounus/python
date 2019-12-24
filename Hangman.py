
def wordToList(word):
    wordList = []
    for x in word:
        wordList.append(x)
    return wordList


letterTries = []

word = "hangman"

list_displayed = ('_ ' * len(word)).split(' ')
strDisplay = " "


while True:

    print("Incorrect: {}".format(letterTries))
    print(strDisplay.join(list_displayed))
    print()

    if word == "".join(list_displayed):
        print("You Win!")
        break

    userGuess = input("Enter a letter guess: ").lower()

    if userGuess in word:
        wordList = wordToList(word)
        for index, x in enumerate(wordList):
            if x == userGuess:
                list_displayed[index] = userGuess

    else:
        print(strDisplay.join(list_displayed))
        letterTries.append(userGuess)
