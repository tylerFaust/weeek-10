########################################################################
##
## CS 101 Lab
## Week 10
## Name: Tyler Faust
## Email: tefqhg@umsystem.edu
##
## PROBLEM : Describe the problem
##      count word frequencies in a text document
## ALGORITHM : 
##      1. user inputs a text file
##      2. tuen text file into a string and find most frequent words
##      3. show user results and end program
## 
## ERROR HANDLING:
##
## OTHER COMMENTS:  
##      The program does not sort by most frequent.
########################################################################

def frequency(word,words):
    freq = 0
    for item in words:
        if word == item:
            freq +=1
    print("{:>3}{:>15}{:>20}".format(number,word,freq))
    if freq == 1:
        return 1
    else:
        return 0

if __name__ == "__main__":
    loop = True
    while loop:
        try: 
            file = input("\nEnter the name of the file to open ")
            file = open(file)
            loop = False
        except: 
            print("Could not open file {}".format(file))
    
    lines = file.readlines()
    space = " " #readlines makes a list. rejoining the list into a string
    linesString = space.join(lines)
    linesString = linesString.lower()

    #removing punctuation
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in linesString:
        if char in punc:
            linesString = linesString.replace(char, "")

    splitLines = linesString.split()

    uniqueWords = []

    for item in splitLines:
        if item not in uniqueWords:
            uniqueWords.append(item)

    number = 1
    once = 0

    print("\nMost frequently used words")
    print("\n{:>3}{:>15}{:>20}".format("#","Word","Freq."))
    print("=======================================")
    for item in uniqueWords:
        once += frequency(item,splitLines)
        number += 1

    print("there are {} unique words in the document".format(len(uniqueWords)))
    print("there are {} words that occur once in the document".format(once))
