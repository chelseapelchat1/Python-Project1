# Chelsea Pelchat, pelchat@usc.edu
# ITP 115, Fall 2021
# Section 32023
# Assignment 6
# Description: program displays a jumbled word to the user
# have the user guess the word until it's correct
# after the user correctly enters the word,
# display the number of guesses it took for them to enter the correct word

import random

def main():

# two lists, one with words, one with hints
    list1 = ['dog', 'horse', 'cow', 'frog']
    list2 = ['woooof', 'neiiiighhh', 'moooooo', 'ribbet ribbet']

# gets a random word and the corresponding hint and saves them into two variables
    randomWord = random.choice(list1)
    randIndex = list1.index(randomWord)
    randomHints = list2[randIndex]

# stores random word into a list and creates an empty string, jumbles word
    inputList = list(randomWord)
    emptyString = ""

# loops through the list while it has elements
    while len(inputList) >= 1:
        word = random.choice(inputList)
        emptyString = emptyString + word
        inputList.remove(word)

    if emptyString == randomWord:
        randomWord = random.choice(list1)
        randIndex = list.index(randomWord)
        randomHints = list2[randomWord]
        inputList = list(randomWord)
        emptyString = ""

        while len(inputList) > 0:
            variable = random.choice(inputList)
            emptyString = emptyString + word
            inputList.remove(word)

    stop = True
    numGuesses = 0

# prints the jumbled word to the user, repeats until they get it right
# counts the number of guesses with the numGuesses variable

    while stop != False:
        print("The jumbled word is " + emptyString)
        guess = input("Enter your guess: ").lower()

        # if guess is correct, prints "you got it!"
        if guess == randomWord:
            print("You got it!")
            numGuesses = numGuesses + 1
            print("It took you " + str(numGuesses) + " guesses")
            stop = False

# when a user does not guess correctly
        if guess != randomWord:
            print("That is not correct")
            numGuesses = numGuesses + 1
            guess2 = input("Do you want a hint (y or n)? ").lower()
            if guess2 == 'y':
                print("The hint is \'" + randomHints + "\"")

main()