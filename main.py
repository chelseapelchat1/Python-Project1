# Chelsea Pelchat, pelchat@usc.edu
# ITP 115, Fall 2021
# Section 32023
# Assignment 9
# Description: this program translates words to different languages

def getLanguages(fileName = "languages.csv"):

    # opens file
    file = open(fileName, "r")

# creates list to store languages in the header row
    languageList = []
    line = file.readline()
    line = line.strip()
    languageList = line.split(",")

# close the file
    file.close()
    return languageList

def getTranslationLanguage(langList):

# langList is a list of the languages

# displays to the user the languages that are available for translation
    print("Translate English words to one of the following languages:\nDanish Dutch Finnish French German Indonesian Italian\nJapanese Latin Norwegian Portuguese Spanish Swahili Swedish")

# this gets a list of all languages without English
    noEnglish = langList[1:14]

# allows user to choose a language
    inputLang = input("Enter a language: ")
    inputLang = inputLang.capitalize()

    while inputLang not in noEnglish:
        print("This program does not support", inputLang)
        inputLang = input("Enter a language: ").capitalize()

    return inputLang

def readFile(langList, langStr, fileName = "languages.csv"):
    tempList = []

#opens file and reads header row to skip it
    file = open(fileName, "r")
    line = file.readline()
    langIndex = langList.index(langStr)

# strips each line, then splits them based off commas
    for line in file:
        line = line.strip()
        lineList = line.split(",")
        tempList.append(lineList[langIndex])

    file.close()
    return tempList

def createResultsFile(language):

# variable stores results text file

    tempVar = language + ".txt"

# overwrites any existing files

    fileObj = open(tempVar, "w")
    print("words translated from English to " + language, file = fileObj)

    fileObj.close()

def translateWords(englishList, translationList, language):
    tempVar = language + ".txt"
    file = open(tempVar, "a")


    choice = "y"

# this while loop reiterates the program til the user opts out

    while choice == "y":
        englishWord = input("Enter an English word to translate: ").lower()

        if englishWord in englishList:

# translates the word to another language

            langIndex = englishList.index(englishWord)
            translatedWord = translationList[langIndex]

            if translatedWord == "-":
                print(englishWord , "does not have a translation!")
                break

            print(englishWord + " is translated to " + translatedWord)
            print(englishWord + " = " + translatedWord, file=file)

# when the word is not in the csv file

        else:
            print(englishWord, "not in English list")

        choice = input("Another word (y or n)?").lower()

# closes file and returns all translated words to a file

    file.close()

    print("Translated words have been saved to " + language + ".txt")


def main():

# executes all the functions
    print("Language Translator")
    languageList = getLanguages()
    englishList = readFile(languageList, langStr = "English", fileName = "languages.csv")
    transLanguage = getTranslationLanguage(languageList)
    transList = readFile(languageList, transLanguage)
    createResultsFile(transLanguage)
    translateWords(englishList, transList,transLanguage)

main()









