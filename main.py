# Chelsea Pelchat, pelchat@usc.edu
# ITP 115, Fall 2021
# Section: 32023
# Lab 5

def main():

    articles = ['a', 'the']
    nouns = ['person', 'place', 'thing']
    verbs = ['danced', 'ate', 'frolicked']

    choice = 1

    while choice != 0:
        print("Welcome to the Sentence Generator")
        print("1) View Words")
        print("2) Add Noun")
        print("3) Remove Verb")
        print("4) Generate Sentence")
        print("5) Exit")
        choice = int(input("> "))

        if choice == 1:
            print("articles: " + str(articles))
            print("nouns: " + str(nouns))
            print("verbs: " + str(verbs))

        elif choice == 2:
            newWord = input("Enter the word: ")
            nouns.append(newWord)

        elif choice == 3:
            remove = input("Enter the word: ")

        elif choice == 4:
            nounR = random.choice(nouns)
            verbR = random.choice(verbs)
            articleR = random.choice(articles)

            print(articleR + nounR + verbR + articleR + nounR)


main()