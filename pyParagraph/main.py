import re

# open the file, give it a name 
para = "paragraph_1.txt"

# open in read only mode and store in the variable "text"
with open(para, "r") as text:
    
    # store all text in a variable called "lines"
    lines = text.read()

    # print the paragraph
    print(lines)

    print ("-------------------------")
    print("Paragraph Analysis")
    print ("-------------------------")

    # set empty list variables
    cTotWords = []
    cTotSentences = []
    cAveLetters = []
    cAveSentence = []

    cTotWords = 0
    #    cTotWords = text.read().split()
    cTotWords = len(words)

    # print the contents
    print("Approximate Word Count: " + str(cTotWords))


    # re.split("?&lt;=[.!?] +", paragraph)

    print("Approximate Sentence Count: " + str(cTotSentences))
    print("Average Letter Count: " + str(cAveLetters))
    print("Average Sentence Count: " + str(cAveSentence))