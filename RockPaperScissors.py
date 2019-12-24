import random


def randRPS():
    rand = random.randint(0, 2)
    options = ["Rock", "Paper", "Scissors"]
    return options[rand]


def validateInput():
    userInput = input("Enter your choice: ").lower()
    while userInput != "rock" and userInput != "paper" and userInput != "scissors":
        print("That is not a valid option, try again (rock, paper or scissors)")
        userInput = input("Enter your choice: ").lower()
    return userInput


def play():
    if computerAnswer == userAnswer:
        print("It's a tie")
    else:
        # print("Not a tie")
        logic()


def logic():
    if computerAnswer == "rock" and userAnswer == "paper":
        print("User wins!")
    elif computerAnswer == "rock" and userAnswer == "scissors":
        print("Computer Wins")

    elif computerAnswer == "paper" and userAnswer == "rock":
        print("Computer Wins")
    elif computerAnswer == "paper" and userAnswer == "scissors":
        print("User Wins")

    elif computerAnswer == "scissors" and userAnswer == "rock":
        print("User Wins")
    elif computerAnswer == "scissors" and userAnswer == "paper":
        print("Computer Wins")


while True:
    print("********************")
    print(">> Welcome to RPS <<")
    print("********************\n\n")

    computerAnswer = randRPS().lower()
    # print(computerAnswer)
    userAnswer = validateInput()

    play()

    prompt = input("Would you like to play again? (yes or no) ").lower()

    if prompt == "yes":
        continue
    else:
        print("\nSee you later")
        break
