
# Description: this program allows the user to play rock-paper-scissors against the computer
# randomly chooses an integer from 0 to 2 inclusive
# 0 for rock, 1 for paper, and 2 for scissors

import random

def displayMenu():
    # prints the menu, no return values, no parameters
    print("Let's play Rock Paper Scissors.")
    print("The rules of the game are: ")
    print(" \t Rock smashes Scissors")
    print(" \t Scissors cut Paper")
    print(" \t Scissors cut Paper")
    print(" \t Paper covers Rock")
    print(" \t If both the choices are the same, it's a tie")

def getComputerChoice():
    # gets a random number between 0 and 2
    return random.randint(0,2)

def getPlayerChoice():
    # allows for user input, repeats loop if not 0,1,2
    playerChoice = 3
    print("Enter 0 for Rock, 1 for Paper or 2 for Scissors")
    while playerChoice != 0 and playerChoice != 1 and playerChoice != 2:
        playerChoice = int(input("> "))
    return playerChoice

def playRound(computerChoice, playerChoice):
    # prints 0 if tie, prints 1 if player wins, prints -1 if computer wins

    if playerChoice == 0 and computerChoice == 1:
        return -1
    if playerChoice == 0 and computerChoice == 2:
        return 1
    if playerChoice == 1 and computerChoice == 0:
        return 1
    if playerChoice == 1 and computerChoice == 2:
        return -1
    if playerChoice == 2 and computerChoice == 0:
        return -1
    if playerChoice == 2 and computerChoice == 1:
        return 1
    if playerChoice == computerChoice:
        return 0

def continueGame():
    #asks user if they want to continue playing
    choice = input("Do you want to continue playing (y or n)?: ").lower()
    if choice == "y":
        return True
    else:
        return False

def main():
    # variables keep track of number of ties, player wins, and computer wins
    countTies = 0
    countPlayerWins = 0
    countCompWins = 0
    temp = True

    while temp == True:
        displayMenu()
        computerChoice = getComputerChoice()
        playerChoice = getPlayerChoice()
        result = playRound(computerChoice, playerChoice)

        if result == 0:
            print("You and the computer tied.")
            countTies +=1
        if result == -1:
            print("Computer Wins")
            countCompWins +=1
        if result == 1:
            print("You win!")
            countPlayerWins +=1
        temp = continueGame()
        print("\n")

    #output all the results at the end

    print("You won " + str(countPlayerWins) + " game(s).")
    print("The computer won " + str(countCompWins) + " game(s).")
    print("You tied with the computer " + str(countTies) + " time(s).")


main()




